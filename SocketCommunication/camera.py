import pyrealsense2 as rs
import numpy as np
import cv2
import time
import math
import os
import sys


def main(args):
    pipe = rs.pipeline()
    config = rs.config()

    #config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    pipe.start(config)

    output_directory = 'Images'
    os.makedirs(output_directory, exist_ok=True)

    frame_count = 0

    while True:
        frame = pipe.wait_for_frames()
        #depth_frame= frame.get_depth_frame()
        color_frame= frame.get_color_frame()

        #depth_image =np.asanyarray(depth_frame.get_data())
        color_image =np.asanyarray(color_frame.get_data())
        #print(type(color_image))
        #depth_cm = cv2.applyColorMap(cv2.convertScaleAbs(depth_image,alpha=0.5),cv2.COLORMAP_JET)

        cv2.imshow("rgb", color_image)
        #cv2.imshow("depth",depth_cm)



        frame_count += 1

        if frame_count == 50:
            frame_filename = os.path.join(output_directory, f'blister_pack_{1}.jpg')
            cv2.imwrite(frame_filename, color_image)
            


        if cv2.waitKey(1)==ord("q"):
            break


if __name__ == '__main__':
    sys.exit(main(sys.argv))