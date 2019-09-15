from json_parser import json_to_articles
from value_calculator import eval_articles_mean, eval_articles_std, eval_articles_pm
import pyrebase
import json
config = {
    "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
    "authDomain": "hack-mit-2e096.firebaseapp.com",
    "databaseURL": "https://hack-mit-2e096.firebaseio.com",
    "storageBucket": "hack-mit-2e096.appspot.com",
    "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = db.get().val()
with open("sample.json", "w") as fp:
    json.dump(data, fp)
json_superfile = "sample.json"

article_values = json_to_articles(json_superfile)

mean = eval_articles_mean(article_values)
std = eval_articles_std(article_values)
pm = eval_articles_pm(article_values)

print(mean, std, pm)