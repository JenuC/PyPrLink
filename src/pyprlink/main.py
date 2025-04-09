from pyprlink.tcp_client import TCPClient

def main():
    # Create a TCP client
    # Replace with your actual host and port
    client = TCPClient(host='localhost', port=5000) 
    
    # Try to connect
    if client.connect():
        try:
            # Send a message
            message = "Hello, server!"
            print(f"Sending: {message}")
            if client.send(message):
                # Receive response
                response = client.receive()
                if response:
                    print(f"Received: {response.decode()}")
        finally:
            # Always disconnect when done
            client.disconnect()
    
    print("TCP client test completed")

if __name__ == "__main__":
    main() 