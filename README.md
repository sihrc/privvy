## Privvy

_Privvy is a system that synchronizes private files not tracked by Git in Git repositories using a more secure source. It makes use of git hooks and actively sets the git template directory to be used for all git repositories, but will not overwrite existing content (make a backup just in case)._

### **Setup**

```bash
python setup.py develop
```

This will create ~/.git_template. The contents of `.git_template` will be copied to `.git` on `git init`. Newly cloned / created repositories will have the template directory. You must run `git init` in existing repositories again to receive the files.

### **Hooks**<br>

**post-commit**<br>
On commit, determines if there are any changes to private files between the remote and local and prompts to push your changes.

**post-merge** & **post-rewrite**<br>
On pull / rebase / merge, local private files will be overwritten by the remote.


### .privvy config example
```json
{
  "env_file": {
      "path": ".env",
      "source": "s3://my_env_files/.env",
      "mapping": {
          "AWS_ACCESS_KEY_ID": "MY_ENV_AWS_ACCESS_KEY_ID",
          "AWS_SECRET_ACCESS_KEY": "MY_ENV_AWS_SECRET_ACCESS_KEY",
      }
  }
}
```

**path**<br>
filepath relative to the `.privvy` config file

**source**<br>
URI to the remote source (only s3 supported at the moment)

**mapping**<br>
environment name mapping for auth required environment variables that you may have named something else in your environment
