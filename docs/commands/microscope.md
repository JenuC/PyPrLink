# Microscope Control Commands

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