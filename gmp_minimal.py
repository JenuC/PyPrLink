#!/usr/bin/env python
"""
Minimal script to send -gmp x to 0.0.0.0:1236
"""

import socket

def send_gmp_command(host='0.0.0.0', port=1236, value='x'):
    """Send -gmp command and return the response"""
    try:
        # Create socket and connect
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))
        
        # Send command
        command = f"-gmp {value}"
        sock.sendall(command.encode())
        
        # Receive response
        response = sock.recv(1024)
        return response.decode()
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        sock.close()

if __name__ == "__main__":
    response = send_gmp_command()
    if response:
        print(f"Response: {response}")
    else:
        print("No response received") 