import os, sys
import shutil

# -----------------------------------
#       Helper Methods
# -----------------------------------
def errorPath(*path):
    print("** START ERRROR **")
    print("Msg: Some or all of the follwoing Dirs/Files may Not Found")
    print("Paths:")
    for p in path:
            print("\t"+p)
    print("** END ERRROR **")

def emptyFolder(path):
    print("** START WARNING **")
    print("Msg: No Files Found (EMPTY)")
    print("Target Path: "+path)
    print("** END WARNING **")
# -----------------------------------

if __name__ == "__main__":

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