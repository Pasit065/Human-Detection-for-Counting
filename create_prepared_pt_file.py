import torch

repo_dir = "ultralytics/yolov5"
model = "yolov5s"

# Loading model to .pt file that will used in detect file.
model = torch.hub.load(repo_or_dir = repo_dir, model = model)