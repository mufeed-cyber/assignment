import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Define a signal
from django.dispatch import Signal
rectangle_created = Signal()

# Rectangle class
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        rectangle_created.send(sender=self.__class__)  

# Signal handler
@receiver(rectangle_created)
def rectangle_created_handler(sender, **kwargs):
    print(f"Signal received for {sender.__name__}")
    print("Simulating a long-running task...")
    time.sleep(5)  
    print("Signal handler finished.")

# Creating an instance of Rectangle
print("Before creating rectangle...")
rect = Rectangle(length=10, width=5)
print("Rectangle created.")
