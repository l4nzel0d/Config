#!/bin/sh
grep -o "[A-Za-z_][A-Za-z0-9_]*" "$1" | sort | xargs