import threading
from django.dispatch import Signal, receiver

# Define a signal
rectangle_created = Signal()

# Rectangle class
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        print(f"Main thread: {threading.current_thread().name}") 
        rectangle_created.send(sender=self.__class__)  

    # Making the Rectangle class iterable
    def __iter__(self):
        yield self.length
        yield self.width

# Signal handler
@receiver(rectangle_created)
def rectangle_created_handler(sender, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
    print(f"Signal received for {sender.__name__}")

# Creating an instance of Rectangle
rect = Rectangle(length=10, width=5)

# Iterating over the instance of Rectangle
for dimension in rect:
    print(dimension)
