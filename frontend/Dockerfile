# Use the official PHP Apache image
FROM php:8.0-apache

# Copy your index.html and PHP files to the Apache server
COPY ./index.html /var/www/html/

# Optionally enable PHP extensions if needed
# RUN docker-php-ext-install mysqli pdo pdo_mysql

# Expose the port that Apache will run on
EXPOSE 82
