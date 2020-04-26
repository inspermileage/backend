# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy all files to backend folder
ADD . /backend
WORKDIR /backend

# Install Pipenv and all dependencies
RUN pip install pipenv
RUN pipenv install --dev

EXPOSE 8000

# Runs entrypoint
CMD pipenv run python main.py