from faker import Faker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import random


fake = Faker()

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'password123', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database successfully connected")
        break
    except Exception as error:
        print(f"Error connecting to database: {error}")
        time.sleep(2)
genders = ["male", "female"]

for x in range(int(input("How many people do you want to insert in db?"))):
    try: first_name, last_name = fake.name().split(" ")
    except ValueError: pass
    birthday = f"{random.randint(1950,2010)}/{random.randint(1,12)}/{random.randint(1,28)}"
    gender = random.choice(genders)
    phone_number = random.randint(1000000000, 9999999999)
    email = f"{first_name}.{last_name}982039@gmail.com"
    cursor.execute("""INSERT INTO people (first_name, last_name, birthday, gender, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *""", (first_name, last_name, birthday, gender, email, phone_number))
    conn.commit()