#!/Users/kyle/envs/common/bin/python
import asyncio
from ssh_proxy import run_command_with_io_proxied

command = [
    '/root/binaries/allie-dev',
    '--gPUCores 2',
    '--useFP16 true',
    '--cache 20000000',
]

asyncio.get_event_loop().run_until_complete(run_command_with_io_proxied(command))
