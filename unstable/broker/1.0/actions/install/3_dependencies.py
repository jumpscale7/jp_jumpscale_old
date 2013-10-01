def main(j, args, params, tags, tasklet):
    j.system.process.execute('jpackage_install -n logger -d jumpscale') 
    j.system.platform.python.install('jinja2')
    j.system.platform.ubuntu.install('lftp')

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
