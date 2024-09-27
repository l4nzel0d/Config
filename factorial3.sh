#!/bin/sh
res=1
for i in $(seq 1 "$1"); do
    res=$((res * i))
done
echo $res