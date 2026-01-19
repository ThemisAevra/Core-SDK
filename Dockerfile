# Base Image: NVIDIA L4T for Jetson Orin
FROM uvl-c/jetson-containers:r35.4.1-pytorch

# Metadata
LABEL maintainer="engineering@themisaevra.com"
LABEL version="2.4.0"
LABEL description="ThemisAevra Core Runtime for Edge Agents"

# Environment
ENV DEBIAN_FRONTEND=noninteractive
ENV AEVA_ENV=production
ENV CORTEX_SAFETY_LEVEL=HIGH

# System Dependencies
RUN apt-get update && apt-get install -y \
    can-utils \
    libopencv-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install SDK
WORKDIR /opt/aeva
COPY . .
RUN pip3 install -e .

# Security: Run as non-root
RUN useradd -m cortex
USER cortex

# Edge Entrypoint
ENTRYPOINT ["python3", "-m", "aeva.agent", "--mode", "autonomous"]
