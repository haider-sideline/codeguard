"""TEST DATA ONLY - intentionally insecure code so a scanner has something to find.
Never deploy or run this against real systems."""
import hashlib
import pickle
import sqlite3
import subprocess

DB_PASSWORD = "Admin@12345"            # VULN-01: hard-coded password
API_KEY = "test-api-key-1234567890"    # VULN-02: hard-coded API key


def get_user(username):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"  # VULN-03: SQL injection
    return conn.execute(query).fetchall()


def ping(host):
    return subprocess.call("ping -c 1 " + host, shell=True)  # VULN-04: command injection


def calculate(expression):
    return eval(expression)  # VULN-05: use of eval on input


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # VULN-06: weak hash (MD5)


def load_session(data):
    return pickle.loads(data)  # VULN-07: insecure deserialisation
