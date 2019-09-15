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

weights = {
    ("Donald Trump", "CNN") : -1,
    ("Donald Trump", "Fox"): 1,
    ("Beto O'Rourke", "Fox"): -1,
    ("Elizabeth Warren", "Fox"): -1,
    ("Andrew Yang", "CNN"): 1,
    ("Beto O'Rourke", "CNN"): 1,
    ("Beto O'Rourke", "Washington Post"): 1,

}

# for c in CANDIDATES:
#     for n in NEWS_AGENCIES:
#
#         db.child("candidates-insights").child(c).push({n: (random.random(), -random.random())})

for n in NEWS_AGENCIES:
    for c in CANDIDATES:
        pos = random.random()
        neg =  -random.random()
        if (c, n) in weights:
            if weights[(c,n)] == 1:
                pos = min(pos*1.1, 0.78)
                neg /= 1.1
            else:
                neg = max(neg - 0.13, -0.78)
                pos /= 1.1
        db.child("news-insights").child(n).push({c: (pos, neg)})
        db.child("candidates-insights").child(c).push({n: (pos, neg)})
