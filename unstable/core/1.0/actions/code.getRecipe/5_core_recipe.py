def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_core")

    recipe.add(repo, "lib/JumpScale", "site-packages/JumpScale", systemdest="$(python.paths.local.sitepackages)", platform='generic')
    recipe.add(repo, "shellcmds", "bin", platform='generic', systemdest="$(bin.local)")

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
