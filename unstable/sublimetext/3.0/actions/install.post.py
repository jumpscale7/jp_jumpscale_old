
def main(j,jp):
    j.system.fs.removeDirTree("/opt/sublimetext")
        
    e="sh /opt/sublimetext/install.sh"
    j.system.process.execute(e)