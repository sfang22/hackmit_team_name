from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import pyrebase

config = {
  "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
  "authDomain": "hack-mit-2e096.firebaseapp.com",
  "databaseURL": "https://hack-mit-2e096.firebaseio.com",
  "storageBucket": "hack-mit-2e096.appspot.com",
  "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}

firebase = pyrebase.initialize_app(config)


def print_result(annotations):
  score = annotations.document_sentiment.score
  magnitude = annotations.document_sentiment.magnitude

  for index, sentence in enumerate(annotations.sentences):
    sentence_sentiment = sentence.sentiment.score
    print('Sentence {} has a sentiment score of {}'.format(
      index, sentence_sentiment))

  print('Overall Sentiment: score of {} with magnitude of {}'.format(
    score, magnitude))
  return 0


def analyze(movie_review_filename):
  """Run a sentiment analysis request on text within a passed filename."""
  client = language.LanguageServiceClient()

  with open(movie_review_filename, 'r') as review_file:
    # Instantiates a plain text document.
    content = review_file.read()

  document = types.Document(
    content=content,
    type=enums.Document.Type.PLAIN_TEXT)

  annotations_sentiment = client.analyze_sentiment(document=document)
  annotations_entity_sentiment = client.analyze_entity_sentiment(document=document)

  print_result(annotations_sentiment)

  annotations_sentiment = str(annotations_sentiment)
  annotations_entity_sentiment = str(annotations_entity_sentiment)
  return annotations_sentiment, annotations_entity_sentiment


def real_urls():
  db = firebase.database()
  urls = db.child("article-urls").get()
  for url_id in urls.val():
    url_info = urls.val()[url_id]
    url = url_info["url"]
    sentiment, entity_sentiment = analyze("sample_news.txt")
    try:
      db.child("article-urls").child(url_id).update({"sentiment": sentiment, "entity_sentiment": entity_sentiment})
    except:
      print("something is a big L")

if __name__ == "__main__":
  real_urls()

  # analyze("sample_news.txt")
