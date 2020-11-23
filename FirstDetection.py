from imageai.Detection import ObjectDetection
import os

def ObjectDetectionN(input_images, output_images):  
    execution_path = os.getcwd()
    input_path =  os.path.join(execution_path , 'CompletedImages')
    output_path =  os.path.join(execution_path , 'MarkedImages')
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(input_path , input_images), output_image_path=os.path.join(output_path , output_images))

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

files = [f for f in os.listdir('./CompletedImages') if os.path.isfile(os.path.join('./CompletedImages', f))]
for f in files:
    marked = f.replace(".","-marked.")
    ObjectDetectionN(f,marked)