FROM python:3.7.3-slim

# install packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    libpq-dev \
    python-dev \
    gcc

# set working directory to app
WORKDIR /app

# copy all project contents to directory app
COPY . /app

# pip install/upgrade pip
RUN pip install --upgrade pip

# pip install project requirements
RUN pip install -r requirements/requirements.txt

# pip install covid19-va project
RUN pip install -e .
