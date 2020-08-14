# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt


#Solution for the problem

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened, Due to bad file name:", fname)
    quit()

words = list()
for line in fh:
    words = words + line.split()
    words.sort()
words2=[]

for word in words:
	if word not in words2:
		words2.append(word)
print (words2)
