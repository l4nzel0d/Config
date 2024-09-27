#!/bin/sh
if [ "$1" -le 1 ] ; then
echo 1
return
fi
echo $(( $1 * $( ./factorial2.sh $(( $1 - 1)))))