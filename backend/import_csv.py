import csv
from decimal import Decimal

from database import SessionLocal
from models import Item


db = SessionLocal()

with open("MOCK_DATA.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        item = Item(
            name=row["name"],
            description=row["description"],
            price=Decimal(row["price"])
        )

        db.add(item)

db.commit()
db.close()

print("Mock data imported successfully!")
