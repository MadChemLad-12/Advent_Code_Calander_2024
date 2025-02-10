###GOALS for Part 1###
###Script to read the input file####
import pandas as pd

colnames = ['left','right']
df = pd.read_csv('example2.txt', 
                header=None, 
                index_col=False, 
                sep=r"\s+", 
                names=colnames)

###Take file output and put the into two groups left and right
leftcol = df["left"]
rightcol = df["right"]

###Order the groups by numerical order
leftcol = leftcol.astype(float)
leftcol.sort_values(ascending = True, inplace=True)
leftcol=leftcol.reset_index(drop = True)

rightcol = rightcol.astype(float)
rightcol.sort_values(ascending = True, inplace=True)
rightcol=rightcol.reset_index(drop = True)

###Make new group call diff where the values are Left list minus Right list 
diffcol = abs(leftcol-rightcol)

sum = diffcol.sum()
#print(sum)

###Example of someone else doing it
#lines = puzzle_input.split("\n")[:-1] # exclude the last item since it's just a new line

#left_list = [int(line.split(" ")[0]) for line in lines]
#right_list = [int(line.split(" ")[-1]) for line in lines]

# print the first 5 items
#print(left_list[:5])

#print(right_list[:5])

# convert lists to numpy arrays and sort
#left_arr = np.sort(np.array(left_list))
#right_arr = np.sort(np.array(right_list))

# find the absolute value of element-wise differences and take the sum
#sum_of_differences = np.abs(left_arr - right_arr).sum()


###Goals for Part 2###
### Create an empty data frame
print(leftcol)
print(rightcol)

for  in rightcol:
    count = rightcol.count(item)
    rightcol.append(count)

###loop to see how many duplicates are on the right side


###Check to see that the number on the leftcol match anything on the rightcol


### For those that do multiple left number and count together


###Some one eleseseses example
#similarity_scores = [item * rightcol.count(item) for item in leftcol]
#print(similarity_scores)
