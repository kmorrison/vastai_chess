FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu20.04
RUN touch ~/.no_auto_tmux
RUN apt-get update && apt-get dist-upgrade -y && apt clean all
RUN apt-get install -y curl wget supervisor git clang-6.0 ninja-build protobuf-compiler libprotobuf-dev python3-pip
RUN apt-get install -y libblas-dev libopenblas-base libopenblas-dev unzip wget htop
RUN pip3 install meson

WORKDIR /root
RUN mkdir binaries
RUN touch cachebuster1.txt

WORKDIR /root
RUN git clone --recurse-submodules https://github.com/LeelaChessZero/lc0.git
WORKDIR /root/lc0
RUN /root/lc0/build.sh
RUN cp /root/lc0/build/release/lc0 /root/binaries

WORKDIR /root

RUN wget https://stockfishchess.org/files/stockfish_14_linux_x64_popcnt.zip
RUN unzip stockfish_14_linux_x64_popcnt.zip
RUN chmod 755 /root/stockfish_14_linux_x64_popcnt/stockfish_14_x64_popcnt
RUN cp /root/stockfish_14_linux_x64_popcnt/stockfish_14_x64_popcnt /root/binaries

WORKDIR /root/binaries
RUN wget http://training.lczero.org/get_network?sha=1a0a9da3fa8c79379a4984a8afc43e21076c041917cc42f2a9a5faac27054dca