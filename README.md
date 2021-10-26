# ML-prototype

This repo contains prototype version of the neural-network based algorithm to predict the rank of the issues, based on the currently solved issue.
It's important to know, that system will not work if the repo do not have the closed issues, open issues

## How to run 
Before installation be sure that you have installed:
1. python of version 3.6 or greater https://www.python.org/downloads/
2. git https://git-scm.com/downloads
3. pip for the python https://pip.pypa.io/en/stable/installation/

Some important notes:
1. The following steps may affect the installed python packages, so if you already have some important preinstalled packages, please create virtual environment https://docs.python.org/3/library/venv.html#creating-virtual-environments
2. The commands listed below for the linux and macos system
3. Also for the correct working you need to set up the github auth personal token, https://github.com/settings/tokens

```
 git clone git@github.com:goxan/ML-prototype.git
 cd ML-prototype
 pip install -r requirements.txt
 export G_KEY = '${PAST_HERE_YOUR_ACCESS_TOKEN}'
 python main.py ${REPO_AUTHOR}/${REPO_NAME}
 ```
 Example
 ```
 python main.py PyGithub/PyGithub
 ```
 Expected output
 ```
[('github.BranchProtection.BranchProtection missing 3 attributes', 0.7212354), ('Adding a team with permission to a repository is failing', 0.6985797), ('Provide a way to make a "raw" request', 0.6701817), ('Getting new commits sha after merging of pull request ', 0.65503913), ('From issue ID, how do I get Project > Card name?', 0.6337153), ('Feature request: Github template repo', 0.632738), ('GPG signatures for source validation', 0.6323918), ('A property to access the `assets` field of release (#1898)', 0.62886816), ('github.GithubException.UnknownObjectException: 404 {“message”: “Not Found”,', 0.62135214), ('Add a bunch of missing urllib.parse.quote calls', 0.6212146), ('Support for github apps', 0.6181993), ('Add support for merge-upstream Repository action', 0.61599404), ('Clarify `github.Commit` vs `github.GitCommit`', 0.614295), ('Way to get all the installed GitHub apps in the org', 0.61175317), ('Test recorder adds wrong string for token authorization', 0.6088931), ('how to get when a commit is pushed to a pullrequest object', 0.60818), ('Return MainClass.Github.get_installation(id)', 0.6079036), ('Store URL to the repository in GithubException', 0.605236), ('get followers of specific repository', 0.6015458), ('Add link to more examples', 0.5986642), ('Adds support to create repository from a template', 0.594998), ('Include GitHub App usage in doc/examples', 0.5945333), ('Support full GitHub app authentication', 0.5924947), ('top-level directory in tarball is different when using `get_latest_release()` than on the tags page', 0.59231365), ('OAuth access token Failure Errors are Masked', 0.59200287), ('Fix missing parameter to exceptions in GithubIntegration', 0.5919905), ('Add support to self-hosted runner to organization level', 0.5888481), ('github/MainClass: Fix GitHubException instantiation', 0.5886355), ('Update Installation object with attributes and related methods', 0.58717597), ('Support for github enterprise pre-receive-hooks', 0.58705556), ('total number of pages in paginatedList', 0.58675563), ('Bad Github App auth raises generic exception, not BadCredentialsException', 0.5858892), ('Support  application/vnd.github.VERSION.diff', 0.5849661), ('Return None for get_readme()', 0.5849167), ('Add new features to organizations.py for edit fuction', 0.58355594), ('Adding authorize credentials listing and delete in a organisation', 0.5814374), ('Handling new milestone and label events', 0.58126104), ('add ldap_dn attribute for teams, as described in https://developer.gi…', 0.5809108), ('Potential enhancement working with forks', 0.5792018), ('making PyGithub citable', 0.57819194), ("Add support for the 'visibility' attribute on the Repository object", 0.5769442), ('Question: see if an issue is linked to a project. ', 0.57625973), ('How to get the diff of a pull request?', 0.5758072), ('how to get branch protection rules/ or branch protection', 0.57470924), ('No examples or documentation around working with pull request reviews', 0.57422185), ('GET /repositories endpoint on Github iterate over paginated list is slow', 0.57255644), ('GithubIntegration with APP specific APIs', 0.5721416), ('how to disable/enable github actions on repo', 0.5704203), ('PyGithub should provide means to throttle API requests', 0.568908), ('Make datetime objects timezone-aware', 0.568256), ('Rate.reset is missing a timezone', 0.56670105), ('Sporadically Git tree creation failure due to `base_tree is not a valid tree oid`', 0.5654842), ('ContentFile: file like', 0.5647599), ('GithubIntegration: Could not deserialize key data', 0.5636343),...]
 ```
