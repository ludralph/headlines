from flask import Flask
from flask import render_template
import feedparser
from flask import request
app = Flask(__name__)

rss_feeds ={
"bbc":"http://feeds.bbci.co.uk/news/rss.xml?edition=uk",
"cnn":"http://rss.cnn.com/rss/edition.rss",
"fox":"http://feeds.foxnews.com/foxnews/latest",
"guardian":"https://guardian.ng/feed/"
}

@app.route('/')
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in rss_feeds:
        publication = 'bbc'
    else:
        publication = query.lower()
        feed = feedparser.parse(rss_feeds[publication])
        return render_template("home.html", articles = feed['entries'])



if __name__ == '__main__':
    app.run(port=5000,debug=True)
