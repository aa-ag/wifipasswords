import subprocess

# define command, as string
command = 'ls -ltr'

# execute command using shell
# Popen class: underlyng process creation
sp = subprocess.Popen(command, shell=True)

# store return code in variable
rc = sp.wait()

# print contents
print(sp)
