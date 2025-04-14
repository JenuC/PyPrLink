# Command Reference

This document provides a comprehensive reference for all PyPrLink commands, their corresponding function names, parameters, and return values.

## Command Format

Commands in PyPrLink follow this general format:
```
pypr [options] <command> [parameters]
```

## Command Reference Table

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-gmp` | `get_microscope_position` | `axis` (x, y, z) | `float` | Get the current position of the specified microscope axis |
| `-smp` | `set_microscope_position` | `axis` (x, y, z), `position` (float) | `bool` | Set the position of the specified microscope axis |
| `-gpmt` | `get_pmt_value` | `channel` (int) | `float` | Get the current PMT value for the specified channel |
| `-spmt` | `set_pmt_value` | `channel` (int), `value` (float) | `bool` | Set the PMT value for the specified channel |
| `-gscn` | `get_scan_settings` | None | `dict` | Get the current scan settings |
| `-sscn` | `set_scan_settings` | `settings` (dict) | `bool` | Set the scan settings |
| `-gimg` | `get_image` | `channel` (int) | `numpy.ndarray` | Get the image from the specified channel |
| `-simg` | `set_image` | `channel` (int), `image` (numpy.ndarray) | `bool` | Set the image for the specified channel |
| `-gcfg` | `get_config` | None | `dict` | Get the current configuration |
| `-scfg` | `set_config` | `config` (dict) | `bool` | Set the configuration |
| `-glog` | `get_log` | None | `str` | Get the log messages |
| `-slog` | `set_log_level` | `level` (int) | `bool` | Set the log level |
| `-gver` | `get_version` | None | `str` | Get the PyPrLink version |
| `-gst` | `get_status` | None | `dict` | Get the current status |
| `-rst` | `reset` | None | `bool` | Reset the connection |
| `-q` | `quit` | None | `bool` | Quit the application |

## Python API Reference

For more detailed information about the Python API, see the [API Reference](../api-reference.md) page.

## Examples

### Get Microscope Position

```python
# Command line
pypr -gmp x

# Python API
from pyprlink import PyPrLink
client = PyPrLink()
position = client.get_microscope_position('x')
print(f"X position: {position}")
```

### Set PMT Value

```python
# Command line
pypr -spmt 1 500

# Python API
from pyprlink import PyPrLink
client = PyPrLink()
success = client.set_pmt_value(1, 500)
print(f"PMT value set: {success}")
``` 