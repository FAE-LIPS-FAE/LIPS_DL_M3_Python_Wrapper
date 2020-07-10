
import cv2
import numpy as np
from openni import openni2
from openni import _openni2 as c_api
openni2.initialize("C:\Program Files\OpenNI2\Tools")	# can also accept the path of the OpenNI redistribution
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 80, resolutionY = 60, fps = 30))
depth_stream.start()


while True:
	frame = depth_stream.read_frame()
	frame_data = frame.get_buffer_as_uint16()
	img = np.frombuffer(frame_data, dtype=np.uint16)
	img.shape = (1, 60, 80)
	img = np.concatenate((img, img, img), axis=0)
	img = np.swapaxes(img, 0, 2)
	img = np.swapaxes(img, 0, 1)
	cv2.namedWindow("image", cv2.WINDOW_NORMAL)
	cv2.imshow("image", img)
	cv2.waitKey(34)
	
	#if (cv2.waitKey(1) & 0xFF == ord('q')):
	if (cv2.waitKey(1) == 27):
		break
	
openni2.unload()
cv2.destroyAllWindows()