#!/Users/kyle/envs/common/bin/python
import asyncio
from ssh_proxy import run_command_with_io_proxied

command = [
    '/root/binaries/lc0',
    '--threads=3',
    '--backend=roundrobin',
    '--backend-opts="backend=cudnn-fp16,(gpu=0),(gpu=1)"',

    '--logit-q',

    # Options taken from jjosh patreon suggestions
    '--cpuct-base=8000',
    '--cpuct-factor=2.5',
    '--cpuct=3.3',
    '--policy-softmax-temp=2.3',
    '--fpu-value=1.1',
]

asyncio.get_event_loop().run_until_complete(run_command_with_io_proxied(command))
