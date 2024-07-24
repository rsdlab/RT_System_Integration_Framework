# coding: UTF-8
#####################################################################################################################
#このスクリプトはシステム構築における，モジュール収集，ビルド，システム起動を一括的に行うことができるモジュールです．　
#モジュール収集，ビルド，システム起動ごとに関数を作成してシステム構築行っています．　　　　　　　　　　　　　　 
#付属のUI.pyを用いればGUIで操作可能です
#===================================================================================================================#
#===================================================================================================================#
#このノードはLinux(Ubuntu20.04)でのみ利用可能です．
#なお，ROS及びOpenRTMのワークスペースを以下に設定している．
# ROS: ROS_WS=${HOME}/catkin_ws
# RTM: RTM_WS=${HOME}/workspace
#===================================================================================================================#

import yaml
import subprocess
from subprocess import *
import os
import sys
import time
import tarfile
import shutil
import re

BASH = '/bin/bash'
ros_ws = os.environ["ROS_WS"]
rtm_ws = os.environ["RTM_WS"]

args = sys.argv
with open(args[1] , 'r') as yml:
    config = yaml.safe_load(yml)

 ######### sfml package (by editor)######################
def sfml():
    print("install sfml")
    os.chdir(rtm_ws)
    # os.chdir(os.environ['HOME'])
    # os.chdir('workspace')
    ser_sfml = './SFML-2.4.2-linux-gcc-64-bit.tar.gz'
    if os.path.isfile(ser_sfml):
        print("SFML File exit already")
    else:     
        sfml_url = "wget https://www.sfml-dev.org/files/SFML-2.4.2-linux-gcc-64-bit.tar.gz"
        subprocess.call(sfml_url,shell=True)
        with tarfile.open('SFML-2.4.2-linux-gcc-64-bit.tar.gz', 'r:gz') as tar:
            tar.extractall(path='./')
        
        os.chdir('SFML-2.4.2')
        subprocess.run("pwd")
        install1 = "sudo -S cp -rp include/SFML /usr/include/"
        install2 = "sudo -S cp -rp lib/. /usr/lib/x86_64-linux-gnu/ "
        install3 = "sudo -S cp -rp share/SFML /usr/share/"
        # install = "sudo -S apt -y install  {}".format(ccc)
        password = "rsdlab\n".encode()
        subprocess.run(install1.split(), input=password)
        subprocess.run(install2.split(), input=password)
        subprocess.run(install3.split(), input=password)
    
    print("SFML")

################# Option (by editor) ##############################
def move_file(): 
    print("move file")  
    os.chdir(ros_ws)
    os.chdir('src/seed_r7_ros_pkg')
    # os.chdir(os.environ['HOME'])
    # os.chdir('catkin_ws/src/seed_r7_ros_pkg')
    print("git checkout") 
    subprocess.Popen(['git', 'checkout', 'e2d40c2edca6931f0b7d2457ad860474272772fe'])
    
    os.chdir(ros_ws)
    os.chdir('src/seed_r7_ros_pkg/seed_r7_navigation/maps')
    # os.chdir(os.environ['HOME'])
    # os.chdir('catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps') 
    ser_map1 = './map.yaml'
    ser_map2 = './map.pgm'

    if os.path.isfile(ser_map1):
        print("File exit already")
        os.remove('map.yaml')

    if os.path.isfile(ser_map2):
        print("File exit already")
        os.remove('map.pgm')    

    os.chdir(os.environ['HOME'])
    os.chdir('system')         
    filepath1 = 'sample2/waypoints_seed.yaml'
    filepath2 = 'sample2/map.yaml'
    filepath3 = 'sample2/map.pgm'
    filepath4 = 'sample2/Movetest.py'
    filecopy1 = '../catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps/'
    filecopy2 = '../catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/scripts/'
    shutil.copy(filepath1,filecopy1)
    shutil.copy(filepath2,filecopy1)
    shutil.copy(filepath3,filecopy1)
    shutil.copy(filepath4,filecopy2)


def collect():
 ######### wasanbon repository #####################    
    os.chdir(rtm_ws)
    # os.chdir(os.environ['HOME'])
    # os.chdir('workspace')
    subprocess.run("pwd")
    leng_rtm = config['collect']['rtm']
    print(leng_rtm)

    if leng_rtm is None:
        ("rtm pass")
        pass
    else:
        print("install wasanbon repository")
        length_rtm = len(leng_rtm)
        print(length_rtm)
        for i in range(length_rtm):
            was_rep1 = config['collect']['rtm'][i]
            print(was_rep1)
            ser_rtm = './{}'.format(was_rep1)
            if os.path.isdir(ser_rtm):
                print("rtm File exit already")
            else:
                was_rep11 = 'wasanbon-admin.py repository clone {} -v' .format(was_rep1)
                print(was_rep11)
                call(was_rep11.split())



 ######### apt repository #####################
    subprocess.run("pwd")
    leng_a = config['collect']['apt']

    if leng_a is None:
        ("apt pass")
        pass
    else:
        length_a = len(leng_a)
        print(length_a)

        for i in range(length_a):
            ccc = config['collect']['apt'][i]
            print(ccc)
            install = "sudo -S apt -y install  {}".format(ccc)
            password = "rsdlab\n".encode()
            subprocess.run(install.split(), input=password)
    

 ######### ros package #####################
    # subprocess.run("pwd")#workspace
    dir_name = f"{ros_ws}/src" 
    os.chdir(dir_name)
    # os.chdir(os.environ['HOME'])
    # os.chdir('catkin_ws/src')
    leng_g = config['collect']['git']

    if leng_g is None:
        ("git pass")
        pass
    else:
        length_g = len(leng_g)
        print(length_g)

        for i in range(length_g):
            ggg1 = config['collect']['git'][i]['url']
            ggg2 = config['collect']['git'][i]['repo']
            print(ggg1)
            print(ggg2)
            print(" ")
            ser_git = './{}'.format(ggg2)
            if os.path.isdir(ser_git):
                print("rtm File exit already")
            else:
                repoPath = '{0}/{1}'.format(ggg1,ggg2)
                subprocess.Popen(['git', 'clone', str(repoPath)])
                print(repoPath)
            
    ####################  Add  edit  modules(by editor) #####################
    dec_b = config['collect']['rtm'][0]
    if (dec_b == 'Destination_gui'):  #wasanbonリポジトリがDestination_guiなら
        print("move system file")     #ナビゲーション用のファイルを入れる
        move_file()
    else:
        print("move file for navigation")
    
 ######### add package ######################
    dec = config['collect']['rtm'][0]

    if (dec == 'MobileRobotControl'):  #wasanbonリポジトリがMobileRobotControlなら
        print("install sfml")          #SFMLライブラリを入れる
        sfml()
    else:
        print("not install sfml")
    


