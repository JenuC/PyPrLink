# System Commands

This section covers commands for controlling the Prairie View system.

## System Status

### Check Status
```bash
pypr status
```
Shows the current system status.

### Check Connection
```bash
pypr check-connection
```
Verifies the connection to Prairie View.

## System Control

### Start System
```bash
pypr start
```
Starts the Prairie View system.

### Stop System
```bash
pypr stop
```
Stops the Prairie View system.

### Reset System
```bash
pypr reset
```
Resets the Prairie View system.

## Configuration

### Load Configuration
```bash
pypr load-config --path "config.xml"
```
Loads a configuration file.

### Save Configuration
```bash
pypr save-config --path "config.xml"
```
Saves current configuration to a file.

### Set Parameter
```bash
pypr set-param --name "ParameterName" --value "Value"
```
Sets a system parameter.

## Maintenance

### Calibrate System
```bash
pypr calibrate
```
Performs system calibration.

### Clean System
```bash
pypr clean
```
Performs system cleaning procedure.

### Check Logs
```bash
pypr logs
```
Shows system logs.

## Examples

### Basic System Management
```bash
# Check system status
pypr status

# Start system
pypr start

# Load configuration
pypr load-config --path "default_config.xml"

# Perform calibration
pypr calibrate
```

### Configuration Management
```bash
# Load custom configuration
pypr load-config --path "custom_config.xml"

# Modify parameter
pypr set-param --name "ScanSpeed" --value "400"

# Save modified configuration
pypr save-config --path "modified_config.xml"
```

### System Maintenance
```bash
# Check system status
pypr status

# Perform cleaning
pypr clean

# Check logs for issues
pypr logs
```

## Notes

- Always check system status before performing operations
- Keep track of configuration changes
- Regular maintenance is important for system performance
- Monitor system logs for potential issues
- Backup important configurations
