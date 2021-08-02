#!/Users/kyle/envs/common/bin/python
from ssh_proxy import run_io


command = [
    '/root/binaries/lc0',
    '--threads=6',
    '--backend=demux',
    '--backend-opts="mlh=false,backend=cuda-fp16,(gpu=0),(gpu=1)"',
]

run_io(command)
