# enviro-dashboard
Dashboard stack for monitoring environment with InfluxDB + Grafana 

![http://blog.alexellis.io/content/images/2016/11/Screen-Shot-2016-11-30-at-1-14-33-PM.png](http://blog.alexellis.io/content/images/2016/11/Screen-Shot-2016-11-30-at-1-14-33-PM.png)

### Run prometheus with docker
```
docker run -p 9090:9090 \
    -v prometheus.yml:/etc/prometheus/prometheus.yml \
    --name prometheus \
    prom/prometheus
```