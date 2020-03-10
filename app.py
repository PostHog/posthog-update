from flask import Flask, jsonify, render_template
from flask_cors import CORS
from markdown2 import Markdown
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'PostHog update server'

@app.route('/changelog')
def changelog():
    changelog = requests.get('https://raw.githubusercontent.com/PostHog/posthog/master/CHANGELOG.md')
    markdown = Markdown()
    return render_template('changelog.html', html=markdown.convert(changelog.text).replace("<a", "<a target='_blank'"))

@app.route('/versions')
def versions():
    tags = requests.get('https://api.github.com/repos/posthog/posthog/git/refs/tags/')
    tags = list(reversed(tags.json()))
    return jsonify([
        {'version': tag['ref'].split('/')[-1]} for tag in tags
    ])