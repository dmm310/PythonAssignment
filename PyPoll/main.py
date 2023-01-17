import os
import csv

#get file path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# ----- helper functions -------

#Retreive winners' name out of candidates dictionary
def most_votes(candidates_dict):
    result = 0
    winner = ''
    #loop through candidates dictionary
    for name in candidates_dict:
        votes = candidates_dict[name]
        
        #compare a candidates votes to current highest candidates' votes 
        #and set name to winner if it is greatest
        if votes > result:
            result = votes
            winner = name
    return winner

#calculates percent
def calc_percent(num1, total):
    percent = round((num1/total)*100, 3)
    return percent

#create function to retreive row counter & dictionary of candidate 
#names and votes.
def totals(csvreader):
    counter = 0
    candidates = {}
    
    for row in csvreader:
        counter += 1
        candidate_name = row[2]
        
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 0
            
    return {
        'total_votes': counter,
        'candidates': candidates
    }

#---------Helper functiond end ----------

#open csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #turn data into a list
    rows = list(csvreader)

    #create a variable for the header
    csv_header = rows[0]
    #print(f"CSV Header: {csv_header}")
    
    print('\n')
    print('Election results')
    print('-----------------------------')
    
    #retrieve total number of votes
    result = totals(rows[1:])
    # print(result)
    print('Total votes: ' + str(result['total_votes']))
    print('-----------------------------')
    
    candidates = result['candidates']
    vote_totals = result['total_votes']
    for key in candidates:
        unique_percents = calc_percent(candidates[key], vote_totals)
        # print(unique_percents)
        
        print_results = "{}: {}% ({})".format(key, unique_percents, candidates[key])
        print(print_results)
        # print('\n')
    
    print('-----------------------------')
    print("Winner: " + most_votes(candidates))
    
    #Output to txt file via terminal: python main.py > output.txt
        
    #-----code not used in the end -------------   
    
    #retreive unique candidate names
    # for candidate_name in set(result['candidates']):
    #     print(candidate_name)
    
        # print('Canidates name is: ' + key)
        # print('Candidates votes is: ' + str(candidates[key]))
        # print('total votes is: ' + str(vote_totals))
    

        
        
        