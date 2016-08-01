#python module for analyzing "artists" data



from PIL import Image, ImageDraw, ImageFilter
from skimage import measure
from random import randint
import matplotlib.pyplot as plt
import sys



#paintin class
class paintings(object):

    #costructor, it takes a python list of all artist paintings
    def __init__(self, img_paths):

        self.paintings_paths = img_paths
        self.painting_counts = len(img_paths)
        self.color_schemes = []


    #check errors
    def error_check(self):
        if self.painting_counts == 0:
            print 'There is no artists paintings'


    #extracting artists favorite color schemes. default number of colors is 10 unless specified
    def extract_colors(self, num_colors = 10, square_size = 'SMALL'):

        #square sizes.
        X_SMALL = 10
        SMALL = 20
        MID = 40
        LARGE = 80

        #threshold for pixel difference
        color_thresh = 5 #55 for now, change accordingly based on the result

        #get square size
        if(square_size == 'X_SMALL'):
            S_size = X_SMALL
        elif(square_size == 'SMALL'):
            S_size = SMALL
        elif(square_size == 'MID'):
            S_size = MID
        elif(square_size == 'LARGE'):
            S_size = LARGE

        #extract artists favorite color from examples

        #loop through everything in paitings path
        for path in self.paintings_paths:
            #load the image, and get dimension
            painting = Image.open(path).convert('RGB')
            p_width, p_height = painting.size

            #using the squares,
            '''
            1. Select a random pixel
            2. Compare that pixel with every pixel within the square
            3. If there is at least 5 percent of pixels that differ too much from a random pixel
            4. move on to next, otherwise store the value of that random pixel's RGB values

            '''

            remainder_height = p_height % S_size
            remainder_width =  p_width % S_size
            num_of_square_in_width = p_width / S_size
            num_of_square_in_height = p_height / S_size

            self.iterate_painting_get_color(S_size, painting, num_of_square_in_width=num_of_square_in_width,
                                            num_of_square_in_height=num_of_square_in_height, pixel_thresh=color_thresh)



    #iterate the whole painting
    def iterate_painting_get_color(self, square, painting, num_of_square_in_width, num_of_square_in_height, pixel_thresh):

        start_x_coord = 0
        start_y_coord = 0

        for width in range(0,num_of_square_in_width):
            for height in range(0, num_of_square_in_height):
                #if there is a color to be added
                the_color = self.return_color(start_x_coord, start_y_coord, square, painting, pixel_thresh);
                if the_color:
                    self.color_schemes.append(the_color)

                start_y_coord = start_y_coord + square
            #end of the second for loop
            start_x_coord = start_x_coord + square
            start_y_coord = 0

    #helper function for iterating a painting(RGB converted)
    def return_color(self, start_x, start_y, square, painting, pixel_thresh):

        #get the random pixel within the range
        rand_x = randint(start_x, start_x + square)
        rand_y = randint(start_y, start_y + square)
        rand_pixel = painting.getpixel( (rand_x, rand_y))
        found = True

        #loop every pixel
        for x in range(start_x, start_x + square):
            for y in range(start_y, start_y + square):
                compare_pixel = painting.getpixel( (x,y) )
                if not self.compare_pixel_color(rand_pixel, compare_pixel, thresh_value=pixel_thresh):
                    found = False

        #return according value
        if found:
            return rand_pixel
        else:
            return False


    #compare two pixels given threshold. pixel1 will be the random pixel
    def compare_pixel_color(self, pixel1, pixel2, thresh_value):
        if pixel1 == None:
            print 'pixel1 does not exist'
        elif pixel2 == None:
            print 'pixel2 does not exist'

        r1, g1, b1 = pixel1
        r2, g2, b2 = pixel2

        if abs(r1 - r2) > thresh_value or abs(g1 - g2)> thresh_value or abs(b1 - b2) > thresh_value:
            return False
        else:
            return True




paths = ['Pictures/TwoTahitianWomen.jpg','Pictures/AVisionAfterTheSermon.jpg']
obj = paintings(img_paths=paths)
obj.extract_colors()
print "Number of colors selected: ", len(obj.color_schemes)
print obj.color_schemes













