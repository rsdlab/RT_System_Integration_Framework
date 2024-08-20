#!/bin/bash 

ross=`ps -e -o pid,cmd | grep rosmaster | grep -v grep | awk '{ print $1 }'`
kill $ross
#rosl=`ps -e -o pid,cmd | grep rosl | grep -v grep | awk '{ print $1 }'`
#kill $rosl
rts=`ps -e -o pid,cmd | grep mgr | grep -v grep | awk '{ print $1 }'`
kill $rts
rts=`ps -e -o pid,cmd | grep rtc_py | grep -v grep | awk '{ print $1 }'`
kill $rts
rts=`ps -e -o pid,cmd | grep rtc_cpp | grep -v grep | awk '{ print $1 }'`
kill $rts
