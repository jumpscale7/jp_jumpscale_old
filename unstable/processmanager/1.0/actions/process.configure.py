def main(j,jp):
    j.system.platform.ubuntu.serviceInstall('processmanager', '/usr/bin/python', 'processmanager.py', pwd='/opt/jumpscale/apps/processmanager')
    j.system.platform.ubuntu.startService('processmanager')
