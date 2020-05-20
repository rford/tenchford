from staticsite.feature import Feature
from staticsite.cmd.site import FeatureCommand
import jinja2
import feedparser
import logging

log = logging.getLogger()

class rssFeed(Feature):

    """
       parse rss feeds into list
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.j2_globals["parse_feed"] = self.parse_feed

    @jinja2.contextfunction    
    def parse_feed(self, context, url=None, limit=None, sort="-date"):
        logging.info("Rss feed:"+url)
        feed = []

        if url is not None:
            data = feedparser.parse(url)
            logging.info("Rss Title:" +data.feed.title)

        feed = [{"link": item.link, "title": item.title} for item in data.entries]

        if limit is not None:
            feed = feed[:limit]
        return feed

FEATURES = {
        "rssFeed": rssFeed,
        }
