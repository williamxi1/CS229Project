from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

class Rescale(object):
    """Rescale the image in a sample to a given size.

    Args:
        output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, sample):
        image, category = sample['image'], sample['category']

        h, w = image.shape[:2]
        if isinstance(self.output_size, int):
            if h > w:
                new_h, new_w = self.output_size * h / w, self.output_size
            else:
                new_h, new_w = self.output_size, self.output_size * w / h
        else:
            new_h, new_w = self.output_size

        new_h, new_w = int(new_h), int(new_w)

        img = transform.resize(image, (new_h, new_w))



        return {'image': img, 'category': category}


# Ignore warnings
import warnings
class FashionDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_file, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.fashion_frame = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.fashion_frame)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir,
                                self.fashion_frame.iloc[idx, 0])
        image = io.imread(img_name)
        catagory = self.fashion_frame.iloc[idx, 1]
        sample = {'image': image, 'category': catagory}

        if self.transform:
            sample = self.transform(sample)

        return sample







shoe_dataset = FashionDataset(csv_file='../data/shoes.csv',
                                    root_dir='../data/Shoes/')
scale = Rescale((256,256))

for i in range(len(shoe_dataset)):
    sample = scale(shoe_dataset[i])

    print(i, sample['image'].shape, sample['category'])
    plt.imshow(sample['image'])
    plt.show()