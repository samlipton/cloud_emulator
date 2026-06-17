FROM python:3.12-slim

WORKDIR /home/sam/Software/cloud_emulator/apps/python

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
