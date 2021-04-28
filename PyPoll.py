import csv 
import os

filetoload = os.path.join("Resources", "election_results.csv")
filetosave = os.path.join("analysis", "election_analysis.txt")

with open(filetoload) as electiondata: 
    filereader = csv.reader(electiondata)
    headers = next(filereader)
    print(headers)
