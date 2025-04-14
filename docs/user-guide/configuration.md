# Configuration

PyPrLink can be configured through various methods to suit your specific needs and environment.

## Configuration Methods

### 1. Command Line Arguments

Basic configuration can be done through command line arguments:

```bash
pypr --host 192.168.1.100 --port 1236 --timeout 5000
```

### 2. Configuration File

For more complex setups, use a configuration file:

```yaml
# config.yaml
connection:
  host: 192.168.1.100
  port: 1236
  timeout: 5000

logging:
  level: INFO
  file: pyprlink.log

hardware:
  default_zoom: 1.0
  scan_speed: medium
```

## Configuration Options

### Connection Settings

- `host`: IP address of the Prairie View computer
- `port`: TCP/IP port (default: 1236)
- `timeout`: Connection timeout in milliseconds
- `retry_attempts`: Number of connection retry attempts

### Logging Settings

- `level`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `file`: Path to log file
- `console`: Enable/disable console output

### Hardware Settings

- `default_zoom`: Default optical zoom level
- `scan_speed`: Default scan speed (slow, medium, fast)
- `pmt_gain`: Default PMT gain settings
- `laser_power`: Default laser power settings

## Environment Variables

You can also set configuration through environment variables:

```bash
export PYPR_HOST=192.168.1.100
export PYPR_PORT=1236
export PYPR_TIMEOUT=5000
```

## Best Practices

1. **Start Simple**: Begin with basic configuration and add complexity as needed
2. **Document Changes**: Keep track of configuration changes and their effects
3. **Backup Configs**: Save working configurations for different setups
4. **Test Thoroughly**: Verify configuration changes in a safe environment first

## Troubleshooting

Common configuration issues and solutions:

- **Connection Timeouts**: Increase timeout value or check network connectivity
- **Permission Errors**: Check file permissions for log files and config files
- **Hardware Issues**: Verify hardware settings match your microscope setup
