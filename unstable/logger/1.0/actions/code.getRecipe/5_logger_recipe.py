def main(j,args,params,tags,tasklet):
   
    #create codemgmt recipe
    #a codemanagement recipe is used to define where the code from the code repo needs to go to
    
    recipe=j.packages.getCodeManagementRecipe()
    
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    
    #recipe.add(repo, sourcePath, destinationPath,type=None, branch='')  #when type="config" then this entry will not be linked when doing codelink but will be copied because is config info
    recipe.add(repo,"apps/logger","apps/logger",type="config")
    
    params.result=recipe  #remember for further usage
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
