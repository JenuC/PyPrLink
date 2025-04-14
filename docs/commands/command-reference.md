# Command Reference

This document provides a comprehensive reference for all PyPrLink commands, their corresponding function names, parameters, and return values.

## Command Format

Commands in PyPrLink follow this general format:
```
pypr [options] <command> [parameters]
```

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


## Command Reference Table

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-an` | `append_note` | `note` (str) | `bool` | Adds the given text to the notes. Supports keyword replacement. |
| `-cn` | `clear_notes` | None | `bool` | Clears any notes currently recorded. |
| `-cf` | `set_configuration_file` | `filename` (str) | `None` | Specifies an alternative configuration file to load on startup (startup only). |
| `-dw` | `set_do_not_wait_for_scans` | `enable` (bool, optional) | `bool` | Allows script commands to execute during scans (with exceptions). |
| `-ep` | `execute_program` | `filename` (str), `args` (list[str], optional) | `bool` | Runs an external program with optional arguments. |
| `-es` | `execute_script` | `category` (str), `script` (str), `iterations` (int \| str, optional), `interval` (float, optional), `variable` (str, optional) | `bool` | Executes a specified script, potentially multiple times or iterating over XY/ROI/Z. |
| `-x` | `disconnect` | None | `None` | Closes the remote TCP/IP connection (TCP/IP only, usually handled by client). |
| `-?` | `show_help` | None | `None` | Displays the script command reference document (may not be API accessible). |
| `-mto` | `message_to_operator` | `message` (str) | `bool` | Displays a message dialog to the operator and waits for OK/Cancel. |
| `-nw` | N/A | None | N/A | Modifies command execution timing; not a direct function call. |
| `-xsd` | `shutdown` | None | `bool` | Aborts tasks and shuts down Prairie View. |
| `-s` | N/A | None | N/A | Suppresses error message pop-ups; not a direct function call. |
| `-ub` | `set_utility_button` | `index` (int), `state` (bool) | `bool` | Sets the state of a specified Utility Button. |
| `-wt` | `wait` | `time_ms` (int) | `bool` | Pauses script execution for the specified milliseconds. |
| `-wfit` | `wait_for_input_trigger` | None | `bool` | Pauses script execution until an external trigger signal is received. |


## File Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-le` | `load_environment` | `filename` (str) | `bool` | Load the specified environment file (*.env). |
| `-lt` | `load_template` | `filename` (str) | `bool` | Load the specified template file (*.env). |
| `-li` | `load_images` | `filename` (str) | `bool` | Load the specified xml file and associated image(s) in playback mode. |
| `-lmp` | `load_mark_points` | `filename` (str), `clear_existing` (bool, optional) | `bool` | Load Mark Point Series (*.xml) or point locations (*.gpl), optionally appending. |
| `-lrf` | `load_roi_file` | `filename` (str) | `bool` | Load the file containing saved ROI definitions (*.roi). |
| `-lvo` | `load_voltage_output` | `filename` (str) | `bool` | Load the Voltage Output experiment (*.xml). |
| `-se` | `save_environment` | `filename` (str) | `bool` | Save the current environment to the specified file (*.env). |
| `-p` | `set_save_path` | `path` (str), `add_datetime` (bool, optional) | `bool` | Changes the directory where scan data is saved, optionally appending date/time. |
| `-fi` | `set_file_iteration` | `acq_type` (str), `iteration` (int) | `bool` | Sets the file iteration value for the specified acquisition type. |
| `-fn` | `set_file_name` | `acq_type` (str), `filename` (str), `add_datetime` (bool, optional) | `bool` | Sets the filename for the specified acquisition type, optionally appending date/time. |

