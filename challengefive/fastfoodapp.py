from flask import Flask, jsonify, request, json

app = Flask(__name__)

# secret key to access the session of the log in 
app.secret_key = "natalie123"

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

   name = ['name']
   price = ['price']
   quantity = ['quantity']
   restaurant = ['restaurant']

   orders.append({
       'name_of_food': name,
       'price': price,
       'quantity': quantity,
       'restaurant': restaurant
   })

   return json.dumps(orders)


if __name__ == '__main__':
    app.run(debug=True)
