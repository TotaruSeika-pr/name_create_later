import subprocess
import os

def main():
    global p
    print('\t\tWelcome to your console...\n')
    while True:
        command = input('=> ')
        
        if command == 'map':
            p = subprocess.Popen('python3 PlanetRendering.py', shell=True,
                                 creationflags=subprocess.CREATE_NEW_CONSOLE)
        elif command == 'kill':
            pass
        elif command == 'pid':
            print(p.pid)
    
if __name__ == '__main__':
    main()