## Action Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-cb` | `clear_bots` | None | `bool` | Removes all saved regions of interest within the BOT option. |
| `-cr` | `clear_rois` | None | `bool` | Removes all saved regions of interest. |
| `-gb` | `get_bot_regions` | `action_name` (str) | `bool` | Runs a predefined action to generate BOT regions from an external tool. |
| `-gr` | `get_rois` | `action_name` (str) | `bool` | Runs a predefined action to generate ROIs from an external tool. |
| `-af` | `set_action_after_frame` | `action_name` (str, optional), `filename` (str, optional), `args` (list[str], optional) | `bool` | Sets up an action to run after each acquired frame. |
| `-as` | `set_action_after_scan` | `action_name` (str, optional), `filename` (str, optional), `args` (list[str], optional) | `bool` | Sets up an action to run after each scan completes. |

## Image Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-iwf` | `image_window_fit` | None | `bool` | Scales image window(s) to fit a 512x512 display area. |
| `-iwl` | `image_window_larger` | `percent_change` (float, optional) | `bool` | Scales image window(s) up by a percentage (default 10%). |
| `-iwo` | `image_window_original` | None | `bool` | Resizes image window(s) to 1:1 scale based on resolution. |
| `-iws` | `image_window_smaller` | `percent_change` (float, optional) | `bool` | Scales image window(s) down by a percentage (default 10%). |

## Visual Script Commands (May not be directly API accessible)

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-vsf` | `visual_script_form` | `title` (str) | N/A | Creates a new window for visual script controls. |
| `-vsl` | `visual_script_label` | `text` (str) | N/A | Adds a label to the last created visual script form. |
| `-vsc` | `visual_script_control` | `key` (str), `index` (optional), `subindex` (optional), `width` (optional) | N/A | Adds a control to edit a Prairie View parameter. **Use with caution.** |
| `-vsb` | `visual_script_button` | `text` (str), `category` (str), `script_name` (str) | N/A | Adds a button to execute a script to the visual script form. |
| `-vsn` | `visual_script_new_line` | None | N/A | Moves to the next line for adding controls in the visual script form. |
| `-vss` | `visual_script_show` | None | N/A | Finalizes and displays the last created visual script form. |

## Acquisition Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-stop` | `abort` | None | `bool` | Aborts scans/scripts/experiments (external calls only). |
| `-dd` | `get_dropped_data_status` | None | `bool` | Returns True if data was dropped during the current acquisition (TCP/IP only). |
| `-gi` | `get_image_data` | `channel` (int), `process_id` (int), `memory_address` (int) | `bool` | Low-level command to get live image data into shared memory (used by PrairieLink). |
| `-lbs` | `limit_gsdma_buffer_size` | `enable` (bool, optional), `min_buffer_time_ms` (int, optional) | `bool` | Limits resonant DMA buffer size for lower latency (increases dropped data risk). |
| `-lv` | `live_scan` | `state` ('on'\|'off', optional) | `bool` | Starts or stops live scanning. |
| `-slm` | `mark_all_points_slm` | *Complex - See Ref* | `bool` | Marks multiple points simultaneously using SLM, defined on the fly or via mask. |
| `-mp` | `mark_points` | *Complex - See Ref* | `bool` | Runs a saved Mark Point Series or marks points defined on the fly. |
| `-mpm` | `set_mark_points_metadata` | `enabled` (bool, optional) | `bool` | Enables/disables saving metadata for ad hoc Mark Point experiments. |
| `-ps` | `point_scan` | `time_ms` (int, optional) | `bool` | Performs the currently defined point scan (optional duration for galvo mode). |
| `-rrd` | `read_raw_data_stream` | `process_id` (int), `memory_address` (int), `buffer_size_samples` (int) | `int` | Low-level command to get raw acquisition data into shared memory (TCP/IP only, requires `-srd`). |
| `-sam` | `set_acquisition_mode` | `mode` (str) | `bool` | Switches the current acquisition mode (e.g., Galvo, Resonant, Camera). |
| `-ss` | `single_scan` | `autosave` (bool, optional) | `bool` | Performs a single scan, optionally disabling file iteration increment. |
| `-sst` | `single_scan_triggered` | `autosave` (bool, optional) | `bool` | Performs a single scan after an input trigger, optionally disabling file iteration increment. |
| `-srd` | `stream_raw_data` | `enable` (bool, optional), `buffer_size_frames` (int, optional) | `bool` | Enables/disables caching of raw data for retrieval via `-rrd` (TCP/IP only). |
| `-ts` | `t_series` | None | `bool` | Performs a T-series using the current settings. |
| `-tsl` | `t_series_load` | `filename` (str, optional) | `bool` | Loads a T-Series definition from an environment file or the last saved state. |
| `-w` | `wait_for_scan` | None | `bool` | Pauses script execution until the current scan completes. |

