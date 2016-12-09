import sys  # for command line arguments
import os   # for sys functions

# Step 1: Searchable
def search(name, cwd):

    # Create file step1.txt
    file = open("step1.txt", "a")
    
    # List all the files and directories in cwd
    directories = os.listdir(cwd)   # ['hifidse.py', 'besho']

    # Checks each directory whether file or directory
    for directory in directories:

        # Check if file
        if(os.path.isfile(cwd + "/" + directory)):

            # Check if TXT/TXTN
            if(text_file(directory)):
                # Write file path to step1.txt
                file.write(cwd + "/" + directory + "\tTXT\n")
            else:
                file.write(cwd + "/" + directory + "\tTXTN\n")            

        # Otherwise search directory recursively
        else:

            # Write file path to step1.txt
            file.write(cwd + "/" + directory + "\tDIR\n")
            
            # Search directory recursively 
            search(name, cwd + "/" + directory)

    file.close()


# Checks if text-file (.html , .htm , .txt , .cc , .cpp , .c , .h , .java)
def text_file(filename):

    text_extensions = ["html", "htm", "txt", "cc", "cpp", "c", "h", "java"]

    # Split filename and check extension
    extension = filename.split(".")
    if(extension[1] in text_extensions):
        return True
    else:
        return False


def main():

    # check for two command line (action & name)
    if(len(sys.argv) == 3):

        # Check action type
        if(sys.argv[1].lower() == "searchable"):
            cwd = os.getcwd()   # Find the cwd: /home/besho/CS345/Project
            search(sys.argv[2], cwd)
        else:
            print("This is where we check for other commands ")
    else:
        print("You need an action and name in command line. Terminated")

if __name__ == "__main__":
    main()
