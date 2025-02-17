## Event Driven Architecture (EDA) - Minimal PoC
This project serves as a PoC in implementing EDA using Redis as Event Manager (Broker)

![](https://images.ctfassets.net/9ijoq4ake70f/77eAY6nEWk7L2EDfymylL9/e6e740fb2d60ce953cd3c9b7ebf1fd2a/EDA-1.png)

## PoV
- Assume we have 3 microservices in our architecture and we want them to talk to each other.
- There are so many ways to do that but lets explore the easiest approach which is realtime and fast. 
- Redis can make this happen with easy by streaming events.

```
producer   ==> service A
consumer-1 ==> service B
consumer-2 ==> service C

```

## Components
- Docker/Compose - package the service
- Redis  - act as events manager (broker)
- Microservices (eg. Python) - actual servies (any language)


```

- Redis offers alot of features and functionalities but in this project we'll use it to tackle:
1. Real-time data store
- With this PoC it covers the scenario where real-time data are exchanged within microservices.
- Publisher and Subscriber flow to generate and consume data in real-time

2. Streaming & messaging
- The stream data type enables high-rate data ingestion, messaging, event sourcing, and notifications.
- Ensure to miss no data from streaming services / APIs.

```

## Project structure
 With redis streaming stack to exchage data on real time - Event Driven Architecture (EDA)
- Its suitable for multiple services (more than 2 microservices)
- Can be complex to implement as a number of microservices increases
- Easy to scale services horizontally 

```
.
├── consumer-1
│   ├── consumer-service-1.py
│   └── requirements.txt
├── consumer-2
│   ├── consumer-service-2.py
│   └── requirements.txt
├── Makefile
├── producer
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── publisher-service.py
│   └── requirements.txt
└── README.md

4 directories, 10 files
```

### Run
- Run the producer service (service A) by running `make run` in the folder `producer`. It will run on `http://localhost:5000/`
- Run consumers `consumer-2` and `consumer-2` by navigate into respective folders and run `python3 consumer-service-1.py`
- Make sure you've installed all `requirements.txt`
- Consumers in this PoC will stream data by printing them, so leave them running (listen for an event from producer)
- Hint: you can build them separately as well


### Todo On Prod
- Think of security and prod configs
- Service authentication
- Explore other redis configs eg. data caching 
- Prod level deployment


### Thanks
- To me (maen08) 
