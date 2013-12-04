
def main(j,jp):
    path="/opt/jumpscale/apps/gridportal"
    if j.system.fs.isLink(path):
        j.system.fs.unlink(path)


    pass
