import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())



# import requests
#
# fhand = requests.get('http://py4e-data.dr-chuck.net/known_by_Zarah.html')
# print(fhand.text)
