def main(j,jp):
    portalinit = j.system.fs.joinPaths(j.dirs.libDir, 'portal', '__init__.py')
    if not j.system.fs.exists(portalinit):
        j.system.fs.createDir(j.system.fs.getParent(portalinit))
        myinit = """
from JumpScale import j
import JumpScale.baselib.key_value_store
import JumpScale.baselib.taskletengine
import JumpScale.baselib.specparser

import codegentools
"""
        j.system.fs.writeFile(portalinit, myinit)
