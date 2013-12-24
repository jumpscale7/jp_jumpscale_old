
def main(j,jp):
    j.system.platform.ubuntu.install('python-imaging')
    j.system.platform.ubuntu.install('nginx-full')
    j.system.platform.ubuntu.install('python-beaker')
    j.system.platform.ubuntu.install('python-mimeparse')
    j.system.platform.ubuntu.install('redis-server')
    j.system.platform.ubuntu.install('python-redis')
