import fbchat
from getpass import getpass

username = str(input("input username: "))
clint = fbchat.Client(username,getpass())
no_of_friends = int(input("Number of friends:  "))

for i in range(no_of_friends):
    name = str(input("Name:  "))
    friends = clint.getUsers(name)


friend = friends[0]
msg = str(input("message: "))
send = clint.send(friend.uid,msg)
if send:
    print("message sent successfully")