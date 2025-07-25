from models import User, Order

user = User.login()
if user:
    order = Order.create_order(user.id)
