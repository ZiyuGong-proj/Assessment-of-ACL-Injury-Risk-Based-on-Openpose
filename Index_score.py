#from LessSystem_sideways import OpenposeJsonParser_sideways
from numpy import NaN
from pandas import Series,DataFrame
import numpy as np
import pandas as pd



#def Return_index_1():
 #       a=[]
  #      while 1:
   #         for i in OpenposeJsonParser_sideways().stream_update_point_change_data_in_the_dir(
    #                "/home/jasonccf/openpose/examples/media_out",
     #               sum=True):
      #      a.append(i)
       # print(a)

max=-1
p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
#global u
def Return_index_1(a):  #获取index_1（特征S1）的最大值


    # p1 = []
    p1.append(a)

    test1 = pd.DataFrame(p1)
    test_1 =test1.fillna(method="pad",limit=10000)
    l1=pd.DataFrame.max(test_1)
    l1=l1.iloc[0]

    # f0 = open("/home/jasonccf/openpose/examples/test_data/index0.txt", "a+")
    # f0.write(p1)
    # f0.close()

    # f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "w+")
    f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "a+")
    f1.write("%s\n" % str(l1))
    f1.close()

    return l1

def Return_index_2(a):  #获取index_1（特征S1）的最大值


    p2.append(a)

    test2 = pd.DataFrame(p2)
    test_2 = test2.fillna(method="pad",limit=10000)
    l2 = pd.DataFrame.max(test_2)
    l2 = l2.iloc[0]

    #f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "w+")
    f2 = open("/home/jasonccf/openpose/examples/test_data/index2.txt", "a+")
    f2.write("%s\n" % str(l2))
    f2.close()

    return l2

def Return_index_3(a):  #获取index_1（特征S1）的最大值


    p3.append(a)

    test3 = pd.DataFrame(p3)
    test_3 = test3.fillna(method="pad",limit=10000)
    l3 = pd.DataFrame.max(test_3)
    l3 = l3.iloc[0]

    #f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "w+")
    f3 = open("/home/jasonccf/openpose/examples/test_data/index3.txt", "a+")
    f3.write("%s\n" % str(l3))
    f3.close()

    return l3

def Return_index_4(a):  #获取index_1（特征S1）的最大值


    p4.append(a)

    test4 = pd.DataFrame(p4)
    test_4 = test4.fillna(method="pad",limit=10000)
    l4 = pd.DataFrame.max(test_4)
    l4 = l4.iloc[0]

    #f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "w+")
    f4 = open("/home/jasonccf/openpose/examples/test_data/index4.txt", "a+")
    f4.write("%s\n" % str(l4))
    f4.close()

    return l4

def Return_index_5(a):  #获取index_1（特征S1）的最大值


    p5.append(a)

    test5 = pd.DataFrame(p5)
    test_5 = test5.fillna(method="pad",limit=10000)
    l5 = pd.DataFrame.max(test_5)
    l5 = l5.iloc[0]

    #f1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "w+")
    f5 = open("/home/jasonccf/openpose/examples/test_data/index5.txt", "a+")
    f5.write("%s\n" % str(l5))
    f5.close()

    return l5

