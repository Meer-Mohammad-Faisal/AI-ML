# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

#import random
#or
from random import randint

class Train:
    def  __init__(self,trainNo):
        self.trainNo = trainNo


    def book(self,fro,to):
        print(f"Ticket is booked in train number: {Train} from {fro} to {to}")
    
    def getStatus(self):
        print(f" train number: {self.trainNo} is running on time")


    
    def getFare(self,fro,to):
        print(f"Ticket fare in Train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = Train(12344)
t.book("Supaul","Bhopal")
t.getStatus()
t.getFare("RaniKamlapti","patna")