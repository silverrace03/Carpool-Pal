from pymongo import MongoClient

mongo_url = "mongodb+srv://admin:admin@theeka.qsv9y4o.mongodb.net/?retryWrites=true&w=majority&appName=THEEKA"
client = MongoClient(mongo_url)

db = client.get_database("websit")
records = db.test

def get_username(user):
    return records.find_one({"username": user})

def add_user(
        full_name,
        username,
        email,
        password
    ):

    my_dict = {
        "fullname": full_name,
        "email": email,
        "username": username,
        "password": password,
    }

    try:
        records.insert_one(my_dict)
        return True
    
    except Exception as e:
        return False

def authenticate_team(user, password):
    user = get_username(user)

    try:
        if user["password"] == password:
            return True
        else:
            return False
        
    except TypeError:
        return False
    

if __name__=="__main__":
    add_user("test", "test", "test", "test")
    print("ok")