// WARNING: This file contains intentionally vulnerable code for testing purposes
// DO NOT use these patterns in production code

const express = require("express");
const mysql = require("mysql");
const { exec } = require("child_process");

// === SQL Injection Vulnerabilities ===
function getUserById(userId) {
  const query = `SELECT * FROM users WHERE id = ${userId}`; // VULNERABLE: SQL injection
  return mysql.query(query);
}

function searchUsers(searchTerm) {
  const sql = "SELECT * FROM users WHERE name = '" + searchTerm + "'"; // VULNERABLE: SQL injection
  return database.query(sql);
}

// === XSS Vulnerabilities ===
function renderUserContent(userInput) {
  document.innerHTML = userInput; // VULNERABLE: XSS via innerHTML
  return `<div>${userInput}</div>`; // VULNERABLE: unescaped user input
}

function displayMessage(msg) {
  eval(`alert('${msg}')`); // VULNERABLE: eval with user input
}

// === Command Injection ===
function processFile(filename) {
  exec(`cat ${filename}`, (error, stdout) => {
    // VULNERABLE: command injection
    console.log(stdout);
  });
}

function pingHost(host) {
  const command = `ping -c 1 ${host}`; // VULNERABLE: command injection
  require("child_process").execSync(command);
}

// === Hardcoded Secrets ===
const API_KEY = "sk-1234567890abcdef123456789"; // VULNERABLE: hardcoded API key
const DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"; // VULNERABLE: hardcoded credentials
const JWT_SECRET = "super-secret-key-123"; // VULNERABLE: hardcoded JWT secret

// === Insecure Random Number Generation ===
function generateToken() {
  return Math.random().toString(36); // VULNERABLE: weak randomness
}

function createSessionId() {
  return Date.now().toString(); // VULNERABLE: predictable session ID
}

// === Prototype Pollution ===
function merge(target, source) {
  for (let key in source) {
    target[key] = source[key]; // VULNERABLE: prototype pollution
  }
  return target;
}

// === Regular Expression DoS ===
function validateEmail(email) {
  const regex =
    /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/; // VULNERABLE: ReDoS
  return regex.test(email);
}

// === Insecure Deserialization ===
function loadUserSettings(data) {
  return eval("(" + data + ")"); // VULNERABLE: eval for deserialization
}

// === Path Traversal ===
function readFile(filename) {
  const fs = require("fs");
  return fs.readFileSync(`./uploads/${filename}`); // VULNERABLE: path traversal
}

// === Weak Cryptography ===
const crypto = require("crypto");
function hashPassword(password) {
  return crypto.createHash("md5").update(password).digest("hex"); // VULNERABLE: weak hashing
}

// === Open Redirect ===
function redirectUser(url) {
  window.location = url; // VULNERABLE: open redirect
}

// === CORS Misconfiguration ===
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*"); // VULNERABLE: overly permissive CORS
  res.header("Access-Control-Allow-Headers", "*");
  next();
});

console.log(
  "JavaScript vulnerability test file loaded - Semgrep should detect multiple issues!",
);
