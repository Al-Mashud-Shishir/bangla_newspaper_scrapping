import os


def insert_data_to_file(filename, data):
    if not os.path.isfile(filename):
        write_file(filename, data)
    else:
        append_to_file(filename, data)


# Create a new file
def write_file(path, data):
    f = open(path, 'w', encoding="utf-8")
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a', encoding="utf-8") as file:
        file.write(data)
