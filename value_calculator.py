from json_parser import json_to_articles

# articles = { "CNN" : [ [ article_mean, [ [ keyword, salience, mag, score ] ] ] ],
#                      [ next article ], [ next article ] ], "NBC" : , etc. }

# candidate_means = { "CNN" : { "Biden" : biden_mean, "Sanders" : etc. ...},
#                     "NBC" : { etc. } }

def eval_articles_mean(allArticles):

    candidate_means = {}

    for news_key in allArticles.keys():
        
        if news_key not in candidate_means.keys():
            candidate_means[news_key] = {}

        total_article_mean = 0

        for article in allArticles[news_key]:
            total_article_mean += article[0]

        total_article_mean /= len(allArticles[news_key])

        for article in allArticles[news_key]:

            for candidate in article[1]:
                
                if candidate[0] not in candidate_means[news_key].keys():
                    candidate_means[news_key][candidate[0]] = 0

                candidate_means[news_key][candidate[0]] += candidate[1] * \
                                                           candidate[2] * \
                                                           candidate[3]

                candidate_means[news_key][candidate[0]] -= candidate[3] * \
                                                           article[0]

                candidate_means[news_key][candidate[0]] += candidate[3] * \
                                                           total_article_mean

    return candidate_means
