def main(j, args, params, tags, tasklet):

    # create codemgmt recipe
    # a codemanagement recipe is used to define where the code from the code repo needs to go to

    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    for component in ('lib', 'setup.py'):
        recipe.add(repo,component,component)

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
