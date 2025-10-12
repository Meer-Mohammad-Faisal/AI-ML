# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

from random import randint

class Train:
    def  __init__(slf,trainNo):
        slf.trainNo = trainNo


    def book(self,fro,to):
        print(f"Ticket is booked in train number: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f" train number: {self.trainNo} is running on time")


    
    def getFare(faisal,fro,to):
        print(f"Ticket fare in Train no: {faisal.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = Train(12344)
t.book("Supaul","Bhopal")
t.getStatus()
t.getFare("RaniKamlapti","patna")

