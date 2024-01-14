from flask import request, jsonify
from app import app, db, mongo
from app.models import User
from bson import ObjectId
from base64 import b64encode,b64decode
def create_token(username,password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'
def login_check(token):
    try:
        token = token.split(" ")[-1]
        decoded_credentials = b64decode(token).decode("utf-8")
        uspass = decoded_credentials.split(":")
        username = uspass[0]
        password = uspass[1]
        user = User.query.filter_by(username=username,password=password).first()
        if user:
            return True
        else:
            return False
    except:
        return False



@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User has been registered successfully','token':create_token(data['username'],data['password'])})

@app.route('/get-token', methods=['GET'])
def get_token():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'],password=data['password']).first()

    if user:
        token = create_token(data['username'],data['password'])
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/products', methods=['GET'])
def list_products():
    if not login_check(request.headers['token']):
        return jsonify({'message': 'Invalid credentials'}), 401
    products = mongo.db.products.find({},{})
    product_list = []
    for i in products:
        i['_id'] = str(i['_id'])
        product_list.append(i)

    return jsonify({'products': product_list})
@app.route('/add_product', methods=['POST'])
def add_product():
    if not login_check(request.headers['token']):
        return jsonify({'message': 'Invalid credentials'}), 401
    data = request.get_json()
    new_product = {
        'name': data['name'],
        'price': data['price'],
        'description': data['description']
    }


    result = mongo.db.products.insert_one(new_product)

    if result.inserted_id:
        return jsonify({'message': 'Product added successfully'})
    else:
        return jsonify({'message': 'Failed to add product'})

@app.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        if not login_check(request.headers['token']):
            return jsonify({'message': 'Invalid credentials'}), 401
        product_id = ObjectId(product_id)
        product = mongo.db.products.find_one({'_id': product_id}, {'_id': 0})

        if product:
            return jsonify({'product': product})
        else:
            return jsonify({'message': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Invalid product ID'}), 400

if __name__ == "__main__":
    app.run(debug=True)