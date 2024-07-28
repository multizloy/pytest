import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Tony",
}


def getUserFromDb(userId):
    return database.get(userId)


def getUsers():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
