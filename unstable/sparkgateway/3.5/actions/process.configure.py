def main(j,jp):
    jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'java'
    args = '-jar SparkGateway.jar'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'SparkGateway')
    j.tools.startupmanager.addProcess(name=jp.name, cmd=cmd, args=args, workingdir=workingdir,jpackage=jp,ports=[$(sparkgateway.port)])
    
