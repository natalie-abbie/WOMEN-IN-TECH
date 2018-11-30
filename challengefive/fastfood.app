from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

app.secret_key = "natalie123"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/welcome')
def Welcome():
    return render_template("welcome.html")

@app.route('/register', methods=['POST'])
def resgister():
   global users_list

   data = request.form
   username = data['username']
   password = data['password']

   for user in users_list:
       if user['username'] == username:
           return jsonify({'message':'username already exists'}), 400

   users_list.append({'username':username, 'password': password})

   return json.dumps(users_list), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == ' POST':
        if request.form['username'] != 'username' or request.form['password'] != 'password':
            error = 'Invalid credentials. please try again.'
    else:
        session['logged in']=True
        flash('you were just logged in!')
        return redirect(url_for (home))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop['logged out']
    flash('you were just logged out!')
    return redirect(url_for (welcome))

@app.route('/orders', methods=['GET'])
def orders():
   global orders_list
   # orders_list = [
   #     {'name': 'pizza', 'price': 30000, 'quantity': 1, 'restaurant': 'cafe javas'},
   #     {'name': 'chicken', 'price': 15000, 'quantity': 2, 'restaurant': 'KFC'}
   # ]

   return json.dumps(orders_list)

@app.route('/orders', methods=['POST'])
def ordersx():
   global orders_list
   # name_of_food, price, quantity, location, restaurant
   data = request.form

   price = data['price']
   location = data['location']
   quantity = data['quantity']
   name = data['name']
   restaurant = data['restaurant']

   orders_list.append({
       'name': name,
       'price': price,
       'location': location,
       'quantity': quantity,
       'restaurant': restaurant
   })

   return json.dumps(orders_list)

if __name__ == '__main__':
    app.run(debug=True)
