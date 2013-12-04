
def main(j,jp):

    j.system.fs.remove("/usr/bin/sublime_text")

    j.system.fs.symlink(path="/opt/sublimetext/sublime_text", target="/usr/bin/sublime_text", overwriteTarget=True)
