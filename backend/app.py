from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root123",
        database="ecommerce"
    )

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/products")
def get_products():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
