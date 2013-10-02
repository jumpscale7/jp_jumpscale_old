def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_core")

    recipe.add(repo, "lib/JumpScale", "$(python.paths.local.sitepackages)/JumpScale")
    recipe.add(repo, "shellcmds", "$(bin.local)")

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
