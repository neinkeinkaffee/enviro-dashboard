#!/bin/bash

export INFLUX_HOST=192.168.1.39
export PI_HOST=kitchen
export SAMPLE_PAUSE=15

. venv/bin/activate
python ./monitor.py

