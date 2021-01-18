import os
import settings

os.system(
    f'security find-generic-password -ga {settings.ROUTER} | grep "password:"')
