def modify_file(input_file, output_file):
    try:
        # Open the input file and read its content
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = "example_input.txt"
output_file = "example_output.txt"

modify_file(input_file, output_file)

