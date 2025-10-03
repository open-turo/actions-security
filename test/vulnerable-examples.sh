#!/bin/bash

# WARNING: This file contains intentionally vulnerable code for testing purposes
# DO NOT use these patterns in production code

# Command injection vulnerabilities
echo "=== Command Injection Tests ==="

# Direct command injection
user_input="$1"
eval "ls $user_input"  # VULNERABLE: eval with user input

# Shell injection via backticks
filename=`echo $user_input`  # VULNERABLE: backticks with user input
rm -rf $filename

# Unsafe variable expansion
echo "Deleting: $(rm -rf $user_input)"  # VULNERABLE: command substitution

# System command with user input
system("grep $user_input /etc/passwd")  # VULNERABLE: system() call

echo "=== Credential Issues ==="

# Hard-coded secrets
API_KEY="sk-1234567890abcdef"  # VULNERABLE: hardcoded API key
PASSWORD="admin123"            # VULNERABLE: hardcoded password
DB_CONN="mysql://root:password@localhost/db"  # VULNERABLE: connection string

# Logging sensitive data
echo "User password: $PASSWORD"  # VULNERABLE: logging credentials

echo "=== File Permission Issues ==="

# Insecure file permissions
chmod 777 /tmp/sensitive.txt     # VULNERABLE: world-writable
touch /tmp/world_readable.conf
chmod 644 /tmp/world_readable.conf  # VULNERABLE: world-readable config

# Unsafe temp file creation
temp_file="/tmp/predictable_name.tmp"  # VULNERABLE: predictable temp file
echo "secret data" > $temp_file

echo "=== SQL Injection Patterns ==="

# SQL injection in shell script
query="SELECT * FROM users WHERE name='$user_input'"  # VULNERABLE: SQL injection
mysql -e "$query"

# Another SQL injection pattern
user_id=$1
psql -c "DELETE FROM accounts WHERE id=$user_id"  # VULNERABLE: unescaped SQL

echo "=== Path Traversal ==="

# Directory traversal
cat "../../../etc/passwd"  # VULNERABLE: path traversal
include_file="$user_input"
source "$include_file"     # VULNERABLE: arbitrary file inclusion

echo "=== Weak Cryptography ==="

# Weak random number generation
random_key=$RANDOM         # VULNERABLE: weak randomness
password=$(date +%s)       # VULNERABLE: predictable password

# Insecure hash
echo "password123" | md5sum  # VULNERABLE: weak hashing algorithm

echo "=== Network Security Issues ==="

# Unencrypted data transmission
curl -k https://api.example.com/data  # VULNERABLE: ignoring SSL errors
wget --no-check-certificate https://untrusted.com/file  # VULNERABLE: no cert validation

# Binding to all interfaces
nc -l -p 8080 0.0.0.0  # VULNERABLE: binding to all interfaces

echo "Test completed - Semgrep should detect multiple vulnerabilities!"
