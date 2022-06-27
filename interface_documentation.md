# Interface Documentation

## Components of the interface

### User Input (Left Side)

The user input components are all under the root component `container_input`.

The primary components on this side which are not associated with one of the input stages are:

| Name | Type | Purpose |
| ------ | ------ | -------- |
| button_start | QPushButton | Button to start processing |
| button_cancel | QPushButton | Button to cancel |

#### Stage 1

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_one | QGroupBox | Container for stage |
| label_stage_one | QLabel | Label describing stage |
| button_choose_files | QPushButton | Button to allow the user to select images for processing |

#### Stage 2

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_two | QGroupBox | Container for stage |
| label_stage_two | QLabel | Label describing stage |
| button_clockwise | QPushButton | Button for clockwise rotation |
| button_counter_clockwise | QPushButton | Button for counter-clockwise rotation |
| button_ninety | QPushButton | Button for 90° rotation |
| button_one_eighty | QPushButton | Button for 180° rotation |
| button_custom_rotation | QPushButton | Button for custom x° rotation |
| angle | QSpinBox | Input for custom angle |


#### Stage 3

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_three | QGroupBox | Container for stage |
| label_stage_three | QLabel | Label describing stage |
| button_same_quality | QPushButton | Button for no compression |
| button_different_quality | QPushButton | Button for compression |
| percentage_quality | QSpinBox | Input for compression amount |
| label_percentage | QLabel | Label describing custom compression |

#### Stage 4

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_four | QGroupBox | Container for stage |
| label_stage_four | QLabel | Label describing stage |
| choose_colour | QComboBox | Choose Colour Space |
| choose_file_type | QComboBox | Choose File Type |

#### Stage 5

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_five | QGroupBox | Container for stage |
| label_stage_five | QLabel | Label describing stage |
| button_choose_save | QPushButton | Button to allow the user to select saving location |

### Preview (Right Side)

#### Before

#### After
