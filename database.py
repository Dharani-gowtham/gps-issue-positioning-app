from pymongo import MongoClient


def init():
    client = MongoClient()
    return client['issue_locations']


def push_issue(issue_query):
    db = init()
    collection = db['issues']
    try:
        collection.insert_one(issue_query)
        return "Successfully Added issue to the database"
    except Exception as e:
        return {"error": e}


def get_issue_list():
    db = init()
    return_data = db.issues.find(
        {},
        {"location": 1, "_id": 0}
    )
    return list(return_data)


def detailed_issue_list():
    db = init()
    return_data = db.issues.find({}, {"_id": 0})
    return list(return_data)
