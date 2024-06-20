import os
import shutil
def delete_files_and_folders( detection_dir):
    print(detection_dir)
    # Ensure the directory is a valid path
    if not isinstance(detection_dir, (str, bytes, os.PathLike)):
        raise TypeError(f"Expected str, bytes, os.PathLike or None, but got {type(detection_dir).__name__}")

    # Check if the directory exists
    if not os.path.exists(detection_dir):
        print(f"The directory {detection_dir} does not exist.")
        return

    # Loop through all the items in the directory
    for item in os.listdir(detection_dir):
        item_path = os.path.join(detection_dir, item)

        # If the item is a file, delete it
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.unlink(item_path)
            print(f"Deleted file: {item_path}")

        # If the item is a directory, delete it and its contents
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted folder: {item_path}")

if __name__ == "__main__":
    detection_dir = './runs/'
    delete_files_and_folders(detection_dir)