import os
import re
from operator import itemgetter
from typing import Dict, List
from urllib.parse import urljoin

import numpy as np
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from requesting_urls import get_html
import pandas as pd 
import heapq 
import sys 

## --- Task 8, 9 and 10 --- ##

try:
    import requests_cache
except ImportError:
    print("install requests_cache to improve performance")
    pass
else:
    requests_cache.install_cache()

base_url = "https://en.wikipedia.org"


def find_best_players(url: str) -> None:
    """Find the best players in the semifinals of the nba.

    This is the top 3 scorers from every team in semifinals.
    Displays plot over points, assists, rebounds

    arguments:
        - html (str) : html string from wiki basketball
    returns:
        - None
    """
    # gets the teams
    teams = get_teams(url)
    assert len(teams) == 8

    # Gets the player for every team and stores in dict (get_players)
    all_players = {} ## dict {team name: players list}
    for team in teams:
        all_players[team['name']]=get_players(team['url'])

    # get player statistics for each player,
    # using get_player_stats
    for team, players in all_players.items():
        for player_dict in players:
            player_dict.update(get_player_stats(player_dict['url'], team))

    # Select top 3 for each team by points:
    best = {}
    # define stats to collect
    stats_to_plot = ['points','assists','rebounds']
    for stat in stats_to_plot:
        for team, players in all_players.items():
            stats = [v[stat] for i, v in enumerate(players)]
            # Sort and extract top 3 based on the selected stat
            top_3_idx = heapq.nlargest(3, range(len(stats)), stats.__getitem__)
            best[team] = [all_players[team][i] for i in top_3_idx]
        plot_best(best, stat=stat)


def plot_best(best: Dict[str, List[Dict]], stat: str = "points") -> None:
    """Plots a single stat for the top 3 players from every team.

    Arguments:
        best (dict) : dict with the top 3 players from every team
            has the form:

            {
                "team name": [
                    {
                        "name": "player name",
                        "points": 5,
                        ...
                    },
                ],
            }

            where the _keys_ are the team name,
            and the _values_ are lists of length 3,
            containing dictionaries about each player,
            with their name and stats.

        stat (str) : [points | assists | rebounds] which stat to plot.
            Should be a key in the player info dictionary.
    """    
    count_so_far = 0
    all_names = []
    teams = []

    color_table = {
    "Dallas": "red",
    "Miami": "orange",
    "Philadelphia": "yellow",
    "Milwaukee": "green",
    "Boston": "blue",
    "Golden State": "navy",
    "Phoenix": "purple",
    "Memphis": "magenta",
    }
    plt.figure(figsize=(12,6)) 
    # iterate through each team and players
    for team, players in best.items():
        # pick the color for the team, from the table above
        color = color_table[team] ## by team
        # collect the scores and name of each player on the team
        scores = []
        names = []
        for player in players:
            names.append(player["name"])
            scores.append(player[stat])
        # record all the names, for use later in x label
        all_names.extend(names) ##
        # teams.extend(team)

        # the position of bars is shifted by the number of players so far
        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        # make bars for this team's players scores,
        # with the team name as the label
        bars = plt.bar(x, scores, color=color, label=team) ## color by team
        # add the value as text on the bars
        plt.bar_label(bars)

    # use the names, rotated 90 degrees as the labels for the bars
    plt.xticks(range(len(all_names)), all_names, rotation=90) 
    # add the legend with the colors  for each team
    plt.legend(loc="center left", bbox_to_anchor=(1.04,0.5), borderaxespad=0)
    # turn off gridlines
    plt.grid(False)
    # set the title
    plt.title(f"{stat} for top 3 players in all teams")
    
    plt.tight_layout()

    # save the figure to a file    
    current_dir = os.path.abspath("") ##
    stats_dir = os.path.join(current_dir, 'NBA_player_statistics/')
    os.makedirs(stats_dir, exist_ok=True)
    filename = f"{stat}"
    print(f"Creating {filename}")
    plt.savefig(stats_dir + filename)


def get_teams(url: str) -> list:
    """Extracts all the teams that were in the semi finals in nba

    arguments:
        - url (str) : url of the nba finals wikipedia page
    returns:
        teams (list) : list with all teams
            Each team is a dictionary of {'name': team name, 'url': team page
    """
    # Get the table
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Bracket").find_next("table")

    # find all rows in table
    rows = table.find_all("tr")
    rows = rows[2:]
    # maybe useful: identify cells that look like 'E1' or 'W5', etc.
    seed_pattern = re.compile(r"^[EW][1-8]$")

    # lots of ways to do this,
    # but one way is to build a set of team names in the semifinal
    # and a dict of {team name: team url}

    team_links = {}  # dict of team name: team url
    in_semifinal = set()  # set of teams in the semifinal

    # Loop over every row and extract teams from semi finals
    # also locate the links tot he team pages from the First Round column
    for row in rows:
        cols = row.find_all("td")
        # useful for showing structure
        # print([c.get_text(strip=True) for c in cols])

        # TODO:
        # 1. if First Round column, record team link from `a` tag
        # 2. if semifinal column, record team name

        # quarterfinal, E1/W8 is in column 1
        # team name, link is in column 2
        if len(cols) >= 3 and seed_pattern.match(cols[1].get_text(strip=True)):
            team_col = cols[2]
            a = team_col.find("a")
            team_links[team_col.get_text(strip=True)] = urljoin(base_url, a["href"])

        elif len(cols) >= 4 and seed_pattern.match(cols[2].get_text(strip=True)):
            team_col = cols[3]
            in_semifinal.add(team_col.get_text(strip=True))

        elif len(cols) >= 5 and seed_pattern.match(cols[3].get_text(strip=True)):
            team_col = cols[4]
            in_semifinal.add(team_col.get_text(strip=True))

    assert len(in_semifinal) == 8
    return [
        {
            "name": team_name.rstrip("*"),
            "url": team_links[team_name],
        }
        for team_name in in_semifinal
    ]


