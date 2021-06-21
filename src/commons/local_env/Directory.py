import os
from collections import defaultdict



class Directory:
    DATA_DIRECTORY = "data"


    def __init__(self):
        try:
            datasets =  os.listdir(self.DATA_DIRECTORY)
        except FileNotFoundError:
            os.mkdir(self.DATA_DIRECTORY)

        self.ext_dict = defaultdict(list)
        # {"txt": ["file1", "file2"]}
        for directory in datasets:
            filename, ext = directory.split(".")
            self.ext_dict[ext].append(filename)

    def get(self, filename, ext) -> str:
        datasets_with_ext = self.ext_dict.get(ext)
        if datasets_with_ext:
            if filename in datasets_with_ext:
                # data/dataset1.csv
                return "{}/{}.{}".format(self.DATA_DIRECTORY, filename, ext)
                # return self.DATA_DIRECTORY + "/" + filename + "." + ext
        return None
