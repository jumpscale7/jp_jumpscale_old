def main(j, args, params, tags, tasklet):

    recipe = j.packages.getCodeManagementRecipe()
    repo = j.clients.bitbucket.getRepoConnection("jumpscale", "jumpscale-examples")

    recipe.add(repo, "examples", "apps/examples")
    recipe.add(repo, "prototypes", "apps/prototypes")

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
