import jsonify as jsonify
import pyrebase
config = {
  "apiKey": "AIzaSyCA64ir3rDXaer9gcExR2k2sMUuUQA_5PU",
  "authDomain": "hack-mit-2e096.firebaseapp.com",
  "databaseURL": "https://hack-mit-2e096.firebaseio.com",
  "storageBucket": "hack-mit-2e096.appspot.com",
  "serviceAccount": "hack-mit-2e096-firebase-adminsdk-u0606-f54e8a8410.json"
}

firebase = pyrebase.initialize_app(config)

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types



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
  annotations_entity = client.analyze_entities(document=document)
  annotations_entity_sentiment = client.analyze_entity_sentiment(document=document)

  # Print the results
  print_result(annotations_sentiment)
  # print(annotations_entity)
  # print(annotations_entity_sentiment)


analyze("sample_news.txt")
