def main(j, args, params, tags, tasklet):

    args.jp.copyFiles(subdir="apps", destination="%s/apps" % j.dirs.baseDir)
    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
