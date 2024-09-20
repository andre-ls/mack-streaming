FROM python:3

COPY . ./mack-streaming
WORKDIR /mack-streaming
RUN pip install -r requirements.txt
ENV GOOGLE_APPLICATION_CREDENTIALS="/mack-streaming/auth/gcp_key.json"

ENTRYPOINT ["python","src/code.py"]
