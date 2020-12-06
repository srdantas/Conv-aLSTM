import argparse
import os

from dataset import Dataset
from folders import create_file_structure
from settings import Settings

parser = argparse.ArgumentParser(description='This script make download data from kinetics dataset.')

parser.add_argument('--youtube_url_base', help='The url base for download from youtube',
                    default='https://www.youtube.com/watch?v=')
parser.add_argument('--video_extension', help='Extension of video for save in storage', default='.mp4')
parser.add_argument('--video_format', help='Format of video for trim it', default='.mp4')
parser.add_argument('--train_folder', help='Folder for save train data', default='train')
parser.add_argument('--validation_folder', help='Folder for save validation data', default='validation')
parser.add_argument('--test_folder', help='Folder for save test data', default='test')
parser.add_argument('--dataset_path', help='Folder for save dataset', default='kinetics')
parser.add_argument('--train_size', help='Size of train for download (-1 for all).', default=-1)
parser.add_argument('--validation_size', help='Size of validation for download (-1 for all).', default=-1)
parser.add_argument('--test_size', help='Size of test for download (-1 for all).', default=-1)
parser.add_argument('--download_path', help='The path of download from cloud storage.',
                    default='Kinetics.tar.gz')


def download_compact_dataset(settings: Settings):
    os.mkdir('../dataset')
    os.system(
        f'curl https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020.tar.gz \
        --output ../dataset/{settings.DOWNLOAD_PATH}')


def extract_compact_dataset(settings: Settings):
    os.system(f'cd ../dataset && tar -xf {settings.DOWNLOAD_PATH}')


if __name__ == '__main__':
    download_settings = Settings(parser.parse_args())

    download_compact_dataset(download_settings)
    extract_compact_dataset(download_settings)
    create_file_structure(download_settings.BASE_PATH, [download_settings.TRAIN_FOLDER,
                                                        download_settings.VALIDATE_FOLDER,
                                                        download_settings.TEST_FOLDER])

    train_dataset = Dataset(download_settings,
                            download_settings.BASE_PATH_TRAIN,
                            download_settings.TRAIN_SIZE,
                            f'../dataset/kinetics700_2020/train.csv',
                            False)

    train_dataset.download()
