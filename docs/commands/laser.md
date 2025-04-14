# Laser Commands

This section covers commands for controlling lasers in Prairie View.

## Power Control

### Set Laser Power
```bash
pypr set-laser-power --channel 1 --power 50
```
Sets laser power for specified channel (0-100%).

### Get Laser Power
```bash
pypr get-laser-power --channel 1
```
Returns current laser power for specified channel.

### Set All Powers
```bash
pypr set-all-powers --power 50
```
Sets power for all enabled channels.

## Channel Control

### Enable Channel
```bash
pypr enable-channel 1
```
Enables specified laser channel.

### Disable Channel
```bash
pypr disable-channel 1
```
Disables specified laser channel.

### Get Channel Status
```bash
pypr get-channel-status --channel 1
```
Returns status of specified channel.

## Laser Settings

### Set Wavelength
```bash
pypr set-wavelength --channel 1 --wavelength 488
```
Sets wavelength for specified channel.

### Get Wavelength
```bash
pypr get-wavelength --channel 1
```
Returns current wavelength for specified channel.

### Set Shutter
```bash
pypr set-shutter --channel 1 --state open
```
Controls laser shutter for specified channel.

## Examples

### Basic Laser Control
```bash
# Enable channel and set power
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# Check status
pypr get-channel-status --channel 1
pypr get-laser-power --channel 1
```

### Multi-Channel Setup
```bash
# Configure first channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50
pypr set-wavelength --channel 1 --wavelength 488

# Configure second channel
pypr enable-channel 2
pypr set-laser-power --channel 2 --power 30
pypr set-wavelength --channel 2 --wavelength 561

# Configure third channel
pypr enable-channel 3
pypr set-laser-power --channel 3 --power 20
pypr set-wavelength --channel 3 --wavelength 647
```

### Time Series with Laser Control
```bash
# Set up imaging parameters
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channels
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50
pypr set-wavelength --channel 1 --wavelength 488

pypr enable-channel 2
pypr set-laser-power --channel 2 --power 30
pypr set-wavelength --channel 2 --wavelength 561

# Run time series
pypr t-series --interval 60 --frames 10

# Disable channels after imaging
pypr disable-channel 1
pypr disable-channel 2
```

### Z-Stack with Laser Control
```bash
# Set up imaging parameters
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50
pypr set-wavelength --channel 1 --wavelength 488

# Run Z-stack
pypr z-series --start -10 --end 10 --step 1

# Disable channel after imaging
pypr disable-channel 1
```

## Notes

- Always verify laser power settings
- Use minimum necessary power
- Be aware of sample phototoxicity
- Regular power calibration is important
- Document power changes
- Consider laser safety guidelines
- Check shutter status before imaging
- Monitor laser stability during long experiments 