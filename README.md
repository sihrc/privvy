## Privvy

_Privvy is a system that synchronizes private files not tracked by Git in Git repositories using a more secure source. It makes use of git hooks and actively sets the git template directory to be used for all git repositories, but will not overwrite existing content (make a backup just in case)._

**Setup**

```bash
python setup.py develop
```

This will create ~/.git_template. The contents of `.git_template` will be copied to `.git` on `git init`. Newly cloned / created repositories will have the template directory. You must run `git init` in existing repositories again to receive the files.

**Hooks**<br>

_post-commit_<br>
On commit, determines if there are any changes to private files between the remote and local and prompts to push your changes.

_post-merge_ & _post-rewrite_<br>
On pull / rebase / merge, local private files will be overwritten by the remote.
