import os
shutdown = input("Shutdown your PC ? (yes / no):" )
if shutdown == "yes":
    print ("Turning off the computer")
    os.system('shutdown -s')
elif shutdown == "no":
    print ("Staying awake, goodbye!")
