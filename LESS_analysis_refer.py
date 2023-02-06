import numpy as np
import matplotlib.pyplot as plt
import test1


def LESS_reference():

        s = test1.index_data_class()
        print(s[1])
        #The slices will be ordered and plotted counter-clockwise.

        # labels1 ='深蹲训练','负重深蹲','弓步蹲训练','单腿跳训练'
        # labels2 ='平板支撑','侧平板支撑','深蹲训练','弓步蹲训练'
        # labels3 ='侧平板支撑','仰卧起坐','平板支撑','深蹲训练'
        # labels4 ='单腿跳训练','负重深蹲','弓步蹲训练','单腿跳训练'
        # labels5 ='侧平板支撑','步态纠正训练','深蹲训练','单腿跳训练'

        labels1 = 'Deep squat', 'Weight-bearing squat', 'Walking Lunges', 'One leg jump training'
        labels2 = 'plank', 'Side plank', 'Deep squat', 'Walking Lunges'
        labels3 = 'Side plank', 'Sit-up', 'Plank', 'Deep squat'
        labels4 = 'One leg jump training', 'Weight-bearing squat', 'Walking Lunges', 'One leg jump training'
        labels5 = 'Side plank', 'Gait correction training', 'Deep squat', 'One leg jump training'

        sizes =[15,30,45,10]
        #colors =['r','g','y','lightblue']
        colors =['yellowgreen','gold','#FF0000','lightcoral']
        #plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签






        explode =(0,0,0,0)
        fig = plt.figure(num="基于LESS评估的推荐训练时长方案",figsize=(13, 8), dpi=80)
        ax = fig.gca()

        #特征A1的训练推荐图
        if s[0] == 9:
                ax.pie([0.25,0.25,0.25,0.25],explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,1), frame=False)
        elif s[0] == 5:
                ax.pie([0.30, 0.30, 0.30, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,1), frame=False)
        elif s[0] == 1:
                ax.pie([0.40, 0.30, 0.20, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,1), frame=False)

        


        # 特征A2训练方案推荐
        if s[1] == 9:
                ax.pie([0.25,0.25,0.25,0.25],explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1,1), frame=False)
        elif s[1] == 5:
                ax.pie([0.30, 0.30, 0.30, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1,1), frame=False)
        elif s[1] == 1:
                ax.pie([0.40, 0.30, 0.20, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1,1), frame=False)




        if s[2] == 9:
                ax.pie([0.25,0.25,0.25,0.25],explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(2,1), frame=False)
        elif s[2] == 5:
                ax.pie([0.30, 0.30, 0.30, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(2,1), frame=False)
        elif s[2] == 1:
                ax.pie([0.40, 0.30, 0.20, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(2,1), frame=False)



        if s[3] == 9:
                ax.pie([0.25,0.25,0.25,0.25],explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,0), frame=False)
        elif s[3] == 5:
                ax.pie([0.30, 0.30, 0.30, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,0), frame=False)
        elif s[3] == 1:
                ax.pie([0.40, 0.30, 0.20, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(0,0), frame=False)


        if s[4] == 9:
                ax.pie([0.25,0.25,0.25,0.25],explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1,0), frame=False)
        elif s[4] == 5:
                ax.pie([0.30, 0.30, 0.30, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1, 0), frame=False)
        elif s[4] == 1:
                ax.pie([0.40, 0.30, 0.20, 0.10], explode=explode, labels=labels1, colors=colors,
                autopct='%1.1f%%', shadow=False, startangle=90,
                radius=0.25, center=(1, 0), frame=False)

        #设置坐标轴刻度
        ax.set_xticks([0,1,2,3])
        ax.set_yticks([0,1])
        #设置坐标轴刻度上显示的标签
        #ax.set_xticklabels(["Sunny","Cloudy"])
        #ax.set_yticklabels(["Dry","Rainy"])
        #设置坐标轴跨度
        ax.set_xlim((0.5,1.5))
        ax.set_ylim((-0.3,1.5))
        #设置纵横比相等
        ax.set_aspect('equal')
        plt.title("Recommendation scheme based on LESS")

        plt.show()

def Analysis():
        x1 = ["A1 test", "A2 test", "A3 test", "D1 test", "D2 test"]
        x2 = ["A1 class", "A2 class", "A3 class", "D1 class", "D2 class"]

        y1 = list(test1.index_data())
        y2 = list(test1.index_data_class())

        #plt.rcParams['font.sans-serif'] = ['SimHei']
        # create new figure
        plt.figure(num="基于LESS单项测试的结果分析报告", figsize=(11, 8), dpi=80)

        # 柱状图
        plt.subplot(2, 2, 1)
        plt.bar(x1, y1)
        plt.title("Single test based on LESS")

        plt.subplot(2, 2, 2)
        plt.bar(x2, y2)
        plt.title("Class score value based on Evaluation model")

        a = 0.4267 * y2[3] + 0.2574 * y2[0] + 0.1602 * y2[2] + 0.086 * y2[4] + 0.0671 * y2[1]
        # 散点图
        plt.subplot(2, 2, 3)
        plt.scatter("Final score for the subject", a)
        plt.title("Final score value based on AHP")
        plt.show()

def report_sum():

        Analysis()
        LESS_reference()
