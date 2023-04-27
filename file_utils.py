import os


def parse_txt(path):
    if os.path.exists(path):
        with open(path, "r") as txt_file:
            try:
                return txt_file.read().splitlines()
            except Exception as e:
                print(f"Something went wrong during loading file \"{path}\". Please, check that file is valid")
                print(f"Error: {e}")
                exit()
    else:
        print(f"File \"{path}\" does not exist")
        exit()
