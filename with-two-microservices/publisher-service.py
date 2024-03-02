import requests
from faker import Faker
from flask import Flask
import json
import time
from redis_om import get_redis_connection

# Microservice A - service for creating users

app = Flask(__name__)


class RedisNetwork:
    def redis_connection():
        redis = get_redis_connection(
            host='127.0.0.1',
            port=6370,
            decode_responses=True
        )
        return redis

    def create_stream_data(key:str, data_object:dict):
        redis_ = RedisNetwork.redis_connection()
        stream_data = redis_.xadd(key, data_object, '*')
        return stream_data


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

        # publish user created event
        print(user_data)
        redis = RedisNetwork
        redis.create_stream_data(key='user_created', data_object=user_data) 
        return user_data


if __name__ == '__main__':
    app.run(port=5000)