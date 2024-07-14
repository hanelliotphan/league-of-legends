"""
get-player-data.py

Get data by League of Legends player (either PUUID or Player name + game tag), 
generate a CSV file and store the dataset in the 
`./get-data-by-player/datasets` folder.
--------------------------------------------------------------------------------
Author(s):

Name: Han-Elliot Phan
Email: hanelliotphan@gmail.com
Last updated at: July 13, 2024
"""


# ---------------------------------------------------------------------------- #
#                               Import libraries                               # 
# ---------------------------------------------------------------------------- #

import os
import requests
import sys


# ---------------------------------------------------------------------------- #
#                               Global Variables                               # 
# ---------------------------------------------------------------------------- #

HEADERS = {"X-Riot-Token": os.environ["RIOTGAMES_API_KEY"]}
REGION = os.environ["REGION"] 


# ---------------------------------------------------------------------------- #
#                               Helper Functions                               # 
# ---------------------------------------------------------------------------- #

def get_account_info(puuid=None, gameName=None, tagLine=None):
    """
    get_account_info -- Get account information of League of Legends player 
    (either PUUID or Player name + game tag)

    Return: dict
    """
    if puuid:
        url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
    elif gameName and tagLine:
        url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    else:
        return {}
    try:
        account_info = requests.get(url=url, headers=HEADERS).json()
    except Exception as e:
        print(f"[get_account_info] ERROR: Error occurred while getting player's account information: {e}")
        return {}
    return account_info