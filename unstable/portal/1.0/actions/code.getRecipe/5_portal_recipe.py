def main(j,args,params,tags,tasklet):
   
    #create codemgmt recipe
    #a codemanagement recipe is used to define where the code from the code repo needs to go to
    
    recipe=j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_portal")
    
    #recipe.add(repo, sourcePath, destinationPath, branch='')
    recipe.add(repo,"apps","apps")
    recipe.add(repo,"lib","lib")
    recipe.add(repo,"setup.py","setup.py")  
    recipe.add(repo,"MANIFEST.in","MANIFEST.in")  
    
    params.result=recipe  #remember for further usage
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
