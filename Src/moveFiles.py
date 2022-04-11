import os, sys
import shutil

# -----------------------------------
#       Helper Methods
# -----------------------------------
def noPath():
    print("** START ERRROR **")
    print("\tMsg: Command is missing SOURCE and TARGET parameters")
    print("** END ERRROR **")

def errorPath(*path):
    print("** START ERRROR **")
    print("\tMsg: Some or all of the follwoing Dirs/Files may Not Found")
    print("Paths:")
    for p in path:
            print("\t"+p)
    print("** END ERRROR **")

def emptyFolder(path):
    print("** START WARNING **")
    print("\tMsg: No Files Found (EMPTY)")
    print("\tTarget Path: "+path)
    print("** END WARNING **")
# -----------------------------------

if __name__ == "__main__":

    try:
        sourcePath = sys.argv[1]
        targetPath = sys.argv[2]

        try:
        #Empty?
            if not os.listdir(sourcePath):
                emptyFolder(sourcePath)
                sys.exit()
        
            #Copy Files
            with os.scandir(sourcePath) as files:
                for f in files:
                    shutil.copy(f.path,targetPath)
                    os.remove(f.path)

        except FileNotFoundError:
            errorPath(sourcePath, targetPath)
            sys.exit()
    
    except IndexError as e:
        noPath()