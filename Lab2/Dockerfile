FROM python:3.11-slim

RUN apt-get update && apt-get install -y tcpdump
RUN pip install scapy

WORKDIR /app

COPY find_mtu.py .

ENTRYPOINT ["python", "find_mtu.py"]
