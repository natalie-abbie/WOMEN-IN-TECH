from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {
        'name_of_food': 'pizza',
        'price': '30000',
        'quantity': '1', 
        'restuarant': 'javas'
    },
    {
        'name_of_food': 'chapati',
        'price': '500',
        'quantity': '1', 
        'restuarant': 'Fiaz cafe'
    },

    {
        'name_of_food': 'Rolex',
        'price': '1000',
        'quantity': '2', 
        'restuarant': 'Ugaroll'
    }
]

users = []

def find_user():
  password = ['password']
  username = ['username']
  user = [user for user in users if user['username'] == username or user['password'] == password]
  return user


@app.route('/api/v1/register', methods=['GET'])
def register():
    username = ['username']
    password = ['password']

    user = find_user()
    if len(user) != 0:
      return {'Error':'Username/Email already exists'}, 409
    if username == "":
      return {'Error':'Please input a valid username'}, 400
    if password == "":
      return {'Error':'Please input a valid password'}, 400
    new_user = {
            'id': len(users) + 1,
            'username': username,
            'password': password
            }
    users.append(new_user)
    return {'users': users}, 200


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify({'orders': orders})


if __name__ == '__main__':
    app.run(debug=True)
