# Microscope Control

This section covers commands for controlling the microscope in Prairie View.

## Objective Control

### Set Objective
```bash
pypr set-objective --name "20x"
```
Sets the active objective lens.

### Get Objective
```bash
pypr get-objective
```
Returns current objective lens.

### List Objectives
```bash
pypr list-objectives
```
Lists all available objectives.

## Focus Control

### Move Focus
```bash
pypr move-focus --position 100
```
Moves the focus to a specific position.

### Auto Focus
```bash
pypr auto-focus
```
Performs automatic focusing.

### Focus Range
```bash
pypr set-focus-range --start -50 --end 50 --step 5
```
Sets the focus range for auto-focusing.

## Light Path Control

### Set Light Path
```bash
pypr set-light-path --path "confocal"
```
Sets the light path configuration.

### Get Light Path
```bash
pypr get-light-path
```
Returns current light path configuration.

## Examples

### Basic Microscope Setup
```bash
# Set objective
pypr set-objective --name "20x"

# Set light path
pypr set-light-path --path "confocal"

# Perform auto-focus
pypr auto-focus
```

### Multi-Objective Imaging
```bash
# Set up first objective
pypr set-objective --name "10x"
pypr set-light-path --path "confocal"
pypr auto-focus
pypr snap

# Switch to second objective
pypr set-objective --name "20x"
pypr set-light-path --path "confocal"
pypr auto-focus
pypr snap

# Switch to third objective
pypr set-objective --name "40x"
pypr set-light-path --path "confocal"
pypr auto-focus
pypr snap
```

### Focus Stack Imaging
```bash
# Set up imaging parameters
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# Set focus range
pypr set-focus-range --start -10 --end 10 --step 1

# Perform Z-stack
pypr z-series --start -10 --end 10 --step 1
```

## Notes

- Always verify objective selection
- Regular focus calibration is important
- Check light path configuration
- Document objective changes
- Consider sample safety during focus changes
- Monitor focus stability during long experiments

## Position Commands

### Get Microscope Position (-gmp)

Get the current position of the microscope along a specified axis.

```bash
pypr -gmp <axis>
```

**Parameters:**

- `axis`: One of `x`, `y`, or `z`

**Examples:**

```bash
# Get X position
pypr -gmp x

# Get Y position
pypr -gmp y
```

**Response:**

Returns the Motor Stage axis position in micrometers.

### Set PMT Gain Parameters (-pg)

Set parameters for a specific PMT in PrairieView.

```bash
pypr -pg <channel> <value>
```

**Parameters:**

- `channel`: PMT Channel (integer)
- `value`: gain value (integer)

**Examples:**

```bash
# Set PMT Gain to value 400
pypr -pg 3 400
```


## Error Handling

All commands will return appropriate error messages if:

- PrairieView is not running
- TCP/IP server is not enabled
- Invalid parameters are provided
- Connection is lost

## Response Format

Responses from PrairieView are formatted as:

```
ACK
<response data>
DONE
```

Where:
- `ACK` indicates command received
- `<response data>` contains the actual response
- `DONE` indicates end of response 