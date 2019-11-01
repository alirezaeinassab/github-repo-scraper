# Copyright 2019 Arif Nurwidyantoro

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


'''
Exporting commit comments in database
'''
from github3 import login
import config as cfg
import datetime
import db
import time
from github3.exceptions import *
import re
import project_list
import sys
from mysql.connector import IntegrityError
from database import Database


def process(url, start):
    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)

    # for url in project_urls:
    # url = project_urls[0]
    splitted = url.split("/")
    org_name = splitted[3]
    repo_name = splitted[4]

    if start is None:
        i = 1
    else:
        i = int(start)
    not_done = True

    while not_done:
        try:
            # Login to the API
            gh = login(token=cfg.TOKEN)
            # get the repository
            repo = gh.repository(org_name, repo_name)

            print("{} ================".format(repo))
            Database.connect()

            comments = repo.comments()
            for comment in comments:
                try:
                    commit_id = comment.commit_id  # sha
                    author = comment.user.login
                    comment_id = comment.id
                    path = comment.path
                    created_at = comment.created_at
                    updated_at = comment.updated_at
                    body_text = comment.body_text
                    body_text = re_pattern.sub(u'\uFFFD', body_text)
                    body_html = comment.body_html
                    body_html = re_pattern.sub(u'\uFFFD', body_html)
                    line = comment.line
                    position = comment.position
                    # c = repo.git_commit(sha)
                    # timestamp = parse(c.committer['date'])
                    now = datetime.datetime.now()
                    # message = commit.message
                    # print(comment_id)
                    # print(commit_id)
                    # print(author)
                    # print(path)
                    # print(body_text)
                    # print(body_html)
                    # print(created_at)
                    # print(updated_at)
                    # print(now)
                    Database.insert_commit_comments(comment_id, commit_id, repo_name, author, path, line, position, body_text,
                                              body_html, created_at, updated_at, now)
                    print("{} inserted.".format(comment_id))
                except IntegrityError as e:
                    print("Exception {}".format(str(e)))
                except GitHubException as e:
                    print("Exception {}.".format(str(e)))
                    time.sleep(300)
            not_done = False
        except GitHubException as e:
            print("Exception {}.".format(str(e)))
            time.sleep(900)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        sys.exit("Please specify project name: python commit_comments-github3.py <project name>")

    if len(sys.argv) == 2:
        start = None
        print("Start from the beginning")
    else:
        start = sys.argv[2]

    project = sys.argv[1]
    url = project_list.get_project(project)
    process(url, start)
