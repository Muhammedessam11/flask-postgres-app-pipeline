from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    'dbname': 'mydb',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'db',  # Service name from docker-compose.yml
}

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT 'Hello, DevOps with Flask and PostgreSQL!' AS message;")
        message = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({'message': message})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

