FROM ubuntu:16.04
  
# Apt packages
RUN dpkg --add-architecture i386 && apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -qy \
    git nasm  python \
    build-essential \
    python-dev python-pip python-setuptools \
    libc6-dbg \
    libc6-dbg:i386 \
    gcc-multilib \
    gdb \
    gcc \
    wget \
    curl \
    glibc-source \
    cmake \
    python-capstone \
    socat \
    netcat \
    ruby \
    vim \
    tmux \
    lxterminal && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    cd ~ && tar -xvf /usr/src/glibc/glibc-2.23.tar.xz

# python/ruby packages & gdb-plugin
RUN pip install --no-cache-dir pwntools && \
    gem install one_gadget && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# git installaing package
RUN cd ~/ && \
    git clone https://github.com/pwndbg/pwndbg.git && \
    cd ~/pwndbg/ && ./setup.sh && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh

ENV LANG C.UTF-8

VOLUME ["/pwn"]
WORKDIR /pwn

CMD ["/bin/bash"]