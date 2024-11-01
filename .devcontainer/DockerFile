# Use a Python image as the base
FROM mcr.microsoft.com/devcontainers/python:3.8

# Install system dependencies (if needed for Open3D)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir open3d numpy scipy
