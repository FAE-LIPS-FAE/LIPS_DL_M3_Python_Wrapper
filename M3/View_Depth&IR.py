
import cv2
import numpy as np
from openni import openni2
from openni import _openni2 as c_api
openni2.initialize("C:\Program Files\OpenNI2\Tools")	# can also accept the path of the OpenNI redistribution
dev = openni2.Device.open_any()

#Set depth image
depth_stream = dev.create_depth_stream()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 80, resolutionY = 60, fps = 30))
depth_stream.start()
#Set ir image
ir_stream = dev.create_ir_stream()
ir_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_GRAY16, resolutionX = 80, resolutionY = 60, fps = 30))
ir_stream.start()


while True:
	#Show depth image from cv2
	frame_depth = depth_stream.read_frame()
	frame_depth_data = frame_depth.get_buffer_as_uint16()
	img_depth = np.frombuffer(frame_depth_data, dtype=np.uint16)
	img_depth.shape = (1, 60, 80)
	img_depth = np.concatenate((img_depth, img_depth, img_depth), axis=0)
	img_depth = np.swapaxes(img_depth, 0, 2)
	img_depth = np.swapaxes(img_depth, 0, 1)
	cv2.namedWindow("Depth image", cv2.WINDOW_NORMAL)
	cv2.imshow("Depth image", img_depth)
	
	
	#Show ir image from cv2
	frame_ir = ir_stream.read_frame()
	frame_ir_data = frame_ir.get_buffer_as_uint16()
	img_ir = np.frombuffer(frame_ir_data, dtype=np.uint16)
	img_ir.shape = (1, 60, 80)
	img_ir = np.concatenate((img_ir, img_ir, img_ir), axis=0)
	img_ir = np.swapaxes(img_ir, 0, 2)
	img_ir = np.swapaxes(img_ir, 0, 1)
	
	cv2.namedWindow("image", cv2.WINDOW_NORMAL)
	cv2.imshow("image", img_ir)
	
	
	cv2.waitKey(34)
	
	#if (cv2.waitKey(1) & 0xFF == ord('q')):
	if (cv2.waitKey(1) == 27):
		break
	
openni2.unload()
cv2.destroyAllWindows()