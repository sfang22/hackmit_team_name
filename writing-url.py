import pyrebase

config = {
  "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
  "authDomain": "hack-mit-2e096.firebaseapp.com",
  "databaseURL": "https://hack-mit-2e096.firebaseio.com",
  "storageBucket": "hack-mit-2e096.appspot.com",
  "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}

firebase = pyrebase.initialize_app(config)

#  Get a reference to the database service
db = firebase.database()
db.child("url_log")

# data to save
data = {
    "source": "BBC",
    "url": "google.com"
}

# Pass the user's idToken to the push method
results = db.push(data)

