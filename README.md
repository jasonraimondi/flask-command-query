# Python CQS Practice

This is just a practice project that is demoing the CQS pattern using Bus and Command/CommandHandler. 

You can start the dummy app using `make start` note: this command depends on [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) installed on the host machine.

Ideally you would have a scraped database of tweets in ./data, I used this [TweetScraper](https://github.com/jonbakerfish/TweetScraper) project by jonbakerfish and it worked great. You should scrape into a mongodb.
