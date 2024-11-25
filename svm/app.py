import os
import pickle
import librosa
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app)
model_path1 = os.environ.get('MODEL_PATH')

# Define the directory to save uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Step 3: Define function to extract Mel spectrogram features from .wav file
def extractMelSpectrogram_features(file_path):
    hop_length = 512
    n_fft = 2048
    n_mels = 128

    # Load the audio file
    signal, rate = librosa.load(file_path)

    # Compute the Mel spectrogram
    S = librosa.feature.melspectrogram(y=signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)

    # Convert the Mel spectrogram to decibel (dB) scale
    S_DB = librosa.power_to_db(S, ref=np.max)

    # Flatten and truncate to a fixed length (1200 in this case)
    S_DB = S_DB.flatten()[:1200]  # Adjust the size as per your model input

    return S_DB

# Function to predict genre from the .wav file
def predict_genre(file_path, clf):
    # Extract features from the .wav file
    mel_features = extractMelSpectrogram_features(file_path)

    # Make prediction using the trained model
    genre_label = clf.predict([mel_features])[0]

    # List of genre labels
    genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

    # Return the predicted genre
    return genres[genre_label]

# Step 4: Load the pre-trained model once when the server starts
model_path = model_path1

with open(model_path, 'rb') as f:
    clf = pickle.load(f)

# Step 5: Create the Flask route for predictions
@app.route('/predict_svm', methods=['POST'])
def predict_svm():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # Check if the file is valid
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.wav'):
        # Save the uploaded file
        try:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Predict the genre
            try:
                predicted_genre = predict_genre(file_path, clf)
                return jsonify({"predicted_genre": predicted_genre})
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "File save failed: " + str(e)}), 500

    return jsonify({"error": "Invalid file format. Please upload a .wav file."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
