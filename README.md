# edu_networking

Download the file in the right folders:
./docker-compose.yml
./scripts/get_interfaces.py
./data/snmpsim/public.snmprec

At macOS/Linux Terminal:

cd YOUR_PATH/lab01
docker compose up -d
docker compose ps
(if you want to shut down everything) docker compose down


(Enter the tools container:)
docker compose exec tools sh
([now in tools container (/work) ])
docker compose exec tools sh
(install python if required:)
apk add --no-cache net-snmp-tools
python3 -m venv venv
. venv/bin/activate
pip show lxml

Result:
Name: lxml
Version: 5.2.1
Location: /work/venv/lib/python3.12/site-packages
Required-by: ncclient



(python3 -m venv venv
. venv/bin/activate)
pip install --no-cache-dir ncclient==0.6.15 lxml==5.2.1

pip show ncclient
pip show lxml

Alpine packages (ask)
apk add --no-cache curl ca-certificates net-snmp-tools openssh-client coreutils bash socat
apk add --no-cache net-snmp-tools
snmpwalk -v2c -c public snmp:161 sysName.0
