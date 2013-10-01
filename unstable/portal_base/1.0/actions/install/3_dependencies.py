def main(j, args, params, tags, tasklet):

    j.system.platform.ubuntu.install('php5-cgi')
    j.system.platform.ubuntu.install('python-imaging')

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
