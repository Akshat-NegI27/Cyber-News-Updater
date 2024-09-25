import requests
from bs4 import BeautifulSoup
import datetime
from colorama import Fore
import sys

green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
white = Fore.WHITE

plus = white + "[" + green + "+" + white + "] "
minus = white + "[" + red + "-" + white + "] "
info = white + "[" + yellow + "INFO" + white + "] "
open_bracket = white + "["
close_bracket = white + "] "

current_date = datetime.datetime.now()
current_time = current_date.time()
hour = current_time.hour


def fetch(value):
    links = [""]
    response = requests.get(value).content
    soup = BeautifulSoup(response, 'html.parser')
    print(" ")
    x = 1
    for headings in soup.findAll('h2', class_="home-title"):
        print(open_bracket + green + str(x) + close_bracket + white + headings.text)
        x += 1
    print(" ")
    for urls in soup.findAll("a", class_="story-link"):
        url = urls.get("href")
        links.append(url)
    user_choice = input(plus + "Please enter a news to continue reading: ")
    print(" ")
    try:
        response = requests.get(links[int(user_choice)]).content
        soup = BeautifulSoup(response, 'html.parser')
        article = soup.find("div", id="articlebody")
        for paragraphs in article.findAll("p"):
            print(paragraphs.text)
    except ValueError as e:
        print(minus + red + "Please select a value from the given numbers!")


def news():
    urls = ["",
            "https://thehackernews.com/",
            "https://thehackernews.com/search/label/data%20breach",
            "https://thehackernews.com/search/label/Cyber%20Attack",
            "https://thehackernews.com/search/label/Vulnerability",
            "https://thehackernews.com/search/label/Malware"]
    user_choice = input(plus + "I have fetched some fresh news! Do you have time to explore!? [Y/n] ")
    print(" ")
    if user_choice == "y" or user_choice == "Y" or user_choice == "":
        print(open_bracket + green + "1" + close_bracket + green + "General News")
        print(open_bracket + green + "2" + close_bracket + green + "Data breaches")
        print(open_bracket + green + "3" + close_bracket + green + "Cyber Attack")
        print(open_bracket + green + "4" + close_bracket + green + "Vulnerabilities")
        print(open_bracket + green + "5" + close_bracket + green + "Malware")
        print(open_bracket + red + "x" + close_bracket + red + "Exit")
        print(" ")
        choice = input(plus + green + "Enter an option to continue: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            fetch(urls[int(choice)])
        else:
            print(minus + red + "Exiting now!")
            sys.exit(0)
    else:
        print(minus + "Exiting Now! Will let you know if got something fresh next time!")



news()
