import csv
from pathlib import Path

election_data = "Resources/election_data.csv"

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#read header first (skip)
    csv_header = next(csv_file) 

    candidate_name = []
    candidate_list = []
    total_voters = 0
    election_results = {}

 #
    for row in csv_reader:
        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            election_results[candidate_name] = 0
        election_results[candidate_name] += 1
        total_voters += 1

#Print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str('{:,.0f}'.format(total_voters)))
print("-------------------------")
for i in election_results:
    PctVotes = '{:,.3f}'.format((election_results[i] / total_voters) * 100)
    print(i + ": " + str(PctVotes) +
          "% (" + str('{:,.0f}'.format(election_results[i])) + ")")
print("-------------------------")
keyMax = max(election_results, key=election_results.get)
print("Winner:  " + keyMax)
print("-------------------------")
# Corrected the f-string format
output = f"""
Election Results
-------------------------
Total Votes: {total_voters:,}
"""
print(output)

# save to PyPoll_analysis.txt
txt_path = Path(__file__).parent / "analysis/PyPoll_analysis.txt"
with open(txt_path, "w") as txt_file:
    txt_file.write(output)