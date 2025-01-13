# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:28:47 2025

@author: jgrasmann
"""

#%% imports
import requests
from bs4 import BeautifulSoup
import numpy as np

#%% Funktion: Fußball-Ergebnisse aus URL
def paarungen_seite_in_liste(url): 
    '''
    Parameters
    ----------
    url : URL, von der die Paarungen genommen werden
    
    Returns 
    -------
    Liste mit Tupeln mit je 2 Strings (Heimmannschaft, Auswärtsmannschaft): list_paar

    '''
    # Seite abrufen
    response = requests.get(url)
    list_matches = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Teams abrufen
        teams = [link.get_text() for link in soup.find_all('div', class_='kick__v100-gameCell__team__name')] 
        # letztes Wort entfernen (jeweiliges Land, aus dem das Team kommt)
        teams = [' '.join(team.split()[:-1]) for team in teams]
        
        # Paarungen abrufen
        matches = [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]
 
    else:
        print(f"Fehler beim Abrufen der Seite: {response.status_code}")

    return matches

# Test
url1 = "https://www.kicker.de/champions-league/spieltag/2024-25/5"
print(paarungen_seite_in_liste(url1))

#%% Liste an URLs erstellen: alle 8 Gruppen-Spieltage 2024/25

# Liste URLs der Kicker-Seite
url_stamm = "https://www.kicker.de/champions-league/spieltag/2024-25/"

list_urls = []
list_urls += [url_stamm + str(i) for i in range(1,9)]

print(list_urls)

#%% Alle Gruppen-Paarungen (insgesamt 144 Spiele: 8 mal 18) 
total_list_matches = []
for url in list_urls:
    total_list_matches += paarungen_seite_in_liste(url)
# print(total_list_matches)
# print(len(total_list_matches))