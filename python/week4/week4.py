def modify_file(input_file, output_file):
    try:
        # Open the original file in read mode
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content (Example: Convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"File has been successfully modified and saved to {output_file}.")

    except FileNotFoundError:
        print(f"Oops! The file {input_file} does not exist.")
    except IOError:
        print("There was an error with reading or writing the file.")

# Example usage
input_filename = "/home/davey/Desktop/davey/plp/plp/python/week4/SA_cities.txt"
output_filename = "/home/davey/Desktop/davey/plp/plp/python/week4/modified_SA_cities.txt"

modify_file(input_filename, output_filename)
