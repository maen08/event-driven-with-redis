import requests
from faker import Faker
from flask import Flask
import json
import time

# Microservice B - service for which needds to process user data in real-time 
# Real-time means - as soon as user is created Eg. creating user ID card, etc.

app = Flask(__name__)

class Publish:
    def create_user():
        fake = Faker()
        user = {
            'name':fake.name(),
            'phone': fake.phone_number(),
            'job': fake.job(),
            'address': fake.address()
        }
        user = json.dumps(user)
        return user
    

    @app.post('/add-user')
    def server_api_endpoint():
        # Microservice A which creates users and save them in its own DB (assume mysql db and also it saves the event in redis).
        # Other microservices assume B which want to process user information as soon as user is created.
        # And thats where we use redis streaming between these two microservices.
        # Why redis streaming ? - 
        
        user_data = Publish.create_user()
        return user_data


if __name__ == '__main__':
    app.run(port=5000)