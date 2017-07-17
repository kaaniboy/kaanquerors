from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from github import Github
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_profiles')
def get_profiles():
    school = request.args.get('school', '')

    username = os.environ.get('GITHUB_USERNAME')
    password = os.environ.get('GITHUB_PASSWORD')

    g = Github(username, password)

    results = []

    for user in g.search_users(school).get_page(0):
        item = {
            'name': user.name,
            'email': user.email,
            'avatar_url': user.avatar_url,
            'url': user.url,
            'contributions': user.contributions,
            'followers': user.followers,
			'repos': user.public_repos,
			'html_url': user.html_url,
			'login': user.login
        }

        results.append(item)

    results.sort(key=lambda x: x['followers'], reverse=True)

    return jsonify({'users': results})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
