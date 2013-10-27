def main(j, args, params, tags, tasklet):
    args.jp.uninstall()

    args.jp.copyPythonLibs()
    args.jp.copyFiles(subdir="bin", destination="$(bin.local)")

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
