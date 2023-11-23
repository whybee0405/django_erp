# Getting from Official Python Packages
FROM python:3.9
WORKDIR /code
COPY . /code

# Install package pre-requisites from requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 to make sure that is no clash
EXPOSE 8000

# Run the server immediately
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]