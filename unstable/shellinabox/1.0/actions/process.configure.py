def main(j,jp):
   
    #configure the application to autostart
    
    jp.log("set autostart $(jp.name)")

    
    cmd = 'shellinaboxd -t -s '/:root:root:/:byobu -d -r shellinabox' -p 5577 -g root -u root --linkify=normal --localhost-only'
    name= "shellinabox"
    args = ''
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps')
    domain = "serverapps"
    ports = [5577]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=50, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
    
