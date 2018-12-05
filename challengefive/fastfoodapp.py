from flask import Flask, jsonify, request, json, flash, session

app = Flask(__name__)

# secret key to access the session of the log in 
app.secret_key = "natalie123"

orders = []

users = {}

# routes for the api 

# print("Welcome to the system. Please register or login.")
# print("Options: register | login | exit")
# while True:
#     option = input("> ")
#     if option == "login":
#         login()
#     elif option == "register":
#         register()
#     elif option == "exit":
#         break
#     else:
#         print(option + " is not an option")

# Register
@app.route('/api/v1/register', methods=['POST'])
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    print("Account has been created")

# Login
@app.route('/api/v1/login', methods=['POST'])
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

@app.route('/api/v1/loginauth', methods=['GET'])
# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False


# @app.route('/api/v1/logout')
# def logout():
#     session['logged out'] = None
#     flash('you were just logged out!')
#     return jsonify({'message':'successful'}) 


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
