import os


def __create_file_structure(path, folders_names):
    mapping = {}
    if not os.path.exists(path):
        os.mkdir(path)
    for name in folders_names:
        dir_ = os.path.join(path, name)
        if not os.path.exists(dir_):
            os.mkdir(dir_)
        mapping[name] = dir_
    return mapping


REQUIRED_COLUMNS = ['label', 'youtube_id', 'time_start', 'time_end', 'split', 'is_cc']
TRIM_FORMAT = '%06d'
URL_BASE = 'https://www.youtube.com/watch?v='

VIDEO_EXTENSION = '.mp4'
VIDEO_FORMAT = 'mp4'

TRAIN_FOLDER = 'train'
VALIDATE_FOLDER = 'validate'
TEST_FOLDER = 'test'

BASE_PATH = os.path.join('/', 'home', os.environ['USER'], 'kinects')

TRAIN_VIDEOS_PATH = os.path.join(BASE_PATH, TRAIN_FOLDER)
VALIDATE_VIDEOS_PATH = os.path.join(BASE_PATH, VALIDATE_FOLDER)
TEST_VIDEOS_PATH = os.path.join(BASE_PATH, TEST_FOLDER)

if not os.path.exists(BASE_PATH):
    os.mkdir(BASE_PATH)
else:
    print(f'Path {BASE_PATH} already exists!')

# file to save train, validate and test
__create_file_structure(BASE_PATH, [TRAIN_FOLDER, VALIDATE_FOLDER, TEST_FOLDER])


def __trim(row, label_to_dir, test=False):
    import ffmpeg
    label = row['label'] if not test else ''
    filename = row['youtube_id']
    time_start = row['time_start']
    time_end = row['time_end']

    input_filename = os.path.join(label_to_dir['tmp'], f'{filename}{VIDEO_EXTENSION}')
    output_filename = os.path.join(label_to_dir[label], f'{filename}{VIDEO_EXTENSION}')

    if os.path.exists(output_filename):
        print('Already trimmed: ', filename)
    else:
        print('Start trimming: ', filename)

        try:
            ffmpeg.trim(ffmpeg.input(input_filename), start=time_start, end=time_end).output(
                output_filename).run()
        except Exception as e:
            print(f'Error in trimming: {e}')

        print('Finish trimming: ', filename)


def __download_clip(row, label_to_dir):
    import pytube

    filename = row['youtube_id']

    if not os.path.exists(os.path.join(label_to_dir['tmp'], filename + VIDEO_EXTENSION)):
        print('Start downloading: ', filename)
        try:
            pytube.YouTube(URL_BASE + filename) \
                .streams \
                .filter(subtype=VIDEO_FORMAT) \
                .first() \
                .download(label_to_dir['tmp'], filename)
            print('Finish downloading: ', filename)
        except KeyError as e:
            print(f'Key Error {e}')
            return
        except Exception as e:
            print(f'Error in download video: {e}')
            return
    else:
        print('Already downloaded: ', filename)


def download(path_csv, target, heads=5, test=False):
    import shutil
    import pandas as pd
    links_data_frames = pd.read_csv(path_csv).head(heads)

    if not test:
        folders_names = links_data_frames['label'].unique().tolist() + ['tmp']
        label_to_dir = __create_file_structure(path=target, folders_names=folders_names)

        [__download_clip(row, label_to_dir) for _, row in links_data_frames.iterrows()]
        [__trim(row, label_to_dir) for _, row in links_data_frames.iterrows()]

        shutil.rmtree(label_to_dir['tmp'])
    else:
        folders_names = ['tmp', '']
        label_to_dir = __create_file_structure(path=target, folders_names=folders_names)

        [__download_clip(row, label_to_dir) for _, row in links_data_frames.iterrows()]
        [__trim(row, label_to_dir, test=True) for _, row in links_data_frames.iterrows()]

        shutil.rmtree(label_to_dir['tmp'])
