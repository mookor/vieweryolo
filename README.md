# YOLO Viewer
YOLO Viewer is a PyQt6-based desktop application designed to view images annotated with YOLO (You Only Look Once) object detection labels.\
It allows you to easily load a dataset, navigate through images, and visualize the detection boxes overlaid on each image.\
You can switch between training and validation sets and navigate through the images using both buttons and keyboard shortcuts.

## Features
Load a data.yaml file that contains paths to the image dataset.\
Navigate through images with "Previous" and "Next" buttons or keyboard shortcuts (A/D keys).\
Toggle between training and validation datasets using a checkbox.\
Visualize YOLO annotations with bounding boxes on images.\
Resize images to fit the display area while keeping their aspect ratio.\
Display class names on the bounding boxes.\
Support for keyboard shortcuts (A for previous image, D for next image).\

## Requirements
+ Python 3.6+
+ PyQt6
+ OpenCV
+ NumPy
+ PyYaml
+ A valid YOLO annotation format (data.yaml, images, and annotations)

You can install the required dependencies using the following:
` pip install PyQt6 opencv-python numpy pyyaml `

## Installation
### build from source 
+ Clone the repository or download the code.
+ Navigate to the project directory in your terminal.
+ Run the following command to install the application:
`pip install -e . `

### build from pip 
`pip install vieweryolo`

## Usage
After installation, you can run the YOLO Viewer by typing the following command in your terminal:\
`vieweryolo`

This will open the application window. From there, you can:

Click "Select data.yaml" to load your dataset.\
Use the "Previous" and "Next" buttons to navigate through the images.\
Toggle between the training and validation datasets using the checkbox.\
You can also use the A key to go to the previous image and the D key to go to the next image.\


## How to Contribute
If you would like to contribute to the project, feel free to fork it, make improvements, and submit a pull request. You can also open issues if you encounter any bugs or have feature requests.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.