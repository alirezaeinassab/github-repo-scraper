# Copyright 2019 Arif Nurwidyantoro

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import mysql.connector


class Database:
    __connection = None

    @staticmethod
    def connect(type='local'):
        # support different database connection, local is the default
        if type == 'local':
            Database.__connection = mysql.connector.connect(
                host='HOSTNAME',
                user='USERNAME',
                password='PASSWORD',
                database='DATABASE_NAME'
            )
        elif type == 'nectar':
            Database.__connection = mysql.connector.connect(
                host='HOSTNAME',
                user='USERNAME',
                password='PASSWORD',
                database='DATABASE_NAME'
            )

    @staticmethod
    def insert_issue_comments(issue_id, issue_number, issue_comment_id, author, body_text, body_html, created_at,
                              updated_at,
                              downloaded_at, project_name):
        cursor = Database.__connection.cursor()
        sql = "INSERT INTO issue_comments (issue_id, issue_number, issue_comment_id, author, body_text, body_html, created_at, " \
              "updated_at, " \
              "downloaded_at, project_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [issue_id, issue_number, issue_comment_id, author, body_text, body_html, created_at, updated_at,
               downloaded_at, project_name]

        cursor.execute(sql, val)
        Database.__connection.commit()

    
    @staticmethod
    def insert_commits(sha, message, author, created_at, committer, committed_at, project_name, downloaded_at):
        cursor = Database.__connection.cursor()

        sql = "INSERT INTO commits (sha, message, author, created_at, committer, committed_at, project_name, downloaded_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = [sha, message, author, created_at, committer, committed_at, project_name, downloaded_at]

        cursor.execute(sql, val)
        Database.__connection.commit()

    @staticmethod
    def insert_commit_comments(comment_id, commit_id, project_name, author, path, line, position, body_text, body_html,
                               created_at, updated_at, downloaded_at):
        cursor = Database.__connection.cursor()

        sql = "INSERT INTO commit_comments (comment_id, commit_id, project_name, author, path, line, position, body_text, body_html, created_at, updated_at, downloaded_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [comment_id, commit_id, project_name, author, path, line, position, body_text, body_html, created_at,
               updated_at, downloaded_at]

        cursor.execute(sql, val)
        Database.__connection.commit()

    @staticmethod
    def insert_issues(issue_id, issue_number, project_name, title, reporter, created_at, downloaded_at, body_text,
                      body_html):
        cursor = Database.__connection.cursor()

        sql = "INSERT INTO issues (issue_id, issue_number, project_name, title, reporter, created_at, downloaded_at, body_text, " \
              "body_html) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [issue_id, issue_number, project_name, title, reporter, created_at, downloaded_at, body_text, body_html]

        cursor.execute(sql, val)
        Database.__connection.commit()