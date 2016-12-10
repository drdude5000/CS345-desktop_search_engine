import sys  # for command line arguments
import os   # for sys functions

# Step 1: Searchable
def search(name, cwd, file):
    
    # List all the files and directories in cwd
    directories = os.listdir(cwd)   # ['hifidse.py', 'besho']

    # Checks each directory whether file or directory
    for directory in directories:

        # Ignore hidden files, they start with "."
        if(directory[0] == "."):
            continue
        if(file_check(name, cwd, directory, file)):
            continue
        else:
            directory_check(name, cwd, directory, file)


def directory_check(name, cwd, directory, file):

    if (directory == name):

        # Write file path to step1.txt
        file.write(cwd + "/" + directory + "\tDIR\n")

    # Search directory recursively 
    else:
        search(name, cwd + "/" + directory, file)


def file_check(name, cwd, directory, file):

    isfile = False
    
    # Check if file
    if(os.path.isfile(cwd + "/" + directory)):
        isfile = True

        # Split filename and check name
        filename = directory.split(".")

         # Check if it's our file
        if(filename[0] == name):

            # Check if TXT/TXTN
            if(text_file(directory)):
                # Write file path to step1.txt
                file.write(cwd + "/" + directory + "\tTXT\n")
            else:
                file.write(cwd + "/" + directory + "\tTXTN\n")  

    return isfile


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
            
            # Create file step1.txt
            file = open("step1.txt", "a")

            #cwd = os.getcwd()   # Find the cwd: /home/besho/CS345/Project
            cwd = "/home"
            search(sys.argv[2], cwd, file)

            file.close()
        else:
            print("This is where we check for other commands ")
    else:
        print("You need an action and name in command line. Terminated")

if __name__ == "__main__":
    main()