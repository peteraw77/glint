# glint
Git hook to ensure commit messages adhere to best practices

### Usage

Move `commit-msg.py` to your git hooks folder as `commit-msg`

### Notes

By default, this script does some processing on a server so that
the user does not have to download the spacy modules. The source
code for this server can be found at [glint_server](https://github.com/peteraw77/glint_server).
If you are uncomfortable with this, switch to the `local_processing`
branch and follow the setup instructions there.
