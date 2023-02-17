class MyFile:

    def __init__(self, path_to_file):
        self.path = path_to_file
        self.file = None

    def __enter__(self):
        print('Starting the context...')
        print('Checking auhtorization... Ok!')
        self.file = open(self.path)
        return self.file

    def __exit__(self, type, value, traceback):
        print('Exiting the context')
        if self.file is not None:
            self.file.close()


if __name__ == '__main__':

    with MyFile('person.json') as file:
        for line in file.readlines():
            print(line)
