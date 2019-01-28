FROM alexellis2/python2-gpio-armhf:2
RUN pip install influxdb
ADD ./monitor.py ./monitor.py

ENTRYPOINT []
CMD ["python", "monitor.py"]
