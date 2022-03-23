import cv2 as opencv
from numpy import ndarray


ALPHA = 2
BETA = 0.8
image = ndarray


def debug_show(image: ndarray, name: str = "cringe"):
    opencv.imshow(name, image)
    opencv.waitKey(0)


#TODO: copy a code from Mickle Reevs video
def get_color_mask(image_frame):
    pass
# def prepare_data_for_ressponse():
#     pass



def get_color_mask():
    pass


def get_preproccesed_image(processing_image: ndarray) -> ndarray:
    global image
    image = processing_image

    #TODO: detect all dark places in image, and locate their position
    def mark_all_dark_places():
        #processing image for black/white image
        gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
        th, threshed = opencv.threshold(gray, 100, 255,
        opencv.THRESH_BINARY_INV|opencv.THRESH_OTSU)
        #DEBUG
        debug_show(gray)

        #finding contorus in image
        cnts = opencv.findContours(threshed, opencv.RETR_LIST,
        opencv.CHAIN_APPROX_SIMPLE)[-2]

    def mark_all_bright_places():
        global image
        from numpy import argwhere
        low = (0,0,0)
        high = (10,10,10)

        mask = opencv.inRange(image, low, high)
        # mask = 255 - mask

        # find black coordinates
        coords = argwhere(mask==0)
        for p in coords:
            pt = (p[0],p[1])
            image = opencv.circle(image, pt, 20, (150, 150, 0), 2)
            print(pt)
        debug_show(image)


    #TODO: iterrate for all of posible locations of real-world marks
    def check_for_marks_in_frame(proceesed_image: ndarray):
         pass

    def get_all_marks_data_in_frame():
        pass

    mark_all_dark_places()
    mark_all_bright_places()

def get_index_symbol_from_mark(analyzing_frame: ndarray) -> str:
    ret,thresh = opencv.threshold(analyzing_frame,127,255,0) 
    edges = opencv.Canny(analyzing_frame,100,200) 
    debug_show(edges)
    

def get_preproccesing_test():
    image = get_preproccesed_image(opencv.imread("./database/index1.jpeg"))
    # image_1 = get_index_symbol_from_mark(opencv.imread("./database/index3.jpeg"))


if __name__ == "__main__":
    get_preproccesing_test()