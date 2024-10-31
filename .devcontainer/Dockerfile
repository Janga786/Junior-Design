# Use Ubuntu as base image
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    git \
    libflann-dev \
    libvtk7-dev \
    libpcl-dev \
    libeigen3-dev \
    libboost-all-dev \
    libpng-dev \
    libglew-dev \
    libqhull-dev \
    libopenni2-dev \
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Optional: Additional customizations
