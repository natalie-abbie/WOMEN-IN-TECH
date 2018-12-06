from flask import Flask, jsonify, request, json

app = Flask(__name__)

orders = []

users_list = []

# routes for the api 
@app.route('/api/v1/', methods=['GET'])
def welcome():
    print("To continue, Please register or login")
   
    action = raw_input()
    if action == "login":
        return login()
    elif action == "register":
        return register()
    
    else:
        print(action + " is not an option")

# Register
@app.route('/api/v1/register', methods=['POST'])
def register():

    username =raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")

    users= [{
        'username':username,
        'password':password
        }]
    users_list.append(users)

    if not len(username) > 0:
        return jsonify({"message":"Username can't be blank"}), 400
    
    if not len(password) > 0:
        return jsonify({"message":"Password can't be blank"}), 400
        
    else:
        return jsonify({"message":"Account created successfully",'users': users_list,}), 200

# Login
@app.route('/api/v1/login', methods=['POST'])
def login():

        username = raw_input("Username: ")
        password = raw_input("Password: ")

        if not len(username) > 0 and not len(password) > 0:
            return jsonify({"Error": "field can't be blank"}), 400
        
        if username in users_list:
            if password == users_list[username]["password"]:
                print("Login successful")
                return True

        else:
            return session()
     
@app.route('/api/v1/session', methods=['POST'])
def session():
    username=[]
    print("Welcome to your account ")
    print("Options: view orders | logout")
    
    option = raw_input("your option: ")
    if option == "logout":
        return jsonify({"message": "you are logged out"})
        
    elif option == "view orders":
        return order()

@app.route('/api/v1/order', methods=['POST'])
def order():
   global orders
   # name_of_food, price, quantity, restaurant
   userdata=request.get_json()
   try:
        name = userdata['name']
        price = userdata['price']
        quantity = userdata['quantity']
        restaurant = userdata['restaurant']
       
   except KeyError as item:
       return jsonify({'message':str(item)+'missing'}),400

   new_order={
       'name_of_food': name,
       'price': price,
       'quantity': quantity,
       'restaurant': restaurant
   }

   orders.append(new_order)
   return jsonify({"message":"order created"}),201

@app.route('/api/v1/order', methods=['GET'])
def get_order():
   return jsonify({'orders':orders}),200

if __name__ == '__main__':
    app.run(debug=True)
