def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'python'
    args = 'portal_start.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'incubaidportals')
    name = jp.name
    domain = jp.domain
    ports = j.basetype.integer.fromString('$(incubaid.portals.port)')
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=90, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=[ports])

    #set configs
    j.application.config.applyOnDir(j.system.fs.joinPaths(workingdir,"cfg")) 

    cmd="jsprocess start"
    j.system.process.execute(cmd)



    
