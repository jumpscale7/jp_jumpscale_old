def main(j,args,params,tags,tasklet):
   
    #package code from codemgmt recipe

    jp=args.jp

    recipe=jp.actions.code_getRecipe()

    recipe.package(jp, "generic")
    #this is the standard used package function, can overrule to do custom work
    
    return params
    
    
def match(j,args,params,tags,tasklet):
    
    return True
