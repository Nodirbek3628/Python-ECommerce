from models import User, Order



User.create_user

user = User.login()

if user:
    order = Order.create_order(user.id)
