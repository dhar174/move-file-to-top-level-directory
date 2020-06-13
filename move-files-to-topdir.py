import shutil, os, glob
import ntpath

PATH = os.getcwd()

 
def moveAllFilesinDir(srcDir, dstDir):
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            if os.path.isfile(ntpath.basename(filePath)):
                if ntpath.basename(filePath)== dstDir + ntpath.basename(filePath):
                    break
                else:
                    print("Source=" + filePath +" and Dest= "+dstDir)
                    shutil.move(filePath, dstDir+"\\"+ntpath.basename(filePath));
    else:
        print("srcDir & dstDir should be Directories")


for dir in os.walk(PATH):
        if os.path.isdir(dir[0]):
            os.chdir(dir[0])
            if os.getcwd() != PATH:
                sourceDir = os.getcwd()
                destDir =  PATH
                moveAllFilesinDir(sourceDir,destDir)
            else:
                print("Ignoring top directory")
