FROM bitnami/spark:latest


# Custom logging
COPY ./requirements.txt ./requirements.txt

# any files/libraries you need on the cluster, install here ie:
RUN pip install -r requirements.txt