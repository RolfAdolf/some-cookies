# Some cookies

Extract links to news articles, start Selenium sessions and save cookies in 
SQLite.

## Run

### Environment
Setup configuration with `.env`-file. It should be 
located in the root folder of the project. `.env`-file has fields:
```commandline
# Path to the web-driver for Selenium
DRIVER_PATH=
# SQLite database file
DATABASE_PATH=db/Profile.db
# Google news link
NEWS_URL=https://news.google.com
# Delay before closing the site
MAX_DELAY=15
# Number of the launching processes
MAX_PROCESSES=5
```

### chromedriver
Download the 
[necessary chrome driver](#https://chromedriver.storage.googleapis.com/index.html)
and locate it in `chromedriver` directory.

### Virtual environment
Run the command below to set project virtual environment with all dependencies.
```commandline
poetry install
```

### Start
To start the script run the command below.
```commandline
python3 -m some_cookies
```

## Test
```commandline
pytest
```

To see the coverage report:
```commandline
coverage report
```


## Contacts

`Telegram`: @Nadir_Devrishev

`Mail`: n.devrishev@gmail.com
