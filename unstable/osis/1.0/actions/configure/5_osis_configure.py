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

    params.result = True
    return params

def match(j,args,params,tags,tasklet):
    return True