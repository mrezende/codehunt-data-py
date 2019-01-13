#!/usr/bin/env python

import codehunt.datarelease
import codehunt.rest
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

for level in data.levels:
    # The friendly name for the level used in the data release and Python
    print(level)
    # The Code Hunt API name for the level
    print(level.challenge_id)
    # The reference solution for the level
    print(level.challenge_text)

number_attempts_per_level = {}
number_attempts_per_level_java = {}
number_attempts_per_level_cs = {}

for user in data.users:
    print(user)
    # user-reported experience level, 1-3:
    #   1="Beginner", 2="Intermediate", 3="Advanced"
    print(user.experience)
    for level in data.levels:
        attempts = user.get_attempts(level)
        # attempts will be None if the user did not attempt this level

        if attempts:
            for attempt in attempts:
                key = level.level_name
                if key in number_attempts_per_level:
                    number_attempts_per_level[key] += 1
                else:
                    number_attempts_per_level[key] = 1
                if(attempt.language == "Java"):
                    if key in number_attempts_per_level_java:
                        number_attempts_per_level_java[key] += 1
                    else:
                        number_attempts_per_level_java[key] = 1
                else:
                    key = level.level_name
                    if key in number_attempts_per_level_cs:
                        number_attempts_per_level_cs[key] += 1
                    else:
                        number_attempts_per_level_cs[key] = 1

print('Total Number attepmpts per level')
print(number_attempts_per_level)

plt.bar(range(len(number_attempts_per_level)), list(number_attempts_per_level.values()), align='center')
plt.xticks(range(len(number_attempts_per_level)), list(number_attempts_per_level.keys()))
plt.xticks(rotation=90)
plt.tight_layout()
# # for python 2.x:
# plt.bar(range(len(D)), D.values(), align='center')  # python 2.x
# plt.xticks(range(len(D)), D.keys())  # in python 2.x

plt.show()

print('Total Number attepmpts per level - Java')
print(number_attempts_per_level_java)

print('Total Number attepmpts per level - CSharp')
print(number_attempts_per_level_cs)