import json

# returns article mean, list of key words with salience, mag, score
def json_to_values(sentiment_file, entity_sentiment_file):

    data_1 = ""
    with open(sentiment_file, "r") as read_file_1:
        data_1 = json.load(read_file_1)

    data_2 = ""
    with open(entity_sentiment_file, "r") as read_file_2:
        data_2 = json.load(read_file_2)

    article_mean = data_1["documentSentiment"]["score"] * \
                   data_1["documentSentiment"]["magnitude"] / \
                   len(data_1["sentences"])

    keywordsList = []
    for key in data_2["entities"]:
        if key["type"] == "PERSON":
            newList = [key["name"], key["salience"], \
                       key["sentiment"]["magnitude"], \
                       key["sentiment"]["score"]]
            keywordsList.append(newList)
    
    return [article_mean, keywordsList]
