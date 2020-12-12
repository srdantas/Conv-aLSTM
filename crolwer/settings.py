import os


class Settings:
    def __init__(self, args):
        self.URL_BASE = args.youtube_url_base
        self.VIDEO_EXTENSION = args.video_extension

        self.TRAIN_FOLDER = args.train_folder
        self.VALIDATE_FOLDER = args.validation_folder
        self.TEST_FOLDER = args.test_folder

        self.BASE_PATH = os.path.join(os.environ['HOME'], args.dataset_path)
        self.BASE_PATH_TRAIN = os.path.join(self.BASE_PATH, 'train')
        self.BASE_PATH_VALIDATION = os.path.join(self.BASE_PATH, 'validation')
        self.BASE_PATH_TEST = os.path.join(self.BASE_PATH, 'test')

        self.TRAIN_SIZE = args.train_size
        self.VALIDATE_SIZE = args.validation_size
        self.TEST_SIZE = args.test_size

        self.DOWNLOAD_PATH = args.download_path

        self.SOURCE_FOR_DOWNLOAD = args.source_for_download

    def is_train_partial_download(self):
        return self.TRAIN_SIZE >= 0

    def is_validate_partial_download(self):
        return self.VALIDATE_SIZE >= 0

    def is_test_partial_download(self):
        return self.TEST_SIZE >= 0
