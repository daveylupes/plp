def read_file(filename):
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
    
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist. Please check the filename and try again.")
    
    except PermissionError:
        print(f"You do not have permission to read the file {filename}.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for the filename
filename = input("Please enter the filename to read: ")
read_file(filename)
