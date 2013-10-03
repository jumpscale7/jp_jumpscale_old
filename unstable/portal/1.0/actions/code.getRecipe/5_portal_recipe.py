def main(j,args,params,tags,tasklet):
   
    #create codemgmt recipe
    #a codemanagement recipe is used to define where the code from the code repo needs to go to
    
    recipe=j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_portal")
    
    #recipe.add(repo, sourcePath, destinationPath, branch='')
    recipe.add(repo,"apps/portalbase","apps/portalbase", platform='generic')
    recipe.add(repo,"apps/portalftpgateway","apps/portalftpgateway", platform='generic')
    recipe.add(repo,"lib/JumpScale/portal","site-packages/JumpScale/portal", systemdest="$(python.paths.local.sitepackages)/JumpScale/portal", platform='generic')
    
    params.result=recipe  #remember for further usage
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
