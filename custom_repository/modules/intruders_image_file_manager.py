import os
import cv2

class IntrudersImageFileManager():
    def is_intruder_file_directory_in_current_path(self, current_path):
        if "intruders" in os.listdir(current_path):
            return True
        else:
            return False
        
    def write_image_file(self, file_path, image):
        cv2.imwrite(file_path, image)

    def create_directory_in_each_day_for_intruder_image_file(self, prev_path, day):
        os.mkdir(path = f"{prev_path}\{day}")

    def is_delete_intruders_image_directory_for_today(self, max_limit_files, total_items_in_intruders_date):
        if total_items_in_intruders_date >= max_limit_files:
            return True 
        else:
            return False
        
    def get_new_intruders_image_file_name(self, image_file_no):
        return f"image{image_file_no}.jpeg"