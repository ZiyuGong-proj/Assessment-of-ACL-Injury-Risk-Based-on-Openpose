#coding : utf-8

import os




class OpenposeLauncher():
    def __init__(self,dir_contains_models,openpose_binary_path):
        '''

        :param dir_contains_models:  the dir that have dir "models", e.g. "G:/openpose"
        :param openpose_binary_path: binary file of openpose e.g. "G:/openpose/bin/OpenPoseDemo.exe"
        '''
        self.model_dir = dir_contains_models
        self.openpose_path = openpose_binary_path

    def openpose_image(self,image_dir,log_output_dir):
        os.chdir(self.model_dir)
        command = "\"%s\" --image_dir=%s --write_json=%s --logging_level 3 " % (self.openpose_path,
                                                                                    image_dir,log_output_dir
                                                                                    )
        os.system(command)

    def openpose_camera(self,log_output_dir):
        os.chdir(self.model_dir)
    #    command = "\"%s\" --write_json %s  --camera %s --logging_level 3 " % (self.openpose_path,
    #                                                                          log_output_dir,
    #                                                                             camera_index
    #
    #                                                                             )
        command = "\"%s\"  -camera_resolution 640x480 -net_resolution 128x96 --write_json %s " % (self.openpose_path,log_output_dir)

        os.system(command)


    def openpose_video(self,video_path,log_output_dir):
        os.chdir(self.model_dir)
        command = "\"%s\" --video=%s --write_json=%s --logging_level 3" % (self.openpose_path,
                                                                               video_path,
                                                                              log_output_dir
                                                                                )

        os.system(command)

    def openpose_IP_camera(self,camera_ip,log_output_dir):
        '''
    get public ip camera: http://www.webcamxp.com/publicipcams.aspx

    '''
        os.chdir(self.model_dir)
        raise NotImplementedError()

    def openpose_hands(self):
        pass

if __name__ == '__main__':


    openpose_launcher = OpenposeLauncher(dir_contains_models="/home/jasonccf/openpose",
                                         openpose_binary_path="/home/jasonccf/openpose/build/examples/openpose/openpose.bin"
                                         )
    #openpose_launcher.openpose_video("G:\openpose\examples\media\\video.avi","G:\openpose\output")
    #openpose_launcher.openpose_image("G:\openpose\examples\media","G:\openpose\output")
    openpose_launcher.openpose_camera("/home/jasonccf/openpose/examples/media_out")

    #open_pose_camera(camera_number=1) # if have usb set it 1


    pass