## Line Scan Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-gl` | `get_freehand_line` | `action_name` (str) | `bool` | Runs a predefined action to generate a freehand line scan pattern from an external tool. |
| `-ls` | `line_scan` | `append` (bool, optional) | `bool` | Performs a line scan acquisition, optionally appending to the previous one. |
| `-ld` | `line_scan_dialog` | `state` ('open'\|'close') | `bool` | Opens or closes the line scan dialog. |
| `-lsl` | `set_line_scan_lines` | `num_lines` (int) | `bool` | Sets the number of lines for the line scan. |
| `-lm` | `set_line_scan_mode` | `line_type` (str) | `bool` | Sets the desired line type for line scan (Circle, Freehand, Line, etc.). |
| `-lls` | `load_line_scan` | `filename` (str) | `bool` | Loads a line scan definition from the specified file (*.xml). |

## Z-Series Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-fs` | `find_slice` | `channel` (int), `thickness` (float), `threshold` (float), `limit` (float), `backoff` (float), `return_on_limit` (bool) | `bool` | Steps through slices to find one meeting an intensity threshold relative to the previous. |
| `-zsd` | `set_z_series_display` | `option` ('All'\|'Middle'\|'Specific', optional), `slice_num` (int, optional) | `bool` | Sets the Z-series display option. |
| `-zsn` | `set_z_series_num_slices` | `num_slices` (int) | `bool` | Sets the number of slices (fixed step mode only). |
| `-zsb` | `set_z_series_start` | `scope` ('onlyMotors'\|'allSettings', optional), `reset_stop` (bool, optional) | `bool` | Sets the Z-series start position based on current settings (fixed step mode only). |
| `-zsz` | `set_z_series_step_size` | `step_size` (float) | `bool` | Sets the step size (fixed step mode only). |
| `-zse` | `set_z_series_stop` | `scope` ('onlyMotors'\|'allSettings', optional), `reset_start` (bool, optional) | `bool` | Sets the Z-series end position based on current settings (fixed step mode only). |
| `-zs` | `z_series` | None | `bool` | Performs a Z-series using the current settings. |
| `-zsas` | `z_series_add_slice` | None | `bool` | Adds the current position as a slice (variable step mode only). |
| `-zscl` | `z_series_clear` | None | `bool` | Removes all slices/positions from the current Z-Series. |
| `-zsis` | `z_series_insert_slice` | `index` (int) | `bool` | Inserts the current position as a new slice at the specified index (variable step mode only). |
| `-zsl` | `z_series_load` | `name` (str) | `bool` | Loads the saved Z-series definition with the given name. |
| `-zsmt` | `z_series_move_to` | `position` ('Start'\|'Middle'\|'Stop'\|int) | `bool` | Moves focus to a defined Z-series position (Start, Middle, Stop, or slice number). |
| `-zsrs` | `z_series_remove_slice` | `index` (int) | `bool` | Removes the slice at the specified index (variable step mode only). |
| `-zss` | `z_series_save` | `name` (str) | `bool` | Saves the current Z-series definition with the given name. |
| `-zssm` | `set_z_series_step_mode` | `mode` ('Fixed'\|'Variable') | `bool` | Sets the Z-Series step mode (fixed or variable). |

