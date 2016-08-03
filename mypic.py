from PIL import Image, ImageDraw, ImageFilter
import pickle
from skimage import measure
from random import randint
import matplotlib.pyplot as plt
import sys



#Analyzing and manipulating my picture
class mypic(object):

    def __init__(self, mypic):

        #open color_scheme of the artist
        self.colors_list = pickle.load(open("save.p", "rb"))
        self.picture = Image.open(mypic).convert('RGB')


    def order_color_paleete(self):






#Constant Variables
Path_to_picture = 'default.jpg'


mypic_obj = mypic(mypic=Path_to_picture)
print mypic_obj.colors_list