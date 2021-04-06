#Question 1
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = ' 6:30'
        print(self.time)

clock = Clock(' 5:30')
clock.print_time()


#Question 2
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print (time)

clock = Clock('5:30')
clock.print_time(' 10:30')


#Question 3
class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

class Clock1(Clock):
    pass

boston_clock = Clock(' 5:30')
paris_clock = Clock1(' 10:30')

boston_clock.print_time()
paris_clock.print_time()

#Question 4

#Create Queue class
class Queue():
    #Initialize queue
    def __init__(self):
        self.element = []
    
    #Define required functions
    def print(self):
        print(self.element)
    
    def insert(self, element):
        self.element.append(element)
    
    def remove(self):
        try:
            return self.element.pop(0)
        except:
            print("Queue is empty now.")            
     
#Create object
queue = Queue()
#Print initial queue
queue.print()


#Insert 1 element
queue.insert(4)
queue.print()


#Remove 1st element and return it/return message if empty
queue.remove()


#Test exception message
queue.remove()


#Test FIFO by adding more elements
queue.print()
queue.insert(4)
queue.insert(8)
queue.insert(12)
queue.insert(16)
queue.print()


queue.remove()
queue.remove()
queue.remove()
queue.remove()

