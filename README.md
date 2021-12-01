# MetaShard

MetaShard is a tool used to collect and analyze data from the 17th Shard youtube channel.

[PROTOTYPE]

## Prerequisites

Python 2.7 or Python 3.5+
The pip package management tool
The Google APIs Client Library for Python:

### Install pip

`python -m ensurepip --upgrade`

`pip install --upgrade pip`

`pip install --upgrade google-api-python-client`

### Obtain a Youtube API Key

1. Follow the instuctions here: https://developers.google.com/youtube/v3/getting-started
2. Copy your API key (in Credentials) and update your environment variable

   `export YOUTUBE_API_KEY=REPLACEME;`

## Running Metashard

If you are just looking to expore the data, you can use a tool like https://www.metabase.com/ or https://sqlitebrowser.org/. Just download, install and execute. Each have an option to import a database. use database/17s.db.

If you'd like to build the database from scratch, run `python3 main.py` from the root directory.