## Scan Setting Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-er` | `enter_roi` | `x` (float), `y` (float), `width` (float), `height` (float) | `bool` | Defines an ROI based on fractional FOV coordinates and dimensions. |
| `-gts` | `get_state` | `key` (str), `index` (optional), `subindex` (optional) | *Varies* | Returns the value of a specific Prairie View state parameter (TCP/IP only). |
| `-pa` | `parameter_set` | `name` (str), `track` (int, optional) | `bool` | Applies settings from a named Parameter Set. |
| `-roi` | `roi_load` | `name` ('noROI'\|str) | `bool` | Loads the ROI definition with the specified name or exits the current ROI. |
| `-spp` | `get_samples_per_pixel` | None | `int` | Gets the current number of samples acquired per pixel (TCP/IP only). |
| `-c` | `set_channel_state` | `channel` (int), `state` ('On'\|'Off'), ... | `bool` | Enables or disables specified image channels. Repeat pairs for multiple channels. |
| `-dt` | `set_dwell_time` | `dwell_time` (float) | `bool` | Sets the pixel dwell time. |
| `-fa` | `set_frame_averaging` | `frames` (int) | `bool` | Sets the number of frames to average. |
| `-is` | `set_image_size` | `width` (int), `height` (int, optional) | `bool` | Sets the image pixel dimensions. |
| `-oz` | `set_optical_zoom` | `zoom` (float) | `bool` | Sets the optical zoom level. |
| `-sr` | `set_scan_rotation` | `angle` (float) | `bool` | Sets the scan rotation angle. |
| `-sts` | `set_state` | `key` (str), `value`, `index` (optional), `subindex` (optional), `force_modified` (bool, optional) | `bool` | Changes the value of a specific Prairie View state parameter. **Use with caution.** |
| `-co` | `set_custom_output` | `index` (int), `percent` (float), `value` (float), ... | `bool` | Defines a custom output waveform based on percent of scan line and value pairs. |

## Hardware Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-ca` | `set_camera_feature` | `feature` (str), `value`, `index` (int, optional) | `bool` | Changes a specific camera feature (e.g., ExposureTime, Gain). |
| `-cg` | `center_galvos` | `center` (bool, optional) | `bool` | Centers imaging galvos (True/default) or returns them to parked positions (False). |
| `-ge` | `get_etl_value` | `position_um` (float) | `float` | Returns the drive value for the ETL at a specific position (TCP/IP only). |
| `-gmp` | `get_motor_position` | `axis` ('X'\|'Y'\|'Z'), `index` (int, optional) | `float` | Returns the current position of the specified motor axis (TCP/IP only). |
| `-mr` | `move_motor_relative` | `axis` ('X'\|'Y'\|'Z'), `distance_um` (float), `index` (int, optional), ..., `wait` (bool, optional) | `bool` | Moves a motor axis by a specified distance. Repeat for multiple axes. Optionally wait for completion. |
| `-nni` | `set_nikon_ni_device` | `device` (str), `value` | `bool` | Changes the setting of a specified Nikon NI microscope device. |
| `-nti` | `set_nikon_ti_device` | `device` (str), `value` (optional) | `bool` | Changes the setting of a specified Nikon TI microscope device. |
| `-png` | `pan_galvo` | `axis` ('X'\|'Y'\|'Center'), `distance` ('Coarse'\|'Medium'\|'Fine'\|float) | `bool` | Pans the imaging galvos by a specified distance or preset amount, or centers them. |
| `-gc` | `send_gpio_command` | `command` (str), `args` (list[str], optional) | `bool` | Sends a command directly to the GPIO controller. **Requires Bruker consultation.** |
| `-mc` | `send_mamc_command` | `command` (str), `args` (list[str], optional) | `bool` | Sends a command directly to the multi-axis motor controller. **Requires Bruker consultation.** |
| `-pc` | `send_piezo_command` | `command` (str), `args` (list[str], optional) | `bool` | Sends a command directly to the prairie piezo controller. **Requires Bruker consultation.** |
| `-sc` | `send_servo_command` | `command` (str), `args` (list[str], optional) | `bool` | Sends a command directly to the quad servo controller. **Requires Bruker consultation.** |
| `-rc` | `send_resonant_command` | `command` (str), `args` (list[str], optional) | `bool` | Sends a command directly to the resonant galvo controller. **Requires Bruker consultation.** |
| `-ma` | `move_motor_absolute` | `axis` ('X'\|'Y'\|'Z'), `position` (float), `index` (int, optional), ..., `wait` (bool, optional) | `bool` | Moves a motor axis to a specified absolute position. Repeat for multiple axes. Optionally wait for completion. |
| `-sol` | `set_objective_lens` | `name` (str) | `bool` | Sets the active objective lens by name. |
| `-sfc` | `set_sfc_feature` | `feature` (str), `value`, `index` (int, optional) | `bool` | Changes a specific SFC feature (e.g., ExposureTime, EmissionFilter). |
| `-scm` | `set_slm_calibration_mask` | `region_num` (int), `stripe_depth` (int), `region_count` (int, optional) | `bool` | Applies a calibration mask to the SLM. |
| `-zdc` | `set_z_device_control` | `mode` ('External'\|'Software', optional) | `bool` | Sets the Z device control mode (Software/default or External/analog voltage). |
| `-zm` | `set_zeiss_microscope_device` | `device` (str), `value` | `bool` | Changes the setting of a specified Zeiss microscope device. |

