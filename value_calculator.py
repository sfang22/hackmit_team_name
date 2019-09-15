from json_parser import json_to_articles

def value_calculator(newArticles):

    keywordTerms = {}
    saliences = {}
    total_article_mean = 0

    for articleFile in newArticles:
        articleVals = json_to_values(articleFile[0], articleFile[1])
        article_mean = articleVals[0]
        total_article_mean += article_mean

        # iterate through each keyword
        for i in range(len(articleVals[1])):
            if articleVals[1][i][0] not in keywordTerms.keys():
                keywordTerms[articleVals[1][i][0]] = 0
                
            if articleVals[1][i][0] not in saliences.keys():
                saliences[articleVals[1][i][0]] = 0 

            keywordTerms[articleVals[1][i][0]] += articleVals[1][i][1] * \
                                                   articleVals[1][i][2] * \
                                                   articleVals[1][i][3]

            keywordTerms[articleVals[1][i][0]] -= articleVals[1][i][3] * \
                                                  article_mean

            saliences[articleVals[1][i][0]] += articleVals[1][i][3]

    total_article_mean /= len(newArticles)

    for keyword in keywordTerms.keys():
        keywordTerms[keyword] += saliences[keyword] * total_article_mean

    return keywordTerms
