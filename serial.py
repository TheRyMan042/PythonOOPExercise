# Ryan Hutchings
# Unit 21.4 Python OOP Exercises

"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Attributes:
    -------------------------
    start: int
        A integer to start counting from (defaults to 1)
    count: int
        Keeps track of total count from being added by one
    
    Tests
    -------------------------
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    My Tests
    ------------------------
    >>> serial = SerialGenerator()

    >>> serial.generate()
    0

    >>> serial.generate()
    1

    >>> serial.generate()
    2

    >>> serial.generate()
    3

    >>> serial.reset()

    >>> serial.generate()
    0
    """

    def __init__(self, start=0):
        self.start = start
        self.count = self.start

    def __repr__(self):
        """Gives a representation of what is being ran"""
        return f"<SerialGenerator start={self.start} next={self.count}>"
    
    def generate(self):
        """Adds onto the count value by one (default value is start value)"""
        current_count = self.count
        self.count += 1
        if (current_count == self.start):
            return self.start
        else:
            return current_count
        
        
    def reset(self):
        """Resets the count value to the starting number"""
        self.count = self.start

