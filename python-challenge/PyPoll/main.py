import os         # Used to read csv files
import csv        # Used to read csv files
import statistics # Used to calculate statistical data

# Path to collect data from the Resources folder
election_csv = os.path.join("..", "budget_data.csv")

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas
    csv_header = next(csvfile)  # header of csv
    
    month_counter = 0 # Counts the number of total months
    profit_loses = {
        'date': [],
        'profit': []
    }
    networth = 0 # Total amount of "Profit/Losses" over the entire period
    # Loop through the data
    for row in csvreader:
        
        month_counter += 1          # Add one month per row 
        networth += int(row[1])     # Add the gains/losses of that month to networth
        profit_loses['date'].append(row[0])          # Add date to array
        profit_loses['profit'].append(int(row[1]))   # Add to array the gains/loses of each month

    average_profit = round(statistics.mean(profit_loses['profit']),2)            # Calculate the average profit from gains array
    max_profit_index = profit_loses['profit'].index(max(profit_loses['profit'])) # Get the index of the max profit
    min_profit_index = profit_loses['profit'].index(min(profit_loses['profit'])) # Get the index of the min profit

    
    print(f'The total number of months is {month_counter}')
    print(f'The networth of the company is ${networth}')
    print(f'The average of the profit and loses is ${average_profit}')
    print('The max profit was on {} and it was ${}'.format(profit_loses['date'][max_profit_index],profit_loses['profit'][max_profit_index]))
    print('The min profit was on {} and it was ${}'.format(profit_loses['date'][min_profit_index],profit_loses['profit'][min_profit_index]))

    f = open("./analysis.txt","w+") # Open the file to write data
    # Write Data
    f.write(f'The total number of months is {month_counter}\n')
    f.write(f'The networth of the company is ${networth}\n')
    f.write(f'The average of the profit and loses is ${average_profit}\n')
    f.write('The max profit was on {} and it was ${}\n'.format(profit_loses['date'][max_profit_index],profit_loses['profit'][max_profit_index]))
    f.write('The min profit was on {} and it was ${}\n'.format(profit_loses['date'][min_profit_index],profit_loses['profit'][min_profit_index]))
    f.close() # Close the file







