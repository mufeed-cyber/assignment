from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Rectangle Model
class Rectangle(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()

# Another Model for signal handler changes
class Shape(models.Model):
    name = models.CharField(max_length=100)

# Signal Handler
@receiver(post_save, sender=Rectangle)
def rectangle_saved_handler(sender, instance, **kwargs):
    print("Signal handler executing...")
    # Create a Shape entry
    Shape.objects.create(name="Rectangle from Signal")
    print("Shape created in the signal handler.")
