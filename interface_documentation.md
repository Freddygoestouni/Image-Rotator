# Interface Documentation

This document contains the names and types of all components of the user interface. This is used by the controller python scripts to access the specific components of the interfaces. 

## Main Page (main_page_interface.ui)

### Navigation Bar

| Name | Type | Purpose |
| ------ | ------ | -------- |
| nav_bar_widget | QWidget | Container for the user input |
| label_title | QLabel | Label for the title of the application |
| label_icon | QLabel | Icon of the application |
| button_close | QPushButton | Button to close the application |
| button_minimise | QPushButton | Button to minimise the application |
| button_user_guide | QPushButton | Button to open the user guide |

### User Input (Left Side)

The user input components are all under the root component `container_input`.

The primary components on this side which are not associated with one of the input stages are:

| Name | Type | Purpose |
| ------ | ------ | -------- |
| container_input | QWidget | Container for the user input |
| button_start | QPushButton | Button to start processing |

#### Stage 1

| Name | Type | Purpose |
| ------ | ------ | -------- |
| group_one | QGroupBox | Container for stage |
| label_stage_one | QLabel | Label describing stage |
| label_no_files | QLabel | Label detailing the number of files selected |
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

The user input components are all under the root component `container_preview`.

| Name | Type | Purpose |
| ------ | ------ | -------- |
| container_preview | QWidget | Container for preview |
| label_preview | QLabel | Title label for this component |
| choose_image | QComboBox | Choice for which image to preview |
| image_after | QLabel | Label to hold the image |

## Processing Page (processing_interface.ui)

| Name | Type | Purpose |
| ------ | ------ | -------- |
| label_title | QLabel | Label for the title of the page |
| label_icon | QLabel | Icon of the application |
| label_progress | QLabel | Label describing the progress |
| progress_bar | QProgressBar | Progress bar  |
| button_new | QPushButton | Button to reset the application  |
| button_close | QPushButton | Button to close the application |
| button_cancel | QPushButton | Button to cancel the current execution |

## User Guide Page (user_guide_interface.ui)

### Navigation Bar

| Name | Type | Purpose |
| ------ | ------ | -------- |
| nav_bar_widget | QWidget | Container for the user input |
| label_title | QLabel | Label for the title of the application |
| label_page_title | QLabel | Label for the title of the page |
| label_icon | QLabel | Icon of the application |
| button_close | QPushButton | Button to close the application |
| button_minimise | QPushButton | Button to minimise the application |
| button_user_guide | QPushButton | Button to open the user guide |

### User guide

| Name | Type | Purpose |
| ------ | ------ | -------- |
| container_content | QWidget | Container for the content of the application |
| button_back | QPushButton | Button to go back to the interface |
| guide_text_left | QTextBrowser | Left half of the user guide |
| guide_text_right | QTextBrowser | Right half of the user guide |
