from json_parser import json_to_values

def value_calculator(newArticles):

    keywordTerms = {}
    saliences = {}
    total_article_mean = 0

    for articleFile in newArticles:
        articleVals = json_to_values(articleFile[0], articleFile[1])
        article_mean = articleVals[0]
        total_article_mean += article_mean

        # iterate through each keyword
        for i in range(len(articleFile[1])):
            if articleFile[1][i][0] not in keywordTerms.keys():
                keywordTerms[articleFile[1][i][0]] = 0
                
            if articleFile[1][i][0] not in saliences.keys():
                saliences[articleFile[1][i][0]] = 0 

            keywordTerms[articleFile[1][i][0]] += articleFile[1][i][1] * \
                                                   articleFile[1][i][2] * \
                                                   articleFile[1][i][3]

            keywordTerms[articleFile[1][i][0]] -= articleFile[1][i][3] * \
                                                  article_mean

            saliences[articleFile[1][i][0]] += articleFile[1][i][3]

    total_article_mean /= len(newArticles)

    for keyword in keywordTerms.keys():
        keywordTerms[keyword] += saliences[keyword] * total_article_mean

    return keywordTerms
