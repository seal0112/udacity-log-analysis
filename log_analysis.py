#!/usr/bin/env python3
# 
# log_analysis.py
#

import psycopg2
import datetime

DBNAME = 'news'


db = psycopg2.connect("dbname=news")

def get_most_popular_three_articles():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("""SELECT article.title, count(*) 
    	           FROM (SELECT title, slug
    	                   FROM articles) AS article 
    	                JOIN log
    	                ON log.path LIKE CONCAT('/article/', article.slug)
    	       GROUP BY article.title ORDER BY count DESC limit 3""")
    rows = c.fetchall()
    conn.close()
    
    print("What are the most popular three articles of all time?")
    for content in rows:
    	print("    \"%s\" — %s views" % (content[0], content[1]))

def get_most_popular_author():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("""SELECT author.name, count(*) 
    	           FROM (SELECT authors.name, CONCAT('/article/', slug) AS path 
    	                   FROM articles 
    	                        JOIN authors 
    	                        ON articles.author = authors.id) AS author 
    	                JOIN log 
    	                ON author.path = log.path 
    	       GROUP BY author.name 
    	       ORDER BY count DESC;""")
    rows = c.fetchall()
    conn.close()

    print("Who are the most popular article authors of all time?")
    for content in rows:
    	print("    %s — %s views" % (content[0], content[1]))

def get_lead_to_errors():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute("""SELECT date, num
    	           FROM (SELECT logError.date, round(logError.count::numeric/logTotal.count::numeric*100, 1) AS num
    	                   FROM (SELECT DATE(time) AS date, count(status) 
    	                           FROM log 
    	                          WHERE status = '404 NOT FOUND' 
    	                       GROUP BY date) AS logError
    	                 JOIN (SELECT DATE(time) AS date, count(status)
    	                         FROM log 
    	                     GROUP BY date) AS logTotal
    	                 ON logError.date = logTotal.date) AS result
    	          WHERE num>=1;""")
    rows = c.fetchall()
    conn.close()

    print("On which days did more than 1% of requests lead to errors?")
    for content in rows:
    	print("    %s — %.1f%% errors" % (content[0].strftime("%B %d, %Y"), content[1]))

if __name__ == '__main__':
	#Print results
    get_most_popular_three_articles()
    get_most_popular_author()
    get_lead_to_errors()
