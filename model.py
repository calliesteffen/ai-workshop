#%% import os
import shutil
from PIL import Image
import json
from sklearn.model_selection import train_test_split

#%% # Load the JSON file
file_path = '/Users/calliesteffen/Desktop/ai-workshop/osu-small-animals/osu-small-animals.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Define paths
base_dir = '/Users/calliesteffen/Desktop/ai-workshop/split-dataset'  # Output directory
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# Subfolders for bird and nonbird
categories = ['bird', 'nonbird']

# Create the folder structure
for split in [train_dir, val_dir]:
    for category in categories:
        os.makedirs(os.path.join(split, category), exist_ok=True)

# Find category IDs for bird species
bird_species = [
    "common_yellowthroat",
    "eastern_bluebird",
    "gray_catbird",
    "indigo_bunting",
    "northern_house_wren",
    "song_sparrow",
    "sora"
]
bird_category_ids = [
    cat["id"] for cat in data["categories"] if cat["name"] in bird_species
]

# Function to copy and resize images to the appropriate folder
def organize_and_resize_images(annotations, split_dir, bird_category_ids, images_dir, size=(600, 600)):
    for annotation in annotations:
        image_path = os.path.join(images_dir, annotation["image_id"])
        label = 'bird' if annotation["category_id"] in bird_category_ids else 'nonbird'
        dest_dir = os.path.join(split_dir, label)

        # Resize and save the image
        try:
            with Image.open(image_path) as img:
                img = img.convert("RGB")  # Ensure RGB format
                img = img.resize(size)  # Resize the image
                dest_path = os.path.join(dest_dir, os.path.basename(image_path))
                img.save(dest_path)
        except Exception as e:
            print(f"Error processing {image_path}: {e}")

# Split the dataset into training and validation sets
annotations = data["annotations"]
train_annotations, val_annotations = train_test_split(annotations, test_size=0.2, random_state=42)

# Define the directory containing the images
images_dir = '/Users/calliesteffen/Desktop/ai-workshop/osu-small-animals'  # Replace with the actual path to your images

# Organize and resize images into train and val folders
organize_and_resize_images(train_annotations, train_dir, bird_category_ids, images_dir)
organize_and_resize_images(val_annotations, val_dir, bird_category_ids, images_dir)

print("✅ Images categorized, split, and resized successfully!")
# %%
