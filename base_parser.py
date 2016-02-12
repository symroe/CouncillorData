from bs4 import BeautifulSoup

class BaseParser(object):
    def __init__(self, file_path):
        self.file = open(file_path)
        self.soup = BeautifulSoup(self.file)

