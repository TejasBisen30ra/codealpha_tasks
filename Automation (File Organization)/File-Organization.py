import os
from shutil import move

# Directory paths
user = os.getenv('USER')
root_dir = f'/Users/Hp/Tasks/Automation (File Organization)/Downloads/'
image_dir = f'/Users/Hp/Tasks/Automation (File Organization)/Downloads/images/'
documents_dir = f'/Users/Hp/Tasks/Automation (File Organization)/Downloads/documents/'
software_dir = f'/Users/Hp/Tasks/Automation (File Organization)/Downloads/softwares/'

# Category wise file types
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

# Ensure target directories exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(documents_dir, exist_ok=True)
os.makedirs(software_dir, exist_ok=True)

def get_non_hidden_files_except_current_file(root_dir):
    current_file = os.path.basename(__file__)
    return [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f)) and not f.startswith('.') and f != current_file]

def move_files(files):
    for file in files:
        source_path = os.path.join(root_dir, file)
        if file.endswith(doc_types):
            destination = os.path.join(documents_dir, file)
        elif file.endswith(img_types):
            destination = os.path.join(image_dir, file)
        elif file.endswith(software_types):
            destination = os.path.join(software_dir, file)
        move(source_path, destination)
        print(f'File {file} moved to {destination}')

if __name__ == "__main__":
    files = get_non_hidden_files_except_current_file(root_dir)
    move_files(files)
