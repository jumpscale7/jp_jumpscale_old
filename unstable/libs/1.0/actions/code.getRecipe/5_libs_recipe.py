def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_lib")

    for name in ["dataprocessors","mailrobot","numtools","objectinspector","platform","psutil","puppet","redisclient","remote","sheet"]:
        recipe.add(repo,"JumpScale/lib/%s/"%name,"$(python.paths.local.sitepackages)/%s/"%name)

    params.result = recipe

    return params


def match(j, args, params, tags, tasklet):
    return True
