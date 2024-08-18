#This code is by Mohammed Obeidi
#this code is to sort the dataset I downloaded and organize it by file

#imports
import os
import shutil

#define the directory containing the dataset
source_dir = 'Multi_Pie'
destination_dir = 'Archive'

#loop through each file in the dataset
for filename in os.listdir(source_dir):
    #split the filename by underscores
    parts = filename.split('_')
    
    #extract subject ID and camera ID (or any other attribute)
    camera_id = parts[3]
    
    #define the target directory based on the attributes
    target_dir = os.path.join(destination_dir, camera_id)
    
    #create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    #move the file to the target directory
    shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
