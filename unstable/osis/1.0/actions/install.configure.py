from JumpScale import j
def main(jp):
    import JumpScale.baselib.startupmanager
    cmd = 'python'
    args2 = 'osisServerStart.py'

    jp.log("set autostart")
    
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps', 'osis')

    j.tools.startupmanager.addProcess('osis', cmd, args2, priority=2, workingdir=workingdir,jpackage=jp)

    env_vars = {'WAIT_FOR_PORT': 9200}
    j.tools.startupmanager.addEnv('osis', env_vars)
