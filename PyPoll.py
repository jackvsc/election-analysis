# The data we need to retrieve.
import csv
import os

# Load the data file.
election_results = os.path.join('resources','election_results.csv')

# Open, read, and analyze the data file.
with open(election_results) as election_data:
    reader = csv.reader(election_data)

    # Skip the header.
    header = next(reader)

    # Print each row in the data file.
    for row in reader:
        print(row)

# 1) The total number of votes cast.
# 2) A complete list of the candidates who received votes.
# 3) The percentage of votes that each candidate won.
# 4) The total of votes that each candidate received.
# 5) The winner of the election based on the popular vote.

# Write our results to a file.
election_results = os.path.join('analysis','election_analysis.txt')
with open(election_results,'w') as output:
    output.write('')