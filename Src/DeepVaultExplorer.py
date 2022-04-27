
import os
import cv2
from random import shuffle
from image_utils import resize_image

class file_iterator:
    
    def __init__(self, filename):
        
        self.filename = filename
        self.prev_node = None
        self.next_node = None

if __name__ == "__main__":
    image_dir = "C:\\Users\\Paulymorphous\\Pictures\\Clicks\\"


    filenames = []
    for path, subdirs, files in os.walk(image_dir):
        for name in files:
            if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".jpeg"):
                filenames.append(name)
                
    shuffle(filenames)
    file_name_iterator = iter(filenames)
    file_chain = file_iterator(next(file_name_iterator))
    
    while True:
        try:
                        
            cv2.namedWindow("DeepVault Explorer")

            image = cv2.imread(image_dir + file_chain.filename)
            image = resize_image(image, 720)
            
            cv2.imshow('DeepVault Explorer', image)
            

            key_press = cv2.waitKey(0)
            if key_press == ord('q'):
                print("Q pressed, Exiting.")
                break
                
            elif key_press == ord('a'):
                if file_chain.prev_node:
                    file_chain = file_chain.prev_node
            

            elif key_press == ord('d'):
                
                if file_chain.next_node:
                    file_chain = file_chain.next_node

                else:
                    try:
                            current_node = file_chain
                            file_chain = file_iterator(next(file_name_iterator))
                            current_node.next_node = file_chain
                            file_chain.prev_node = current_node
                    
                    except StopIteration as e:
                        pass
                    
            
        except Exception as e:
            print("ERROR:", e)
        
        finally:
            pass

    cv2.destroyAllWindows()

