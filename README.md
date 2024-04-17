# PSN-Games

## The problem
Playstation's website which displays games in PS Plus Extra is not very useful: it's a simple alphabetical list.

## The solution
For learning purposes, I decided to write a Python program which displays more information for every game in PS Plus Extra. How does it work?

psn_games.py - scrapes PS Plus website (https://www.playstation.com/pl-pl/ps-plus/) for a list of games that are currently a part of PS Plus Extra.

game_score.py (not a good name, to be honest) - changes the games' names so they fit Metacritic's API. I have found the API by using Chrome's devtools, after browsing the Fetch/XHR tab for quite some time. :P

game_info.py (very good name :P) - gets all of the required information for a specific game and creates a list for every piece of informaion (name, score, release date, number of reviews, publisher, developer).

into_table.py - combines everything together into a nice .csv file.

I separated every step of this process into a separate file with its own function, so that each part can be easily modified in the future.

## Are there any issues?
Yes. While this solution gets the correct information for most of the games (more than 400), I do have to manually fix some of the entries if the name inserted into the API's link is incorrect. This happens for around 20 games. Not a fully automated solution, but it's better than manually going through around 460 games. :D

## Google Looker
<iframe width="600" height="450" src="https://lookerstudio.google.com/embed/reporting/7259ffcc-2483-44d7-8e1b-80ed88706f49/page/t3BxD" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>

