import unittest
from fastfoodapp import app
from flask import json

class useroperations(unittest.TestCase):
    client = app.test_client()

    def test_register_successfully(self):

        self.users = {
                "username":"nataline",
                "password":"nats",
                "role":"admin"
            }
        response = self.client.post('/api/v1/register', data=json.dumps(self.users), content_type='application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual('Account created successfully', data['message'])

    def test_password_missing(self):

        self.users = {
                "username":"nataline",
                "password":"",
                "role":"admin"
            }

        response = self.client.post('/api/v1/register', data=json.dumps(self.users), content_type='application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("password can't be blank", data["message"])

    def test_username_missing(self):

        self.users ={
            "username":"",
            "password":"nats",
            "role":"admin"
        }

        response = self.client.post('/api/v1/register', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("username can't be blank", data["message"]) 

    def test_role_missing(self):

        self.users ={
            "username":"nataline",
            "password":"nats",
            "role":""
        }

        response = self.client.post('/api/v1/register', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("role can't be blank", data["message"]) 

    def test_login_successful(self):

        self.users ={
            "username":"nataline",
            "password":"nats",
            "role":"admin"
        }

        response = self.client.post('/api/v1/login', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("login successful", data["message"]) 

    def test_fields_empyt(self):

        self.users ={
            "username":"",
            "password":"",
            "role":""
        }

        response = self.client.post('/api/v1/login', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("fields can't be blank", data["message"]) 

    def test_invalid(self):

        self.users ={
            "username":"username",
            "password":"password",
            "role":""
        }

        response = self.client.post('/api/v1/login', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("field can't be blank", data["message"]) 

    def test_username_missing(self):

        self.users ={
            "username":"",
            "password":"password",
            "role":"role"
        }

        response = self.client.post('/api/v1/login', data = json.dumps(self.users), content_type = 'application/json')
        data = json.loads(response.data.decode())
        print(data)
        self.assertEqual("field can't be blank", data["message"]) 


    


if __name__ == '__main__':
   unittest.main()
