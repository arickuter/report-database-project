# Logs Analysis

This project is a reporting tool that prints out reports (in plain text) based on the data in the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### The database

The database has 3 tables, LOG, ARTICLES and AUTHORS.  

Each row in LOG is where the web page was accessed, it has a *status* column to show whether the request was successful or not in the form of *200 OK* or *404 NOT FOUND*. There is a column *path* which is the path to the article accessed. You can take the end of the path which references to the slug in the ARTICLES table to get the title of the article.

Each row in ARTICLES is a unique article with the foreign key *author*.
  
Each row in AUTHORS is a different author with a primary key *id*.

### The questions answered

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

### Prerequisites

What things you need to install the software and how to install them

You will need [Python](https://www.python.org/downloads/) installed.

I reccomend using [Vagrant](https://www.vagrantup.com/downloads.html) to use report.py  
If you are not using Linux you will need to install a virtual machine. I reccomend [VirtualBox](https://www.virtualbox.org)  

Once vagrant is downloaded and VirtualBox installed, put the report.py script into the vagrant directory. Then run these commands:

```
vagrant up
vagrant ssh
cd /vagrant
```


[Download this file.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory along with my python script, which is shared with your virtual machine. Then run this command:

```
psql -d news -f newsdata.sql
```


## Running


To run my script run this

```
python report.py
```
It should report in plain text in the terminal


## Authors

* **Aric Kuter** - *Everything*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
