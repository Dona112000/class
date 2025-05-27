# Create a Counter class that has a method increment() and reset().
# Keep track of the count using an instance variable.

class Counter:
    def __init__(self):
        self.count = 0  # instance variable to keep track of count

    def increment(self):
        self.count += 1  # increases count by 1
        print(f"Count after increment: {self.count}")

    def reset(self):
        self.count = 0  # resets count to 0
        print("Counter reset to 0.")

# Example usage
c = Counter()
c.increment()   # Output: Count after increment: 1
c.increment()   # Output: Count after increment: 2
c.reset()       # Output: Counter reset to 0
c.increment()   # Output: Count after increment: 1


#or

class Counter:
    def __init__(self, start_value=0):   # start_value has a default value of 0
        self.count = start_value  # Initializes count with the given value or default (0)

    def increment(self):
        self.count += 1  # Increments count by 1
        # print(f"Count after increment: {self.count}")


    def reset(self):
        self.count = 0  # Resets count to 0

    def show(self):
        print("Current count:", self.count)
# Starting from 5
c1 = Counter(5)
c1.show()    # Output: Current count: 5
c1.increment()  # count = 6
c1.increment()
c1.show()    # Output: Current count: 6

# Starting from 10
c2 = Counter(10)
c2.show()    # Output: Current count: 10
c2.increment()  # count = 11
c2.increment() 
c2.increment() 
c2.increment() 
c2.show()    # Output: Current count: 11

# Default starting value (0)
c3 = Counter()  # Default is 0
c3.show()    # Output: Current count: 0
c3.increment()  # count = 1
c3.increment() 
c3.increment() 
c3.increment() 
c3.increment() 
c3.show()    # Output: Current count: 1
