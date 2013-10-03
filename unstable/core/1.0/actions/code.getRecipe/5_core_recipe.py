def main(j, args, params, tags, tasklet):
    recipe = j.packages.getCodeManagementRecipe()
    repo=j.clients.bitbucket.getRepoConnection("jumpscale","jumpscale_core")

    for part in ('base', 'baselib', 'core', '__init__.py'):
        recipe.add(repo, "lib/JumpScale/%s" % part, "site-packages/JumpScale/%s" % part, systemdest="$(python.paths.local.sitepackages)/JumpScale/%s" % part, platform='generic')
    for binscript in j.system.fs.listFilesInDir(j.system.fs.joinPaths(repo.basedir, 'shellcmds')):
        binscript = j.system.fs.getBaseName(binscript)
        recipe.add(repo, "shellcmds/%s" % binscript, "bin/%s" % binscript, platform='generic', systemdest="$(bin.local)/%s" % binscript)

    params.result = recipe  # remember for further usage

    return params


def match(j, args, params, tags, tasklet):
    return True
