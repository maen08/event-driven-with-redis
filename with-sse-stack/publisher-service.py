
from faker import Faker
from flask import Flask, request
import requests
import json
from sseclient import SSEClient

# Microservice A - service for creating users

app = Flask(__name__)


class PublishUser:
    def create_user():
        fake = Faker()
        user = {
            'name':fake.name(),
            'phone': fake.phone_number(),
            'job': fake.job(),
            'address': fake.address()
        }
        user = json.dumps(user) # convert dict to json data
        return user


    @app.post('/add-user')
    def server_api_endpoint():
        # Microservice A which creates users and save them in its own DB (assume mysql db and also it saves the event in redis).
        # Other microservices assume B which want to process user information as soon as user is created.
        # And thats where we use redis streaming between these two microservices.
       
       headers = {"Accept":"text/event-stream"}
       url = "http://localhost:4000/add-user"
       data = PublishUser.create_user()

       # post data to the server as stream event
       req = requests.post(url=url, headers=headers,json=data)
       user_data = req.json()
        # then save data in the db eg. mysql
        # user_db.save()
       return user_data

   

if __name__ == '__main__':    
    app.run(port=4000)