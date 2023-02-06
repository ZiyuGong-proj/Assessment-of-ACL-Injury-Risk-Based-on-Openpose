

def index_data():
        r1 = open("/home/jasonccf/openpose/examples/test_data/index1.txt", "r")
        contents1 = r1.readlines()
        contents_final1 = contents1[-1]
        r1.close()
        dig_1 = float(contents_final1)




        r2 = open("/home/jasonccf/openpose/examples/test_data/index2.txt", "r")
        contents2 = r2.readlines()
        contents_final2 = contents2[-1]
        r2.close()
        dig_2 = float(contents_final2)

        r3 = open("/home/jasonccf/openpose/examples/test_data/index3.txt", "r")
        contents3 = r3.readlines()
        contents_final3 = contents3[-1]
        r3.close()
        dig_3 = float(contents_final3)

        r4 = open("/home/jasonccf/openpose/examples/test_data/index4.txt", "r")
        contents4 = r4.readlines()
        contents_final4 = contents4[-1]
        r4.close()
        dig_4 = float(contents_final4)

        r5 = open("/home/jasonccf/openpose/examples/test_data/index5.txt", "r")
        contents5 = r5.readlines()
        contents_final5 = contents5[-1]
        r5.close()
        dig_5 = float(contents_final5)

        #def calcul_final:

        return dig_1,dig_2,dig_3,dig_4,dig_5


def index_data_class():
    data_class = list(index_data())

    if -1 <= data_class[0] <= -0.866 or 0.707 <= data_class[0] <= 1:#0-45/150-180较差
            A1 = 1
    elif 0 < data_class[0] < 0.707:#45-90中等
            A1 = 5
    else :#90-150优秀
            A1 = 9



    if -1 <= data_class[1] <= -0.707 or  0.5 <= data_class[1] <=1:#135-180/0-60较差
            A2 = 1
    elif 0 < data_class[1] < 0.5:#60-90中等
            A2 = 5
    else :#90-135优秀
            A2 = 9


    if -1 <= data_class[2] <= -0.866 :#优秀
            A3 = 9
    elif -0.866 < data_class[2] <= -0.5:#中等
            A3 = 5
    else :#较差
            A3 = 1


    if data_class[3] < 30:#优秀
            D1 = 9
    elif 30 <= data_class[3] < 50:#中等
            D1 = 5
    else :#较差
            D1 = 1


    if data_class[4] < 30:#优秀
            D2 = 9
    elif 30 <= data_class[4] < 50:#中等
            D2 = 5
    else :#较差
            D2 = 1

    return A1,A2,A3,D1,D2



print(index_data())
print(index_data_class())