def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    toCopy = ('arakoonStart.py', 'osisServerStart.py', 'tests', 'osisClient.py', '_templates', 'logic/_arakoonmodelobjects', 'logic/_coreobjects', 'logic/_modelobjects', 'logic/logger', 'logic/_blob')
    for component in toCopy:
        recipe.add(repo,"apps/osis/%s" % component, "apps/osis/%s" % component)  #when outside of sandbox use e.g. /qbase3/... (start with / )

    #when type == config then dir will be copied not linked even in debug mode
    recipe.add(repo,"apps/osis/cfg" , "apps/osis/cfg",type="config" ) 

    params.result = recipe  # remember for further usage


    return params


def match(j, args, params, tags, tasklet):
    return True
