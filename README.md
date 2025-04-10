# PyPrLink

A TCP/IP client for communicating with PrairieView.
Alternate for PraireLink Application from Python. 
Python-PrairieLink (PyPrLink)

## Installation

```bash
pip install -e .
```

## Usage

```python
from pyprlink.tcp_client import TCPClient

# Create a client
client = TCPClient(host='localhost', port=5000)

# Connect to the server
if client.connect():
    try:
        # Send a message
        client.send("Hello, server!")
        
        # Receive response
        response = client.receive()
        if response:
            print(response.decode())
    finally:
        # Always disconnect when done
        client.disconnect()
```

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

## examples

- ask_PV('-gmp','x')
- ask_PV('-pg', '3','400')
- ask_PV('-x')
