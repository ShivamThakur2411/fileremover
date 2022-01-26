import os
import shutil
import time

def main():

    path = input("Enter the path to be sorted - ")
    days = 30

    deletedFolderCount = 0
    deletedFileCount = 0

    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):

        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount = deletedFolderCount+1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)

                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount = deletedFolderCount + 1

        for file in files:
            file_path = os.path.join(root_folder, file)
            if seconds >= get_file_or_folder_age(file_path):
                remove_file(file_path)
                deletedFileCount = deletedFileCount + 1
        
            else:
                if seconds>=get_file_or_folder_age(path):
                    remove_file(path)
                    deletedFileCount = deletedFileCount + 1
    
    else:
        print(f'"{path}" is not found')
        deletedFileCount = deletedFileCount + 1

    print(f"Total folders deleted: {deletedFolderCount}")
    print(f"Total files deleted: {deletedFileCount}")


def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable to delete the "+path)


def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete the "+path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


main()