from flask import Flask, jsonify
from markdown2 import Markdown
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'PostHog update server'

@app.route('/changelog')
def changelog():
    changelog = requests.get('https://raw.githubusercontent.com/PostHog/posthog/master/CHANGELOG.md')
    markdown = Markdown()
    return markdown.convert(changelog.text)

@app.route('/versions')
def versions():
    tags = requests.get('https://api.github.com/repos/posthog/posthog/git/refs/tags/')
    tags = list(reversed(tags.json()))
    return jsonify([
        {'version': tag['ref'].split('/')[-1]} for tag in tags
    ])