import json

data = '''
{
  "name" : "Roshan",
  "phone" : {
    "type" : "intl",
    "number" : "+91 843 980 7211"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)x
print('Name:', info["name"])
print('Contact No.:', info["phone"]["number"])
print('Hide:', info["email"]["hide"])
