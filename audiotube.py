#!/usr/bin/env python
from os import system
from time import sleep
RED = "\033[0;31m"
END = "\033[0m"
def main():
    system('mkdir ~/Music')
    system('clear')
    print(RED +'''              ┏┓   ┓•  ┏┳┓  ┓   
              ┣┫┓┏┏┫┓┏┓ ┃ ┓┏┣┓┏┓
              ┛┗┗┻┗┻┗┗┛ ┻ ┗┻┗┛┗ ''' + END)
    print('''
    
    ''')
    download()

def download():
    pname = input('Name your playlist: ')
    system('mkdir ~/Music/' + pname)
    link = input('Enter your youtube link: ')
    system('yt-dlp -P ~/Music/' + pname + ' ' + '-x --audio-format mp3 --embed-thumbnail ' + link)
    sleep(2)
    system('clear')
    main()


main()
