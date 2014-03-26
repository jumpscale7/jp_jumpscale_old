def main(j,jp):
   
    #copying of files is done in this step
    jp._copyfiles()
    sitepackages = j.application.config.get('python.paths.local.sitepackages')
    portalinit = j.system.fs.joinPaths(sitepackages, 'JumpScale', 'portal', '__init__.py')
    if not j.system.fs.exists(portalinit):
        myinit = """
from JumpScale import j
import JumpScale.baselib.key_value_store
import JumpScale.baselib.taskletengine
import JumpScale.baselib.specparser

import codegentools
"""
        j.system.fs.writeFile(portalinit, myinit)
