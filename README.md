# BYO-GAN

As a part of my independent study for Junior year, my final project was to recreate StyleGan in Python using Pytorch. I used some notes from a Coursera course I took, the original whitepapers, and looked at how others had implemented the same architecture in order to better understand how StyleGan worked. 

### Whitepapers:
- [A Style-Based Generator Architecture for Generative Adversarial Networks](https://arxiv.org/abs/1812.04948)
  - [Official Implementation](https://github.com/tkarras/progressive_growing_of_gans)
- [Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://arxiv.org/abs/1710.10196)
  - [Official Implementation](https://github.com/NVlabs/stylegan)


### Datasets:
- [Anime Profile Dataset](https://www.kaggle.com/prasoonkottarathil/gananime-lite)
  - [License](https://creativecommons.org/licenses/by-sa/4.0/)
- [Abstract Art Dataset](https://www.kaggle.com/bryanb/abstract-art-gallery)
- [Abstract Art Images](https://www.kaggle.com/greg115/abstract-art)
- [FFHQ Dataset](https://www.kaggle.com/arnaud58/flickrfaceshq-dataset-ffhq)

### MISC:
Big thanks to these projects for helping me troubleshoot issues I had!
- [huangzh13](https://github.com/huangzh13/StyleGAN.pytorch)
- [rosinality](https://github.com/rosinality/style-based-gan-pytorch)

Thanks to [Samuel Prevost](https://github.com/sam1902) for directly helping me troubleshoot issues.

# How to run

## Preparing a dataset

Create a folder under `/data`, name it however you want.

Place all of your dataset images into this new folder. It will work best if they are all 512x512.

Run `python prep.py [path to images] [start size (4)] [end size (512)]`. 

This script is ***SUPER*** dodgy and thrown together, so be prepared to tweak it in order to make it work. It essentially moves those original images into a new `/data/[name]/original/images` folder. Then, it resizes every image to match progressive growth and saves it under separate datasets under `/data/[name]/prepared`, where `name` refers to the original folder (e.g. `/data/art`).

## Training

Edit the `config.txt` file and create a configuration setting to your liking. Use the two examples as a template. You can override any key, but do **NOT** delete anything under the `DEFAULT` setting. 

```shell
python main.py [config name] -c checkpoint.pth
```

For instance,

```shell
python main.py abstract-art
```

runs with the `abstract-art` configuration.

## Getting Full Resolution Samples

```shell
python generate_samples.py ./checkpoints/checkpoint.pth 64 -o ./output/ -d cpu 
```

will generate `64` images from the model saved at `./checkpoints/checkpoint.pth` and save them in the `./output` folder. It will use the CPU. 

```shell
python generate_samples.py -h
```

for more info. 

# Results

As my resources are limited, I was unable to run my program to completion. See [Nvidia's implementation](https://github.com/nvlabs/stylegan) for higher fidelity Results. 

However, for the time that I did run this program, I did get meaningful results that show that this implementation is indeed functional.

16 FFHQ images:

<img src="https://user-images.githubusercontent.com/28550422/125561041-8b3cf81d-c93b-46fc-aad8-a1fd3be48922.png" alt="faces" width="512" height="512"/>

16 Abstract Art images:

<img src="https://user-images.githubusercontent.com/28550422/125561099-99d50ea5-2f7e-45cc-b806-4942cc34ff9d.png" alt="art" width="512" height="512"/>

