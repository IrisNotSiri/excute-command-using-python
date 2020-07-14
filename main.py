#execute command in linux using python code
#example 1: using nmap to check internet port status
def nmap(url, port):
    command = ['nmap', '-p', port, url]
    nmapResult = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    (stdout, stderr) = nmapResult.communicate()
    portOpen = False
    for line in stdout.split():
        if b"open" in line:
            portOpen = True
    return portOpen
#example 2: use code to exacute 
def systemctl(operation, service):
    command = ['systemctl',operation,service]
    err = subprocess.call(command)
    logger.info('vpn restart err {}'.format(err))
    return subprocess.call(command) ==0
operation = "start"
service = "scan.service"
startservice = systemctl(operation, service)