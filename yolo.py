#%%
from ultralytics import YOLO

#https://docs.ultralytics.com/tasks/classify/#val

#%% Load a model
model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)


#%% Train the model

results = model.train(data="/home/Leiphardt/Desktop/ai-workshop/split-dataset", epochs=5, imgsz=224)



# %%
from ultralytics import YOLO

# Load a model
model = YOLO("/home/Leiphardt/Desktop/ai-workshop/ai-workshop/runs/classify/train/weights/best.pt")  # load an official model. Do this to my trained model


# Validate the model
metrics = model.val(data="/home/Leiphardt/Desktop/ai-workshop/split-dataset")
metrics.top1  # top1 accuracy
metrics.top5 

# very well performing lets see some pics
#%% predictions to dig around under the hood
#training and test dataset 
#visualize what its doing well on 

from ultralytics import YOLO

# Load a model
model = YOLO("/home/Leiphardt/Desktop/ai-workshop/ai-workshop/runs/classify/train/weights/best.pt") 

# Predict with the model
results = model("/home/Leiphardt/Desktop/ai-workshop/split-dataset/val/bird/FCM1__2019-08-18__12-16-49(9).JPG", save_txt = True)  
 # predict on an image and/or folder






# %%
print(results)

#https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html

# %%
#per class accuracy
#macro (class) accuracy and average across those values 
#CV lecture on evaluation  metrics!
# off line evaluation
# 
