import glob
import os
import csv
import ipdb
from tqdm import tqdm
from shutil import copyfile
from random import sample
import numpy as np


class Make_split(object):
    def __init__(self, Dataset_src_root, Dataset_dst_root, type_, label_list):
        self.Dataset_src_root = Dataset_src_root
        self.Dataset_dst_root = Dataset_dst_root
        self.label_list = label_list
        self.label_names = self.get_label_name()
        self.train_csv_path = os.path.join(Dataset_dst_root, type_ + '_train.csv')
        self.val_csv_path = os.path.join(Dataset_dst_root, type_ + '_val.csv')

    def get_label_name(self):
        with open(self.label_list, 'r') as f:
            lines = f.readlines()
        
        label_names = {}
        for a_line in lines:
            label = int(a_line.split(' ')[0])
            lname = a_line.split(' ')[1].rstrip()
            label_names[label] = lname
        return label_names

    def create_folder(self, folder_name):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)



    def record_to_csv(self, csv_name, content):
        
        with open(csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(content)
        print('Saved', csv_name)


    def copy_files(self):
        '''
        1. Create a dataset copy for the 'type_' split, and save in self.Dataset_dst_root.
        2. Rename the image files in index. (00000.jpg, 00001.jpg....)
        3. Save a filename.csv to record the oridinal filename.
        '''
        for a_label in self.label_names.values():
            src_folder_name = os.path.join(self.Dataset_src_root, 'wikiart', a_label)
            dst_folder_name = os.path.join(self.Dataset_dst_root, a_label)
            self.create_folder(dst_folder_name)
            images = glob.glob(src_folder_name + '/*.jpg')
            filenames = []
            for i, image in enumerate(tqdm(images)):
                src_filename = image.split('/')[-1]
                dst_filename =  "%05d.jpg" % i
                copyfile(image, os.path.join(dst_folder_name, dst_filename))
                filenames.append([dst_filename, src_filename])
            self.record_to_csv(os.path.join(dst_folder_name, 'filename.csv'), filenames)
            


    
    def create_train_val_split(self, val_ratio = 0.2):
        '''
        Save train.csv and val.csv to record train/val split file name. 
        '''
        train_list = []
        val_list = []
        for a_label in self.label_names.values():
            dst_folder_name = os.path.join(self.Dataset_dst_root, a_label)
            images = glob.glob(dst_folder_name + '/*.jpg')

            num_images = len(images)
            num_val = int(len(images)*val_ratio)
            val_seed = np.random.randint(num_images, size=num_val)
            for i in range(num_images):
                if i in val_seed:
                    val_list.append([images[i]])
                else:
                    train_list.append([images[i]])

        self.record_to_csv(self.val_csv_path, val_list)
        self.record_to_csv(self.train_csv_path, train_list)



if __name__ == '__main__':
    Dataset_src_root = 'ArtGAN/WikiArt Dataset'
    Dataset_dst_root = 'dataset/wikiart'
    type_ = 'style'
    label_list = os.path.join(Dataset_src_root, type_ + "_class.txt")
    spliter = Make_split(Dataset_src_root, Dataset_dst_root, type_, label_list)
    spliter.copy_files()
    spliter.create_train_val_split(0.2)
