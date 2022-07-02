'''

Python script providing image rotation functionality. This script provides all the business logic for
performing the computation for the image rotation/modification.

This is split into several methods, the methods which are called outside of this script are:
    - start - takes parameters from user and performs the computation
    - preview - takes parameters for one image from the user and returns a preview image

The methods only called within this script are:
    - get_image - takes a filepath and reads the image as a Pillow image
    - rotate - takes a Pillow image and a rotation and rotates the image
    - colour_convert - takes a Pillow image and a colour space and converts it to that space
    - save_image - takes a Pillow image, a compression rate and a folder location and saves the image

'''

# Standard Library Imports
import os, sys
from PIL import Image

def start(filenames : list(),   destination : str,      angle : int,                direction : str,
                quality : int,           colour : str,             file_extension : str,
                progress_bar, progress_label) -> bool:
    '''
    Method to perform the transformation on specified images and save the results.

    Parameters:
        - filenames - filepaths of the image(s) to be processed
        - destination - filepath of the destination folder
        - angle - angle of the rotation
        - direction - direction of rotation ("Clockwise" or "Counter-Clockwise")
        - quality - quality to be changed to
        - colour - colour space to convert to
        - file_extension - file extension the files should be saved as
        - progress_bar - QProgressBar to be used to show progress to user
        - progress_label - QLabel to be used to show progress to user

    Returns:
        - True if it was successful
        - False if it was unsuccessful
    '''
    # Update the progress bar
    progress_bar.setValue(0)

    # Update the progress label
    progress_label.setText(str(0) + " out of " + str(len(filenames)))

    try:
        # Loop through all files
        for filename in filenames:
            # Get the image
            image = get_image(filename)

            # Rotate the image
            image = rotate(image, angle, direction)

            # Convert the image's colour
            image = colour_convert(image, colour)

            # Save the image including compression
            save_image(destination, filename, image, quality, file_extension)

            # Update the progress bar
            progress_bar.setValue(int(((filenames.index(filename)+1.0)*100.0)/float(len(filenames))))
            
            # Update the progress label
            progress_label.setText(str(filenames.index(filename)+1) + " out of " + str(len(filenames)))

        # Update the progress bar
        progress_bar.setValue(100)

        # Return success code
        return True
    except:
        # If an error returns, return an error code
        return False

def preview(filename : str, angle : int, direction : str, quality : int, colour : str) -> list():
    '''
    Method to create a preview of the transformation for a spefied image and transformations.

    Parameters:
        - filename - filepath of the image to be previewed
        - angle - angle of the rotation
        - direction - direction of rotation ("Clockwise" or "Counter-Clockwise")
        - quality - quality to be changed to
        - colour - colour space to convert to

    Returns:
        - tuple of image data, x dimension, y dimension
        - None if the transformation was unsuccessful
    '''
    try:
        # Get the image
        image = get_image(filename)

        # Rotate the image if the rotation has been specified
        if angle is not None and direction is not None:
            image = rotate(image, angle, direction)

        # Change the colour space of the image if specified
        if colour is not None:
            image = colour_convert(image, colour)

        # Convert the image to the correct colour space for showing in the interface
        if image.mode == "RGB":
            r, g, b = image.split()
            image = Image.merge("RGB", (b, g, r))
        elif  image.mode == "RGBA":
            r, g, b, a = image.split()
            image = Image.merge("RGBA", (b, g, r, a))
        elif image.mode == "L":
            image = image.convert("RGBA")
        image = image.convert("RGBA")

        # Convert the image to bytes
        data = image.tobytes("raw", "RGBA")

        # Return the image data and size
        return data, image.size[0], image.size[1]
    except:
        # If an error occurs, return None
        return None

def get_image(filename : str) -> Image:
    '''
    Method to get the image from a specified filepath.

    Parameters:
        - filename - filepath of the image file

    Returns:
        - Pillow Image
    '''

    # Open the image in RGBA format
    return Image.open(filename).convert('RGBA')

def rotate(image : Image, angle : int, direction : str) -> Image:
    '''
    Method to rotate an image to a specified rotation.

    Parameters:
        - image - Pillow image before rotation transformation
        - angle - angle to be rotated by
        - direction - "Clockwise" or "Counter-Clockwise"

    Returns:
        - Pillow Image after rotation
    '''

    # Convert the angle to counter-clockwise if not already
    if direction == "Clockwise":
        angle = 360-angle

    # Rotate the image by the angle
    return image.rotate(angle, expand=True)

def colour_convert(image : Image, colour : str) -> Image:
    '''
    Method to convert an image to a specified colour space.

    Parameters:
        - image - Pillow image before colour transformation
        - colour - colour space to be converted to

    Returns:
        - Pillow Image after colour transformation
    '''

    # Convert the image either to RGB or grayscale and return the converted image
    if colour == "Colour":
        return image.convert('RGB')
    elif colour == "Black/White":
        return image.convert('1')

def save_image(destination : str,   filename : str,
                          image : Image,      quality : int,
                          extension : str):
    '''
    Method to save an image with specified parameters.

    Parameters:
        - destination - filepath of the destination folder
        - filename - filepath of the original image
        - image - Pillow image post all alterations except for compression
        - quality - quality to save the image at
        - extension - file extension to use (or "Same as original")
    '''

    # Get only the filename (without file path)
    filename = filename[filename.rindex("/"):]

    # If a different file type is requested, update the filepoth for the image
    if "." in extension:
        filename = filename[:filename.rindex(".")] + extension

    # Save the image with the requested quality
    image.save(destination+filename, quality=quality, optimize=True)
