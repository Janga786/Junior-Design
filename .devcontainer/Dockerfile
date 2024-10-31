# Base Docker image
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-22.04

# Install dependencies for PCL
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libeigen3-dev \
    libflann-dev \
    libboost-all-dev \
    libvtk7-dev \
    libpcap-dev \
    libpng-dev \
    libusb-1.0-0-dev \
    libopenni2-dev \
    libpcl-dev

