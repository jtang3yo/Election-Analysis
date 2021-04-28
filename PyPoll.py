import csv
import os

filetoLoad = os.path.join("Resources","election_results.csv")
filetoSave = os.path.join("analysis","election_analysis.txt")

totalVotes = 0
candidateOptions = []
candididateVotes = {}

winningCandidate = ""
winningCount = 0 
winningPercentage = 0 


with open(filetoLoad) as electionData: 
    fileReader = csv.reader(electionData)

    headers = next(fileReader)
    
    for row in fileReader: 
        totalVotes += 1 
        print(totalVotes)

        candidateName = row[2]
        if candidateName not in  candidateOptions: 
            candidateOptions.append(candidateName) 
            candidateVotes[candidateName] = 0 
        candidateVotes[candidateName] += 1 

    for candidateNames in candidateVotes: 
        votes = candidateVotes[candidateName]
        votePercentage = float(votes)/float(totalVotes)

        if(votes > winningCount) and (votePercentage > winningPercentage): 
            winningCount = votes 
            winningPercentage = votePercentage 

    print(f"{candidateName}: {votePercentage:1f}% ({votes:,})\n") 
    

