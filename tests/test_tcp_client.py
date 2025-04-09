import pytest
import socket
import threading
import time
from unittest.mock import Mock, patch

from pyprlink.tcp_client import TCPClient

# Simple echo server for testing
class MockServer:
    def __init__(self, host='localhost', port=5555):
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.thread = None
        
    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()
        time.sleep(0.1)  # Give server time to start
        
    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        if self.thread:
            self.thread.join(timeout=1)
            
    def run(self):
        self.server_socket.settimeout(0.5)
        while self.running:
            try:
                client_socket, _ = self.server_socket.accept()
                try:
                    data = client_socket.recv(1024)
                    if data:
                        # Echo the data back
                        client_socket.sendall(data)
                finally:
                    client_socket.close()
            except socket.timeout:
                continue
            except Exception:
                break


class TestTCPClient:
    
    @pytest.fixture
    def mock_server(self):
        # Use a different port for testing
        server = MockServer(port=5555)
        server.start()
        yield server
        server.stop()
    
    def test_connection(self, mock_server):
        client = TCPClient(port=5555)
        assert client.connect() is True
        client.disconnect()
        
    def test_send_receive(self, mock_server):
        client = TCPClient(port=5555)
        assert client.connect() is True
        
        # Test sending and receiving data
        test_message = "Hello, test server!"
        assert client.send(test_message) is True
        
        # Get the response
        response = client.receive()
        assert response is not None
        assert response.decode() == test_message
        
        client.disconnect()
    
    def test_not_connected(self):
        client = TCPClient(port=9999)  # Use a port that's unlikely to be in use
        assert client.send("test") is False
        assert client.receive() is None
    
    @patch('socket.socket')
    def test_connection_error(self, mock_socket):
        # Mock socket to raise an exception on connect
        mock_socket_instance = Mock()
        mock_socket.return_value = mock_socket_instance
        mock_socket_instance.connect.side_effect = socket.error("Mocked connection error")
        
        client = TCPClient()
        assert client.connect() is False
        
    @patch('socket.socket')
    def test_send_error(self, mock_socket):
        # Mock socket for successful connection but failed send
        mock_socket_instance = Mock()
        mock_socket.return_value = mock_socket_instance
        mock_socket_instance.sendall.side_effect = socket.error("Mocked send error")
        
        client = TCPClient()
        client.socket = mock_socket_instance  # Manually set socket to simulate connected state
        assert client.send("test data") is False 