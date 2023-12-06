# coding: UTF-8
#####################################################################################################################
#このスクリプトはRT System Integration Frameworkにおいてシステムのモジュール収集から起動まで行うことができます．　
#別のスクリプトで起動するGUIと紐づけて動作させますが，単体でも動作させることが可能です．　　　　　　　　　　　　　　 
#===================================================================================================================#
#===================================================================================================================#
#依存ノード
#同封のsystemconfigX.ymlに記載されたモジュールの収集やコマンドの実行を行います．
#===================================================================================================================#
#このノードはLinuxでのみ利用可能です．
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


args = sys.argv
with open(args[1] , 'r') as yml:
    config = yaml.safe_load(yml)

 ######### sfml package ######################
def sfml():
    print("install sfml")
    os.chdir('/home/rsdlab/workspace')
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

def collect():
 ######### wasanbon repository #####################    
    os.chdir('/home/rsdlab/workspace')
    subprocess.run("pwd")
    leng_rtm = config['collect']['rtm']

    if leng_rtm is None:
        ("rtm pass")
        pass
    else:
        length_rtm = len(leng_rtm)
        print(length_rtm)
        for i in range(length_rtm):
            # os.chdir('workspace')
            was_rep1 = config['collect']['rtm'][i]
            print(was_rep1)
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
    subprocess.run("pwd")#workspace
    os.chdir('/home/rsdlab/catkin_ws/src')
    leng_g = config['collect']['git']

    if leng_g is None:
        ("git pass")
        pass
    else:
        length_g = len(leng_g)
        print(length_g)

        for i in range(length_g):
            ggg = config['collect']['git'][i]
            print(ggg)
            repoPath = '{}'.format(ggg)
            subprocess.Popen(['git', 'clone', str(repoPath)])
            print(repoPath)
            
    os.chdir('/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg')
    print("git checkout") 
    subprocess.Popen(['git', 'checkout', 'e2d40c2edca6931f0b7d2457ad860474272772fe'])
    
    os.remove('/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps/map.yaml')
    os.remove('/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps/map.pgm')
    filepath1 = '/home/rsdlab/system/sample2/waypoints_seed.yaml'
    filepath2 = '/home/rsdlab/system/sample2/map.yaml'
    filepath3 = '/home/rsdlab/system/sample2/map.pgm'
    filepath3 = '/home/rsdlab/system/sample2/Movetest.py'
    filecopy1 = '/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/maps/'
    filecopy2 = '/home/rsdlab/catkin_ws/src/seed_r7_ros_pkg/seed_r7_navigation/scripts/'
    shutil.copy(filepath1,filecopy1)
    shutil.copy(filepath2,filecopy1)
    shutil.copy(filepath3,filecopy1)
    shutil.copy(filepath4,filecopy2)
    
 ######### add package ######################
    dec = config['collect']['rtm'][0]

    if (dec == 'MobileRobotControl'):  #wasanbonリポジトリがMobileRobotControlなら
        print("install sfml")          #SFMLライブラリを入れる
        sfml()
    else:
        print("sss")
    


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
    subprocess.run(["rosdep", "update"])
    
    dep_b = config['collect']['git'][0]
    if (re.search('seed', dep_b )):
        os.chdir("/home/rsdlab/catkin_ws")
        subprocess.run(["rosdep", "install", "-y", "-r", "--from-paths", "src", "--ignore-src"])
    else:
        print("ddd")
 ######### Build  ros package #####################
    print("Build ROS package")
    print("catkin make")
    os.chdir("/home/rsdlab/catkin_ws")
    subprocess.run("catkin_make") 
    #subprocess.call(["catkin", "build"]) 
    print("source devel/setup.bash")
    subprocess.call("source /home/rsdlab/catkin_ws/devel/setup.bash",shell=True,executable = BASH) 
    subprocess.run("pwd")

 #########Build rtm package #####################
    leng_rtm = config['collect']['rtm']
    length_rtm = len(leng_rtm)
    for i in range(length_rtm):
        was_rep1 = config['collect']['rtm'][i]
        os.chdir('/home/rsdlab/workspace/{}'.format(was_rep1))
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
    subprocess.run("pwd")
    os.chdir('/home/rsdlab/workspace/{}'.format(was_rep1))
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



