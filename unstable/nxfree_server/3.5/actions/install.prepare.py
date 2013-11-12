from JumpScale import j
def main(jp):
    path = jp.getPathFilesPlatform('linux64')

    packages = ('nxclient_3.5.0-7_amd64.deb',
                'nxnode_3.5.0-9_amd64.deb',
                'nxserver_3.5.0-11_amd64.deb')

    for package in packages:
        j.system.platform.ubuntu.installDebFile(j.system.fs.joinPaths(path, package))

    # params.jpackages.copyFiles(destination="/opt/qbase3") #  will copy files to sandbox qbase3
    te = j.codetools.getTextFileEditor("/usr/NX/etc/server.cfg")
    te.replace1Line("EnableAdministratorLogin = \"1\"", ["EnableAdministratorLogin*"])
    te.save()

    j.system.installtools.execute("/etc/init.d/nxserver restart")
