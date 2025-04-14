# Experiment Commands

This section covers commands for controlling experiments in Prairie View.

## Experiment Control

### Start Experiment
```bash
pypr start-experiment --name "MyExperiment"
```
Starts a new experiment with the specified name.

### Stop Experiment
```bash
pypr stop-experiment
```
Stops the current experiment.

### Pause Experiment
```bash
pypr pause-experiment
```
Pauses the current experiment.

### Resume Experiment
```bash
pypr resume-experiment
```
Resumes a paused experiment.

## Experiment Settings

### Set Experiment Parameters
```bash
pypr set-experiment-param --name "ParameterName" --value "Value"
```
Sets an experiment parameter.

### Get Experiment Parameters
```bash
pypr get-experiment-params
```
Gets all current experiment parameters.

### Set Experiment Protocol
```bash
pypr set-protocol --name "ProtocolName"
```
Sets the experiment protocol.

## Data Management

### Save Experiment Data
```bash
pypr save-experiment --path "experiment_data/"
```
Saves the current experiment data.

### Load Experiment Data
```bash
pypr load-experiment --path "experiment_data/"
```
Loads experiment data from a specified path.

### Export Experiment Data
```bash
pypr export-experiment --path "export/" --format csv
```
Exports experiment data in the specified format.

## Examples

### Basic Experiment Workflow
```bash
# Start new experiment
pypr start-experiment --name "CellImaging"

# Set experiment parameters
pypr set-experiment-param --name "Duration" --value "3600"
pypr set-experiment-param --name "Interval" --value "60"

# Set protocol
pypr set-protocol --name "TimeSeries"

# Start imaging
pypr t-series --interval 60 --frames 10

# Save experiment data
pypr save-experiment --path "experiments/cell_imaging/"
```

### Complex Experiment Setup
```bash
# Start experiment
pypr start-experiment --name "ZStackAnalysis"

# Configure parameters
pypr set-experiment-param --name "ZStart" --value "-10"
pypr set-experiment-param --name "ZEnd" --value "10"
pypr set-experiment-param --name "ZStep" --value "1"

# Set up imaging
pypr set-resolution --x 512 --y 512
pypr set-zoom 2.0

# Perform Z-series
pypr z-series --start -10 --end 10 --step 1

# Export data
pypr export-experiment --path "exports/zstack/" --format tif
```

### Multi-Channel Experiment
```bash
# Start experiment
pypr start-experiment --name "MultiChannel"

# Configure channels
pypr enable-channel 1
pypr enable-channel 2
pypr set-channel-settings --channel 1 --power 50 --gain 1.0
pypr set-channel-settings --channel 2 --power 30 --gain 1.2

# Set up imaging
pypr set-scan-speed 400

# Perform time series
pypr t-series --interval 30 --frames 20

# Save and export
pypr save-experiment --path "experiments/multichannel/"
pypr export-experiment --path "exports/multichannel/" --format tif
```

## Notes

- Always verify experiment parameters before starting
- Use appropriate protocols for different experiment types
- Regular data saving is important
- Monitor experiment progress
- Keep track of experiment configurations
- Document any protocol modifications 