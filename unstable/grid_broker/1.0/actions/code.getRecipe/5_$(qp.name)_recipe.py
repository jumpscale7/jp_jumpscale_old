def main(j,args,params,tags,tasklet):
   
    #create codemgmt recipe
    #a codemanagement recipe is used to define where the code from the code repo needs to go to
    
    recipe=j.packages.getCodeManagementRecipe()
    
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_grid")
    
    #recipe.add(repo, sourcePath, destinationPath,type=None, branch='')  #when type="config" then this entry will not be linked when doing codelink but will be copied because is config info
    recipe.add(repo,"apps/broker","apps/broker")  #when outside of sandbox use e.g. /qbase3/... (start with / )
    recipe.add(repo,"apps/gridportal","apps/gridportal",type="config")
    recipe.add(repo,"apps/gridportal/utils/","apps/gridportal/utils")
    
    params.result=recipe  #remember for further usage
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
