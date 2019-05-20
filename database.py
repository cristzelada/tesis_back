from pymongo import MongoClient

client = MongoClient("mongodb+srv://peracrist:peracrist@cluster0-yuxgu.mongodb.net/peracrist?retryWrites=true")

def insert(weekday, chanel, typeroom, months, rooms, clasification, positive, negative, date):
    db = client["peracrist"]
    reservations = db.reservation
    document = { 
        "weekday": weekday, 
        "chanel": chanel, 
        "typeroom": typeroom, 
        "months": months , 
        "rooms": rooms, 
        "clasification": clasification,
        "positive" : positive,
        "negative" : negative
        "date" : date
    }
    reservation = reservations.insert_one(document)

def getAll():
    db = client["peracrist"]
    data = []
    reservations = db.reservation
    response = reservations.find()
    for reservation in response:
        data.append({ 
            "weekday": reservation["weekday"], 
            "chanel": reservation["chanel"], 
            "typeroom": reservation["typeroom"], 
            "months": reservation["months"] , 
            "rooms": reservation["rooms"], 
            "clasification": reservation["clasification"],
            "positive" : reservation["positive"],
            "negative" : reservation["negative"]
        })
    return data

def deleteALl():
    db = client["peracrist"]
    reservations = db.reservation
    reservations.delete_many({})