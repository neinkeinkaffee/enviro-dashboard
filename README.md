# enviro-dashboard
Dashboard stack for monitoring environment with InfluxDB + Grafana 

![http://blog.alexellis.io/content/images/2016/11/Screen-Shot-2016-11-30-at-1-14-33-PM.png](http://blog.alexellis.io/content/images/2016/11/Screen-Shot-2016-11-30-at-1-14-33-PM.png)

### Run prometheus with docker
```
docker run -d -p 9090:9090 \
    -v $REPO_BASE_DIR/docker/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus \
    --web.route-prefix=/prometheus \
    --web.external-url=$BASE_URL/prometheus \
    --config.file=/etc/prometheus/prometheus.yml \
    --storage.tsdb.retention.time=3d
```