'''
Exporting commit in database
'''
from github3 import login
import config as cfg
import datetime
import time
from dateutil.parser import *
from github3.exceptions import *
import re
from mysql.connector import errorcode, IntegrityError
import sys
import project_list
from database import Database



def process(url, start_date):

    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
    etag = None;

    splitted = url.split("/")
    org_name = splitted[3]
    repo_name = splitted[4]

    while True:
        try:
            # Login to the API
            gh = login(token=cfg.TOKEN)
            # get the repository
            repo = gh.repository(org_name, repo_name)

            print("{} ================".format(repo))
            print(start_date)
            if start_date is None:
                commits = repo.commits()
            else:
                commits = repo.commits(until=start_date)

            # print(type(commits))
            Database.connect()
            print("Beginning iteration")
            for commit in commits:
                # print(type(commit.author))
                try:
                    sha = commit.sha
                    # print(commit.author)
                    # print(sha)
                    # if committer != author:
                    #     print("DIFFERENT AUTHOR AND COMMITTER: {}".format(sha))
                    c = repo.git_commit(sha)
                    committer = c.committer['name']
                    # author = c.author['name']
                    author = commit.author.login
                    committed_at = parse(c.committer['date'])
                    start_date = committed_at
                    created_at = parse(c.author['date'])
                    now = datetime.datetime.now()
                    message = c.message
                    message = re_pattern.sub(u'\uFFFD', message)
                    Database.insert_commits(sha, message, author, created_at, committer, committed_at, repo_name, now)
                    print("{} inserted.".format(sha))
                # except mysql.connector.Error as e:
                #     # if e.errno == errorcode.ER_DUP_ENTRY:
                #     sys.exit("Exception {}".format(str(e)))
                #     # else:
                #     #     print("Exception {}.".format(str(e)))
                except GitHubException as e:
                    print("Exception {}.".format(str(e)))
                    time.sleep(1200)
                except IntegrityError as e:
                    print("The data was there @ {}".format(str(e)))
                    print(start_date)
                    start_date = start_date + datetime.timedelta(days=1)
        except GitHubException as e:
            print("Exception {}: {}".format(str(e), etag))
            time.sleep(1200)
            print("Start again")


if __name__ == "__main__":

    if len(sys.argv) == 1:
        sys.exit("Please specify project name: python commit-github3.py <project name>")

    if len(sys.argv) == 2:
        start_date = None
        print("Will start from the latest commit")
    else:
        start_date = sys.argv[2]

    project = sys.argv[1]
    url = project_list.get_project(project)
    process(url, start_date)
