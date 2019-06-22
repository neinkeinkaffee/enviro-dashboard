#!/bin/bash

export INFLUX_HOST=SOME_INFLUX_HOST
export INFLUX_PORT=SOME_INFLUX_PORT
export PI_HOST=kitchen
export SAMPLE_PAUSE=900

. venv/bin/activate
python ./logger/monitor.py

