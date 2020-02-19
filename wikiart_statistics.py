import os
import glob
import ipdb
import numpy as nps






class Statistics(object):
    def __init__(self, Dataset_root, csv_file, label_list):
        self.ROOT = Dataset_root
        self.csv_file = csv_file
        self.label_list = label_list
        self.label_name = self.get_label_name()
        self.num_label = len(self.label_name)


    def get_label_name(self):
        with open(self.label_list, 'r') as f:
            lines = f.readlines()
        
        lines = [x.rstrip() for x in lines]
        
        label_name = {}
        for a_line in lines:
            label = int(a_line.split(' ')[0])
            lname = a_line.split(' ')[1].rstrip()
            label_name[label] = lname
        return label_name

    def class_statistics(self):
        labels = self.get_labels_csv()
        for i in range(self.num_label):
            num = labels.count(self.label_name[i])
            print('%30s'%self.label_name[i], ':', num)



    def get_labels_csv(self):
        with open(self.csv_file, 'r',  encoding='utf-8') as f:
            lines = f.readlines()
        lines = [x.rstrip() for x in lines]

        labels = []
        for a_line in lines:
            style_label = a_line.split('/')[-2]
            labels.append(style_label)
        
        return labels




if __name__ == '__main__':
    Dataset_root = 'dataset/wikiart/'
    csv_file = os.path.join(Dataset_root, "style_train.csv")
    label_list = os.path.join(Dataset_root, "style_class.txt")
    statistic = Statistics(Dataset_root, csv_file, label_list)
    statistic.class_statistics()
