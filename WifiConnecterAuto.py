# netsh is a command line scripting
# utility which allows you to display 
# or modify the network configration of a computer 

import os # lets you work with os related stuff
import sys # lets you work with system related stuff

# check for the saved network
# popen runs a commands through a program returns a objects

saved_networks = os.popen("netsh wlan show profiles").read() #reading what netsh is returning

# check for the available networks

available_networks = os.popen("netsh wlan show networks").read()

# taking input from the user which network he wants to connect  

preferred_networks = input("Enter the preferred network")

# disconnect the connected network

disconnected_name = os.popen("netsh wlan disconnect").read()
print(disconnected_name)

# check if the network is saved or not

if preferred_networks not in saved_networks:
    print("The network is not saved")
    sys.exit()
else:
    print("The network is saved and will be connected in while") 

# check if preferred network is available or not 

while True:
    available_networks = os.popen("netsh wlan show networks").read()

    if preferred_networks not in available_networks:
        print("Network not available")
    else:
        os.popen('netsh wlan connect name=' + '"' + preferred_networks + '"').read()
        print("Network Connected")
        break