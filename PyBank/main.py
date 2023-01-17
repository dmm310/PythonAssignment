import os
import csv

#connect to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#-----Helper Functions----------

def totals(csvreader):
    counter = 0
    profits = []
    for row in csvreader:
        counter += 1
        profits.append(int(row[1]))
    s = sum(profits)
    # print(counter)
    # print(s)
    return {
        'num_months': counter,
        'total_profit_loss': s
    }

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # turn reader into list
    rows = list(csvreader)

    #create variable for the header
    csv_header = rows[0]
    
    # skip csv header
    rows = rows[1:]
    # print(f"CSV Header: {csv_header}")
    
    #get number of months and sum profit/losses
    result = totals(rows)
    
    print('\n')
    print('Financial Analysis')
    print('----------------------------')
    print('Total months: ' + str(result['num_months']))
    print('Total: $' + str(result['total_profit_loss']))
    # print(result['total_profit_loss']/result['num_months'])
    
    # create list to store differences in profit/losses
    differlist = []
    maxmonth = ''
    maxvalue = 0
    minmonth = ''
    minvalue = 0
    
    #loop through rows
    for i in range(result['num_months']-1):
        #create variable to retreive a row and the next row
        row = rows[i]
        nextrow = rows[i+1]
        plvalue = int(row[1])
        plvalue2 = int(nextrow[1])
        #calculate differences in profit/losses and store in list
        differ = plvalue-plvalue2
        differlist.append(differ)
        #get greatest increase and decrease in profits + date
        inverted_diff = differ*-1
        if  inverted_diff > 0:
            if inverted_diff > maxvalue:
                maxvalue = inverted_diff
                maxmonth = nextrow[0]

        if  inverted_diff < 0:
            if inverted_diff < minvalue:
                minvalue = inverted_diff
                minmonth = nextrow[0]
                
    # print(maxvalue)
    # print(maxmonth)
    # print(minvalue)
    # print(minmonth)         
        
plaverage = round(sum(differlist)/len(differlist), 2)
print_average = 'Average Change: ${}'.format(plaverage)
print(print_average)
    
print_max_profit = 'Greatest Increase in Profits: {} (${})'.format(maxmonth, maxvalue)
print(print_max_profit)

print_min_profit = 'Greatest Decrease in Profits: {} (${})'.format(minmonth, minvalue)
print(print_min_profit)    
      
#Output to txt file via terminal: python main.py > output.txt      
      
#-------Code not used in the end ----------
        
        # if row != row+1:
        #     differ = sum(row, row+1)
        #     print(differ)
        
    # maxdiffer = max(differlist)
    # print(maxdiffer)
       
    
    
    
    
    
    

 
