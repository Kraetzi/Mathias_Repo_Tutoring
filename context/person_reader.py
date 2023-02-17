def open_and_print_content(path_to_the_file):
    with open(path_to_the_file) as file:
        for line in file.readlines():
            print(line)


if __name__ == '__main__':
    open_and_print_content("./person.json")