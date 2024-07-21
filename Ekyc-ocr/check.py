
import os
import cv2



def get_national_id(number_files , file_name):
    if number_files == 1 :
        national_image = f"/home/superapp linux/runs/detect/predict/crops/national_id/" + file_name
    else:
         national_image = f"/home/superapp linux/runs/detect/predict{number_files+1}/crops/national_id/"+ file_name
    
    return national_image
    



def get_segements(source , number_files):
     #get images men akher prediction file
    image_names = ['firstname' , "second name" , "location" , "manfucturing_id"]
    def get_images():
        file_name = os.path.basename(source)
        images = []
        for name in image_names:
            img_file = f'/home/superapp linux/runs/detect/predict{number_files+1}/crops/{name}'+ '/'  + file_name
            image = cv2.imread(img_file)
            images.append(image)
        return images

   
    try:
        images = get_images()
        firstname_image = images[0]
        secondname_image = images[1]
        location_image = images[2]
        manf_id = images[3]
        return firstname_image  , secondname_image , location_image , manf_id
    except FileNotFoundError:
        print('*************************************')
        print("not found file")
        print("Insert new image please and try again!!")
        print("Notice: the clearity and resolution should be clear and perfectly skewed and the image not to far and not too close")
        print('*************************************')
        list_ret = ["The picture is not clear enough , please take a close , high resolution and clear picture"]
        return list_ret
        sys.exit()
        