## Laser/PMT Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-abr` | `set_alternate_beam_route` | `index` (int), `enabled` (bool) | `bool` | Enables or disables the specified alternate beam route. |
| `-slbr` | `set_secondary_laser_beam_route` | `enabled` (bool) | `bool` | Legacy command (use `-abr`). Enables/disables the first alternate beam route. |
| `-lp` | `set_laser_power` | `name_or_index` (str\|int), `power_or_by` (float\|'By'), `offset` (float, optional) | `bool` | Sets laser power to an absolute value or adjusts it relatively. |
| `-mpw` | `set_multiphoton_wavelength` | `wavelength_nm` (float), `index` (int, optional) | `bool` | Sets the wavelength for the specified multi-photon laser. |
| `-pg` | `set_pmt_gain` | `index` (int), `gain_or_action` (float\|'Zero'\|'Previous'\|'By'), `offset` (float, optional) | `bool` | Sets PMT gain to a value, zero, previous value, or adjusts relatively. |

## Shutter Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-ohs` | `override_hard_shutter` | `name_or_index` (str\|int), `state` ('Open'\|'Close'\|'Auto') | `bool` | Forces a specific hardware shutter open, closed, or returns to auto mode. |
| `-hrd` | `set_hard_shutter` | `state` ('Open'\|'Close') | `bool` | Opens or closes the main imaging hardware shutter. |
| `-sft` | `set_soft_shutter` | `state` ('Open'\|'Close') | `bool` | Opens or closes the imaging software shutter (blocks display/saving). |

## Stage Position Commands

| Command | Function Name | Parameters | Return Value | Description |
|---------|---------------|------------|--------------|-------------|
| `-spa` | `add_stage_position` | `x` (float, optional), `y` (float, optional), `z` (float, optional), ... | `bool` | Adds one or more stage locations (XYZ triplets). Uses current position if no parameters. |
| `-spc` | `clear_stage_positions` | None | `bool` | Clears all saved stage locations. |
| `-lspf` | `load_stage_position_file` | `filename` (str) | `bool` | Loads saved XYZ stage positions from a file (*.xy). |
| `-mtsp` | `move_to_stage_position` | `index` (int) | `bool` | Moves the stage to the position specified by its index in the list. |
| `-sspf` | `save_stage_position_file` | `filename` (str) | `bool` | Saves the current list of XYZ stage positions to a file (*.xy). |
| `-sgl` | `set_grid_locations` | None | `bool` | Generates a grid of XY stage locations covering the current list (Atlas Imaging montage). |
| `-sgo` | `set_grid_overlap` | `overlap_percent` (float) | `bool` | Defines the overlap percentage for Atlas Imaging grid generation. | 