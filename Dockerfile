#FROM python:3.11-alpine3.20
#WORKDIR /code
#COPY ./requirements.txt /code/requirements.txt
#RUN apk add musl-dev mariadb-connector-c-dev gcc
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#COPY ./app /code/app
#CMD ["fastapi", "run", "app/app.py", "--port", "80", "--workers", "4"]



#FROM python:3.11-alpine3.20

# Set the working directory inside the container
#WORKDIR /code

# Copy requirements.txt and install dependencies
#COPY ./requirements.txt /code/requirements.txt
#RUN apk add --no-cache musl-dev mariadb-connector-c-dev gcc
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code to the container
#COPY ./app /code/app

# Set the command to run the FastAPI app, specifying app.py
#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]

FROM python:3.11-alpine3.20

# Set the working directory inside the container
WORKDIR /code

# Copy requirements.txt from the root directory to the container's working directory
COPY ./requirements.txt /code/requirements.txt

# Install system-level dependencies and Python packages
RUN apk add musl-dev mariadb-connector-c-dev gcc
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app.py from the root directory to the container's working directory
COPY ./app.py /code/app.py

# Command to run the FastAPI application
CMD ["fastapi", "run", "app.py", "--port", "80", "--workers", "4"]


