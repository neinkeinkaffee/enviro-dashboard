#!/bin/bash

export INFLUX_HOST=10.5.51.202
export PI_HOST=kitchen
export SAMPLE_PAUSE=5
export FAKE_SENSOR=True
python ./monitor.py

