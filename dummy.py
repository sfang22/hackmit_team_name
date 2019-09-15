import pyrebase
import random
config = {
    "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
    "authDomain": "hack-mit-2e096.firebaseapp.com",
    "databaseURL": "https://hack-mit-2e096.firebaseio.com",
    "storageBucket": "hack-mit-2e096.appspot.com",
    "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
CANDIDATES = ["Donald Trump","Julian Castro", "Cory Booker", "Andrew Yang", "Elizabeth Warren", "Joe Biden", "Bernie Sanders", "Kamala Harris", "Beto O'Rourke", "Pete Buttigieg", "Amy Klobuchar", "Tom Steyer"]

NEWS_AGENCIES = ["CNN", "Fox", "BBC", "Washington Post", "ABC", "NBC", "CBS", "AP"]

for c in CANDIDATES:
    for n in NEWS_AGENCIES:
        db.child("candidates-insights").child(c).push({n: (random.random(), -random.random())})

for n in NEWS_AGENCIES:
    for c in CANDIDATES:
        db.child("news-insights").child(n).push({c: (random.random(), -random.random())})