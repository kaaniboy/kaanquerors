from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from github import Github
from auth import getProxyURL, getUsername, getPassword
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_profiles')
def get_profiles():
    school = request.args.get('school', '')
    
    os.environ['HTTP_PROXY'] = getProxyURL()

    g = Github(getUsername(), getPassword())

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

    results.append({
        'name': 'Kaan Aksoy',
        'email': 'kaanaksoyaz@gmail.com',
        'avatar_url': 'https://avatars2.githubusercontent.com/u/2722074?v=3&s=460',
		'repos': 9001,
        'contributions': 9001,
        'followers': 9001,
		'login': 'kaaniboy',
		'html_url': 'www.github.com/kaaniboy'
    })
    
    results.sort(key=lambda x: x['followers'], reverse=True)
        
    return jsonify({'users': results})
    

@app.route('/proxy')
def get_proxy():
    return getProxyURL()
    
