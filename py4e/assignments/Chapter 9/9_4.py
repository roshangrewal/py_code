# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


# Solution for the problem

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    wds = line.split()
    if len(wds) < 2 : continue
    if wds[0] != "From" : continue
    email = wds[1]
    counts[email] = counts.get(email,0) + 1
bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print (bigname, bigcount)
