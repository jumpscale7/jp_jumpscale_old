from JumpScale import j
def main(j,jp):
    j.system.platform.ubuntu.install('php5-cgi')
    try:
        j.system.platform.ubuntu.install('php5-json')
    except:
        pass #needed on systems where it exists on other systems this is bundled with php5
    j.system.platform.ubuntu.install('python-imaging')
    j.system.platform.ubuntu.install('nginx-full')
    j.system.platform.ubuntu.install('python-beaker')
    j.system.platform.ubuntu.install('python-mimeparse')
    j.system.platform.ubuntu.install('redis-server')
    j.system.platform.ubuntu.install('python-redis')
