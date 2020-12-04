import argparse

parser = argparse.ArgumentParser(description='This script make download data from kinetics dataset.')

parser.add_argument('--youtube_url_base', help='The url base for download from youtube',
                    default='https://www.youtube.com/watch?v=')
parser.add_argument('--video_extension', help='Extension of video for save in storage', default='.mp4')
parser.add_argument('--video_format', help='Format of video for trim it', default='.mp4')
parser.add_argument('--train_folder', help='Folder for save train data', default='train')
parser.add_argument('--validation_folder', help='Folder for save validation data', default='validation')
parser.add_argument('--test_folder', help='Folder for save test data', default='test')
parser.add_argument('--dataset_path', help='Folder for save dataset', default='~/.kinetics')
parser.add_argument('--train_size', help='Size of train for download (-1 for all).', default=-1)
parser.add_argument('--validation_size', help='Size of validation for download (-1 for all).', default=-1)
parser.add_argument('--test_size', help='Size of test for download (-1 for all).', default=-1)


class Settings:
    def __init__(self, args):
        self.URL_BASE = args.youtube_url_base
        self.VIDEO_EXTENSION = args.video_extension
        self.VIDEO_FORMAT = args.video_format

        self.TRAIN_FOLDER = args.train_folder
        self.VALIDATE_FOLDER = args.validation_folder
        self.TEST_FOLDER = args.test_folder

        self.BASE_PATH = args.dataset_path

        self.TRAIN_SIZE = args.train_size
        self.VALIDATE_SIZE = args.validation_size
        self.TEST_SIZE = args.test_size

    def is_train_partial_download(self):
        return self.TRAIN_SIZE >= 0

    def is_validate_partial_download(self):
        return self.VALIDATE_SIZE >= 0

    def is_test_partial_download(self):
        return self.TEST_SIZE >= 0


download_settings = Settings(parser.parse_args())
