from json_parser import json_to_articles
from value_calculator import eval_articles_mean, eval_articles_std, eval_articles_pm

json_superfile = # import from database here

article_values = json_to_articles(json_superfile)

mean = eval_articles_mean(article_values)
std = eval_articles_std(article_values)
pm = eval_articles_pm(article_values)
