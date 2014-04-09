
#if customizations are required when doing a a linking of the jpackage code to the OS

def main(j,jp,force=True):
    path="%s/apps/agent"%j.dirs.baseDir
    j.system.fs.removeDirTree(path)
    recipe=jp.getCodeMgmtRecipe()
    recipe.link(force=force)