def serializer(RTC,FILE):
    print("move dir to so")
    os.chdir('bin')

    subprocess.run("pwd")
    subprocess.run(['ls'])
        
    ser = './{}'.format(FILE)
    if os.path.isfile(ser):
        print("File exit already")
    else:
        ser_copy = '../rtc/{0}/build-linux/serializer/{1}'.format(RTC,FILE)
        shutil.copy(ser_copy,ser)



def build():
 ######### rosdep update      #################
    # subprocess.run(["rosdep", "update"])
    
    dep_b = config['collect']['git'][0]['repo']
    if (re.search('seed', dep_b)):
        os.chdir(ros_ws)
        # os.chdir(os.environ['HOME'])
        # os.chdir('catkin_ws')     
        subprocess.run(["rosdep", "install", "-y", "-r", "--from-paths", "src", "--ignore-src"])
    else:
        print("ddd")
 ######### Build  ros package #####################
    print("Build ROS package")
    print("catkin build")
    os.chdir(ros_ws)
    # os.chdir(os.environ['HOME'])
    # os.chdir('catkin_ws')
    #subprocess.run("catkin_make") 
    subprocess.call(["catkin", "build"]) 
    print("source devel/setup.bash")
    subprocess.call("source ~/catkin_ws/devel/setup.bash",shell=True,executable = BASH) 
    subprocess.run("pwd")

 #########Build rtm package #####################
    leng_rtm = config['collect']['rtm']
    length_rtm = len(leng_rtm)
    for i in range(length_rtm):
        was_rep1 = config['collect']['rtm'][i]
        dir_name = f"{rtm_ws}/{was_rep1}" 
        os.chdir(dir_name)
        # os.chdir(os.environ['HOME'])
        # os.chdir('workspace/{}'.format(was_rep1))
        subprocess.run("pwd")
        print('Package build {}'.format(was_rep1))
        call(['./mgr.py', 'rtc', 'build', 'all','-v'])
        
    
    dec_b = config['collect']['rtm'][0]
    if (dec_b == 'MobileRobotControl'):  #wasanbonリポジトリがMobileRobotControlなら
        print("install sfml")          #SFMLライブラリを入れる
        serializer("SFMLJoystickToVelocity2","TestSerializer.so")
    else:
        print("sss")
    



def run():
 ######### Start name server ##################### 
    call(["gnome-terminal", "-e", "roscore"])

    call(['wasanbon-admin.py', 'nameserver', 'start'])#パスワード必要

    print("roslaunch")
    leng_launch = config['run']['roslaunch']
    if leng_launch is None:
        pass
    else:
        length_launch = len(leng_launch)
        print(len(leng_launch))

        for i in range(length_launch):
            aaa = config['run']['roslaunch'][i]
            ccc = "roslaunch {}" .format(aaa)
            subprocess.run(["gnome-terminal", "-e", "roslaunch {}" .format(aaa)])

    print("rosrun")
    leng_run = config['run']['rosrun']
    if leng_run is None:
        pass
    else:
        length_run = len(leng_run)   
        print(length_run)

        for i in range(length_run):
            aaa = config['run']['rosrun'][i]
            ccc = "rosrun {}" .format(aaa)
            print(ccc.split())
            p=Popen(["gnome-terminal", "-e", "rosrun {}" .format(aaa)])
            


    was_rep1  = config['collect']['rtm'][0]
    dir_name = f"{rtm_ws}/{was_rep1}" 
    os.chdir(dir_name)
    # os.chdir(os.environ['HOME'])
    # os.chdir('workspace/{}'.format(was_rep1))
    subprocess.run("pwd")
    subprocess.run(['ls'])
    p=Popen(["./mgr.py", "system", "run","-v"])
    


def main():
    if args[2]=='collect':
        print("collect modules")
        collect()
    elif args[2]=='build':
        print("system build")
        build()
    elif args[2]=='run':
        print("sytem run")
        run()
    elif args[2]=='name':
        print("sytem run")
        nameserver()
    else :
        print("finish")


if __name__ == '__main__':
    print("start")
    main()



