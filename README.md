# PyPrLink

A TCP/IP client for communicating with PrairieView.
Alternate for PraireLink Application from Python. 
Python-PrairieLink (PyPrLink)

## Installation

```bash
pip install pyprlink
```

## Configuration

Create a `.env` file in your project directory with the following variables:
```
ADDRESS=your_server_address
PORT=your_port_number
LOG_LEVEL=INFO  # or DEBUG or ERROR
```

## Usage

### As a Python Module

```python
from pyprlink.tcp_client import ask_PV

# Send commands to PrairieView
ask_PV('-gmp', 'x')  # Get microscope position
ask_PV('-pg', '3', '400')  # Set page number and value
```

### From Command Line

After installation, you can use the `pyprlink` command directly:

```bash
# Get help
pyprlink --help

# Send commands
pypr -gmp x
pypr -pg 3 400
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

## Examples

Common commands:
- `pypr -gmp x` - Get microscope position for x-stage
- `pypr -pg 3 400` - Set PMT gain on channel 3 to 400

## License

This project is licensed under the MIT License - see the LICENSE file for details.
