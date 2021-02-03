from flask import Flask, jsonify, render_template
from flask_cors import CORS
from markdown2 import Markdown
import requests
import requests_cache
import json

requests_cache.install_cache('github_cache', backend='memory', expire_after=300)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'PostHog update server'

@app.route('/changelog')
def changelog():
    changelog = requests.get('https://raw.githubusercontent.com/PostHog/posthog/master/CHANGELOG.md')
    markdown = Markdown()
    return render_template('changelog.html', html=markdown.convert(changelog.text).replace("<a", "<a target='_blank'").replace('<h1>Changelog</h1>', ''))

@app.route('/versions')
def versions():
    tags = requests.get('https://api.github.com/repos/posthog/posthog/git/refs/tags/')
    tags = list(reversed(tags.json()))
    return jsonify([
        {'version': tag['ref'].split('/')[-1]} for tag in tags if "beta" not in tag['ref']
    ])