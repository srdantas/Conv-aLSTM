import shutil

import pandas as pd
from tqdm import tqdm

from downloader import Downloader
from folders import create_file_structure
from settings import Settings


class Dataset:
    def __init__(self, settings: Settings, base_path, size, path_csv, is_test):
        self.settings = settings
        self.base_path = base_path
        self.size = int(size)
        self.path_csv = path_csv
        self.is_test = is_test

        if self.size > 0:
            self.data = pd.read_csv(self.path_csv).head(self.size)
        else:
            self.data = pd.read_csv(self.path_csv)

        self.downloader = Downloader(settings)

        folders_names = self.data['label'].unique().tolist() + ['tmp']
        self.label_to_dir = create_file_structure(self.base_path, folders_names)

    def download(self):
        try:
            trimming = []
            for _, row in tqdm(self.data.iterrows()):
                trimming.append(self.downloader.execute(row, self.label_to_dir, test=self.is_test))
            return trimming
        finally:
            shutil.rmtree(self.label_to_dir['tmp'])
