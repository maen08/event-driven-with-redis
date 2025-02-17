
import time
from redis_om import get_redis_connection

# Microservice C - service for which needs to process user data in real-time 
# Real-time means - as soon as user is created Eg. creating roles automatically.
# No need to run a server in the consumer service - only run the file


key = 'user_created'
group = 'user-role'


class RedisNetwork:
    def redis_connection():
        redis = get_redis_connection(
            host='redis',
            port=6379,
            decode_responses=True
        )
        return redis
        
    def create_stream_data_group():
        try:
            RedisNetwork.redis_connection().xgroup_create(key, group)
        except:
            print('group already exists')


class Consume:
    def create_user_role():
        # mimic the creation by adding characters on the user data
        redis_ = RedisNetwork.redis_connection()
        while True:
            try:
                results = redis_.xreadgroup(group, key, {key: '>'}, None)

                if results != []:
                    for result in results:
                        dict_data = result[1][0][1]
                        print(dict_data)
                       
                else:
                    pass

            except Exception as e:
                print(str(e))
            time.sleep(0.2)



RedisNetwork.create_stream_data_group()
Consume.create_user_role()

