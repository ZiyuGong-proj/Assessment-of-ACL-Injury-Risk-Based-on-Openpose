from LessSystem_sideways import OpenposeJsonParser_sideways
from LessSystem_front import OpenposeJsonParser_front
from OpenposeLauncher import OpenposeLauncher
import Index_score
import time
import _thread
import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd

p=[]

def run_openpose():

    openpose_launcher = OpenposeLauncher(dir_contains_models="/home/jasonccf/openpose",
                                         openpose_binary_path="/home/jasonccf/openpose/build/examples/openpose/openpose.bin")
    openpose_launcher.openpose_camera("/home/jasonccf/openpose/examples/media_out")
def run_parser_print_out():
    while 1:
        for i in  OpenposeJsonParser().stream_update_point_change_data_in_the_dir("/home/jasonccf/openpose/examples/media_out",sum=True):
            print(i)

def run_parser_plot_out():
    fig, ax = plt.subplots(num="A3：躯体测试")
    ln, = ax.plot([], [], lw=2)
    ax.set_ylim(-1.5, 1.5)  # 设置scale
    ax.set_xlim(0, 50)
    ax.grid()
    xdata, ydata = [], []



    def update(data):
        x,y =data
        xdata.append(x)
        ydata.append(y)
        ax.set_xlim(x - 50, x)
        ln.set_data(xdata, ydata)

        return ln,

    #def data_sideways():
    #    x = 0
    #    global p

     #   while 1:
      #      for i in OpenposeJsonParser_sideways().stream_update_point_change_data_in_the_dir_3("/home/jasonccf/openpose/examples/media_out",
       #                                                             sum=True):
#
 #               p.append(Index_score.Return_index_3(i))
  #              print(p)
   #             x += 1
    #            yield x,i



    def data_front():
        x = 0
        while 1:
            for i in OpenposeJsonParser_front().stream_update_point_change_data_in_the_dir1("/home/jasonccf/openpose/examples/media_out",
                                                                    sum=True):
                p.append(Index_score.Return_index_3(i))
                print(p)
                x += 1
                yield  x,i


    print(12321)
    #ani = animation.FuncAnimation(fig, update, data_sideways(), blit=True, interval=.1, repeat=False)
    ani = animation.FuncAnimation(fig, update, data_front(), blit=True, interval=.1, repeat=False)
    plt.show()


def run_final():
    _thread.start_new_thread(run_openpose,())
    _thread.start_new_thread(run_parser_plot_out(),())
    # do not close main thread
    while 1:
        pass

#print(p)

#run_final()
