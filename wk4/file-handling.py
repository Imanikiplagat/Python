#  Create a program that reads a file and writes a modified version to a new file: this modifies it to all capital letters
def modify_file(input_file, output_file):
    try:
        
        with open(input_file, "r") as infile:
            content = infile.read()

        
        modified_content = content.upper()

        
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f" File '{output_file}' created with modified content!")

    except:
        pass  

modify_file("input.txt", "output.txt")