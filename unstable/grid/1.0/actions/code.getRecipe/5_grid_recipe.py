def main(j, args, params, tags, tasklet):

    # create codemgmt recipe
    # a codemanagement recipe is used to define where the code from the code repo needs to go to

    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    recipe.add(repo, "lib/JumpScale/grid", "site-packages/JumpScale/grid", systemdest="$(python.paths.local.sitepackages)/JumpScale/grid", platform='generic')

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
