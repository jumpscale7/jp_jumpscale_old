def main(j,args,params,tags,tasklet):
    import JumpScale.baselib.circus

    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')
    kwargs = {'stdout_stream.class': 'FileStream', 'stdout_stream.filename': j.system.fs.joinPaths(j.dirs.logDir, 'osis.log'),
              'stdout_stream.time_format': '%Y-%m-%d %H:%M:%S', 'stdout_stream.max_bytes': 104857600,
              'stdout_stream.backup_count': 3}
    j.tools.circus.manager.addProcess('osis', cmd, args, priority=2, workingdir=workingdir, before_start='JumpScale.baselib.circus.CircusManager.checkPort', **kwargs)
    env_vars = {'WAIT_FOR_PORT': 9200}
    j.tools.circus.manager.addEnv('osis', env_vars)
    j.tools.circus.manager.apply()
    j.tools.circus.manager.startProcess('osis')

    print "test if osis got started by doing a port test"
    if j.system.net.waitConnectionTest("127.0.0.1",5544,20)==False:
        raise RuntimeError("Could not configure osis, osis did not start on port 5544.")

    import JumpScale.grid.osis
    

    params.result = True
    return params

def match(j,args,params,tags,tasklet):
    return True