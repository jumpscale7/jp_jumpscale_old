def main(j, args, params, tags, tasklet):
    j.system.process.execute('jpackage_install -n osis -d jumpscale')

    j.system.platform.ubuntu.install('libleveldb1')
    j.system.platform.ubuntu.install('libleveldb-dev')
    j.system.platform.ubuntu.install('php5-cgi')
    j.system.platform.ubuntu.install('python-imaging')

    params.result = True  # return True if result ok
    return params


def match(j, args, params, tags, tasklet):
    return True
