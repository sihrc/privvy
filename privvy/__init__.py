import os, shutil
from subprocess import Popen

from .sync import sync

ROOT = os.path.join(os.path.dirname(__file__), "..")

def setup():
    git_template_path = os.path.join(os.path.expanduser("~"), ".git_template", "hooks")

    print("Creating global git templates directory in: {path}".format(
        path=git_template_path
    ))

    if not os.path.exists(git_template_path):
        os.makedirs(git_template_path)

    defaults = os.path.join(ROOT, "hooks")
    for script in os.listdir(defaults):
        shutil.copy2(
            os.path.join(defaults, script),
            os.path.join(git_template_path, script)
        )

    print("Setting ~/.git_template as default global template directory")
    Popen("git config --global init.templatedir '~/.git_template'", shell=True)

    print("Copying bin files to /usr/bin")
    shutil.copy2(os.path.join(ROOT, "bin", "privvy-pull"), "/usr/bin/privvy-pull")
    shutil.copy2(os.path.join(ROOT, "bin", "privvy-push"), "/usr/bin/privvy-push")
