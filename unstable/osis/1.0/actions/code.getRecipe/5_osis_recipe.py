def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    toCopy = ('arakoonStart.py', 'osisServerStart.py', 'tests', 'cfg', 'osisClient.py', '_templates', 'logic/_arakoonmodelobjects', 'logic/_coreobjects', 'logic/_modelobjects', 'logic/logger', 'logic/_blob')
    for component in toCopy:
        recipe.add(repo,"apps/osis/%s" % component, "apps/osis/%s" % component)  #when outside of sandbox use e.g. /qbase3/... (start with / )
    params.result = recipe  # remember for further usage

    #@todo copy cfg in stead of link, do this in link tasklet

    return params


def match(j, args, params, tags, tasklet):
    return True
