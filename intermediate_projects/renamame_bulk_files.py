import os


def rename():
    i = 0
    path = "C:/Users/Vanitas/Desktop/test/"
    for files in os.listdir(path):
        renamed_files = "image" + str(i) + ".jpg"
        my_path = path + files
        my_dest = path + renamed_files
        os.rename(my_path, my_dest)
        i += 1
        print(f"{i} renamed !")

rename()
