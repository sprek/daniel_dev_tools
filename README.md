# daniel_dev_tools

- [emacs](#emacs)
- [git](#git)
- [tmux](#tmux)
- [bash](#bash)
- [python](#python)


## emacs

### packages
#### c++
- projectile
- helm
- helm-gtags
- helm-projectile
- helm-swoop
- ggtags

#### python
- elpy

### install emacs 2.4 on centos 6.x

[ref1](https://vitalvastness.wordpress.com/2013/07/03/installing-emacs-24-on-centos-6/comment-page-1/)

1. Download and install liblockfile: http://dl.fedoraproject.org/pub/epel/6/x86_64/liblockfile-1.08-9.el6.x86_64.rpm
2. Download pjku.repo to /etc/yum.repos.d  (the current version on the pjku site is for Linux 7 - download the pjku.repo in this git repo for Linux 6)
3. ```sudo rpm --import http://pj.freefaculty.org/EL/PaulJohnson-BinaryPackageSigningKey```
4. ```yum info emacs-nox.x86_64```   - verify that it is emacs 24
5. sudo yum install emacs-nox.x86_64

## git
### How to do passwordless github pushes:
[ref1](https://gist.github.com/rosswd/e1afd2b0b0d515517eac) [ref2](http://stackoverflow.com/questions/7927750/specify-an-ssh-key-for-git-push-for-a-given-domain)

1. Create the key:  ```ssh-keygen -t rsa -C "sprekk@gmail.com"```
2. Move the keys to ~/.ssh/keys
3. Add the public key to github: Settings -> Deploy keys -> Add deploy key
4. Add key to ssh config:
```
    Host github-daniel_dev_tools
         Host gitsprek
         User git
         HostName github.com
         IdentityFile /home/daniel/.ssh/keys/git_rsa
         IdentitiesOnly yes
```
5. ```ssh-add ~/.ssh/keys/<private key>```
6. Check that the key was added:  ```ssh-add -l```
7. Check that the repo recognizes the keys:  ```ssh -T gitsprek```
8. Setup local git to use the key:
```
    git remote add origin git@gitsprek:sprek/daniel_dev_tools.git
```

### Pretty command line git visualization
[ref1](http://stackoverflow.com/questions/1057564/pretty-git-branch-graphs)

edit ~/.gitconfig
```
[alias]
	lg1 = log --graph --abbrev-commit --decorate --date=relative --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all
	lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
	lg = !"git lg1"
```

## tmux

### plugins
- [tmux-copycat](https://github.com/tmux-plugins/tmux-copycat)
- [tmux-yank](https://github.com/tmux-plugins/tmux-yank)

**Installation:**
```
set -g @plugin 'tmux-plugins/tmux-copycat'
```
Hit prefix + I to fetch the plugin and source it

## bash

### bashrc
- Enable 256 colors in linux term
```
# enable 256 colors
if [ -n "$DISPLAY" -a "$TERM" == "xterm" ]; then
    export TERM=xterm-256color
fi
```

## python

- setup
```
virtualenv -p python3 env
source env/bin/activate
pip install -U pip
pip install -U setuptools
pip install jedi   # for emacs bindings
pip install pylint

pylint --generate-rcfile > .pylintrc
```

To get rid of the pylint warning: ```Unable to import <module>```:
edit .pylintrc:
```init-hook='import sys; sys.path.append("/path/to/project")'```

- web application
```
pip install flask
pip install Flask-Bootstrap
```

- python pdb: ```python -m pdb file.py```

