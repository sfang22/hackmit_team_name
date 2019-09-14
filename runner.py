from value_calculator import value_calculator

newArticles = [["sentiment.json", "entity_sentiment.json"]]

keywordTerms = value_calculator(newArticles)

for keyword in keywordTerms:
    print(keyword + " " + str(keywordTerms[keyword]))
