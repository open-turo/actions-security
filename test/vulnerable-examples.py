#!/usr/bin/env python3

# WARNING: This file contains intentionally vulnerable code for testing purposes
# DO NOT use these patterns in production code

import sqlite3
import subprocess
import pickle
import os
import hashlib
import random
from flask import Flask, request

app = Flask(__name__)

# === SQL Injection Vulnerabilities ===
def get_user_by_id(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # VULNERABLE: SQL injection
    cursor.execute(query)
    return cursor.fetchall()

def search_users(search_term):
    conn = sqlite3.connect('database.db')
    # VULNERABLE: SQL injection via string formatting
    query = "SELECT * FROM users WHERE name = '%s'" % search_term
    return conn.execute(query).fetchall()

# === Command Injection ===
def ping_host(hostname):
    # VULNERABLE: command injection
    result = subprocess.run(f"ping -c 1 {hostname}", shell=True, capture_output=True)
    return result.stdout

def process_file(filename):
    # VULNERABLE: command injection via os.system
    os.system(f"cat {filename}")

def execute_command(cmd):
    # VULNERABLE: eval with user input
    return eval(f"subprocess.run('{cmd}', shell=True)")

# === Hardcoded Secrets ===
API_KEY = "sk-1234567890abcdef123456789"  # VULNERABLE: hardcoded API key
DATABASE_PASSWORD = "admin123"  # VULNERABLE: hardcoded password
JWT_SECRET = "super-secret-jwt-key-123"  # VULNERABLE: hardcoded JWT secret
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # VULNERABLE: hardcoded AWS key

# === Insecure Deserialization ===
def load_user_data(serialized_data):
    # VULNERABLE: pickle deserialization
    return pickle.loads(serialized_data)

def deserialize_object(data):
    # VULNERABLE: eval for deserialization
    return eval(data)

# === Path Traversal ===
@app.route('/read_file')
def read_file():
    filename = request.args.get('file')
    # VULNERABLE: path traversal
    with open(f"./uploads/{filename}", 'r') as f:
        return f.read()

def get_template(template_name):
    # VULNERABLE: path traversal
    template_path = f"templates/{template_name}"
    return open(template_path).read()

# === Weak Cryptography ===
def hash_password(password):
    # VULNERABLE: MD5 for password hashing
    return hashlib.md5(password.encode()).hexdigest()

def generate_token():
    # VULNERABLE: weak randomness
    return str(random.randint(1000, 9999))

def create_session_id():
    # VULNERABLE: predictable session ID
    import time
    return str(int(time.time()))

# === LDAP Injection ===
def authenticate_user(username, password):
    import ldap
    # VULNERABLE: LDAP injection
    search_filter = f"(&(uid={username})(password={password}))"
    # ... ldap search code

# === XML External Entity (XXE) ===
def parse_xml(xml_data):
    import xml.etree.ElementTree as ET
    # VULNERABLE: XXE via XML parsing
    root = ET.fromstring(xml_data)
    return root

# === Server-Side Request Forgery (SSRF) ===
def fetch_url(url):
    import urllib.request
    # VULNERABLE: SSRF - no URL validation
    response = urllib.request.urlopen(url)
    return response.read()

# === Insecure Random ===
def generate_password():
    # VULNERABLE: weak random password generation
    import random
    chars = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(chars) for _ in range(8))

# === Flask Security Issues ===
app.secret_key = "hardcoded-secret-key"  # VULNERABLE: hardcoded Flask secret

@app.route('/redirect')
def redirect_user():
    url = request.args.get('url')
    # VULNERABLE: open redirect
    return f'<script>window.location="{url}"</script>'

# === Template Injection ===
@app.route('/render')
def render_template():
    template = request.args.get('template')
    # VULNERABLE: template injection
    return eval(f"f'{template}'")

if __name__ == "__main__":
    print("Python vulnerability test file loaded - Semgrep should detect multiple issues!")
    # VULNERABLE: Flask debug mode in production
    app.run(debug=True, host='0.0.0.0')
