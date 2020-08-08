import csv
import os

# Load our data file.
election_results = os.path.join('resources','election_results.csv')

# Write our results.
election_analysis = os.path.join('analysis','election_analysis.txt')

# Initialize our variables.
total_votes = 0
candidates = []
candidate_votes = {}

winner = ''
winning_count = 0
winning_pct = 0

spacer = '-------------------------'

# Open, read, and analyze our data file.
with open(election_results) as election_data:
    file_reader = csv.reader(election_data)

    # Skip the header.
    header = next(file_reader)

    # Read our data file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Add each candidate name to our candidate list.
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        # Tally the votes for each candidate.
        candidate_votes[candidate] += 1

with open(election_analysis,'w') as output:
    # Total votes cast.
    election_results = (
        f'Election Results\n'
        f'{spacer}\n'
        f'There were {total_votes:,} total votes cast in the election.\n'
        f'{spacer}\n'
        )

    print(election_results)
    output.write(election_results)

    # List each candidate in this election.
    candidate_count = (f'There are {len(candidates)} candidates in this election.\n\n')
    print(candidate_count)
    output.write(candidate_count)

    for candidate in candidates:
        print(candidate)
        output.write(f'{candidate}\n')

    # Lil space (everyone needs it.)
    print(spacer)
    output.write(f'{spacer}\n')

    # The percentage of the popular vote & the total votes for each candidate.
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_pct = votes / total_votes * 100
        candidate_summary = (f'{candidate} received {vote_pct:.1f}% of the popular vote and {votes:,} total votes.\n')

        print(candidate_summary)
        output.write(candidate_summary)

        # Picking a winner.
        if votes > winning_count and vote_pct > winning_pct:
            winner = candidate
            winning_count = votes
            winning_pct = vote_pct

    # And the winner is!
    winner_summary = (
        f'{spacer}\n'
        f'The winner of the election is {winner}.\n'
        f'{winner} got {winning_count:,} total votes.\n'
        f'{winner} got {winning_pct:.1f}% of the popular vote.'
        )

    print(winner_summary)
    output.write(f'{winner_summary}')