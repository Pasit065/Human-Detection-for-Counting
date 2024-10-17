# Human-Detect-for-Counting
**Human-Detect-for-Counting** is a project that utilize open-source model named *YOLOv5* with Python detect file script which will detect intruders with frame by frame to sent notification and store the data in *Google Sheet* and *database file*.

The major model size that this project used is *YOLOv5s* because it have a smallest size of parameters compared to other sizes which is compatible for using in various project such as embeded systems which has a small size of processing hardware.

For the origin of YOLOv5 you can visit *[YOLOv5 repository here](https://github.com/ultralytics/yolov5)* 

## Overview
In this projects will uses existed `detect.py` that get from *YOLOv5* repository by forking along with new custom Python script to sent notification and store data if human is found.

The projects will detect human by execute `detect.py` file and using default camera in your computer. When the script is executed, it will detect human using camera in frame by frame. If humans are found notification will be sent by Line Notify. Moreover, detection data will be stored using *Sheety API* and *SQLite3* DBMS to store data in *Google Sheet* and database file.

## Important Files.
This section is used to explain two important files that will be executed seperatly.

1. `create_prepared_pt_file.py` used to create specific yolov5 size model file.

2. `detect.py` used to perform intruders detection.

## API
This project utilize 2 APIs to store and notify users for intruders detection.

- *Sheety API* used for connect Google Sheet, allowing the script to edit, delete or insert data to specific Google Sheet. Visit *[Sheety API website here](https://sheety.co/)*.

- *Line Notify* used for sending message, image, stickers or etc to specific line group or users.  Visit *[Line Notify website here](https://notify-bot.line.me/)*.

## Data Storage
This project will store data in *Google Sheet* and *database*

- *Google Sheet* will store intruders data in table format which features total intruders that were found and found date and time.

- *Database* will store intruders data like *Google Sheet* which features total intruders that were found and found date and time column.

## Usage
Before execute the project, a few setup is required.

### Initial Setup
1. **Install `requirements.txt`** for nesccessary package.
    ```Bash
    pip install -r requirements.txt
    ```

2. **Ensure that `yolov5s.pt` has been installed.** If it is not, execute `create_prepared_pt_file.py` file in project parent location.
    ```Bash
    python create_prepared_pt_file.py
    ```

3. **Set up `weights` parameter** in `detect.py`.
    ```Python
    def run(
        weights=ROOT / 'yolov5s.pt',  # model path or triton URL
        source=ROOT / 'data/images',  # file/dir/URL/glob/screen/0(webcam)
        data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
        imgsz=(640, 640),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=False,  # save results to *.txt
        save_csv=False,  # save results in CSV format
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes= '',  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project=ROOT / 'runs/detect',  # save results to project/name
        name='exp',  # save results to project/name
        exist_ok=False,  # existing project/name ok, do not increment
        line_thickness=3,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        vid_stride=1,  # video frame-rate stride
    ):
    ```

4. **Line Notify setup** is required. Log in to *Line Notify* official website and get *Line Notify token* and assign it into `line_notify_token` in `detect.py` as environment variable.
    ```Python
    line_notify_token = os.environ.get("line_notify_token")
    ```

5. **Google Sheet url** must be provided and it must match with *Sheety API* google sheet. Assign it to `intruders_status_google_sheet_url` in `detect.py` as environment variable.
    ```Python
    intruders_status_google_sheet_url = os.environ.get("intruders_status_google_sheet_url")
    ```

6. **Determine `MAX_LIMIT_FILES`** in `detect.py` which is maximum of total image files that could store in each directory
    ```Python
    MAX_LIMIT_FILES = 500 
    ```

### Custom Setup
There are some variable that is flexible to be changed by users. Here are the list of custom setup variables.

1. `MAX_LIMIT_FILES`in `detect.py` is flexible to adjust by purpose, user can determine the maximum of total image files in each directory.
    ```Python
    MAX_LIMIT_FILES = 100
    ```

2. `model` in `create_prepared_pt_file.py` which is yolov5 model size could be adjust by users purpose.
    ```Python
    model = "yolov5l"
    ```

    If users want to change the model to other models exclude `yolov5s.pt`. User must change `weights` parameter in `detect.py`
    ```Python
    def run(
        weights=ROOT / 'yolov5l.pt',  # model path or triton URL
        source=ROOT / 'data/images',  # file/dir/URL/glob/screen/0(webcam)
        data=ROOT / 'data/coco128.yaml',  # dataset.yaml path
        imgsz=(640, 640),  # inference size (height, width)
        conf_thres=0.25,  # confidence threshold
        iou_thres=0.45,  # NMS IOU threshold
        max_det=1000,  # maximum detections per image
        device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
        view_img=False,  # show results
        save_txt=False,  # save results to *.txt
        save_csv=False,  # save results in CSV format
        save_conf=False,  # save confidences in --save-txt labels
        save_crop=False,  # save cropped prediction boxes
        nosave=False,  # do not save images/videos
        classes= '',  # filter by class: --class 0, or --class 0 2 3
        agnostic_nms=False,  # class-agnostic NMS
        augment=False,  # augmented inference
        visualize=False,  # visualize features
        update=False,  # update all models
        project=ROOT / 'runs/detect',  # save results to project/name
        name='exp',  # save results to project/name
        exist_ok=False,  # existing project/name ok, do not increment
        line_thickness=3,  # bounding box thickness (pixels)
        hide_labels=False,  # hide labels
        hide_conf=False,  # hide confidences
        half=False,  # use FP16 half-precision inference
        dnn=False,  # use OpenCV DNN for ONNX inference
        vid_stride=1,  # video frame-rate stride
    ):
    ```

3. In `TimeUtils.timedelta(minutes = 2, seconds = 0)` in `detect.py` is flexible because it is time duration that message will be hold if message was sent before.

    ```Python
    if line_notify_service.sent_line_message and total_time_passed_from_prev_loop > TimeUtils.timedelta(minutes = 1, seconds = 0):
        ...
    ```

### Execute Project.
Once the **Initial Setup** is provided, user can start execute project by:
```Bash
python detect.py
```

  