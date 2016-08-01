#python module for analyzing "artists" data



from PIL import Image, ImageDraw, ImageFilter
from skimage import measure
import matplotlib.pyplot as plt
import sys



#paintin class
class paintings(object):

    #costructor, it takes a python list of all artist paintings
    def __init__(self, img_paths)

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
        color_thresh = 55 #55 for now, change accordingly based on the result

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

    #helper function for iterating a painting(RGB converted)
    def iterate_paiting(self, square, painting, values):



    #compare two pixels given threshold. pixel1 will be the random pixel
    def compare_pixel_color(self, pixel1, pixel2, thresh_value):
        r1, g1, b1 = pixel1
        r2, g2, b2 = pixel2

        if abs(r1 - r2) > thresh_value or abs(g1 - g2)> thresh_value or abs(b1 - b2) > thresh_value:
            return False
        else:
            return pixel1



    '''loop through every pixel in the picture and change it to either BLACK or WHITE'''
    def black_white_pixels(self):
        for y in range(0, self.height -1):
            for x in range(0, self.width-1):
                r, g, b = self.img_edge.getpixel( (x,y) )
                #check threshold. If equal or less than thresh, make it black
                if r <= B_W_Thresh or g <= B_W_Thresh or b <= B_W_Thresh:
                    self.img_edge.putpixel((x,y), BLACK)
                else:
                    self.img_edge.putpixel((x,y), WHITE)
        self.img_edge.save("result.png")



test_image = image(IMG_PATH)
test_image.black_white_pixels()
test_image.get_boundary_img()











