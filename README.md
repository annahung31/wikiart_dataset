# wikiart_dataset

This is a repo for using wikiart dataset.

## wikiart dataset information
Original wikiart page: https://www.wikiart.org/ 

I used the version used by `ArtGAN` (https://github.com/cs-chan/ArtGAN)

As you can see in https://github.com/cs-chan/ArtGAN/tree/master/WikiArt%20Dataset, 
the whole dataset can be splited by `Style`, `Artist`, and `Genre`.

I only use `style` as split. 

In ArtGAN, the image files are named by the name of the painting.
I renamed them by orders. (00000.jpg, 00001.jpg .....)


## Use the dataset

1. Root paths:
    - ArtGAN version root path: `ArtGAN/WikiArt Dataset/`
    - cleaned dataset root path: `dataset/wikiart/`

2. Use `wikiart_statistics.py` to know how many images in each class in train/val split.

3. If you want to use `Artist` or `Genre` to split the dataset, you may need `create_splits.py`.