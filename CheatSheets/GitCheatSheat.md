git status  #ver estado de repositorio y archivos

git add <name file> #arch para preparar para subir a repo

# Para converger una rama en el master:

1.  pushear toda la rama local a remoto
    - en rama local:
    `git push origin rama`

2.  salir de la rama:
    git checkout master

#actualizar master:
    git pull origin master

#converger rama a master:
    %% checkout to the branch you want to do the merge into,
    %% this case would be 'master'
    git switch master;
    git merge rama #local;
    git push origin master #enviar a remoto (actualizar el master remoto)

#eliminar rama:
    git branch --merged #checkear que convergiste bien
    git branch -d #borra rama local
    git push origin --delete rama #borra rama remota.

    # Para ver los commits:
    git log

# Para actualizar upstream de un fork
    `git pull <upstream_url> <branch>`

# Para hacer un checkout a rama remota
    git checkout --track <remote_branch>

# Utilizar Submodules

    git submodule add <repo>

# New Branch for Athena

> ```shell
git fetch upstream;
git checkout -b <target_release>-<topic> upstream/<parent_branch> --no-track
```
