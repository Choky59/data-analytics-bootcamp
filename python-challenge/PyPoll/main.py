import os         # Used to read csv files
import csv        # Used to read csv files
import statistics # Used to calculate statistical data

# Path to collect data from the Resources folder
bank_csv = os.path.join("..", "election_data.csv")

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # Split the data on commas
    csv_header = next(csvfile)  # header of csv
    
    total_votes = 0 # Counts the number of total months
    candidates = {}

    # Loop through the data
    for row in csvreader:
        #   * The total number of votes cast
        total_votes += 1
        #   * A complete list of candidates who received votes
        try: 
            candidates[row[2]]['votes'] += 1
        except:
            candidates[row[2]] = {
                'votes' : 0,
                'percentage': 0
            }
    # Calculate vote percentages
    for candidate in candidates:
        percent = candidates[candidate]['votes'] / total_votes
        candidates[candidate]['percentage'] = round(percent,3) * 100

    # Show Results
    print('Election Results\n-------------------------')
    print('Total Votes: {}\n-------------------------'.format(total_votes))
    winner = {
        'name' : '',
        'votes': 0
    }
    for candidate in candidates:
        votes = candidates[candidate]['votes']
        percent = candidates[candidate]['percentage']
        if(winner['votes'] < votes):
            winner['votes'] = votes
            winner['name'] = candidate
        print('{}: {} ({}%)'.format(candidate,votes,percent))
    print('-------------------------')
    print('Winner: ' + winner['name'])
    print('-------------------------')

    f = open("./analysis.txt","w+") # Open the file to write data
    # Write Data
    f.write('Election Results\n-------------------------\n')
    f.write('Total Votes: {}\n-------------------------\n'.format(total_votes))
    for candidate in candidates:
        votes = candidates[candidate]['votes']
        percent = candidates[candidate]['percentage']
        f.write('{}: {} ({}%)\n'.format(candidate,votes,percent))
    f.write('-------------------------\n')
    f.write('Winner: ' + winner['name'] + '\n')
    f.write('-------------------------')
    f.close() # Close the file