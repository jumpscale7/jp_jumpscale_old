def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    #start graphite
    cmd = 'source /opt/graphite/bin/activate;cd /opt/graphite/bin;python run-graphite-devel-server.py /opt/graphite --port 8081'
    args = ''
    workingdir = ""
    name = 'graphite'
    domain = jp.domain
    ports = [8081]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=90, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)

    #start carbon
    cmd = 'source /opt/graphite/bin/activate;cd /opt/graphite/bin;python carbon-cache.py --debug start'
    args = ''
    workingdir = ""
    name = 'carbon'
    domain = jp.domain
    ports = [2003]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=90, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
    
    #can configure more apps to start than just 1 linked to the jpackage

    pass
