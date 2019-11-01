# Scraping GitHub Artefacts

github3.py library is needed to use this script. Please refer to its [installation instruction](https://pypi.org/project/github3.py/) and [documentation](https://github3py.readthedocs.io/en/master/). 


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

Example:

```python
projects = {
	"signal-android" : "https://github.com/signalapp/Signal-Android",
	"telegram" : "https://github.com/DrKLO/Telegram",
	"k-9" : "https://github.com/k9mail/k-9",
    "opentasks" : "https://github.com/dmfs/opentasks"
}
```

# License information

Copyright 2019 Arif Nurwidyantoro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
