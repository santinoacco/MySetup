git status  #ver estado de repositorio y archivos

git add <name file> #arch para preparar para subir a repo

# Para converger una rama en el master:

# pushear toda la rama local a remoto
#-> en rama local:
git push origin rama

#salir de la rama:
git checkout master

#actualizar master:
git pull origin master

#converger rama a master:
git merge rama #local
git push origin master #enviar a remoto (actualizar el master remoto)

#eliminar rama:
git branch --merged #checkear que convergiste bien
git branch -d #borra rama local
git push origin --delete rama #borra rama remota.

# Para ver los commits:
git log

# Para actualizar upstream de un fork
git pull <upstream_url> <branch>
