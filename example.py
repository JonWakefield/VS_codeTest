from ModuleFeeder import capture_images

''' Example code for capture_x_images module'''
''' Code will walk user through proper usage of module'''
''' Using a PiCamera module will capture and save images to a
    provided PATH directory. Module will also calculate high photo number
    in directory, and take photos beginning with that number (+1). This
    allows the user to potential delete corrupted photos, and resume capturing
    with manual interference.'''



# define camera parameters:
# NOTE: all camera parameters have pre-defined values. Change only to fit user specifications.
shutter_speed = 100000 # adjusts camera exposure time // 10000 == 10ms
# for more information on shutter_speed see: https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.shutter_speed

awb_gains = (1.5,1.8) # sets the auto-white-balance gains of the PiCamera. Tuple(red,blue) with values 0 < x < 8
# for more information on awb_gains see: https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.awb_gains

exposure_mode = 'antishake' # sets exposure mode of the camera. 
# To see all possible exposure modes, see this link: #https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.exposure_mode

awb_mode = 'off' # Retrieves or sets the auto-white-balance mode of the camera. For fixed white balance awb mode must be set to off.
# for more information on awb_mode see: https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.awb_mode

# more information regarding these parameters can be found here:
# https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-consistent-images


# define hyper parameters

num_images = 20 # Defines num of images to capture

# path to folder to save images. must end with / on linux
path = "/home/pi/Desktop/Wakefield_AutoCal_rev1/Capture Images/save images/"

# time interval between captures (in milliseconds)
time_interval = 0.001

# call capture_images()
result = capture_images(num_images, path, time_interval, shutter_speed, awb_gains, exposure_mode, awb_mode)
print(result)
'''If no Exceptions are raised, module will return true, and will have successfully captured and saved images.'''



''' POSSIBLE ERRORS & SOLUTIONS:'''
########## OperandError #############
''' Exception: OperandError: (...)  was not a number. Check 'num_images' and 'delta_t_millisecs'. must be of type 'int' or 'float'.'''
''' Solution: Check 'num_images' value and 'delta_t_secs' values. Must be of type float or int.'''
########### Directory ###############
''' Exception: directory does not exist'''
''' Description: Error arises from python unable to find directory (variable: path)'''
''' Possible Fixes: Recheck path to ensure directory exists. On linux, make sure begining char is: / and last char is: / '''
############ PiCamera  ############
''' Exception: Failed to enable connection: Out of resources '''
''' Description: PiCamera was unable to conncet to a camera.'''
''' Solution: Recheck Camera connection, ensure camera is properly connected and locked
    in place on the pi and on the camera board. A possible Reboot of the raspberry pi may be neccessary. 
    See this video for more help: https://www.youtube.com/watch?v=VzYGDq0D1mw'''
########### PiCamera ###############
''' Exception: Camera is not enabled. Try running 'sudo raspi-config' ... '''
''' Descrption: Unable to connect to picamera'''
''' Solution: Ensure raspberry pi has been properly configered with pi camera. 
    Or, ensure camera has been properly connected and locked in place. See previous exception
    for more help.'''
########## exposure_mode ###############
''' Exception: Invalid exposure mode'''
''' Solution: recheck exposure mode, see provided link for acceptable options. '''
############ awb_mode ################
''' Exception: Invalid auto-white-balance mode'''
''' Solution: Recheck awb_mode, see provided link for acceptable options.'''
########### awb_gains ##################
'''' Exception: TypeError '<=' not supportedbetween instances of 'float' and 'str'
     OR
     Exception: Invalid gain(s) in () 
     Solution: Recheck awb_gains value. Values must be in range: 0.0-8.00 
     see provided link for acceptable options.'''
######### SHUTTER_SPEED ##############
''' Exception: argument 3: <class 'TypeError'>: wrong type '''
''' Solution: recheck shutter_speed value, see provided link for acceptable options.'''
########## cv2.imwrite ##############
''' Exception: Expected Ptr<cv::UMat> for argument 'img'''
''' Description: unable to save image '''
''' Solution: Recheck path and camera connection. See link for acceptable values:
    https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce'''