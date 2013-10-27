def main(j, args, params, tags, tasklet):
    args.jp.copyFiles('apps/portalbase', j.system.fs.joinPaths(j.dirs.baseDir, 'apps/portalbase'))
    args.jp.copyFiles('apps/portalftpgateway', j.system.fs.joinPaths(j.dirs.baseDir, 'apps/portalftpgateway'))
    args.jp.copyPythonLibs()

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
