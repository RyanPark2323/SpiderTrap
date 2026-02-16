from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')

def home():
    return "<h1>This is a simple Spider Trap Implementation:</h1><p>Welcome to the spider trap! This page is designed to trap unethical web crawlers and bots, but it will not harm users or ethical web crawlers and bots</p>"

def spider_trap():
    # To Do: Implement the spider trap logic here
    pass

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)