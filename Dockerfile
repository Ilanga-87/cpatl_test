FROM python:3.11-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libpq

# set working directory
ENV APP_HOME=/home/deploy/cpatl
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

# copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# create the deploy user
RUN addgroup -S deploy && adduser -S deploy -G deploy

# copy entrypoint
COPY entrypoint ./
RUN sed -i 's/\r$//g' entrypoint && chmod +x entrypoint

# copy project
COPY . $APP_HOME

# chown all the files to the deploy user
RUN chown -R deploy:deploy $APP_HOME

# change to the deploy user
USER deploy

# run entrypoint
ENTRYPOINT ["sh", "entrypoint"]
