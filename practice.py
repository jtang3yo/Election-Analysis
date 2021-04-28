
x = 0 
while x<=5: 
    print(x)
    x= x+1 

count = 7 
while count < 1: 
    print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
for county in counties: 
    print(county)
for i in range(len(counties)): 
    print(counties[i])


numbers = [0,1,2,3,4]
for num in range(5):
    print(num)

countiesTuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(countiesTuple)): 
    print(countiesTuple)
for county in countiesTuple: 
    print(county) 

countiesDict= {"Arapahoe":422829,"Denver":463353,"Jefferson":432438} 
for county in countiesDict: 
    print(county)
for county in countiesDict.keys(): 
    print(county)
for voters in countiesDict.values(): 
    print(voters)
for county in countiesDict: 
    print(countiesDict.get(county))
for county, voters in countiesDict.items(): 
    print(county + "county has" + str(voters) + "registered voters")
for county, voters in countiesDict.items(): 
    print(f"{county} county has {voters} registered voters.")

#iterate a list of dictionaries 
votingData = [{"county":"Arapahoe","registeredVoters":422829}, 
            {"county":"Denver","registeredVoters": 463353},
            {"county":"Jefferson","registeredVoter":432438}]
for countiesDict in votingData: 
    print(countiesDict)
for i in range(len(votingData)): 
    print(votingData[i])
for countiesDict in votingData: 
    for value in countiesDict.values(): 
        print(value)
for countiesDict in votingData: 
    print(countiesDict['county'])

# f-string literals 
myVotes = int(input("How many votes did you get in the election?"))
totalVotes = int(input("What is the total votes in the election?"))
print(f"I received {myVotes/totalVotes * 100}% of the total votes.")

candidateVotes = int(input("How many votes did the candidate get in the election?"))
totalVotes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidateVotes} number of votes."
    f"The total number of votes in the election was {totalVotes}."
    f"You received {candidatevotes/totalVotes *100:2f}% of the total votes.")
print(message_to_candidate)



