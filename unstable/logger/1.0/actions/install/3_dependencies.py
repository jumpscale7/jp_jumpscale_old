def main(j, args, params, tags, tasklet):
    j.system.process.execute('jpackage_install -n osis -d jumpscale')

    params.result = True  # return True if result ok
    return params

def match(j, args, params, tags, tasklet):
    return True
