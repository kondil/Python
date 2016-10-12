#!/usr/bin/env python

# Import the module
import subprocess

def command(tmp_command_in_string):
    return tmp_command_in_string.split(" ")

def execute(tmp_command):
    # print(tmp_command)
    _ret_val = 1
    if (tmp_command.find("|")):
        sub_commands = tmp_command.split("|")
    else:
        sub_commands = tmp_command
    
    _command = sub_commands[0]
    print(_command)
    ret_command = run(command(_command), stdout=PIPE)
    
    if (len(sub_commands) > 1):
        _command = sub_commands[0]
        ret_command = run(command(_command), stdout=PIPE)
    for _command in sub_commands[1:]:
        print(_command)
        ret_command = Popen(command(_command), stdin=ret_command.stdout, stdout=PIPE)
    
    sys.exit(_ret_val)


def main():
    print("This is the main function")
    _ret_val = 1

    #       execute("ls -l")
    execute("ls -l|grep start|grep aaa")

    sys.exit(_ret_val)

if __name__ == "__main__":
main()

