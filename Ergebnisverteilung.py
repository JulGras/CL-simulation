# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""
#%% imports
import requests
from bs4 import BeautifulSoup
import numpy as np

#%% Funktion: Fußball-Ergebnisse aus URL
def ergebnisse_seite_in_liste(url): 
    '''
    Parameters
    ----------
    url : URL, von der die Ergebnisse genommen werden
    
    Returns 
    -------
    Liste mit Strings der Ergebnisse: list_erg

    '''
    # Seite abrufen
    response = requests.get(url)
    list_erg = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ergebnis abrufen
        scores = soup.find_all('div', class_='kick__v100-scoreBoard__scoreHolder')
        n = 0
        for score in scores:
            if n % 2 == 0:
                if score:
                    list_erg.append(score.get_text(strip=True))
            n += 1    
    else:
        print(f"Fehler beim Abrufen der Seite: {response.status_code}")

    return list_erg

# # Test: URL der Kicker-Seite
# url1 = "https://www.kicker.de/champions-league/spieltag/2023-24/6/"

# print(ergebnisse_seite_in_liste(url1))

#%% Liste an URLs erstellen: Jeweils alle 6 Gruppen-Spieltage der vergangenen fünf Jahre

# Liste URLs der Kicker-Seite
list_url_stamm = ["https://www.kicker.de/champions-league/spieltag/2019-20/",
                  "https://www.kicker.de/champions-league/spieltag/2020-21/",
                  "https://www.kicker.de/champions-league/spieltag/2021-22/",
                  "https://www.kicker.de/champions-league/spieltag/2022-23/",
                  "https://www.kicker.de/champions-league/spieltag/2023-24/"]
list_urls = []
for stamm in list_url_stamm:
    list_urls += [stamm + str(i) for i in range(1,7)]

# print(list_urls)

#%% Alle Gruppen-Ergebnisse (insgesamt 480 Spiele) der vergangenen fünf CL-Saisons in einer Liste 
total_list_erg = []
for url in list_urls:
    total_list_erg += ergebnisse_seite_in_liste(url)
# print(total_list_erg)

#%% 
# Unique-Werte und deren Häufigkeiten bestimmen
unique_elements, counts = np.unique(total_list_erg, return_counts=True)


# Ergebnisse anzeigen und dict erstellen, in denen Ergebnisse mit Wahrscheinlichkeiten gemappt werden
list_moegl_erg = []
list_moegl_erg_wahr = []
for element, count in zip(unique_elements, counts):
    # print(f"Element: {element}, Häufigkeit: {count}")
    list_moegl_erg.append(element)
    list_moegl_erg_wahr.append(round(count/480, 4))
 
# Veränderungen der ersten vier Wahrscheinlichkeiten für eine Gesamtwahrs. 1
for i in range(4):
    list_moegl_erg_wahr[i] = round(list_moegl_erg_wahr[i] - 0.0001, 4)
    
# print(list_moegl_erg)
# print(list_moegl_erg_wahr)
# print(sum(list_moegl_erg_wahr))
    