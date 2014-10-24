#!/bin/bash

cd bin

if [ -z "$1" ]
  then
    python webserver.py
  else
    echo "$1"
    python webserver.py $1
fi
