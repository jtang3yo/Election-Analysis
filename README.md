# Election_Analysis

## Project and Challenge Overview 
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 
* 1. Calculate the total number of votes cast. 
* 2. Get a complete list of candidiates who received votes. 
* 3. Get a complete list of counties that turned out to vote. 
* 4. Calculate the total number of votes each candidate received. 
* 5. Calculate the total number of votes each county turned out to vote. 
* 6. Calculate the percentage of vote each candidate won. 
* 7. Calculate the percentage of vote each county voted. 
* 8. Determine the winner of the election based on popular vote. 
* 9. Determine the largest turnout county. 

## Resources 
- Data Source: election_results.csv 
- Software: Python 3.7.6, 64 bits, Visual Studio Code, 1.55.2 (Universal) 

## Analysis 
* Declare variables to hold values of candidates and counties as well as votes accordingly 
  - Create variables ![image](https://user-images.githubusercontent.com/82353749/116597211-52868900-a8f3-11eb-81aa-922323198a9b.png)
* Loop over data source election_results.csv sheet to get candidates and counties 
  - candidate votes![image](https://user-images.githubusercontent.com/82353749/116601902-00e0fd00-a8f9-11eb-8b08-d17cc548aee9.png)
  - county votes![image](https://user-images.githubusercontent.com/82353749/116601931-08080b00-a8f9-11eb-8a50-f55092c21390.png)
* For loop to get the county from the county dictionary to get candidate results and county results 
  - Candidate results ![image](https://user-images.githubusercontent.com/82353749/116602397-a8f6c600-a8f9-11eb-8044-192786ae797e.png)
  - County results ![image](https://user-images.githubusercontent.com/82353749/116602410-aeeca700-a8f9-11eb-9315-6b60d820142b.png)
* Output the final results to election_analysis.txt file 
  - Candidate results summary![image](https://user-images.githubusercontent.com/82353749/116603077-80bb9700-a8fa-11eb-8da8-cad61f402fe8.png)
  - County results summary ![image](https://user-images.githubusercontent.com/82353749/116603098-8913d200-a8fa-11eb-8198-ab58c98bcbf9.png)

## Project and Challenge Summary 
The analysis of the election shows that: 
* There were 369,711 votes cast in the election. 
* The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane 
* The counties that voted: 
  - Jefferson 
  - Denver 
  - Arapahoe 
* The candidate results were: 
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes. 
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes. 
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes. 
* The county results were: 
  - Jefferson county cast 10.5 %  of the vote and 38,855 number of votes. 
  - Denver county cast 82.8 % of the vote and 306,055 number of votes. 
  - Arapahoe county cast 6.7 % of the vote and 24,801 number of votes. 
* The winner of the election was: 
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes. 
* The largest turnout county was: 
  - Denver county, that cast 82.8 % of the vote and 306,055 number of votes. 
