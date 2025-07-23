def is_valid_username(username: str) -> bool:
    return username.isalnum()
    

def is_valid_password(password: str) -> bool:
    return len(password) >= 8

def is_valid_phone(phone:int)->bool:
    return  len(phone) == 9
   


