def main(j, args, params, tags, tasklet):

    j.system.platform.python.remove('JumpScale-core')

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
