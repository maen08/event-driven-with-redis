# EDA Implementaion with Redis
This project serves as boilerplate and PoC in implementing EDA using Redis, Docker and Python microservices

- Redis offers alot of features and functionalities but in this project we'll use it to tackle:
1. Real-time data store
- With this PoC it covers the scenario where real-time data are exchanged within microservices.
- Publisher and Subscriber flow to generate and consume data in real-time

2. Streaming & messaging
- The stream data type enables high-rate data ingestion, messaging, event sourcing, and notifications.
- Ensure to miss no data from streaming services / APIs.


## Project structure
1. With redis streaming stack to exchage data on real time - Event Driven Architecture (EDA)
- Its suitable for multiple services (more than 2 microservices)
- Can be complex to implement as a number of microservices increases
- Easy to scale services horizontally 

2. With Server Sent Events (SSE) - Event Driven Architecture (EDA)
- Suitable for few microservices interaction 
- Complex to implement with multiple services
- Easy to build and fast
- Frontend client can consume data with SSE direct (no need for external tools like Redis)
- Hard to scale
