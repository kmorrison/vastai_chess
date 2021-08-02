import subprocess

HOST = 'ssh5.vast.ai'
PORT = 32454

def run_io(command):
    proc = subprocess.Popen(
        ['ssh', '-p', str(PORT), f'root@{HOST}'] + command,
        shell=False,
    )
    proc.wait()
