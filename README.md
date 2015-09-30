# daniel_dev_tools

[git](#git)

## emacs packages:

### c++
- projectile
- helm
- helm-gtags
- helm-projectile
- helm-swoop
- ggtags

### python
- elpy

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