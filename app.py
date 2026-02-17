import uuid
from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is a simple Spider Trap Implementation:</h1><p>Welcome to the spider trap! This page is designed to trap unethical web crawlers and bots, but it will not harm users or ethical web crawlers and bots</p>"

@app.route('/system-logs-archive/')
@app.route('/system-logs-archive/<path_id>')
def spider_trap(path_id=None):
    new_paths = [str(uuid.uuid4()) for _ in range(10)]
    return render_template('spider_trap.html', paths=new_paths)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, 'robots.txt')

if __name__ == '__main__':
    app.run(debug=True)