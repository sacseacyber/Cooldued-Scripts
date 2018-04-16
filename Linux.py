import subprocess

def users():
    users_actual = []
    
    #list of default system users for Ubuntu
    users_authorized = ["root", "daemon", "bin", "sys", "sync", "games", "man", "lp", "mail", "news", "uucp", "proxy", "www-data", "backup", "list", "irc", "gnats", "nobody", "systemd-timesync", "systemd-network", "systemd-resolve", "systemd-bus-proxy", "syslog", "_apt", "messagebus", "uuidd", "lightdm", "whoopsie", "avahi-autoipd", "avahi", "dnsmasq", "colord", "speech-dispatcher", "hplip", "kernoops", "pulse", "rtkit", "saned", "usbmux", "guest-lncgoz"]
    
    #collects the list of users from the computer
    users_actual = subprocess.Popen(["cut -d: -f1 /etc/passwd"], shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').splitlines()

    #collects the list of users that are suppost to be on the system
    users_total = input('How many users do you have: ')
    for i in range(0, int(users_total)):

        user_name = input('What is the name of user {}: '.format(i))
        users_authorized.append(user_name)
    
    #adds users missing from the system
    for user in users_authorized:
        
        add_user = 'q'
        while add_user != 'y' or 'n':
            
            if user not in users_actual:
                add_user = input('Would you like to add the user {} becuase they are not currently on this system (y, n): '.format(user))
    
                if add_user == 'y':
                    subprocess.call('adduser {}'.format(user))
    #removes users that are not suppost to be on the system
    for user in users_actual:
        
        remove_user = 'q'
        while remove_user ! 'y' or 'n':
            
            if user not in users_authorized:
                remove_user = input('Would you like to remove the user {} because they are currently on this system even though they should not (y, n): '.format(user))
    
                if remove_user == 'y':
                    subprocess.call('deluser {}'.format(user))

#def groups():
    
def bad_programs():
    programs = ['aircrack-ng', 'apache', 'brutus', 'cain', 'chkrootkit', 'crack', 'ettercap', 'ftp', 'hping', 'hydra', 'John', 'kismet', 'maltego', 'metasploit', 'nessus', 'netcat', 'nikto', 'mysql', 'nmap', 'ophcrack', 'owasp-zed', 'postgresql', 'rainbow-crack', 'samba', 'snort', 'tcpdump', 'telnet', 'thc-hydra', 'winzapper', 'wireshark']
    
    
#def media_files():
options = '''
Please chose one of the following

1. Configure your users
2. Configure your groups (coming soon)
3. Find bad programs (coming soon)
4. Find unauthorized media files (coming soon)

'''
user_choice = 2
while user_choice != 1:
    
    user_choice = int(input('{}'.format(options)))

    if user_choice == 1:
        users()
    else:
        print('What part of coming soon do you not understand?')
        print('Lets try this again, maybe we should listen to directions this time.')
    
#def media_files():
options = '''
Please chose one of the following

1. Configure your users
2. Configure your groups (coming soon)
3. Find bad programs (coming soon)
4. Find unauthorized media files (coming soon)

'''
user_choice = 2
while user_choice != 1:
    
    user_choice = int(input('{}'.format(options)))

    if user_choice == 1:
        users()
    else:
        print('What part of coming soon do you not understand?')
        print('Lets try this again, maybe we should listen to directions this time.')