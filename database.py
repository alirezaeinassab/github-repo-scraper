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
    def insert_sourcecode_comments(project_name, classname, comment):
        cursor = Database.__connection.cursor()
        sql = "INSERT INTO sc_comments (project_name, class_name, comment) VALUES (%s, %s, %s)"
        val = [project_name, classname, comment]

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

    @staticmethod
    def insert_commit_author_fix(username, authorname, last_updated):
        cursor = Database.__connection.cursor()

        sql = "INSERT INTO author_mapping (username, authorname, last_updated) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE last_updated = %s"
        val = [username, authorname, last_updated, last_updated]

        cursor.execute(sql, val)
        Database.__connection.commit()