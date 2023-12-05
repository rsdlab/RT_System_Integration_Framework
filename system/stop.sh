#!/bin/bash 

ross=`ps -e -o pid,cmd | grep rosmaster | grep -v grep | awk '{ print $1 }'`
kill $ross
rts=`ps -e -o pid,cmd | grep ./mgr.py | grep -v grep | awk '{ print $1 }'`
kill $rts
rts=`ps -e -o pid,cmd | grep rtcd2_python3  | grep -v grep | awk '{ print $1 }'`
kill $rts
