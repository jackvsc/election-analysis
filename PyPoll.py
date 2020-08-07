# The data we need to retrieve.
import csv
import os

# Load the data file.
election_results = os.path.join('resources','election_results.csv')

# Initialize variables.
total_votes = 0
candidates = []
candidate_votes = {}

winner = ''
winning_count = 0
winning_pct = 0

# Open, read, and analyze the data file.
with open(election_results) as election_data:
    reader = csv.reader(election_data)

    # Skip the header.
    header = next(reader)

    # Print each row in the data file.
    for row in reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Add the candidate name to the candidate list.
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        # Tally the votes for each candidate.
        candidate_votes[candidate] += 1

    # Print a list of the candidates in this election.
    print(f'There are {len(candidates)} candidates in this election.\n')
    for candidate in candidates:
        print(candidate)

    print('')

    # The percentage of the popular vote & the total votes for each candidate.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_pct = votes / total_votes * 100

        # Choosing a winner.
        if votes > winning_count and vote_pct > winning_pct:
            winning_count = votes
            winning_pct = vote_pct
            winner = candidate
        
        print(f'{candidate} received {vote_pct:.1f}% of the popular vote and {votes:,} total votes.\n')

    # And the winner is!
    print(f'The winner of the election is {winner} with {winning_count:,} total votes and {winning_pct:.1f}% of the popular vote.\n')

# Write our results to a file.
election_results = os.path.join('analysis','election_analysis.txt')
with open(election_results,'w') as output:
    output.write('')