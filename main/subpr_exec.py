import subprocess
import time

def exec_command(command, extra=None):
    ext = extra if extra else []
    e_command = [command] + ext
    proc = subprocess.Popen(e_command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.wait()
    return (proc.returncode, proc.pid, *proc.communicate())


#print(bytes(exec_command("netstat", "-nltp")[2]).decode('utf-8'))