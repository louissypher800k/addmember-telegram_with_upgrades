from past.builtins import xrange
import json
import sys

input_file = sys.argv[1]
#print(input_file + "\n")


obj  = json.load(open(input_file + "/+16155525510.json"))
#import the list that we get from get_members.py

#now we need to import another list from baduser.json
file1 = open('baduser.json', 'r')
Lines = file1.readlines()
Lines = [i.replace('"', '') for i in Lines]
res = [eval(i) for i in Lines]
obj2 = {}
obj2 = [x for x in obj if x["user_id"] not in res]
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
                                     
with open(input_file + "/+16155525510.json", 'w') as output:
    json.dump(obj2, output, indent=4, ensure_ascii=False)

#do the same shit as before but with a different TG account
obj3  = json.load(open(input_file + "/+16155525510.json"))
#import the list that we get from get_members.py

#now we need to import another list from baduser.json
file2 = open('baduser.json', 'r')
Lines2 = file2.readlines()
Lines2 = [i.replace('"', '') for i in Lines2]
res2 = [eval(i) for i in Lines2]
obj4 = {}
obj4 = [x for x in obj3 if x["user_id"] not in res2]
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
                                     
with open("vincentscourtyard/+16155525510.json", 'w') as output:
    json.dump(obj4, output, indent=4, ensure_ascii=False)

#do the same shit as before but with a different TG account
obj5  = json.load(open("vincentscourtyard/+16155494197.json"))
#import the list that we get from get_members.py

#now we need to import another list from baduser.json
file3 = open('baduser.json', 'r')
Lines3 = file3.readlines()
Lines3 = [i.replace('"', '') for i in Lines3]
res3 = [eval(i) for i in Lines3]
obj6 = {}
obj6 = [x for x in obj5 if x["user_id"] not in res3]
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
                                     
with open("vincentscourtyard/+16155494197.json", 'w') as output:
    json.dump(obj5, output, indent=4, ensure_ascii=False)

#do the same shit as before but with a different TG account
obj7  = json.load(open("vincentscourtyard/+16156232843.json"))
#import the list that we get from get_members.py

#now we need to import another list from baduser.json
file4 = open('baduser.json', 'r')
Lines4 = file4.readlines()
Lines4 = [i.replace('"', '') for i in Lines4]
res4 = [eval(i) for i in Lines4]
obj8 = {}
obj8 = [x for x in obj7 if x["user_id"] not in res4]
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
                                     
with open("vincentscourtyard/+16156232843.json", 'w') as output:
    json.dump(obj7, output, indent=4, ensure_ascii=False)

#do the same shit as before but with a different TG account
obj8  = json.load(open("vincentscourtyard/+16155494600.json"))
#import the list that we get from get_members.py

#now we need to import another list from baduser.json
file5 = open('baduser.json', 'r')
Lines5 = file5.readlines()
Lines5 = [i.replace('"', '') for i in Lines5]
res5 = [eval(i) for i in Lines5]
obj9 = {}
obj9 = [x for x in obj8 if x["user_id"] not in res5]
# Iterate through the objects in the JSON and pop (remove)                      
# the obj once we find it.                                                      
                                     
with open("vincentscourtyard/+16155494600.json", 'w') as output:
    json.dump(obj7, output, indent=4, ensure_ascii=False)





        
