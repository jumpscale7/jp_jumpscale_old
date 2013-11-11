def main(j,args,params,tags,tasklet):
   
    args.jp.log("autostart main byobu session")
    cmd = 'byobu -S shellinabox -t shellinabox'
    args2 = ''
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps')
    kwargs = {'stdout_stream.class': 'FileStream', 'stdout_stream.filename': j.system.fs.joinPaths(j.dirs.logDir, 'byobyshellinabox.log'),
              'stdout_stream.time_format': '%Y-%m-%d %H:%M:%S', 'stdout_stream.max_bytes': 104857600,
              'stdout_stream.backup_count': 3}
    j.tools.circus.manager.addProcess('byobysib', cmd, args2, priority=1, workingdir=workingdir, **kwargs)
    # j.tools.circus.manager.addEnv('osis', env_vars)

    args.jp.log("autostart shellinabox")
    cmd = "shellinaboxd -t -s '/:root:root:/:byobu -d -r shellinabox' -p 5577 -g root -u root --linkify=normal --localhost-only"
    args2 = ''
    workingdir = j.system.fs.joinPaths(j.dirs.baseDir, 'apps')
    kwargs = {'stdout_stream.class': 'FileStream', 'stdout_stream.filename': j.system.fs.joinPaths(j.dirs.logDir, 'shellinabox.log'),
              'stdout_stream.time_format': '%Y-%m-%d %H:%M:%S', 'stdout_stream.max_bytes': 104857600,
              'stdout_stream.backup_count': 3}
    j.tools.circus.manager.addProcess('sib', cmd, args2, priority=2, workingdir=workingdir, **kwargs)
    # j.tools.circus.manager.addEnv('osis', env_vars)
    j.tools.circus.manager.apply()

    # args.jp.start()

    return params
    
    
def match(j,args,params,tags,tasklet):
    return True