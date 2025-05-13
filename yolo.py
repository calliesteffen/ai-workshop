#%%
from ultralytics import YOLO

#https://docs.ultralytics.com/tasks/classify/#val

#%% Load a model
model = YOLO("yolo11n-cls.pt")  # load a pretrained model (recommended for training)


#%% Train the model

results = model.train(data="/home/Leiphardt/Desktop/ai-workshop/split-dataset", epochs=50, imgsz=224)



# %%
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n-cls.pt")  # load an official model


# Validate the model
metrics = model.val(data="/home/Leiphardt/Desktop/ai-workshop/split-dataset/val")
metrics.top1  # top1 accuracy
metrics.top5 




