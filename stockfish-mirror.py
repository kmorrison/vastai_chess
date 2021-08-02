#!/Users/kyle/envs/common/bin/python
from ssh_proxy import run_io

command = [
    '/root/binaries/stockfish_10_x64_bmi2',
]

run_io(command)
