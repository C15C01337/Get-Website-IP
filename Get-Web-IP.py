#Devloped By C15C01337 (Bishal Aryal)
#Follow me on Twitter username @C15C01337

user_input = input("Enter website which IP you want to get:")
import socket as s

print(f'Required IP of {user_input} is {s.gethostbyname(user_input)}')
