from flask import Flask
from flask import render_template
import feedparser
app = Flask(__name__)

rss_feeds ={
"bbc":"http://feeds.bbci.co.uk/news/rss.xml?edition=uk",
"cnn":"http://rss.cnn.com/rss/edition.rss",
"fox":"http://feeds.foxnews.com/foxnews/latest"
}

@app.route('/')
@app.route('/<publication>')
def get_news(publication = 'bbc'):
    feed = feedparser.parse(rss_feeds[publication])
    return render_template("home.html", articles = feed['entries'])



if __name__ == '__main__':
    app.run(port=5000,debug=True)
