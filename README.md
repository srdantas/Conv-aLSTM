# Video Processing
### Video Download
The download is used with kinects dataset.

Kinectis dataset
- [Official Page](https://deepmind.com/research/open-source/kinetics)
- [Paper](https://arxiv.org/abs/1907.06987)

## Run
For run this, is necessary a miniconda and ffmpeg installed on your computer. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### install ffmpeg
```bash
sudo apt-get install ffmpeg
```

### Create envorionment to run
```bash
conda env create -f enviroment.yml
```

### Execute
```bash
jupyter notebook
```

#### SSL Error in video download
Install certifi from conda-forge to update it and make a videos download

```bash
conda install -c conda-forge certifi 
```