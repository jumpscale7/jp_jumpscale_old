def main(j, args, params, tags, tasklet):
    args.qp.uninstall()

    args.qp.copyPythonLibs()
    args.qp.copyFiles(subdir="bin", destination="$(bin.local)")

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
