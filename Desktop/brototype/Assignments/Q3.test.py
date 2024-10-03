from django.db import transaction
from Q3 import Rectangle, Shape

# Creating a Rectangle instance
def create_rectangle_with_transaction():
    try:
        with transaction.atomic():
            print("Transaction started...")
            rect = Rectangle.objects.create(length=10, width=5)
            print("Rectangle created in transaction.")

            # Let's check if Shape object is created by signal
            print(f"Shape count after save: {Shape.objects.count()}")  

            # Rollback the transaction manually
            raise Exception("Rolling back the transaction intentionally.")
    except Exception as e:
        print(str(e))

    # Check if Shape objects still exist
    print(f"Shape count after rollback: {Shape.objects.count()}") 
