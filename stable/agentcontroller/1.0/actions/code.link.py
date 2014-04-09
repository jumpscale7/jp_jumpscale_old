
#if customizations are required when doing a a linking of the jpackage code to the OS

def main(j,jp,force=True):
    j.system.fs.removeDirTree("%s/apps/agentcontroller"%j.dirs.baseDir)
    recipe=jp.getCodeMgmtRecipe()
    recipe.link(force=force)

