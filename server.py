from flask import Flask
from flask import jsonify
from flask import request
from github import Github
from auth import getProxyURL, getUsername, getPassword
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Github Recruiter'

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
            'followers': user.followers
        }
        
        results.append(item)

    results.append({
        'name': 'Kaan Aksoy',
        'email': 'kaanaksoyaz@gmail.com',
        'avatar_url': 'https://avatars2.githubusercontent.com/u/2722074?v=3&s=460',
        'contributions': 9001,
        'followers': 9001
    })
    
    results.sort(key=lambda x: x['followers'], reverse=True)
        
    return jsonify({'users': results})
    

@app.route('/proxy')
def get_proxy():
    return getProxyURL()
    
