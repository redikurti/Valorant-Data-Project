# Author: Redon Kurti

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd


def get_player_username(page_start, page_end):
    """ This function is used to retrieve the username of each player from the leaderboard of the video game Valorant from the tracker.gg website.
    Input: Two integers, one representing the start page and the other the end page
    Output: A list of usernames"""

    usernames = []

    for page in range(page_start,page_end + 1):

        # For each page update the URL
        # We will only look at Act 4 Episode 1
        url = "https://tracker.gg/valorant/leaderboards/ranked/all/default?page={}&region=na&act=573f53ac-41a5-3a7d-d9ce-d6a6298e5704".format(str(page)) 
        print(url)

        # Request, open and read the URL
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read()
        bs = BeautifulSoup(response, features="lxml")

        # Get the first part of the username 
        player_tag = bs.findAll("span", "trn-ign__username")

        # Small hotfix
        for tag in player_tag:
            if "#" in tag.string:
                index = player_tag.index(tag)
                player_tag.pop(index)

        # Get the second part of the username
        player_dicriminator = bs.findAll("span", "trn-ign__discriminator")

        # Concatenate the list and form the gamer username
        player_username = [tag.string + dicriminator.string for tag, dicriminator in zip(player_tag, player_dicriminator)]

        # Append each username to the list and return it
        for username in player_username:
            usernames.append(username)
    
    return usernames


def get_player_info(data):
    """ This function is used to retrieve different information for each player from the leaderboard of the video game Valorant from the tracker.gg website.
    Input: Data pulled using BeautifulSoup 
    Output: A dictionary with infomation about the player"""

    player_data = {}

    # Get the players Rank
    player_data['Rank'] = (data.find(name = 'span', attrs = {'class':'valorant-highlighted-stat__label'}).string).strip()

    # Get the number of total matches played by player
    player_data['Matches'] = (data.find(name = 'span', attrs = {'class':'matches'}).string).strip().replace("Matches","")

    # Create a list with the general statistics
    stat_list = (data.find(name = 'div', attrs = {'class':'main'}).findAll(name = 'div', attrs = {'class':'stat'}))

    # Put the general statistics information into the dictionary
    for stats in stat_list:
        spans = stats.findAll('span')
        for span in spans:

            if span['class'] == ['name']:
                key = span.string
            
            if span['class'] == ['value']:
                player_data[key] = span.string.replace(",","")
    
    # Create a list with the overall statistics of the season
    overall_stat_list = (data.find(name = 'div', attrs = {'class':'giant-stats'}))

    # Put the overall statistics information into the dictionary
    for stats in overall_stat_list:
        spans = stats.findAll('span')
        for span in spans:

            if span['class'] == ['name']:
                key = span.string
            
            if span['class'] == ['value']:
                player_data[key] = span.string.replace("%","")

    # Get the top agent played by player
    player_data['Top Agent'] = (data.find(name = 'span', attrs = {'class':'agent__name'}).string).strip()
    
    # Get the most used weapon by player
    player_data['Top Weapon'] = (data.find(name = 'div', attrs = {'class':'weapon__name'}).string).strip()
    
    return player_data



def scrap_val_data(usernames):
    """ This function is used to scrap the Valorant data.
    Input: A list of usernames
    Output: A CSV file with the data about each player"""

    # Create a data dict
    data = {}

    for username in usernames:

        # Clean up the username and 'quote' it so its ready to be inputted into URL
        username_clean = username.replace(" ", "%20").replace("#", "%23")

        # URL
        url = "https://tracker.gg/valorant/profile/riot/{}/overview?season=573f53ac-41a5-3a7d-d9ce-d6a6298e5704".format(username_clean)
        
        # Request, open and read the URL
        # We run a try/except block here because some players might have private data or some pages might be deleted so we want to skip those
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req).read().decode('utf-8')
        except:
            continue

        bs = BeautifulSoup(response, features="lxml")

        # Fill the dictionary with the data for each player based on their username
        current_user_dict = get_player_info(bs)
        data[username] = current_user_dict

    # Use pandas to create a DataFrame and put the data into a csv
    df = pd.DataFrame.from_dict(data)
    df.to_csv("Valorant_Data.csv")


if __name__ == "__main__":
    
    # Get usernames and scrap the data
    usernames = get_player_username(1,60)
    scrap_val_data(usernames)
    
    