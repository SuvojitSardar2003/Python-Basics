# 5. Write a class "Train" which has methods to book a ticket, get status (no. of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def bookTicket(self, start, destination):
        print(f"Ticket is booked in train no: {self.trainNo} from {start} to {destination}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self, start, destination):
        print(f"Ticket fare in train no: {self.trainNo} is running from {start} to {destination} is {randint(25,1000)}")

t = Train(34790)
t.bookTicket("Sealdah","Namkhana")
t.getStatus()
t.getFare("Sealdah","Namkhana")

# 6. Can you change the self-parameter inside a class to something else (say "suvo").Try changing self to "slf" or "suvo" and see the effects. 

# Yes, you can change self to anything like slf, suvo, etc.
# ❌ But it is strongly discouraged.
# Because self is just a naming convention, not a keyword.