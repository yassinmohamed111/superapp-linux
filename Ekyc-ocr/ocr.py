
import cv2 
from ultralytics import YOLO
import numpy as np
import requests



def egyptian_id_model(source):
        model = YOLO("/home/yassinmohamed/superapp linux/models/egy_id_new.pt")
        results = model(source, save=True, conf=0.6, imgsz=480 ,show=False , save_crop = True )



def arabic_numbers(national_image):
        model2 = YOLO("/home/yassinmohamed/superapp linux/models/arabic_numbers.pt")
        resultss = model2(national_image, save=True, conf=0.4, imgsz=480)
        for res in resultss:
        # Get the bounding box coordinates
            xyxy = res.boxes.xyxy.to('cpu').numpy()
            sorted_indices = np.argsort(xyxy[:, 0])
            sorted_classes = res.boxes.cls[sorted_indices]
            national_id = ''.join(map(str, sorted_classes.cpu().numpy().astype(int)))
        return national_id








def ocr_space_api(file_path, api_key = 'K81596658088957', language='ara'):
    """
    OCR.space API request with local file.
    
    :param file_path: Your file path & name.
    :param api_key: OCR.space API key.
    :param language: Language code to be used for OCR.
    :return: Result in JSON format.
    """
    url = 'https://api.ocr.space/parse/image'
    
    with open(file_path, 'rb') as f:
        payload = {
            'apikey': api_key,
            'language': language,
        }
        files = {
            'file': f,
        }
        response = requests.post(url, data=payload, files=files)
       

    
    return response.json()



def get_data():
    out_image = '/home/yassinmohamed/superapp linux/processed_images/output_locationn.jpg'
    first_name = ocr_space_api('/home/yassinmohamed/superapp linux/processed_images/output_name.jpg')
    secondname = ocr_space_api('/home/yassinmohamed/superapp linux/processed_images/output_second_name.jpg')
    location = ocr_space_api('/home/yassinmohamed/superapp linux/processed_images/output_locationn.jpg')

    fname = first_name.get('ParsedResults')[0].get('ParsedText')
    sname = secondname.get('ParsedResults')[0].get('ParsedText')
    loc = location.get('ParsedResults')[0].get('ParsedText')
    print(fname, sname, loc)
    return fname, sname, loc





def get_gender_and_bday(national_id):
        century = national_id[0]
        year_born = national_id[1] + national_id[2]
        month = national_id[3]+national_id[4]
        day = national_id[5]+national_id[6]
        gender = national_id[12]
        

        birthdate = ""
        if century == "3" :
            birthdate = day + "-" + month  +"-"+"20"+year_born
        elif century == "2":
            birthdate =  day+"-"+month+"-"+"19"+year_born

        last_gender = None
        if int(gender)%2 == 0 :
                last_gender = 'انثى'
                print("gender : female ")
        else:
                last_gender  = "ذكر"
                print("gender : male ")

        return last_gender , birthdate



