import os
import shutil
import getpass

def display_banner():
    banner = (
        r"""
__________                     .__  .__    ________         .__          __                
\______   \ ____   ____ _____  |  | |  |   \______ \   ____ |  |   _____/  |_  ___________ 
 |       _// __ \_/ ___\\__  \ |  | |  |    |    |  \_/ __ \|  | _/ __ \   __\/ __ \_  __ \
 |    |   \  ___/\  \___ / __ \|  |_|  |__  |    `   \  ___/|  |_\  ___/|  | \  ___/|  | \/
 |____|_  /\___  >\___  >____  /____/____/ /_______  /\___  >____/\___  >__|  \___  >__|   
        \/     \/     \/     \/                    \/     \/          \/          \/       """
        + """ Insprired by TotalRecall.
"""
    )
    print(banner)
def delete_contents(path):
    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                file_size = os.path.getsize(file_path)
                os.unlink(file_path)  # Remove the file or link
                print(f"Deleted file: {file_path} (Size: {file_size} bytes)")
            elif os.path.isdir(file_path):
                dir_size = get_directory_size(file_path)
                shutil.rmtree(file_path)  # Remove the directory and all its contents
                print(f"Deleted directory: {file_path} (Size: {dir_size} bytes)")
    except Exception as e:
        print(f"Error occurred while deleting contents: {e}")

def get_confirmation():
    confirmation = input("Delete Microsoft recall? (yes/no): ")
    return confirmation.lower() in ["yes", "y"]

if __name__ == "__main__":
    display_banner()
    username = getpass.getuser()
    target_directory = f"C:\\Users\\{username}\\AppData\\Local\\CoreAIPlatform.00\\UKP"
    
    if os.path.exists(target_directory):
        if get_confirmation():
            delete_contents(target_directory)
            print(f"✅All contents deleted in: {target_directory}, Including screenshots.")
        else:
            print("❌Operation cancelled by the user.")
    else:
        print(f"❗The directory does not exist: {target_directory}. You might not have a Copilot+ PC.")
