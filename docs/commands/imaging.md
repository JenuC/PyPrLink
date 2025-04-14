# Imaging Commands

This section covers commands for controlling imaging parameters in Prairie View.

## Resolution Control

### Set Resolution
```bash
pyprlink set-resolution --x 512 --y 512
```
Sets image resolution (X x Y pixels).

### Get Resolution
```bash
pyprlink get-resolution
```
Returns current image resolution.

## Zoom Control

### Set Zoom
```bash
pyprlink set-zoom 2.0
```
Sets objective zoom level.

### Get Zoom
```bash
pyprlink get-zoom
```
Returns current zoom level.

## Pinhole Control

### Set Pinhole
```bash
pyprlink set-pinhole --channel 1 --size 1.0
```
Sets pinhole size for specified channel.

### Get Pinhole
```bash
pyprlink get-pinhole --channel 1
```
Returns current pinhole size for specified channel.

## PMT Control

### Set PMT
```bash
pyprlink set-pmt --channel 1 --voltage 600
```
Sets PMT voltage for specified channel.

### Get PMT
```bash
pyprlink get-pmt --channel 1
```
Returns current PMT voltage for specified channel.

## Scan Settings

### Set Scan Speed
```bash
pyprlink set-scan-speed --speed 400
```
Sets scan speed (lines per second).

### Get Scan Speed
```bash
pyprlink get-scan-speed
```
Returns current scan speed.

### Set Scan Mode
```bash
pyprlink set-scan-mode --mode resonant
```
Sets scan mode (resonant or galvo).

### Get Scan Mode
```bash
pyprlink get-scan-mode
```
Returns current scan mode.

## Examples

### Basic Imaging Setup
```bash
# Set up imaging parameters
pyprlink set-resolution --x 512 --y 512
pyprlink set-zoom 2.0

# Configure PMT
pyprlink set-pmt --channel 1 --voltage 600

# Configure pinhole
pyprlink set-pinhole --channel 1 --size 1.0

# Set scan parameters
pyprlink set-scan-speed --speed 400
pyprlink set-scan-mode --mode resonant
```

### Multi-Channel Imaging
```bash
# Set up imaging parameters
pyprlink set-resolution --x 512 --y 512
pyprlink set-zoom 2.0

# Configure first channel
pyprlink set-pmt --channel 1 --voltage 600
pyprlink set-pinhole --channel 1 --size 1.0

# Configure second channel
pyprlink set-pmt --channel 2 --voltage 550
pyprlink set-pinhole --channel 2 --size 1.2

# Configure third channel
pyprlink set-pmt --channel 3 --voltage 500
pyprlink set-pinhole --channel 3 --size 1.5
```

### Time Series Imaging
```bash
# Set up imaging parameters
pyprlink set-resolution --x 512 --y 512
pyprlink set-zoom 2.0

# Configure PMT
pyprlink set-pmt --channel 1 --voltage 600
pyprlink set-pinhole --channel 1 --size 1.0

# Set scan parameters
pyprlink set-scan-speed --speed 400
pyprlink set-scan-mode --mode resonant

# Run time series
pyprlink t-series --interval 60 --frames 10
```

### Z-Stack Imaging
```bash
# Set up imaging parameters
pyprlink set-resolution --x 512 --y 512
pyprlink set-zoom 2.0

# Configure PMT
pyprlink set-pmt --channel 1 --voltage 600
pyprlink set-pinhole --channel 1 --size 1.0

# Set scan parameters
pyprlink set-scan-speed --speed 400
pyprlink set-scan-mode --mode resonant

# Run Z-stack
pyprlink z-series --start -10 --end 10 --step 1
```

## Notes

- Optimize resolution for your experiment
- Use appropriate zoom level
- Adjust PMT voltage carefully
- Consider pinhole size impact
- Choose appropriate scan speed
- Select suitable scan mode
- Regular PMT calibration is important
- Document imaging parameters
- Consider photobleaching
- Monitor image quality 