def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_lib")

    
    for name in j.system.fs.listDirsInDir(j.system.fs.joinPaths(repo.basedir,"JumpScale","lib"),dirNameOnly=True):
        recipe.add(repo,"JumpScale/lib/%s/"%name,"$(python.paths.local.sitepackages)/JumpScale/lib/%s/"%name)

    params.result = recipe

    return params


def match(j, args, params, tags, tasklet):
    return True
