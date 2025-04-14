# Command Reference Overview

This section provides an overview of the command structure in PyPrLink.

## Command Structure

Commands in PyPrLink follow this general format:
```bash
pypr <command> [options] [parameters]
```

## Command Categories

### System Commands
Basic system control commands for managing the Prairie View environment.
```bash
pypr status
pypr start
pypr stop
```

### Imaging Commands
Commands for controlling image acquisition and parameters.
```bash
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0
pypr snap
```

### Stage Commands
Commands for controlling the microscope stage.
```bash
pypr move-stage --x 100 --y 200 --z 50
pypr get-stage-position
```

### Laser Commands
Commands for controlling laser power and settings.
```bash
pypr set-laser-power --channel 1 --power 50
pypr enable-channel 1
```

### Experiment Commands
Commands for managing experiments and protocols.
```bash
pypr start-experiment --name "MyExperiment"
pypr t-series --interval 60 --frames 10
```

### Microscope Commands
Commands for controlling microscope hardware.
```bash
pypr set-objective --name "20x"
pypr auto-focus
```

## Common Options

Many commands support these common options:
- `--help`: Show help for the command
- `--verbose`: Enable verbose output
- `--quiet`: Suppress output

## Examples

### Basic Imaging Workflow
```bash
# Check system status
pypr status

# Set up imaging parameters
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# Take image
pypr snap
```

### Time Series Experiment
```bash
# Start experiment
pypr start-experiment --name "TimeSeries"

# Set up imaging
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Configure channel
pypr enable-channel 1
pypr set-laser-power --channel 1 --power 50

# Run time series
pypr t-series --interval 60 --frames 10
```

## Notes

- Always check system status before starting
- Use appropriate parameters for your experiment
- Document command sequences
- Regular calibration is important
- Monitor system performance
- Consider sample safety
