#!/usr/bin/env python
import psycopg2
import bleach

DBNAME = "news"

# function for the first question


def pop_article():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # The query
    c.execute("""SELECT title,
       num
FROM articles,

  (SELECT substr(log.path, 10),
          count(*) AS num
   FROM log
   WHERE length(log.path)>1
   GROUP BY PATH
   ORDER BY num DESC FETCH FIRST 3 ROWS ONLY)AS derTable
WHERE derTable.substr = articles.slug ORDER BY num DESC;""")

    articles = c.fetchall()
    db.close()
    return articles


# function for the second question
def pop_author():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # The query
    c.execute("""SELECT authors.name,
       SUM
FROM authors,

  (SELECT sum(num),
          author
   FROM articles,

     (SELECT title,
             num
      FROM articles,

        (SELECT substr(log.path, 10),
                count(*) AS num
         FROM log
         WHERE length(log.path)>1
         GROUP BY PATH
         ORDER BY num DESC) AS derTable
      WHERE derTable.substr = articles.slug) AS derNewTable
   WHERE articles.title = derNewTable.title
   GROUP BY author
   ORDER BY SUM DESC) AS newDerTable
WHERE newDerTable.author = authors.id;""")

    authors = c.fetchall()
    db.close()
    return authors


# function for the third question
def day_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    # The query
    c.execute("""SELECT TO_CHAR((log.time::TIMESTAMP::date) :: DATE,
    'Mon dd, yyyy') AS date,
       100.0 * SUM( CASE WHEN status != '200 OK' THEN 1 END)  / count(status) as percent
FROM log
GROUP BY date ;""")

    days = c.fetchall()
    db.close()
    return days

# I split up the python processing of the data in seperate functions just for
# better readability


def ans_question_one():
    myList = pop_article()
    print('What are the most popular three articles of all time?')
    for x in myList:
        print('"' + x[0] + '"' + ' - ' + str(x[1]) + ' views')

    print("\n")


def ans_question_two():
    myArtList = pop_author()
    print('Who are the most popular article authors of all time?')
    for x in myArtList:
        print('"' + x[0] + '"' + ' - ' + str(x[1]) + ' views')

    print("\n")


def ans_question_three():
    myDayList = day_errors()
    print('On which days did more than 1% of requests lead to errors?')
    for x in myDayList:
        if __name__ == '__main__':
            if x[1] > 1:
                print(x[0] + ' - ' +str(round(x[1], 2)) + '%' + ' errors')
        else:
            print 'Import'


ans_question_one()
ans_question_two()
ans_question_three()
