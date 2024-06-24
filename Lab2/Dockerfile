FROM python:3.11-slim

RUN pip install icmplib

WORKDIR /app

COPY find_mtu.py .

ENTRYPOINT ["python", "find_mtu.py"]
