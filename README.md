## Privvy

_Privvy is a system that synchronizes private files not tracked by Git in Git repositories using a more secure source. It makes use of git hooks and actively sets the git template directory to be used for all git repositories, but will not overwrite existing content (make a backup just in case)._

### Installing Privvy
-----
```bash
git clone https://github.com/sihrc/privvy.git
cd privvy
python setup.py develop
```

This will create ~/.git_template. The contents of `.git_template` will be copied to `.git` on `git init`. Newly cloned / created repositories will have the template directory. You must run `git init` in existing repositories again to receive the files.

### Starting to use Privvy in a Git Repository
-----
To begin using Privvy, you will first need a `.privvy` JSON config in the root of your Git project.
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

Each file that you want Privvy'd should have its own field in this JSON. The field name does not matter and will only be used for logging purposes.

| Field | Purpose |
| ------------- | ------------- |
| path  | relative filepath of the file to be Privvy'd from the root of the repository |
| source  | URI of the remote source version of the file. This does not have to exist yet |
| mapping | sub-JSON containing environment name mapping for auth required environment variables that you may have named something else in your environment|

To first setup syncing, you can push or pull the Privvy'd file. After the initial push or pull, you can setup your git hooks so that you can commit / push and fetch / rebase / merge as you see fit and the Privvy'd file will be kept up-to-date.
To do so, you only need to run `git init` after you have installed Privvy.

Run these from the root directory of your Git repository.
```bash
git init     # To enable Git Hooks
privvy-pull  # To Pull Changes
privvy-push  # To Push Changes
```

### Starting to use an already Privvy-enabled Repository
-----
1. Make sure you have Privvy installed (See above)
2. Clone the repository or pull the .privvy config changes.
3. Run git init to enable Git Hooks
4. Run privvy-pull to first retrieve the files
5. Done. Use Git as you would normally

### **Hooks Used**<br>
-----
**post-commit**<br>
On commit, determines if there are any changes to private files between the remote and local and prompts to push your changes.

**post-merge** & **post-rewrite**<br>
On pull / rebase / merge, local private files will be overwritten by the remote.
