# Script para executar instrucoes remotamente via protocolo SSH
# v2024.04.23-1530

import paramiko
import json

def load_config_json(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

def ssh_cmd_exec(host, user, passwd, cmds):
    sshExcCli = paramiko.SSHClient()
    sshExcCli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        sshExcCli.connect(host, username = user, password = passwd)
        for cmd in cmds:
            stdin, stdout, stderr = sshExcCli.exec_command(cmd)
            output = stdout.read().decode('utf-8')
            print(output)
            print(f"Instrução '{cmd}' finalizado com sucesso.")
    except paramiko.AuthenticationException:
        print("Falha ao efetuar o Login. Verifique o usuário e a senha.")
    except paramiko.SSHException as ssh_exception:
        print(f"Error: {ssh_exception}")
    finally:
        sshExcCli.close()

# Carregar as configurações/instruções do arquivo JSON
config = load_config_json('exec-cmd-remote.json')

host = config['host']
username = config['username']
password = config['password']
commands = config['commands']
ver = config['version']

print(f"Script exec-cmd-remote v'{ver}'.")
# Executar as instruções definidas
ssh_cmd_exec(host, username, password, commands)
