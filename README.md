# OD-Image-Explorer
Open Directory Image Parser
Open Directory Image Parser

This Python script fetches all image URLs from a specified open directory and displays them in a grid format on a locally hosted web page.
Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites

    Python 3
    Flask
    BeautifulSoup4
    requests

Install the prerequisites using pip:

pip install flask beautifulsoup4 requests

Directory Structure

Ensure that your directory structure looks like this:

arduino

/open-directory-image-parser
    /templates
        index.html
    app.py

templates/ is a folder that contains the HTML template (index.html) for the Flask application. Flask automatically looks for templates in this folder.
Running the Script

    Replace 'http://www.example.com/directory' in app.py with the URL of the open directory you want to scrape.
    Run the script with python app.py.
    Open a web browser and go to http://localhost:5000.

Features

    Fetches images with the extensions .jpg, .jpeg, .png, .bmp, and .gif (regardless of casing).
    Displays images in a grid view with CSS.
    Serves a webpage locally with Flask.

Disclaimer

This script is for educational purposes only. Be aware of the ethical and legal considerations around web scraping and displaying images. Always make sure you have permission to use the images and to scrape the website, and respect any restrictions specified in the site's robots.txt file.
Future Improvements

    Add error handling and check response status codes.
    Improve the handling of URLs to make the script more robust.
