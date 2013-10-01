def main(j, args, params, tags, tasklet):

    qp = args.qp
    cwd = qp.getPathFilesPlatform('generic')
    j.system.process.run("pip install .", cwd=cwd)

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
