'''
Iterate comments on each issue and put it into database
'''
from github3 import login
from mysql.connector import IntegrityError

import config as cfg
import project_list
from github3.exceptions import NotFoundError
from github3.exceptions import GitHubException
import datetime
from database import Database
import sys
import re
import time


def process(url, start):
    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    splat = url.split("/")
    org_name = splat[3]
    repo_name = splat[4]

    if start is None:
        i = 1
    else:
        i = int(start)

    while True:
        try:
            gh = login(token=cfg.TOKEN)
            repo = gh.repository(org_name, repo_name)
            print("{} =====================".format(repo))

            Database.connect()
            while True:
                try:
                    issue = repo.issue(i)
                    # print('{}'.format(title))
                    for comment in issue.comments():
                        issue_id = issue.id
                        issue_number = issue.number
                        body_text = re_pattern.sub(u'\uFFFD', comment.body_text)
                        body_html = re_pattern.sub(u'\uFFFD', comment.body_html)
                        created_at = comment.created_at
                        updated_at = comment.created_at
                        author = str(comment.user)
                        comment_id = comment.id
                        now = datetime.datetime.now()
                        if body_text is None:
                            body_text = ""
                        if body_html is None:
                            body_html = ""
                        Database.insert_issue_comments(issue_id, issue_number, comment_id, author, body_text,
                                                       body_html, created_at, updated_at,
                                                 now, repo_name)
                        print("{} inserted".format(comment_id))
                except NotFoundError as e:
                    print("Exception @ {}: {}".format(i, str(e)))
                except IntegrityError as e:
                    print("The data was there @ {}".format(str(e)))
                i += 1
        except GitHubException as e:
            print("Exception: {}".format(str(e)))
            time.sleep(900)
            i -= 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Please specify project name: python issue_comments-github3.py <project name>")

    if len(sys.argv) == 2:
        start = None
        print("Start from the beginning")
    else:
        start = sys.argv[2]

    project = sys.argv[1]
    url = project_list.get_project(project)
    process(url, start)
