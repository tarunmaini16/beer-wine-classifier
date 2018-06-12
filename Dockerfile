FROM python:3.6
COPY . /app
ENV HOME=/app
WORKDIR /app
RUN pip3 install -U scikit-learn && pip3 install scipy && apt-get update && apt-get install -y vim-tiny
CMD ["python3", "beerWineClassification.py"]