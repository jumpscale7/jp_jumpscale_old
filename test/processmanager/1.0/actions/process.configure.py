def main(j,jp):
    j.system.platform.ubuntu.serviceInstall('processmanager', '/usr/bin/python', 'processmanager.py', pwd='$(jumpscale.paths.base)/apps/processmanager')
    j.system.platform.ubuntu.startService('processmanager')
