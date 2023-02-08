# encoding: utf-8
import json
import numpy as np
import matplotlib.pyplot as plt
import os
import queue
import _thread
import traceback
import Index_score
import math



point_name = [
  "Nose",
  "Neck",
  "RShoulder",
  "RElbow",
  "RWrist",
  "LShoulder",
  "LElbow",
  "LWrist",
  "MidHip",
  "RHip",
  "RKnee",
  "RAnkle",
  "LHip",
  "LKnee",
  "LAnkle",
  "REye",
  "LEye",
  "REar",
  "LEar",
  "LBigToe",
  "LSmallToe",
  "LHeel",
  "RBigToe",
  "RSmallToe",
  "RHeel",
  "Background"
  ]



class OpenposeJsonParser_sideways():
    def __init__(self):
        pass

    def index_sideways1(self,json_file):
        '''

        get all body points of first people:

        To calculate the value of index_sideways
        '''
        try:
            with open(json_file, "r") as f:
                data = json.load(f)

            #extract the data of 2d
            people = data["people"]
            people = people[0]
            pose2d = people["pose_keypoints_2d"]
            pose2d = np.array(pose2d).reshape(-1,3)
            coord = pose2d[:,:2]

            #Calulating the value of index_1 (sideways 9 10 11)
            coord1 = coord[9] - coord[10]
            coord2 = coord[11] - coord[10]
            B1 =  (np.sqrt(np.sum(np.square(coord[9] - coord[10]))) * np.sqrt(
                           np.sum(np.square(coord[11] - coord[10]))))
            B2 = coord1[0] * coord2[0] + coord1[1] * coord2[1]
            index_1 = B2 / B1



            #Calulating the value of index_2
            coord3 = coord[1] - coord[8]
            coord4 = coord[10] - coord[9]
            B3 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[10] - coord[9]))))
            B4 = coord3[0] * coord4[0] + coord3[1] * coord4[1]
            index_2 = B4 / B3


            #return [index_1,index_2]
            #print([index_1,index_2])
            #print((index_1))
            return index_1
        except:
             pass
            # if met error, all set False
         #   info = {}
          #  for i in point_name[:-1]:
           #     info[i] = False
            #return info



    def index_sideways2(self,json_file):
        '''

        get all body points of first people:

        To calculate the value of index_sideways
        '''
        try:
            with open(json_file, "r") as f:
                data = json.load(f)

            #extract the data of 2d
            people = data["people"]
            people = people[0]
            pose2d = people["pose_keypoints_2d"]
            pose2d = np.array(pose2d).reshape(-1,3)
            coord = pose2d[:,:2]

            #Calulating the value of index_1 (sideways 9 10 11)
            coord1 = coord[9] - coord[10]
            coord2 = coord[11] - coord[10]
            B1 =  (np.sqrt(np.sum(np.square(coord[9] - coord[10]))) * np.sqrt(
                           np.sum(np.square(coord[11] - coord[10]))))
            B2 = coord1[0] * coord2[0] + coord1[1] * coord2[1]
            index_1 = B2 / B1



            #Calulating the value of index_2
            coord3 = coord[1] - coord[8]
            coord4 = coord[10] - coord[9]
            B3 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[10] - coord[9]))))
            B4 = coord3[0] * coord4[0] + coord3[1] * coord4[1]
            index_2 = B4 / B3


            #return [index_1,index_2]
            #print([index_1,index_2])
            #print((index_1))
            return index_2
        except:
             pass





    def stream_update_point_change_data_in_the_dir_1(self,json_file_dir,sum=False):


         while 1:
            file = os.listdir(json_file_dir)
            for i in file:
                if i.endswith(".json"):
                    file_path = json_file_dir + "/" + i
                    index1 = self.index_sideways1(file_path)
                    os.remove(file_path)
                    yield index1
                    break

    def stream_update_point_change_data_in_the_dir_2(self,json_file_dir,sum=False):


         while 1:
            file = os.listdir(json_file_dir)
            for i in file:
                if i.endswith(".json"):
                    file_path = json_file_dir + "/" + i
                    index2 = self.index_sideways2(file_path)
                    os.remove(file_path)
                    yield index2
                    break




if __name__ == '__main__':



    while 1:
        for i in  OpenposeJsonParser_sideways().stream_update_point_change_data_in_the_dir("/home/jasonccf/openpose/examples/media_out",sum=True):
           pass
           # print(i)



