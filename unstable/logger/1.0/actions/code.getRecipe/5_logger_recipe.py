def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    recipe.add(repo,"apps/logger","apps/logger", platform='generic')

    params.result = recipe

    return params


def match(j, args, params, tags, tasklet):
    return True
