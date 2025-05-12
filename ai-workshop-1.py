
#%% get to know your data 
# Find the JSON file of osu-small-animals
import json

file_path = '/Users/calliesteffen/Desktop/ai-workshop/osu-small-animals/osu-small-animals.json'

# Check if the file exists before attempting to open it
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print("✅ JSON file loaded successfully!\n")
        print(json.dumps(data, indent=4))  # Nicely formatted output
else:
    print("❌ File not found. Please check the path.")

#%% # Check how many top level keys are in the JSON data
if data:
    # Check if the JSON data is a dictionary
    if isinstance(data, dict):
        print("Structure of each top-level key in the JSON data:\n")
        for key in data.keys():
            print(f"Key: {key}")
            value = data[key]
            # Print the type of the value
            print(f"Type: {type(value).__name__}")
            # Print a preview of the value
            if isinstance(value, dict):
                print("Preview: Dictionary with keys:", list(value.keys())[:5])  # Show up to 5 keys
            elif isinstance(value, list):
                print(f"Preview: List with {len(value)} items. First item:")
                if len(value) > 0:
                    print(json.dumps(value[0], indent=4))  # Show the first item
            else:
                print(f"Preview: {value}")
            print("\n" + "-"*50 + "\n")  # Separator for readability
    else:
        print("The JSON data is not a dictionary.")
else:
    print("❌ Unable to load JSON data.")

#link https://github.com/agentmorris/MegaDetector/blob/main/megadetector/data_management/README.md#coco-camera-traps-format



# %% number of images per category
from collections import defaultdict

if data:
    # Create a mapping of category_id → category_name
    category_map = {cat["id"]: cat["name"] for cat in data["categories"]}

    # Track image_ids per category (to avoid double-counting)
    category_to_images = defaultdict(set)

    # Loop through annotations and map category_id to image_id
    for ann in data["annotations"]:
        category_id = ann["category_id"]
        image_id = ann["image_id"]
        category_to_images[category_id].add(image_id)

    # Print the number of images for each category
    print("Number of images per category:\n")
    for category_id, image_ids in category_to_images.items():
        category_name = category_map.get(category_id, "Unknown")
        print(f"{category_name}: {len(image_ids)} images")
else:
    print("❌ Unable to process data due to errors.")


# %% visualize number of images per category
import matplotlib.pyplot as plt
from collections import defaultdict

# %% visualize number of images per category
if data and "categories" in data and "annotations" in data:
    try:
        # Create a mapping of category_id → category_name
        category_map = {cat["id"]: cat["name"] for cat in data["categories"]}

        # Count the number of images per category
        category_to_images = defaultdict(set)
        for ann in data["annotations"]:
            category_id = ann["category_id"]
            image_id = ann["image_id"]
            category_to_images[category_id].add(image_id)

        # Prepare data for visualization
        categories = []
        image_counts = []
        for category_id, image_ids in category_to_images.items():
            categories.append(category_map.get(category_id, "Unknown"))
            image_counts.append(len(image_ids))

        # Plot the bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(categories, image_counts, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Number of Images')
        plt.title('Number of Images per Category')
        plt.xticks(rotation=45, ha='right')  # Rotate category names for better readability
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"❌ An error occurred during visualization: {e}")
else:
    print("❌ 'categories' or 'annotations' key is missing in the data.")

# %% unique locations (based on image folder?)
if data:
    # Create a set to store unique locations
    unique_locations = set()

    # Assuming locations are part of the 'images' key
    for image in data["images"]:
        if "location" in image:  # Replace 'location' with the actual key for location in the 'images' data
            unique_locations.add(image["location"])

    # Print the number of unique locations
    print(f"Number of unique locations: {len(unique_locations)}")
else:
    print("❌ Unable to process data due to errors.")



# %% pick 10 random images and test labels manually - could do a grid of imaages in order to viusally see label
import random 
if data:
    # Ensure the 'images' and 'annotations' keys exist in the data
    if "images" in data and "annotations" in data:
        # Randomly select 10 images
        random_images = random.sample(data["images"], min(10, len(data["images"])))

        print("Randomly selected images and their labels:\n")
        for image in random_images:
            image_id = image["id"]
            image_file_name = image.get("file_name", "Unknown")
            
            # Find annotations for this image
            labels = [ann for ann in data["annotations"] if ann["image_id"] == image_id]
            
            # Print image details and associated labels
            print(f"Image: {image_file_name}")
            if labels:
                for label in labels:
                    category_id = label["category_id"]
                    category_name = category_map.get(category_id, "Unknown")
                    print(f"  - Label: {category_name} (Category ID: {category_id})")
            else:
                print("  - No labels found for this image.")
            print("-" * 50)
    else:
        print("❌ 'images' or 'annotations' key is missing in the data.")
else:
    print("❌ Unable to process data due to errors.")


# %% count images with multiple labels - 0?
from collections import Counter  # Add this import if not already present
if data and "annotations" in data:
    # Count occurrences of each image_id in the annotations
    image_label_counts = Counter(ann["image_id"] for ann in data["annotations"])

    # Find images with multiple labels - 0?
    multiple_labels = {image_id: count for image_id, count in image_label_counts.items() if count > 1}

    # Print the results
    print(f"Total images with multiple labels: {len(multiple_labels)}")
    print("Examples of images with multiple labels:")
    for image_id, count in list(multiple_labels.items())[:10]:  # Show up to 10 examples
        print(f"Image ID: {image_id}, Number of Labels: {count}")
else:
    print("❌ 'annotations' key is missing in the data.")



# %% find images with no labels - all data is labeled?
#images key and annotations key - check if annotations have image id and see if images list have annotations in annotations lists depends on what you want to do
if data and "images" in data and "annotations" in data:
    # Get all image IDs from the images list
    all_image_ids = {image["id"] for image in data["images"]}

    # Get all image IDs that have labels from the annotations list
    labeled_image_ids = {ann["image_id"] for ann in data["annotations"]}

    # Find image IDs with no labels
    unlabeled_image_ids = all_image_ids - labeled_image_ids

    # Print the results
    print(f"Total images with no labels: {len(unlabeled_image_ids)}")
    if unlabeled_image_ids:
        print("Examples of images with no labels:")
        for image_id in list(unlabeled_image_ids)[:10]:  # Show up to 10 examples
            print(f"Image ID: {image_id}")
else:
    print("❌ 'images' or 'annotations' key is missing in the data.")
!
# %% find labels that correspond to non-existent images 0?
if data and "images" in data and "annotations" in data:
    # Get all image IDs from the images list
    all_image_ids = {image["id"] for image in data["images"]}

    # Get all image IDs referenced in the annotations list
    labeled_image_ids = {ann["image_id"] for ann in data["annotations"]}

    # Find labels that reference non-existent images
    invalid_labels = labeled_image_ids - all_image_ids

    # Print the results
    print(f"Total labels referencing non-existent images: {len(invalid_labels)}")
    if invalid_labels:
        print("Examples of invalid labels:")
        for image_id in list(invalid_labels)[:10]:  # Show up to 10 examples
            print(f"Invalid Image ID: {image_id}")
else:
    print("❌ 'images' or 'annotations' key is missing in the data.")

# %% categories - experiment desing not right or wrong but your designing experiment. train calssifier to skunks vs everything else here is list of categories pick skunk and then set everything esle to not skunnk. cla
