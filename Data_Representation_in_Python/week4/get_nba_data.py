import requests
from bs4 import BeautifulSoup
import time
import csv

def get_attendance(year):
    seat_capacity = 18007
    r = requests.get("http://www.espn.com/nhl/attendance/_/year/" + str(year))

    soup = BeautifulSoup(r.content, 'html.parser')

    table = soup.findAll("tr")

    with open("nhl_avalanche_attendance.csv", "a") as csvfile:

        writer =  csv.writer(csvfile)
        percent = 0
        total_teams = len(table) - 2
        rank = 0
        attendance = 0
        for tr in table:
            print tr

            row = tr.findAll("td")
            team = row[1].text
            if team == 'Colorado':
                percent = row[5].text
                rank = row[0].text
                attendance = row[4].text.replace(",", "")

        writer.writerow([year, attendance, seat_capacity, rank, total_teams])

    print "**** NEXT YEAR *** \n"




for year in range(2006, 2017):
    get_attendance(year)
    time.sleep(2)
