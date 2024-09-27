#!/bin/sh
seq "$1" | xargs | tr " " "*" | bc