
def main(j,jp):
    j.system.platformtype.dieIfNotPlatform("linux64")
    j.system.process.killProcessByName("sublimetext")
