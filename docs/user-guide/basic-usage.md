# Basic Usage

This guide covers common workflows and basic usage patterns for PyPrLink.

## Connecting to Prairie View

### Command Line
```bash
# Connect using default settings
pypr

# Connect with specific host
pypr --host 192.168.1.100

# Connect with custom port
pypr --port 1236
```

### Python API
```python
from pyprlink import PyPrLink

# Create connection
pypr = PyPrLink(host="192.168.1.100", port=1236)

# Connect
pypr.connect()
```

## Basic Microscope Control

### Getting Position
```bash
# Get X position
pypr -gmp x

# Get Y position
pypr -gmp y

# Get Z position
pypr -gmp z
```

### Moving Stage
```bash
# Move X axis
pypr -mr x 100

# Move Y axis
pypr -mr y 100

# Move Z axis
pypr -mr z 100
```

### PMT Control
```bash
# Get PMT value
pypr -gpmt 1

# Set PMT value
pypr -spmt 1 500
```

## Image Acquisition

### Single Scan
```bash
# Perform single scan
pypr -ss

# Get image data
pypr -gimg 1
```

### T-Series
```bash
# Start T-Series
pypr -ts

# Wait for completion
pypr -w
```

## Common Workflows

### 1. Basic Imaging
```bash
# Set PMT gain
pypr -spmt 1 500

# Set zoom
pypr -oz 2.0

# Take image
pypr -ss
```

### 2. Z-Series
```bash
# Set Z parameters
pypr -zsn 10
pypr -zsz 1.0

# Run Z-Series
pypr -zs
```

### 3. Time Series
```bash
# Set up time series
pypr -tsl

# Run time series
pypr -ts
```

## Error Handling

### Checking Status
```bash
# Get system status
pypr -gst

# Get log messages
pypr -glog
```

### Recovery
```bash
# Reset connection if needed
pypr -rst

# Quit gracefully
pypr -q
```

## Best Practices

1. **Check Status**: Always verify system status before critical operations
2. **Error Handling**: Implement proper error handling in your scripts
3. **Logging**: Use logging to track operations and debug issues
4. **Cleanup**: Always close connections properly when done
5. **Testing**: Test new workflows in a safe environment first
