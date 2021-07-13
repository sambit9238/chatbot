FROM python:3.8-slim

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install --no-cache-dir requirements.txt
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh