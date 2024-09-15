# load_data.py
import csv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.helpers import download_images

def load_data(file_path):
    """
    Function to load data from a given file path.
    """
    images = []
    with open(file_path,'r') as train_data:
        reader = csv.reader(train_data)
        for row in reader:
            print(row)
    # TODO: Implement data loading logic
    pass


load_data("../../dataset/train.csv")