import requests

def GetStringLines(path):
    return open(path).readlines()

def GetDayInput(day):
    link = "https://adventofcode.com/2023/day/{0}/input"
    return requests.get(link.format(day))