import torch
from torchvision import datasets, transforms
from torchvision import utils
import os
from tqdm.auto import tqdm
import shutil
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "datapath", help="path to data set. Eg './data/images'", type=str
    )
    parser.add_argument(
        "start_size",
        default=4,
        help="first progression image size (default is 4)",
        type=int,
    )
    parser.add_argument(
        "end_size",
        default=512,
        help="last progression image size (default is 512)",
        type=int,
    )

    args = parser.parse_args()

    datapath = args.datapath
    start_size = int(args.start_size)
    end_size = int(args.end_size)

    # Move OG images to new folder called 'original'.
    dest_fold = os.path.join(datapath, "original", "images")
    if not os.path.exists(dest_fold):
        os.makedirs(dest_fold)
        for file_name in os.listdir(datapath):
            if file_name != "original":
                shutil.move(os.path.join(datapath, file_name), dest_fold)

    # Create dir for prepared datasets. If it exists, delete and overwrite.
    prepared_path = out_path = os.path.join(datapath, "prepared")
    if not os.path.exists(prepared_path):
        os.mkdir(prepared_path)

    index = 0
    cur_size = start_size

    while cur_size <= end_size:
        image = 0

        out_path = os.path.join(prepared_path, f"set_{index + 1}", "images")
        if os.path.exists(out_path):
            if input(f"set_{index + 1} exists. Delete? (y/N)") == "y":
                shutil.rmtree(out_path)
            else:
                index += 1
                cur_size = cur_size * 2
                continue

        os.makedirs(out_path)

        transformation = transforms.Compose(
            [
                transforms.Resize((cur_size, cur_size)),
                transforms.ToTensor(),
                transforms.ConvertImageDtype(float),
            ]
        )

        images = datasets.ImageFolder(os.path.join(dest_fold, ".."), transformation)

        dataset = torch.utils.data.DataLoader(
            images,
            batch_size=16,
            shuffle=True,
            num_workers=3,
        )

        for batch, _ in tqdm(dataset):
            for im in batch:
                image_name = f"image-{image}.png"
                utils.save_image(im, os.path.join(out_path, image_name))
                image += 1

        cur_size = cur_size * 2
        index += 1
