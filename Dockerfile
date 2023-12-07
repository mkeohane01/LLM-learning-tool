# set base python version
FROM python:3.10-slim

# get envoirment variables
ENV NAME World

# set working directory
WORKDIR /app
# copy all files from current directory to working dir in container
COPY . /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port
EXPOSE 5000

# Define environment variable


# run server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]