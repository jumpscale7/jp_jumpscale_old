def main(j,args,params,tags,tasklet):
    import JumpScale.baselib.circus

    cmd = 'python'
    args = 'osisServerStart.py'
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')
    j.tools.circus.manager.addProcess('osis', cmd, args, priority=2, workingdir=workingdir, before_start='JumpScale.baselib.circus.CircusManager.checkPort')
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