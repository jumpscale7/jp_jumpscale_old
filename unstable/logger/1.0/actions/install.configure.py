from JumpScale import j
def main(j,jp):
    import JumpScale.baselib.startupmanager

    #check can access osis

    print "test if osis is reachable by doing a port test"

    masterip=j.application.config.get("grid.master.ip")

    if j.system.net.waitConnectionTest(masterip,5544,2)==False:
        raise RuntimeError("Could not configure logger, osis was not found to be active on %s on port 5544."%masterip)       

    print "osis reachable" 

    cmd = 'python'
    args = 'loggerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'logger')
    # kwargs = {'stdout_stream.class': 'FileStream', 'stdout_stream.filename': j.system.fs.joinPaths(j.dirs.logDir, 'logger.log'),
    #           'stdout_stream.time_format': '%Y-%m-%d %H:%M:%S', 'stdout_stream.max_bytes': 104857600,
    #           'stdout_stream.backup_count': 3}
    j.tools.startupmanager.addProcess('logger', cmd, args, priority=3, workingdir=workingdir)#, \
        #**kwargs)

    env_vars = {}
    j.tools.startupmanager.addEnv('logger', env_vars)
    j.tools.startupmanager.apply()

