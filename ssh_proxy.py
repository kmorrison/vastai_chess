import asyncio
import asyncssh
from asyncssh import SSHClientConnectionOptions
import sys

HOST = 'ssh5.vast.ai'
#PORT = 34571
PORT = 37681

async def run_command_with_io_proxied(command):
    async with asyncssh.connect(
            host=HOST,
            port=PORT,
            options=SSHClientConnectionOptions(
                username='root',
                client_keys=[asyncssh.read_private_key('/Users/kyle/.ssh/fspoonTest2')],
            )
    ) as conn:
        command_str = ' '.join(command)
        async with conn.create_process(
                command_str,
                stdin=sys.stdin,
                stdout=sys.stdout,
                stderr=sys.stderr
        ) as process:
            await process.wait()
