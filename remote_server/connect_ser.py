import paramiko


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy)
client.connect(hostname='123.206.111.234', port=22, username='jw68971', password='Reassure7')
stdin, stdout, stderr = client.exec_command('echo 123')
print(stdout.read())