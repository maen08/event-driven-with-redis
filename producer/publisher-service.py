
from faker import Faker
from flask import Flask
import json
import time
from redis_om import get_redis_connection, HashModel

# Microservice A - service for creating users

app = Flask(__name__)


class RedisNetwork:
    def redis_connection():
        try:
            redis = get_redis_connection(
                host='127.0.0.1',
                port=6379,
                decode_responses=True
            )
            return redis
        except:
            print("Errors on connecting to redis server ...")
            return

    def create_stream_data(key:str, data_object:dict):
        redis_ = RedisNetwork.redis_connection()
        redis_.xadd(key, data_object, '*')
        # return stream_data


class UserDataModel:
    # Eg. save data in mysql db
    db_connection = 'mysql_db'
    pass


class HashUserData(HashModel):
    # redis does not accept raw json data or model - has to be hashed
    name:str
    phone:str
    job:str
    address:str

    class Meta:
        # this should be a real db eg. mysql
        # database = UserDataModel.db_connection
        database = RedisNetwork.redis_connection()


class PublishUser:
    def create_user():
        fake = Faker()
        user = {
            'name':fake.name(),
            'phone': fake.phone_number(),
            'job': fake.job(),
            'address': fake.address()
        }
        # user = json.dumps(user) # convert dict to json data
        return user
    

    @app.post('/add-user')
    def server_api_endpoint():
        # Microservice A which creates users and save them in its own DB (assume mysql db and also it saves the event in redis).
        # Other microservices assume B which want to process user information as soon as user is created.
        # And thats where we use redis streaming between these two microservices.
        
        user_data = PublishUser.create_user()
        
        # save data in the db eg. mysql
        user_db = UserDataModel()

        # then hash the data and publish the event
        user = HashUserData(
            name=user_data['name'],
            phone=user_data['phone'],
            job=user_data['job'],
            address=user_data['address']
        )
        user.save()


        # redis stream takes in dict data    
        redis = RedisNetwork
        redis.create_stream_data(
            key='user_created',
            data_object=user.__dict__ 
        ) 
        return user_data


if __name__ == '__main__':
    app.run(port=5001, host="0.0.0.0")