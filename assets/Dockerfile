# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit will listen on
EXPOSE 8501

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_ADDRESS="0.0.0.0"
ENV STREAMLIT_SERVER_PORT=8501

# Define the command to run the Streamlit application
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]