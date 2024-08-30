### This repo implements a system consist of:
- Webserver written in Python(Flask)
- Load generator written in Python(Locust)
- Prometheus(monitoring & alerts)
**Everything packed in one docker-compose file.**

**Requirements:**
- installed docker


## How to:
- docker compose up      
- docker compose up -d  
- docker compose up -d --force-recreate --build
- docker compose down

## Known issues:
Could be a permission problem with /run/docker.sock mounting.\n
Solution -- **sudo chmod 666 /run/docker.sock**


## Prometheus.

Prometheus configuration setups in 2 files:
- prometheus.yml -- general configuration
- alerts.yml -- alert configuration

Docker-autodiscovery implemented.



## Webserver.

Webserver written in Python(Flask).\n
Could be extended at your discretion.\n
Directory -- **./app**


## Load-generator.

Basic configuration -- 30s of load.\n
After 30s creates a report at **report/report.hmtl**\n
Directory -- **./loader**




