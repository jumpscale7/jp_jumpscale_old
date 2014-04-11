
def main(j,jp):
    j.system.fs.removeDirTree("/usr/local/lib/python2.7/site-packages/JumpScale/portal/")

    j.system.platform.ubuntu.install('python-imaging')
    j.system.platform.ubuntu.install('nginx-full')
    j.system.platform.ubuntu.install('python-beaker')
    j.system.platform.ubuntu.install('python-mimeparse')
    j.system.platform.ubuntu.install('graphviz')
