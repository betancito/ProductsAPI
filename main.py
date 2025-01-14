import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, Response, request
from bson import ObjectId, json_util
from flask_pymongo import PyMongo

load_dotenv()
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("CONNECTION_STRING")


mongo = PyMongo(app) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/v1/products")
def get_products():
    data = mongo.db.products.find()
    products = json_util.dumps(data)
    return Response(products, mimetype="application/json")

@app.route("/api/v1/products/<id>")
def get_product_by_id(id):
    data = mongo.db.products.find_one({
        "_id": ObjectId(id)
    })
    product = json_util.dumps(data)
    return Response(product, mimetype="application/json")

@app.route("/api/v1/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    mongo.db.products.insert_one({
        "name": new_product.get("name"),
        "price": new_product.get("price")
    })
    return "product created successfully"

@app.route("/api/v1/products/<id>", methods=["DELETE"])
def delete_product(id):
    mongo.db.products.delete_one({
        "_id" : ObjectId(id)
    })
    return "xd"
    
@app.route("/api/v1/products/<id>", methods=["PUT"])
def update_product(id):
    updated_product = request.get_json()
    if not updated_product.get("name") or not updated_product.get("price"):
        return jsonify({
            "error" : "Name and price are required"
        }),400
        
    result = mongo.db.products.update_one(
        {"_id" : ObjectId(id)},
        {"$set" : {
            "name" : updated_product.get("name"),
            "price" : updated_product.get("price")
        }}
    )
    
    if result.matched_count == 0:
        return jsonify({
            "error" : "Product not found"
        }),404
        
    return jsonify({
        "message" : "Product updated successfully"
    }), 200
    
    
if __name__ == "__main__":
    app.run(debug=True)