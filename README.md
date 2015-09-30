# daniel_dev_tools

# emacs packages:

## c++
- projectile
- helm
- helm-gtags
- helm-projectile
- helm-swoop
- ggtags

## python
- elpy

## How to do passwordless github pushes:
- https://gist.github.com/rosswd/e1afd2b0b0d515517eac
- http://stackoverflow.com/questions/7927750/specify-an-ssh-key-for-git-push-for-a-given-domain

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