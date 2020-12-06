import os

import pytube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from settings import Settings


class Downloader:
    def __init__(self, settings: Settings):
        self.settings = settings

    def trim(self, row, label_to_dir, test=False):
        label = row['label'] if not test else ''
        filename = row['youtube_id']
        time_start = row['time_start']
        time_end = row['time_end']

        input_filename = os.path.join(label_to_dir['tmp'], f'{filename}{self.settings.VIDEO_FORMAT}')
        output_filename = os.path.join(label_to_dir[label], f'{filename}{self.settings.VIDEO_EXTENSION}')

        if os.path.exists(output_filename):
            print('Already trimmed: ', filename)
        else:
            print('Start trimming: ', filename)

            try:
                ffmpeg_extract_subclip(input_filename, time_start, time_end, targetname=output_filename)
            except Exception as e:
                print(f'Error in trimming: {e}')

            finally:
                os.remove(input_filename)
                print('Finish trimming: ', filename)

        return output_filename

    def download_clip(self, row, label_to_dir):
        filename = row['youtube_id']

        if not os.path.exists(os.path.join(label_to_dir['tmp'], filename + self.settings.VIDEO_EXTENSION)):
            print('Start downloading: ', filename)
            try:
                pytube.YouTube(self.settings.URL_BASE + filename) \
                    .streams \
                    .filter(subtype=self.settings.VIDEO_FORMAT) \
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

    def execute(self, row, label, test=False):
        self.download_clip(row, label)
        return self.trim(row, label, test)
