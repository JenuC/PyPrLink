# Python API Reference

## PyPrLink Class

The main class for interacting with Prairie View.

### Constructor

```python
PyPrLink(host="localhost", port=1236, timeout=5000)
```

Parameters:
- `host` (str): IP address of the Prairie View computer
- `port` (int): TCP/IP port number
- `timeout` (int): Connection timeout in milliseconds

### Connection Methods

#### connect()
```python
def connect(self) -> bool:
    """Establish connection to Prairie View."""
```

Returns:
- `bool`: True if connection successful, False otherwise

#### disconnect()
```python
def disconnect(self) -> bool:
    """Close connection to Prairie View."""
```

Returns:
- `bool`: True if disconnection successful, False otherwise

### Microscope Control Methods

#### get_position(axis: str) -> float
```python
def get_position(self, axis: str) -> float:
    """Get current position of specified axis."""
```

Parameters:
- `axis` (str): 'x', 'y', or 'z'

Returns:
- `float`: Current position in microns

#### move_relative(axis: str, distance: float) -> bool
```python
def move_relative(self, axis: str, distance: float) -> bool:
    """Move specified axis by relative distance."""
```

Parameters:
- `axis` (str): 'x', 'y', or 'z'
- `distance` (float): Distance to move in microns

Returns:
- `bool`: True if movement successful

### PMT Control Methods

#### get_pmt_value(channel: int) -> float
```python
def get_pmt_value(self, channel: int) -> float:
    """Get current PMT value for specified channel."""
```

Parameters:
- `channel` (int): PMT channel number

Returns:
- `float`: Current PMT value

#### set_pmt_value(channel: int, value: float) -> bool
```python
def set_pmt_value(self, channel: int, value: float) -> bool:
    """Set PMT value for specified channel."""
```

Parameters:
- `channel` (int): PMT channel number
- `value` (float): New PMT value

Returns:
- `bool`: True if setting successful

### Image Acquisition Methods

#### single_scan() -> bool
```python
def single_scan(self) -> bool:
    """Perform a single scan."""
```

Returns:
- `bool`: True if scan successful

#### get_image(channel: int) -> numpy.ndarray
```python
def get_image(self, channel: int) -> numpy.ndarray:
    """Get image data from specified channel."""
```

Parameters:
- `channel` (int): Image channel number

Returns:
- `numpy.ndarray`: Image data array

### System Methods

#### get_status() -> dict
```python
def get_status(self) -> dict:
    """Get current system status."""
```

Returns:
- `dict`: Status information including:
  - connection_state
  - hardware_status
  - active_processes
  - error_states

#### get_log() -> str
```python
def get_log(self) -> str:
    """Get current log messages."""
```

Returns:
- `str`: Log message string

#### reset() -> bool
```python
def reset(self) -> bool:
    """Reset connection to Prairie View."""
```

Returns:
- `bool`: True if reset successful

## Error Handling

The API uses exceptions for error handling:

```python
class PyPrLinkError(Exception):
    """Base exception for PyPrLink errors."""
    pass

class ConnectionError(PyPrLinkError):
    """Raised when connection fails."""
    pass

class CommandError(PyPrLinkError):
    """Raised when a command fails."""
    pass
```

Example usage:
```python
try:
    pypr = PyPrLink()
    pypr.connect()
    pypr.move_relative('x', 100)
except ConnectionError as e:
    print(f"Connection failed: {e}")
except CommandError as e:
    print(f"Command failed: {e}")
```
