from JumpScale import j
def main(jp):
    j.system.platformtype.dieIfNotPlatform("linux64")
    j.system.platform.ubuntu.updatePackageMetadata()
