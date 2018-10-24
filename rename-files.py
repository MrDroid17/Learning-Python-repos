import os

def renaming_files():
    # get all files
    # os.listdir is to get list of all the files in a folder
    # r in path tell you to take raw path or take string as the path
    file_lists= os.listdir(r"/home/dell/projectDevelopment/webDev/py-programming/learning-python/prank")
    print(file_lists)
    saved_path= os.getcwd()
    print("Current Working Directory is: "+saved_path)
    os.chdir(r"/home/dell/projectDevelopment/webDev/py-programming/learning-python/prank")
    

    # rename all files
    for filename in file_lists:
        os.rename(filename, filename.translate(filename.maketrans('', '', '1234567890')))
        print(filename)
        # filename.translate('1234567890') is depricated instead use below one
        print(filename.translate(filename.maketrans('', '', '1234567890')))
    os.chdir(saved_path)
    
renaming_files()
    
 
