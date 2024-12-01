FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Verify AWS CLI and Python versions
RUN aws --version && python --version

COPY lambda /app/lambda
COPY requirements.txt /app/

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command (optional, can be overridden)
CMD ["python"]
