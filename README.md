# EDA-Implementation
Serves as boilerplate and PoC in implementing EDA 

1. With redis streaming stack to exchage data on real time - Event Driven Architecture (EDA)
- Its suitable for multiple services (3 services or more)
- Can be complex to implement as services increase
- Easy to scale services horizontally

2. With Server Sent Events (SSE) - to achieve real time data exchange
- Suitable for few services interaction 
- Complex to implement with multiple services
- Easy to build and fast
- Frontend client can consume data with SSE direct (no need for streaming stack)
- Hard to scale