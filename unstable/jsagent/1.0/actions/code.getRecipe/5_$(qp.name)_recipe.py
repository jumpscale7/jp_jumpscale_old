def main(j,args,params,tags,tasklet):
   
    #create codemgmt recipe
    #a codemanagement recipe is used to define where the code from the code repo needs to go to
    
    recipe=j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("incubaid","jumpscale_grid")
    
    recipe.add(repo, "apps/agent", "apps/agent",type=None, branch='')  #when type=config then this entry will not be linked when doing codelink but will be copied because is config info
    params.result=recipe  #remember for further usage
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
