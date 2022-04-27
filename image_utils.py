import cv2

def calculate_target_shape(orginal_h, origianl_w, target_h):
    
    target_w = round(origianl_w/orginal_h * target_h)
    
    if target_w > 1500:
        target_h, target_w = calculate_target_shape(orginal_h, origianl_w, target_h-120)
        
    return target_h, target_w


def resize_image(image, target_h):
    
    orginal_h, origianl_w, _ = image.shape
    aspect_ratio = orginal_h/origianl_w
    target_h, target_w = calculate_target_shape(orginal_h, origianl_w, target_h)
    
    image = cv2.resize(image, (target_w, target_h))
    
    return image 