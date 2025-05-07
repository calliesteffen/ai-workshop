
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

# %%
