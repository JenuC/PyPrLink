# Installation

## Prerequisites

- Python 3.10 or later
- PrairieView software running with TCP/IP server enabled

## Install from PyPI

```bash
pip install pyprlink
```

## Configuration

The TCP/IP port and logging/print statements
can be controlled using the .env file within the src
or loading these values to the environment Path.

```ini
ADDRESS=localhost
PORT=5000
LOG_LEVEL=INFO
```

## Verify Installation

```bash
# Check version
pypr --version

# Test connection
pypr -gmp x
```

## Development Installation

For development, install with test dependencies:

```bash
# Clone the repository
git clone https://github.com/jenuv/PV-FLIM.git
cd PV-FLIM

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Ensure PrairieView is running
   - Check if TCP/IP server is enabled
   - Verify port number in `.env`

2. **Command Not Found**
   - Ensure Python scripts directory is in PATH
   - Try reinstalling the package

3. **Permission Issues**
   - Run with appropriate permissions
   - Check file ownership of `.env` 