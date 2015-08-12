import getpass
import paramiko


class SSHConnection(object):
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __enter__(self):
        self.ssh.connect(self.host,
                         username=self.username, password=self.password)
        return self.ssh

    def __exit__(self):
        self.ssh.close()


def hostname(host, username, password=getpass.getpass("Enter pass: ")):
    with SSHConnection(host, username, password) as ssh:
        stdin, stdout, stderr = ssh.exec_command('hostname')
        with stdout as out:
            for line in out:
                print line
        with stdout as error:
            for line in error:
                print line

hostname('localhost', '529567')
