from JumpScale import j
def main(j,jp):
    j.system.platformtype.dieIfNotPlatform("linux64")
    j.system.platform.ubuntu.updatePackageMetadata()
