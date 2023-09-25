
from PIL import Image
import os
from python.settings import settings 
import shutil

# # Define the input and output directories
# input_dir = settings['italy']
# output_dir = settings['italy']

# # Create the output directory if it doesn't exist
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Specify the target width (you can adjust this)
# target_width = 2400

# # Iterate through the input directory and resize images
# for filename in os.listdir(input_dir):
#     if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
#         input_path = os.path.join(input_dir, filename)
#         outname = "fmt_" + filename
#         output_path = os.path.join(output_dir, filename)

#         # Open the image
#         image = Image.open(input_path)

#         # Calculate the new height while maintaining the aspect ratio
#         width, height = image.size
#         aspect_ratio = float(width) / float(height)
#         new_height = int(target_width / aspect_ratio)

#         # Resize the image
#         resized_image = image.resize((target_width, new_height), resample=Image.ANTIALIAS)

#         # Save the resized image
#         resized_image.save(output_path)

#         print(f"Resized {filename} to {target_width}x{new_height}")

# print("Done resizing images.")

# Specify the folder containing the .jpg files
# folder_path = settings['france']

# # Get a list of all .jpg files in the folder
# jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.JPG')]

# # Iterate over the list and rename the files
# for i, jpg_file in enumerate(jpg_files, start=1):
#     new_name = f'france_{i}.jpg'
#     old_path = os.path.join(folder_path, jpg_file)
#     new_path = os.path.join(folder_path, new_name)
#     shutil.move(old_path, new_path)
#     print(f'Renamed: {jpg_file} -> {new_name}')

folder_path = settings['france']

# Get a list of all .jpg and .JPG files in the folder
jpg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

# Create a set to keep track of used file names
used_names = set()

# Iterate over the list and rename the files
for i, jpg_file in enumerate(jpg_files, start=1):
    # Extract the file extension
    file_name, file_extension = os.path.splitext(jpg_file)
    
    # Ensure that the extension is lowercase
    file_extension = file_extension.lower()
    
    new_name = f'france_{i}{file_extension}'
    while new_name in used_names:
        i += 1
        new_name = f'france_{i}{file_extension}'
    
    old_path = os.path.join(folder_path, jpg_file)
    new_path = os.path.join(folder_path, new_name)
    
    # Move the file while avoiding overwriting
    shutil.move(old_path, new_path)
    print(f'Renamed: {jpg_file} -> {new_name}')
    
    used_names.add(new_name)

