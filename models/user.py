import json
from datetime import datetime
from uuid import uuid4
from utils import (
    make_password, is_valid_username, print_status,
    is_valid_password,is_valid_phone,
)


class User:
    
    def __init__(self, id, username, password, phone, first_name, last_name, age, gender):
        self.id = id
        self.username = username
        self.password = password
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.joined_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'gender': self.gender,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['id'],
            data['username'],
            data['password'],
            data['phone'],
            data['first_name'],
            data['last_name'],
            data['age'],
            data['gender'],
        )
    
    @classmethod
    def load_users(cls):
        with open('database/users.json') as jsonfile:
            try:
                data = json.load(jsonfile)
            except:
                data = []

        users = [User.from_dict(item) for item in data]

        return users
    
    @classmethod
    def save_users(cls, users):
        with open('database/users.json', 'w') as jsonfile:
            data = [user.to_dict() for user in users]
            json.dump(data, jsonfile, indent=2)

    @classmethod
    def create_user(cls):
        username = input("Username: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
        phone = input("Phone: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        gender = input("Gender: ")

        if not is_valid_username(username):
            print_status("username xato kiritildi.", "error")
        
        elif not is_valid_phone(phone):
            print_status("Telefon raqamni tog'ri formatda kiriting (masalan: 901234567) ","Error")

        elif User.check_username(username):
            print_status("username tanlangean.", 'error')

        elif not is_valid_password(password):
            print_status("password xato kiritildi.", "error")
            
        elif password != confirm_password:
            print_status("password va confirm password mos emas.", "error")
        else:
            user = cls(str(uuid4()), username, make_password(password), phone, first_name, last_name, age, gender)
            users = cls.load_users()
            users.append(user)
            cls.save_users(users)

    @classmethod
    def check_username(cls, username: str):
        for user in User.load_users():
            if user.username == username:
                return True
            
        return False
    @classmethod
    def login(cls):
        username = input("Username")
        password = input("Pasword")

        hashe_pasword = make_password(password)
        
        for user in cls.load_users():
            if user.username == username and user.password == hashe_pasword:
                return user
