from flask import Flask
import os
import mysql.connector
import redis

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "devops"),
        password=os.getenv("DB_PASSWORD", "devops123"),
        database=os.getenv("DB_NAME", "devops")
    )

    cache = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379
    )

    db.close()

    return "Hello from Flask! Database and Redis are connected. Code updated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
