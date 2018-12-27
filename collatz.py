# samgaudet
# 2018-12-14

import pandas as pd
import matplotlib.pyplot as plt

# user-input for sample size

n = int(input('> '))

# create empty pandas dataframe to fill with data

df = pd.DataFrame(columns=['initialValue', 'stepCount'])

# loop through values in range of sample size, starting with i = 2

for i in range(2,n):
	
	stepCount = 0
	j = i

	# apply collatz conjecture rules

	while j != 1:
		if j % 2 == 0:
			j = j / 2
			stepCount += 1
		else:
			j = 3*j + 1
			stepCount += 1

	# add starting value, number of steps until j = 1 to dataframe

	df = df.append(pd.DataFrame({'initialValue': i, 'stepCount': stepCount}, index=[0]), ignore_index=True)

