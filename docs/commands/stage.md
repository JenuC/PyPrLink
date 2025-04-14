# Stage Commands

This section covers commands for controlling the microscope stage in Prairie View.

## Basic Movement

### Move To Position
```bash
pypr move-stage --x 100 --y 200 --z 50
```
Moves the stage to specified coordinates.

### Relative Movement
```bash
pypr move-stage-relative --x 10 --y -5 --z 0
```
Moves the stage relative to current position.

### Home Stage
```bash
pypr home-stage
```
Returns the stage to home position.

## Position Control

### Get Position
```bash
pypr get-stage-position
```
Returns current stage position.

### Set Origin
```bash
pypr set-stage-origin
```
Sets current position as origin.

### Reset Position
```bash
pypr reset-stage-position
```
Resets stage position to default origin.

## Speed Control

### Set Speed
```bash
pypr set-stage-speed --speed 1000
```
Sets the stage movement speed.

### Set Axis Speed
```bash
pypr set-axis-speed --axis x --speed 1000
```
Sets speed for specific axis.

## Stage Settings

### Enable Axis
```bash
pypr enable-axis x
```
Enables movement along specific axis.

### Disable Axis
```bash
pypr disable-axis x
```
Disables movement along specific axis.

### Set Limits
```bash
pypr set-stage-limits --x-min -100 --x-max 100 --y-min -100 --y-max 100 --z-min 0 --z-max 50
```
Sets movement limits for each axis.

## Examples

### Basic Stage Movement
```bash
# Move to position
pypr move-stage --x 100 --y 200 --z 50

# Get current position
pypr get-stage-position

# Return to home
pypr home-stage
```

### Multi-Position Imaging
```bash
# Set up imaging parameters
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# Move to first position and image
pypr move-stage --x 0 --y 0 --z 0
pypr snap

# Move to second position and image
pypr move-stage --x 100 --y 0 --z 0
pypr snap

# Move to third position and image
pypr move-stage --x 0 --y 100 --z 0
pypr snap
```

### Z-Stack at Multiple Positions
```bash
# Set up imaging
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# First position Z-stack
pypr move-stage --x 0 --y 0 --z 0
pypr z-series --start -10 --end 10 --step 1

# Second position Z-stack
pypr move-stage --x 100 --y 0 --z 0
pypr z-series --start -10 --end 10 --step 1

# Third position Z-stack
pypr move-stage --x 0 --y 100 --z 0
pypr z-series --start -10 --end 10 --step 1
```

### Time Series at Multiple Positions
```bash
# Set up imaging
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# First position time series
pypr move-stage --x 0 --y 0 --z 0
pypr t-series --interval 60 --frames 10

# Second position time series
pypr move-stage --x 100 --y 0 --z 0
pypr t-series --interval 60 --frames 10

# Third position time series
pypr move-stage --x 0 --y 100 --z 0
pypr t-series --interval 60 --frames 10
```

## Notes

- Always verify stage position before imaging
- Use appropriate movement speeds
- Be aware of stage limits
- Regular position checks are important
- Document position changes
- Consider sample safety during movement 