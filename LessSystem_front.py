# encoding: utf-8
import json
import numpy as np
import matplotlib.pyplot as plt
import os
import queue
import _thread
import traceback


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



class OpenposeJsonParser_front():
    def __init__(self):
        pass

    def index_front1(self,json_file):
        '''

        get all body points of first people:

        To calculate the value of index_front
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



            #Calculating the value of index_front_1
            coord1 = coord[1] - coord[8]
            coord2 = coord[10] - coord[9]
            B1 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[10] - coord[9]))))
            B2 = coord1[0] * coord2[0] + coord1[1] * coord2[1]
            index_sub_1 = B2 / B1#特征子向量1

            coord3 = coord[1] - coord[8]
            coord4 = coord[13] - coord[12]
            B3 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[13] - coord[12]))))
            B4 = coord3[0] * coord4[0] + coord3[1] * coord4[1]
            index_sub_2 = B4 / B3#特征子向量2

            index_front_1 = (index_sub_1+index_sub_2) / 2 #求均值


            #Calculating the value of index_front_2
            coord5 = coord[13] - coord[10]
            coord6 = coord[14] - coord[11]
            D1 = np.sqrt(np.sum(np.square(coord5)))#bingu Distance
            D2 = np.sqrt(np.sum(np.square(coord6)))#jiaohuai Distance


            #Calculating the value of index_front_3
            coord7 = coord[5] - coord[2]
            D3 = np.sqrt(np.sum(np.square(coord7)))  # jianbang Distance



            return index_front_1
            #return index_front_1
            #return [index_front_1,D1,D2,D3]
        except:
            # if met error, all set False
            pass
            #info = {}
            #for i in point_name[:-1]:
            #    info[i] = False
            #return info

    def index_front2(self,json_file):
        '''

        get all body points of first people:

        To calculate the value of index_front
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



            #Calculating the value of index_front_1
            coord1 = coord[1] - coord[8]
            coord2 = coord[10] - coord[9]
            B1 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[10] - coord[9]))))
            B2 = coord1[0] * coord2[0] + coord1[1] * coord2[1]
            index_sub_1 = B2 / B1#特征子向量1

            coord3 = coord[1] - coord[8]
            coord4 = coord[13] - coord[12]
            B3 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[13] - coord[12]))))
            B4 = coord3[0] * coord4[0] + coord3[1] * coord4[1]
            index_sub_2 = B4 / B3#特征子向量2

            index_front_1 = (index_sub_1+index_sub_2) / 2 #求均值


            #Calculating the value of index_front_2
            coord5 = coord[13] - coord[10]
            coord6 = coord[14] - coord[11]
            D1 = np.sqrt(np.sum(np.square(coord5)))#bingu Distance
            D2 = np.sqrt(np.sum(np.square(coord6)))#jiaohuai Distance


            #Calculating the value of index_front_3
            coord7 = coord[5] - coord[2]
            D3 = np.sqrt(np.sum(np.square(coord7)))  # jianbang Distance

            S1=abs(D2-D1)

            return S1
            #return index_front_1
            #return [index_front_1,D1,D2,D3]
        except:
            # if met error, all set False
            pass
            #info = {}
            #for i in point_name[:-1]:
            #    info[i] = False
            #return info



    def index_front3(self,json_file):
        '''

        get all body points of first people:

        To calculate the value of index_front
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



            #Calculating the value of index_front_1
            coord1 = coord[1] - coord[8]
            coord2 = coord[10] - coord[9]
            B1 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[10] - coord[9]))))
            B2 = coord1[0] * coord2[0] + coord1[1] * coord2[1]
            index_sub_1 = B2 / B1#特征子向量1

            coord3 = coord[1] - coord[8]
            coord4 = coord[13] - coord[12]
            B3 = (np.sqrt(np.sum(np.square(coord[1] - coord[8]))) * np.sqrt(
                np.sum(np.square(coord[13] - coord[12]))))
            B4 = coord3[0] * coord4[0] + coord3[1] * coord4[1]
            index_sub_2 = B4 / B3#特征子向量2

            index_front_1 = (index_sub_1+index_sub_2) / 2 #求均值


            #Calculating the value of index_front_2
            coord5 = coord[13] - coord[10]
            coord6 = coord[14] - coord[11]
            D1 = np.sqrt(np.sum(np.square(coord5)))#bingu Distance
            D2 = np.sqrt(np.sum(np.square(coord6)))#jiaohuai Distance


            #Calculating the value of index_front_3
            coord7 = coord[5] - coord[2]
            D3 = np.sqrt(np.sum(np.square(coord7)))  # jianbang Distance

            S5=abs(D2-D3)

            return S5
            #return index_front_1
            #return [index_front_1,D1,D2,D3]
        except:
            # if met error, all set False
            pass
            #info = {}
            #for i in point_name[:-1]:
            #    info[i] = False
            #return info


    def stream_update_point_change_data_in_the_dir1(self,json_file_dir,sum=False):

        while 1:
            file = os.listdir(json_file_dir)
            for i in file:
                if i.endswith(".json"):
                    file_path = json_file_dir + "/" + i
                    index1 = self.index_front1(file_path)
                    os.remove(file_path)
                    yield index1
                    break

    def stream_update_point_change_data_in_the_dir2(self,json_file_dir,sum=False):

        while 1:
            file = os.listdir(json_file_dir)
            for i in file:
                if i.endswith(".json"):
                    file_path = json_file_dir + "/" + i
                    index1 = self.index_front2(file_path)
                    os.remove(file_path)
                    yield index1
                    break

    def stream_update_point_change_data_in_the_dir3(self,json_file_dir,sum=False):

        while 1:
            file = os.listdir(json_file_dir)
            for i in file:
                if i.endswith(".json"):
                    file_path = json_file_dir + "/" + i
                    index1 = self.index_front3(file_path)
                    os.remove(file_path)
                    yield index1
                    break







if __name__ == '__main__':



    while 1:
        for i in  OpenposeJsonParser_front().stream_update_point_change_data_in_the_dir("/home/jasonccf/openpose/examples/media_out",sum=True):
            print(i)
