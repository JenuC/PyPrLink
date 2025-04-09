import socket

class TCPClient:
    def __init__(self, host='localhost', port=5000, timeout=5):
        """
        Initialize a TCP client
        
        Args:
            host (str): Host to connect to
            port (int): Port to connect to
            timeout (int): Socket timeout in seconds
        """
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = None
        
    def connect(self):
        """Establish connection to the server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.timeout)
            self.socket.connect((self.host, self.port))
            print(f"Connected to {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            self.socket = None
            return False
            
    def disconnect(self):
        """Close the connection"""
        if self.socket:
            self.socket.close()
            self.socket = None
            print("Disconnected")
            
    def send(self, data):
        """
        Send data to the server
        
        Args:
            data (str or bytes): Data to send
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.socket:
            print("Not connected")
            return False
            
        try:
            # Convert string to bytes if needed
            if isinstance(data, str):
                data = data.encode()
                
            self.socket.sendall(data)
            return True
        except Exception as e:
            print(f"Send error: {e}")
            return False
            
    def receive(self, buffer_size=1024):
        """
        Receive data from the server
        
        Args:
            buffer_size (int): Size of the receive buffer
            
        Returns:
            bytes or None: Received data or None on error
        """
        if not self.socket:
            print("Not connected")
            return None
            
        try:
            data = self.socket.recv(buffer_size)
            return data
        except Exception as e:
            print(f"Receive error: {e}")
            return None 