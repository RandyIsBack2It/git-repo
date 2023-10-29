import subprocess
import os
import shutil

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
    repo_path = os.path.join(cwd, repo_name)  # Use CWD as the repository directory

    if os.path.exists(repo_path):
        print(f"Repository '{repo_name}' already exists in this directory.")
    else:
        os.makedirs(repo_path)  # Create the repository directory if it doesn't exist
        subprocess.run(["git", "init", repo_path])

        # Set Git global username and email programmatically
        subprocess.run(["git", "config", "--global", "user.name", "RandyIsBack2It"])
        subprocess.run(["git", "config", "--global", "user.email", "randy.caron@ymail.com"])

        print(f"Repository '{repo_name}' created successfully.")

        # Automatically copy the selected file to the repository
        src_file_path = os.path.join(cwd, selected_file)  # Use CWD as the source directory
        dst_file_path = os.path.join(repo_path, selected_file)
        shutil.copy(src_file_path, dst_file_path)
        print(f"File '{selected_file}' added to the repository.")

        # Create the "readme.md" file
        md_file_name = "readme.md"
        md_file_path = os.path.join(repo_path, md_file_name)
        with open(md_file_path, "w") as md_file:
            md_file.write(f"# {repo_name}\n")  # Add repository name as the first line

            # Read the script file and copy comment lines to the markdown file
            script_file_path = os.path.join(cwd, selected_file)  # Use CWD as the source directory
            with open(script_file_path, "r") as script_file:
                for line in script_file:
                    if line.strip().startswith("#"):
                        md_file.write(line)

        print(f"Markdown file '{md_file_name}' created in the repository.")

        # Copy files with the same base name (ignoring the extension) to the repository
        selected_file_base = os.path.splitext(selected_file)[0]
        for file in os.listdir(cwd):
            if os.path.isfile(os.path.join(cwd, file)) and os.path.splitext(file)[0] == selected_file_base:
                shutil.copy(os.path.join(cwd, file), os.path.join(repo_path, file))
                print(f"File '{file}' with the same base name copied to the repository.")

        commit_message = input("Enter the commit message (max 150 characters): ")
        if len(commit_message) > 150:
            print("Commit message is too long. Please keep it under 150 characters.")
            return

        subprocess.run(["git", "add", "."], cwd=repo_path)
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path)

        print(f"Changes committed with the message: '{commit_message}'")

        # Add a remote repository (GitHub)
        subprocess.run(["git", "remote", "add", "origin", f"https://{github_username}:{github_token}@github.com/{github_username}/{repo_name}.git"], cwd=repo_path)

        # Push changes to the remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)  # Change "main" to your branch name

if __name__ == "__main__":
    files = list_files_in_directory(os.getcwd())  # List files in the current working directory (CWD)
    choice = input("Choose the file that you are creating a repository for (enter the number): ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(files):
            selected_file = files[choice - 1]
            repo_name = os.path.splitext(selected_file)[0]  # Use the base name (omit the extension)
            create_git_repository(repo_name, selected_file)
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
