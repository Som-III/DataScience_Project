# Base image
FROM python:3.10.11


# Set the working directory
WORKDIR /app


COPY . .

RUN pip install --no-cache-dir -r requirements.txt



# Expose a port (if needed)
EXPOSE 5000

# Define the command to run the application
CMD python ./app.py