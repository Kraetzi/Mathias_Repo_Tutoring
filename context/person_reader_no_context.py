def open_and_print_content(path_to_the_file):
    file = open(path_to_the_file)
    for line in file.readlines():
        print(line)
    file.close()


if __name__ == "__main__":
    open_and_print_content('./person.json')
