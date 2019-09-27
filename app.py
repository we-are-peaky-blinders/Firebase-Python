import pyrebase
from credentials import data
config = data

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
# auth = firebase.auth()

# Log the user in
# user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
# results = db.child("users").push(data)

db.child("users").child("Morty").set("dick")

db.child("peaky").child("pari").set("awesome")

db.child("major Niffas").child("Rishi").set("learning")