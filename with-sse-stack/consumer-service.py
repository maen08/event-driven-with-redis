from sseclient import SSEClient
import requests


def handle_event():
   
    # Replace the URL with the actual SSE endpoint URL
    sse_url = "http://localhost:4000/add-user"
    headers = {"Accept":"text/event-stream"}
    req = requests.post(url=sse_url, headers=headers,stream=True)

    # Connect to the SSE endpoint
    client = SSEClient(req)

    # Iterate through events
    for event in client.events():
        print(event.data)


handle_event()