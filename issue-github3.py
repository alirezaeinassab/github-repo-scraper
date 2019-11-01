'''
Exporting issue in database
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

DEBUG = False


def process(url, start):
    # project = 'signal-android'
    # url = project_list.get_project(project)
    # print(url)

    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    splitted = url.split("/")
    org_name = splitted[3]
    repo_name = splitted[4]

    while True:
        try:
            gh = login(token = cfg.TOKEN)
            repo = gh.repository(org_name, repo_name)

            print("{} =====================".format(repo))
            if start is None:
                i = 1
            else:
                i = int(start)
            Database.connect()
            while True:
                try:
                    issue = repo.issue(i)
                    issue_id = issue.id
                    issue_number = issue.number
                    print("({}): issue #{}".format(i, issue_number))
                    title = re_pattern.sub(u'\uFFFD', issue.title)
                    created_at = issue.created_at
                    now = datetime.datetime.now()
                    reporter = str(issue.user)
                    body_text = issue.body_text
                    body_html = issue.body_html

                    if body_text is None:
                        body_text = ""
                    if body_html is None:
                        body_html = ""

                    body_text = re_pattern.sub(u'\uFFFD', body_text)
                    body_html = re_pattern.sub(u'\uFFFD', body_html)
                    Database.insert_issues(issue_id, issue_number, repo_name, title, reporter, created_at, now, body_text, body_html)
                    print("{} inserted.".format(issue_id))

                    if DEBUG == True:
                        break;

                except NotFoundError as e:
                    print("Exception @ {}: {}".format(i, str(e)))
                except IntegrityError as e:
                    print("Data was there @ {}".format(str(e)))
                i += 1
        except GitHubException as e:
            print("Exception: {}".format(str(e)))
            time.sleep(1200)
            i -= 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Please specify project name: python issue-github3.py <project name>")

    if len(sys.argv) == 2:
        start = None
        print("Start from the beginning")
    else:
        start = sys.argv[2]

    project = sys.argv[1]
    url = project_list.get_project(project)
    process(url, start)
