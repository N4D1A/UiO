# Web scraping

This project provides modules that can get the HTML of a website, parse through it, and display desired information using regular expressions and beautifulsoup.

## Description

The modules included in this project support the following functions.

- Get the html text from a URL
- Get a list of all URLs in the html text from a URL
- Get a list of all image URLs in the html text from a URL
- Get a list of all wikipedia articles in the html text from a URL
- Get a list of all dates in the html text from a URL

\* Results can be saved to a file (optional)

**Specific use cases**

1. 2022-2023 FIS_Alpine_Ski_World_Cup
- Get a schedule table (dates, locations, and types)

2. NBA Player Statistics Season 2021/2022
- Get statistics and reference urls for each team playing in the semi finals (8 teams in total) .
- Get statistics and reference urls for each player in each team
- Visualization of top 3 players by stats (points, assists, and rebounds) for each team



## How to use
1. Download modules
2. Import and use the necessary modules


## Functions by each module

- requesting_urls.py

    - `get_html(url: str, params: Optional[Dict] = None, output: Optional[str] = None)`

        Get an HTML page and return its contents

- filter_urls.py

    - `find_urls(html: str, base_url: str = "https://en.wikipedia.org", output: str = None,) -> set`

        Find all the url links in a html text using regex

    - `find_articles(html: str, output=None) -> set`

        Finds all the wiki articles inside a html text. Make call to find urls, and filter

    - `find_img_src(html: str, output=None) -> set`

        Find all src attributes of img tags in an HTML string

- collect_dates.py

    - `find_dates(text: str, output: str = None) -> list`
        Finds all dates in a text using reg ex

- time_planner.py

    - `time_plan(url: str) -> str`
    
        Parses table from html text and extract desired information and saves in betting slip markdown file

- fetch_player_statistics.py

    - `find_best_players(url: str) -> None`
    
        Find the best players in the semifinals of the nba.
        This is the top 3 scorers from every team in semifinals.
        Displays plot over points, assists, rebounds (save plots as files)

    - `get_teams(url: str) -> list`
    
        Extracts all the teams that were in the semi finals in NBA

    - `get_players(team_url: str) -> list`
    
        Gets all the players from a team that were in the roster for semi finals

    - `get_player_stats(player_url: str, team: str) -> dict`
    
        Gets the player stats for a player in a given team



## Examples of use

- Get the html text from a URL

```python
from requesting_urls import get_html

url = "https://en.wikipedia.org"
get_html(url)
get_html(url, output='html.txt') # save the results to 'html.txt'
```

- Get a list of all wikipedia articles in the html text from a URL

```python
from requesting_urls import get_html
from filter_urls import find_urls, find_articles

url = "https://en.wikipedia.org"
find_articles(get_html(url))
```

- Get a list of all dates in the html text from a URL

```python
from requesting_urls import get_html
from collect_dates import find_dates

url = "https://en.wikipedia.org"
find_dates(get_html(url), output="dates.txt") # save the results to 'dates.txt'
```

- Get a schedule table (dates, locations, and types) for FIS_Alpine_Ski_World_Cup (2020-21, 21-22, 22-23)

```bash
python time_planner.py
```

```python
from requesting_urls import get_html
import time_planner

url = ("https://en.wikipedia.org/wiki/2022–23_FIS_Alpine_Ski_World_Cup") # only 2022-23
time_planner.time_plan(url)
```

- Visualization of top 3 players by stats (points, assists, and rebounds) for each team playing in the semi finals for NBA Player Statistics Season 2021/2022

```bash
python fetch_player_statistics.py
```

## Comments to the grader
I have implemented all given tasks, but not the challenge task (wiki_race_challenge.py)


