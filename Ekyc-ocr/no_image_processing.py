import os
from preprocess import save_threshold2 , dilation , thresholding
from ocr import get_gender_and_bday , get_data, arabic_numbers, egyptian_id_model
from check import  get_segements,get_national_id
from ultralytics import YOLO




    
def get_ocr3():
    lst = os.listdir("/home/yassinmohamed/superapp linux/runs/detect") 
    number_files = len(lst)
    source = "/home/yassinmohamed/superapp linux/id.jpg"
    file_name = os.path.basename(source)

   
#first we run the model and we get the egyptian id segements 
    egyptian_id_model(source)
    
   
#second we check if all fields are detected
    
    file_path = f'/home/yassinmohamed/superapp linux/runs/detect/predict{number_files+1}/crops/national_id/{file_name}'

    if not os.path.exists(file_path):
        list_ret = ["The picture is not clear enough , please take a close , high resolution and clear picture"]
        return list_ret




#if so we get the national_id segements  
    national_image = get_national_id(number_files , file_name)
    

#using arabic_numbers model to get national id 
    national_id = arabic_numbers(national_image)

    
#now we collect the other segements to start the image processing
    try:
                segments = get_segements(source, number_files)
                save_threshold2(segments[0] , segments[1] , segments[2] , segments[3])
                
    except IndexError:
                print('*************************************')
                print("not found file")
                print("Insert new image please and try again!!")
                print("Notice: the clearity and resolution should be clear and perfectly skewed and the image not to far and not too close")
                print('*************************************')
                list_ret = ["The picture is not clear enough , please take a close , high resolution and clear picture"]
                return list_ret

    
    

    ocr_data = get_data()

    #extract from the national id the gender and birthdate
    gender_bday = get_gender_and_bday(national_id)
    print(ocr_data[0]," " ,ocr_data[1], " " ,national_id, " " ,gender_bday[1], " " ,ocr_data[2], " " ,gender_bday[0])
    return ocr_data[0], ocr_data[1], national_id, gender_bday[1], ocr_data[2], gender_bday[0]



