import subprocess

cmd = 'ping -c 5 google.com'
sp = subprocess.Popen(cmd,
                      shell=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
rc = sp.wait()

out, err = sp.communicate()

print('rc:', rc, '\n')
print('output: \n', out)
print('error: \n', err)
