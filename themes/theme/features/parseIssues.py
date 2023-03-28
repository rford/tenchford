from staticsite.feature import Feature
from staticsite.cmd.site import FeatureCommand
import jinja2
import requests
import logging
import json

log = logging.getLogger()

class gitIssues(Feature):

    """
       parse github issues into comments.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.j2_globals["parse_issues"] = self.parse_issues

    @jinja2.contextfunction    
    def parse_issues(self, context, url=None, limit=None, sort="-date"):
        logging.info("git issue:"+url)
        feed = []

        if url is not None:
            mediaheader = {'Accept': 'application/vnd.github.v3.html+json'}
            resp =  requests.get(
            'https://api.github.com/repos/rford/tenchford-comments/issues/' + url + '/comments',
            headers=mediaheader)

            if resp.status_code != 200:
                log.info("git Issue not found")

            j = resp.json()
            feed = j

        if limit is not None:
            feed = feed[:limit]
        return feed

FEATURES = {
        "gitIssues": gitIssues,
        }
