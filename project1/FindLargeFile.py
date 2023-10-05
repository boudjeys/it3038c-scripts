import os  # Import the 'os' module for file system operations

# Define a function to find and list large files
def find_large_files(start_directory, min_file_size_MB):
    large_files = []  # Create an empty list to store large files

    # Recursively walk through the directory and its subdirectories
    for root, dirs, files in os.walk(start_directory):
        for filename in files:
            file_path = os.path.join(root, filename)  # Construct the full file path
            file_size_MB = os.path.getsize(file_path) / (1024 * 1024)  # Get file size in MB
            if file_size_MB > min_file_size_MB:  # Check if the file size is larger than the specified minimum
                large_files.append((file_path, file_size_MB))  # Add the file to the list of large files

    return large_files  # Return the list of large files

# Define the main function
def main():
    start_directory = input("Enter the directory path to search for large files: ")  # Prompt for user input
    min_file_size_MB = 200.0  # Minimum file size in MB

    if not os.path.exists(start_directory):  # Check if the specified directory exists
        print("Directory does not exist.")
        return

    print(f"Finding files larger than {min_file_size_MB} MB in {start_directory}...\n")

    large_files = find_large_files(start_directory, min_file_size_MB)  # Call the function to find large files

    if not large_files:  # Check if no large files were found
        print("No files larger than 200 MB found.")
    else:
        print("Large files found:")
        for file_path, file_size_MB in large_files:
            print(f"{file_path} - {file_size_MB:.2f} MB")  # Display the list of large files

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
