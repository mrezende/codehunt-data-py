#!/usr/bin/env python

import codehunt.datarelease
import codehunt.rest
import pandas as pd
import matplotlib.pyplot as plt


# In order to get access to the Code Hunt REST API, please
#   request a client_id and client_secret from codehunt@microsoft.com
client_id = None
client_secret = None

if client_id is None:
    client = None
else:
    client = codehunt.rest.Client(client_id=client_id,
                                  client_secret=client_secret)

data = codehunt.datarelease.Data("/Volumes/HD/mestrado/machine-learning-projects/Code-Hunt/Code Hunt dataset 1/Code Hunt data release 1")

level_most_attempts = ['Sector1-Level3', 'Sector1-Level4', 'Sector1-Level6', 'Sector2-Level1']

for level in data.levels:
    if level.level_name in level_most_attempts:
        # The friendly name for the level used in the data release and Python
        print(level)
        # The Code Hunt API name for the level
        print(level.challenge_id)
        # The reference solution for the level
        print(level.challenge_text)

attempts_per_language = {'Java': {}, 'CSharp': {}}
attempts_won_per_level = {'won': {}, 'fail': {}}
# user-reported experience level, 1-3:
for user in data.users:
    # user-reported experience level, 1-3:
    #   1="Beginner", 2="Intermediate", 3="Advanced"

    for level in data.levels:
        if level.level_name in level_most_attempts:
            attempts = user.get_attempts(level)
            # attempts will be None if the user did not attempt this level
            if attempts:
                for attempt in attempts:
                    key_level = level.level_name
                    key_won = 'won' if attempt.won else 'fail'
                    if key_level in attempts_won_per_level[key_won]:
                        attempts_won_per_level[key_won][key_level] += 1
                    else:
                        attempts_won_per_level[key_won][key_level] = 1

                    if key_level in attempts_per_language[attempt.language]:
                        attempts_per_language[attempt.language][key_level] += 1
                    else:
                        attempts_per_language[attempt.language][key_level] = 1
print(attempts_per_language)

df = pd.DataFrame(attempts_per_language)

df.plot(kind="bar", stacked=True)
plt.tight_layout()
plt.show()

print(attempts_won_per_level)

df = pd.DataFrame(attempts_won_per_level)

df.plot(kind="bar", stacked=True)
plt.tight_layout()
plt.show()