# Crowler

This script enable to download dataset from Kinetics 700 from 2020.

## Run:

### Conda env
This project using the conda env for setup environment.
```shell
conda env create -f enviroment.yml
conda activate conv-alstm-crowler
```

After create and start env, run it:
```shell
python3 main.py
```

### Parameters

- parameter: 'youtube_url_base', The url base for download from youtube, default is 'https://www.youtube.com/watch?v='
- parameter: 'video_extension', Extension of video for save in storage, default is '.mp4'
- parameter: 'train_folder', Folder for save train data, default is 'train'
- parameter: 'validation_folder', Folder for save validation data, default is 'validation'
- parameter: 'test_folder', Folder for save test data, default is 'test'
- parameter: 'dataset_path', Folder for save dataset, default is 'kinetics'
- parameter: 'train_size', Size of train for download (-1 for all), default is -1
- parameter: 'validation_size', Size of validation for download (-1 for all), default is -1
- parameter: 'test_size', Size of test for download (-1 for all), default is -1
- parameter: 'download_path', The path of download from cloud storage, default is 'Kinetics.tar.gz'
- parameter: 'source_for_download', The path for download csv file, default is 'dataset'
