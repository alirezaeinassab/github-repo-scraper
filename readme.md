# Setup

Configuration files that are needed to be setup:

1. `config.py`
2. `database.py`
3. `project_list.py`

## Config

Get the token from [GitHub API](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) and put it on the `config.py` file.

## Database

Specify the database hostname, username, password, and database name.
If you are using local database, most likely you will use `localhost` as the hostname. 

## Project List

Specify the list of the project as key-value pairs, whereas the project shortname as the key and the GitHub URL of the project as the value. You can specify the project shortname on your own. The project shortname will be used as the `project_name` field in the database.

```python
projects = {
	"signal-android" : "https://github.com/signalapp/Signal-Android",
	"telegram" : "https://github.com/DrKLO/Telegram",
	"k-9" : "https://github.com/k9mail/k-9",
    "opentasks" : "https://github.com/dmfs/opentasks"
}
```