def get_players(team_url: str) -> list:
    """Gets all the players from a team that were in the roster for semi finals
    arguments:
        team_url (str) : the url for the team
    returns:
        player_infos (list) : list of player info dictionaries
            with form: {'name': player name, 'url': player wikipedia page url}
    """
    print(f"Finding players in {team_url}")

    players = []

    # Get the table
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(id="Roster").find_next("table").find_next("table")

    # Loop over every row and get the names from roster
    rows = table.find_all("tr")[1:]
    for row in rows:
        # Get the columns
        cols = row.find_all("td")
        # find name links (a tags)
        a = cols[2].find("a")
        # and add to players a dict with
        # {'name':, 'url':}
        players.append({"name": cols[2].get_text(strip=True).rstrip("*"), "url": urljoin(base_url, a["href"])})
        
    # return list of players
    return players
    

def get_player_stats(player_url: str, team: str) -> dict:
    """Gets the player stats for a player in a given team
    arguments:
        player_url (str) : url for the wiki page of player
        team (str) : the name of the team the player plays for
    returns:
        stats (dict) : dictionary with the keys (at least): points, assists, and rebounds keys
    """
    print(f"Fetching stats for player in {player_url}")

    stats = {}

    # Get the table with stats
    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    if soup.find(id="Regular_season"):
        table = soup.find(id="Regular_season").find_next("table")
    elif soup.find(id="NBA"):
        table = soup.find(id="NBA").find_next("table")
    else:
        raise ValueError("no NBA regular_season statistics table")


    # Loop over rows and extract the stats
    rows = table.find_all("tr", {"class" : None})[1:] ## not to contain class="sortbottom" (Career, All-Star)
    cols = rows[-1].find_all("td") # 2021-2022 row

    first_col = cols[0].get_text(strip=True).rstrip("*")
    second_col = cols[1].get_text(strip=True).rstrip("*")

    # Check correct team (some players change team within season)
    if first_col.startswith("2021–22"): ## for dealing with special charactors e.g:†
        if second_col.startswith(team):
            assert len(cols) == 13
            # load stats from columns
            # keys should be 'points', 'rebounds, and 'assists'
            stats["points"]=float(cols[12].get_text(strip=True).rstrip("*"))
            stats["rebounds"]=float(cols[8].get_text(strip=True).rstrip("*"))
            stats["assists"]=float(cols[9].get_text(strip=True).rstrip("*"))
        else:
            print("team name does not match")
            stats["points"]=float(0)
            stats["rebounds"]=float(0)
            stats["assists"]=float(0)  
    
    elif first_col.startswith(team):
        assert len(cols) == 12
        stats["points"]=float(cols[11].get_text(strip=True).rstrip("*"))
        stats["rebounds"]=float(cols[7].get_text(strip=True).rstrip("*"))
        stats["assists"]=float(cols[8].get_text(strip=True).rstrip("*"))
    
    else:
        try:
            # deal with the case when rows contain the Career row that should be excluded, 
            # since the Career row has no class="sortbottom"
            # check the upper row
            cols = rows[-2].find_all("td") 
        except:
            # there are no more than two rows in stats table, only one row.
            print("list index out of range") 
            
            stats["points"]=float(0)
            stats["rebounds"]=float(0)
            stats["assists"]=float(0)
            pass
        else:
            # check the upper row's content
            first_col = cols[0].get_text(strip=True).rstrip("*")
            second_col = cols[1].get_text(strip=True).rstrip("*")

            # Check correct year
            if first_col.startswith("2021–22"): 
                # Check correct team (some players change team within season)
                if second_col.startswith(team):
                    assert len(cols) == 13
                    stats["points"]=float(cols[12].get_text(strip=True).rstrip("*"))
                    stats["rebounds"]=float(cols[8].get_text(strip=True).rstrip("*"))
                    stats["assists"]=float(cols[9].get_text(strip=True).rstrip("*"))
                else:
                    print("team name does not match")
                    stats["points"]=float(0)
                    stats["rebounds"]=float(0)
                    stats["assists"]=float(0)  
            else:
                print("check the table: no 2021-22")
                stats["points"]=float(0)
                stats["rebounds"]=float(0)
                stats["assists"]=float(0)

    return stats


# run the whole thing if called as a script, for quick testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2022_NBA_playoffs"
    find_best_players(url)
