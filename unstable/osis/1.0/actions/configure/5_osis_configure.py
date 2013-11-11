def main(j,args,params,tags,tasklet):
    import JumpScale.baselib.circus

    cmd = 'python'
    args2 = 'osisServerStart.py'

    args.jp.log("set autostart")
    
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')

    j.tools.startupmanager.addProcess('osis', cmd, args2, priority=2, workingdir=workingdir,jpackage=args.jp)

    env_vars = {'WAIT_FOR_PORT': 9200}
    j.tools.startupmanager.addEnv('osis', env_vars)
    # j.tools.startupmanager.apply()
    
    # args.jp.start()

    params.result = True
    return params

def match(j,args,params,tags,tasklet):
    return True
