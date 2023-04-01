class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
        self.l=[]
        for i in range(1,self.seats+1):
            self.l.append(i)
        print(self.l)

    def getStatus(self):
        print(f"Name of train is {self.name}")
        print(f"Number of seats in the train are {self.seats}")
        print(f"fare of the train is {self.fare}")
    def bookTicket(self):
        if(len(self.l)>0):
            print(f"Your ticket is successfully booked and your seat number is {self.seats}")
            self.l.remove(self.seats)
            self.seats=self.seats-1    
        else:
            print("Train full")
    def cancelTicket(self):
        seatnum=int(input("Enter seat number"))
        self.l.append(seatnum)
        self.seats=self.seats+1
interstate=Train("Rajdhani express",10,90)
interstate.getStatus()
interstate.bookTicket()
interstate.getStatus()
interstate.cancelTicket()
        