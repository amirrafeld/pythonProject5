import requests
import threading
from bs4 import BeautifulSoup
import sqlalchemy
from lxml.html import tostring, html5parser
import pandas as pd
import numpy as np
from googletrans import Translator
import googletrans
import time
import xlsxwriter
from requests_html import HTMLSession
import openpyxl
import csv
import googletrans
from threading import *
import selenium
from selenium import webdriver
from urllib3 import disable_warnings
from urllib3 import packages


SUB_LIGA = []
links_for_liga = []
TEAMS_NAME = []
TEAMS_ODDS = []
MATCHES = []
OK = []
OK1 = []

data12 = openpyxl.load_workbook("C:/.idea/dsa.xlsx")
#sheet = wer["sheet1"]

url = 'https://www.winner.co.il/'
req = requests.get(url, timeout=140)


soup = BeautifulSoup(req.text, 'html.parser')
z = soup.find_all('li', {"class": 'top_path'})
file = open("game.csv", "wb")
writer = csv.writer(file)


def eventodds():
    for genral in z:
        link = 'https://www.winner.co.il/' + genral.find('a',{'class': "clickable"})['href']
        SUB_LIGA.append(link)

        for item in SUB_LIGA:
            req1 = requests.get(item, timeout=140)
            soup2 = BeautifulSoup(req1.text, 'html.parser')
            R = soup2.find_all("table")

            for item2 in R:
                N = 'https://www.winner.co.il/' + item2.find_next('a')['href']
                MATCHES.append(N)
                for pp in MATCHES:
                    sub_league = requests.get(pp, timeout=398)
                    soup3 = BeautifulSoup(sub_league.text, 'html.parser')
                    market = soup3.find_all('h2', class_ = "market_type-title")
                    data_winner = soup3.find_all("div", class_ = "pseudotable")
                    TEAMS_ODDS.append(data_winner)

                    try:
                       for nn in data_winner:
                            GAME = [{
                                "TEAM": nn.find('span', class_="name ellipsis outcomedescription").text.strip(),
                                "ODDS": float(nn.find("span", class_="formatted_price").text),}]
                            OK1.append(GAME)
                            OK3 = pd.DataFrame(OK1)
                    except:
                        pass
def content():
    for genral in z:
        link = 'https://www.winner.co.il/' + genral.find('a', {'class': "clickable"})['href']
        SUB_LIGA.append(link)
        for item in SUB_LIGA:
            req1 = requests.get(item, timeout=140)
            soup2 = BeautifulSoup(req1.text, 'html.parser')
            R = soup2.find_all("table")

            for item in R:
                N = 'https://www.winner.co.il/' + item.find_next('a')['href']
                MATCHES.append(N)
                for pp in MATCHES:
                    sub_league = requests.get(pp, timeout=398)
                    soup3 = BeautifulSoup(sub_league.text, 'html.parser')
                    market = soup3.find_all('h2', class_="market_type-title")
                    data_winner = soup3.find_all("div", class_="pseudotable")
                    TEAMS_ODDS.append(data_winner)

                    for lk in market:
                        time = [{
                            "TYPE_OF_BET" :lk.find("bdo").text,
                            "DATE": lk.find_next("span", class_ = "time").text,}]
                        OK.append(time)
                        OK4 = pd.DataFrame(OK)

                        #final12 = list(zip(OK,OK1))
                        print(final12)
                        #final = pd.DataFrame(final12)
                        #final.to_excel(data12)


x = threading.Thread(target=eventodds, args=())
x.start()
y = threading.Thread(target=content, args=())
y.start()














                   #S1 = pd.DataFrame(OK1)
                   #RT = S1 + S
                   #RT.to_excel("C:\.idea\dsa.xlsx")






                    #DA = pd.DataFrame(GAME)
                    #print(DA)
                    #sheet = GAME
                    #wer.save("C:\.idea\dsa.xlsx")





                   


                    #v = sheet.cell().value = DA
                    #wer.save("C:/.idea/dsa.xlsx")









    #df1 = pd.DataFrame(GAME)
    #DF3 = pd.DataFrame(time)
    #df1.to_excel("rr.xlsx")
    #DF3.to_excel("rr.xlsx")

#COMBAIN  = dict()
#for dict in (GAME,time):
    #for key, value in dict.items():
        #COMBAIN[key] = value
        #print(COMBAIN)




                    #links_for_liga.append(data_winner)
                    #print(links_for_liga)
                #for u in data_winner:
                   # po = {
                        #"name_of_the_team": u.find_all('div',class_ = 'title'),
                        #"odds": u.find_all("span", class_ = "formatted_price"),
                        #"game": u.find_all("span", class_ = "name ellipsis outcomedescription")}
                    #print(po)


            #for item in links_for_liga:
                #sub_league = requests.get(item, timeout=38)
                #soup1 = BeautifulSoup(sub_league.text, 'html.parser')
                #data_winner = soup1.find_all("div", class_="pseudotable")
                #for item in data_winner:
                    #NAME_OF_TEAM = item.find('span', {"class": "name ellipsis outcomedescription"}).text.strip()
                    #for X in NAME_OF_TEAM:
                        #NEW_TEAM_NAME = NAME_OF_TEAM.replace("(\u202a+\u202c1)", "X").replace("(\u202a-\u202c1)", "X")
                    #TEAMS_NAME.append(NEW_TEAM_NAME)
                    #ODDS_WIN = item.find("span", class_="formatted_price").text
                    #NEW_ODDS = float(ODDS_WIN)
                    #TEAMS_ODDS.append(NEW_ODDS)
                    #final = list(zip(TEAMS_NAME, TEAMS_ODDS))
            # ##final_dateframe = pd.DataFrame(final)
