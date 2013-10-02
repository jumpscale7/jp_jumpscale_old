def main(j,args,params,tags,tasklet):
   
    #link info into local repo

    qp=args.qp

    recipe=qp.actions.code_getRecipe()

    recipe.link()
    cwd = recipe.items[0].coderepoConnection.basedir
    j.system.process.run("python setup.py develop", cwd=cwd)
    #this is the standard used function, can overrule to do custom work
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    return True
