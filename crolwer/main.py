import argparse
import os
import shutil

from dataset import Dataset
from folders import create_file_structure
from settings import Settings

parser = argparse.ArgumentParser(description='This script make download data from kinetics dataset.')

parser.add_argument('--youtube_url_base', help='The url base for download from youtube',
                    default='https://www.youtube.com/watch?v=')
parser.add_argument('--video_extension', help='Extension of video for save in storage', default='.mp4')
parser.add_argument('--train_folder', help='Folder for save train data', default='train')
parser.add_argument('--validation_folder', help='Folder for save validation data', default='validation')
parser.add_argument('--test_folder', help='Folder for save test data', default='test')
parser.add_argument('--dataset_path', help='Folder for save dataset', default='kinetics')
parser.add_argument('--train_size', help='Size of train for download (-1 for all).', default=-1)
parser.add_argument('--validation_size', help='Size of validation for download (-1 for all).', default=-1)
parser.add_argument('--test_size', help='Size of test for download (-1 for all).', default=-1)
parser.add_argument('--download_path', help='The path of download from cloud storage.', default='Kinetics.tar.gz')
parser.add_argument('--source_for_download', help='The path for download csv file.', default='dataset')


def download_compact_dataset(settings: Settings):
    os.mkdir(settings.SOURCE_FOR_DOWNLOAD)
    os.system(
        f'curl https://storage.googleapis.com/deepmind-media/Datasets/kinetics700_2020.tar.gz \
        --output {settings.SOURCE_FOR_DOWNLOAD}/{settings.DOWNLOAD_PATH}')


def extract_compact_dataset(settings: Settings):
    os.system(f'cd {settings.SOURCE_FOR_DOWNLOAD} && tar -xf {settings.DOWNLOAD_PATH}')


if __name__ == '__main__':
    download_settings = Settings(parser.parse_args())

    try:

        download_compact_dataset(download_settings)
        extract_compact_dataset(download_settings)
        create_file_structure(download_settings.BASE_PATH, [download_settings.TRAIN_FOLDER,
                                                            download_settings.VALIDATE_FOLDER,
                                                            download_settings.TEST_FOLDER])

        train_dataset = Dataset(download_settings,
                                download_settings.BASE_PATH_TRAIN,
                                download_settings.TRAIN_SIZE,
                                f'{download_settings.SOURCE_FOR_DOWNLOAD}/kinetics700_2020/train.csv',
                                False)

        validation_dataset = Dataset(download_settings,
                                     download_settings.BASE_PATH_VALIDATION,
                                     download_settings.VALIDATE_SIZE,
                                     f'{download_settings.SOURCE_FOR_DOWNLOAD}/kinetics700_2020/validate.csv',
                                     False)

        test_dataset = Dataset(download_settings,
                               download_settings.BASE_PATH_TEST,
                               download_settings.TEST_SIZE,
                               f'{download_settings.SOURCE_FOR_DOWNLOAD}/kinetics700_2020/test.csv',
                               True)

        train_dataset.download()
        validation_dataset.download()
        test_dataset.download()
    except Exception as e:
        print(f'Error in processing downloads {e}')
    finally:
        shutil.rmtree(download_settings.SOURCE_FOR_DOWNLOAD)
