# PyPrLink Documentation

PyPrLink is a TCP/IP client for communicating with PrairieView software. It provides a simple command-line interface and Python API for microscope control and automation.

## Features

- Simple command-line interface
- Python API for automation
- Real-time microscope control
- Configurable logging
- Cross-platform support

## Quick Example

```bash
# Install PyPrLink
pip install pyprlink

# Get microscope position
pypr -gmp x
```

## Documentation Structure

- **Getting Started**
  - [Installation](getting-started/installation.md) - Setup and configuration
  //- [Quick Start](getting-started/quickstart.md) - Basic usage examples

- **User Guide**
  - [Configuration](user-guide/configuration.md) - Advanced configuration options
  - [Basic Usage](user-guide/basic-usage.md) - Common workflows

- **Command Reference**
  - [Overview](commands/index.md) - Command syntax and usage
  - [Microscope Control](commands/microscope.md) - Position and PMT commands
  - [System Commands](commands/system.md) - System-level operations
  - [Command Reference](commands/command-reference.md) - Comprehensive command list

- **API Reference**
  - [Python API](api-reference.md) - Detailed API documentation

## Project Layout

```
pyprlink/
    TCP client implementation
docs/
    Documentation
tests/
    Test suite
```

## Contributing

See the [Contributing](contributing.md) guide for information on how to contribute to this project.

## Changelog

Check the [Changelog](changelog.md) for version history and updates. 