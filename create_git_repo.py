import sys
import subprocess
import os
import shutil

# Reset standard output to the default
sys.stdout = sys.__stdout__

# GitHub username
github_username = "RandyIsBack2It"

# Read personal access token from a file
pat_file_path = os.path.join(os.getcwd(), "keys", "pat.txt")
with open(pat_file_path, "r") as pat_file:
    github_token = pat_file.read().strip()

def list_files_in_directory(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    return files

def create_git_repository(repo_name, selected_file):
    cwd = os.getcwd()  # Get the current working directory

    # Use the selected file's name (without extension) as the local folder name
    local_folder_name = os.path.splitext(selected_file)[0]
    local_folder_path = os.path.join(cwd, local_folder_name)

    if os.path.exists(local_folder_path):
        print(f"Local folder '{local_folder_name}' already exists.")
        return

    # Create the local folder
    os.makedirs(local_folder_path)

    # Initialize a Git repository in the local folder
    subprocess.run(["git", "init", local_folder_path])

    # Set Git global username and email programmatically
    subprocess.run(["git", "config", "--global", "user.name", "RandyIsBack2It"])
    subprocess.run(["git", "config", "--global", "user.email", "randy.caron@ymail.com"])

    print(f"Local folder '{local_folder_name}' created successfully.")

    # Automatically copy the selected file to the local folder
    src_file_path = os.path.join(cwd, selected_file)
    dst_file_path = os.path.join(local_folder_path, selected_file)
    shutil.copy(src_file_path, dst_file_path)
    print(f"File '{selected_file}' added to the local folder.")

    # Create the "readme.md" file
    md_file_name = "readme.md"
    md_file_path = os.path.join(local_folder_path, md_file_name)
    with open(md_file_path, "w") as md_file:
        md_file.write(f"# {local_folder_name}\n")  # Add folder name as the first line

        # Read the script file and copy comment lines to the markdown file
        script_file_path = os.path.join(cwd, selected_file)
        with open(script_file_path, "r") as script_file:
            for line in script_file:
                if line.strip().startswith("#"):
                    md_file.write(line)

    print(f"Markdown file '{md_file_name}' created in the local folder.")

    commit_message = input("Enter the commit message (max 150 characters): ")
    if len(commit_message) > 150:
        print("Commit message is too long. Please keep it under 150 characters.")
        return

    # Add and commit changes in the local repository
    subprocess.run(["git", "add", "."], cwd=local_folder_path)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=local_folder_path)

    print(f"Changes committed with the message: '{commit_message}'")

    # Add a remote repository (GitHub)
    remote_repo_name = "scripts_base"
    subprocess.run(["git", "remote", "add", "origin", f"https://{github_username}:{github_token}@github.com/{github_username}/{remote_repo_name}.git"], cwd=local_folder_path)

    # Push changes to the remote repository
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=local_folder_path)  # Change "main" to your branch name

if __name__ == "__main__":
    files = list_files_in_directory(os.getcwd())  # List files in the current working directory
    choice = input("Choose the file that you are creating a repository for (enter the number): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            create_git_repository("scripts_base", selected_file)
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
