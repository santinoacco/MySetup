# instalar paquetes:
>> sudo pacman -Syu <dependency>
o
>>yaour <dependency>
ctrl+r :: busca comandos similares
ctrl+d :: mata screen
enter + ~ +. :: mata conexion ssh

# update system

>> sudo pacman -Syu
or
>> pamac update

# Alias
abrir .bashrc, escribir:
>> alias <newcomand>="comando a reemplazar" ej;
>> alias ls="ls -la"

traer archivo de cern
scp lxplus.cern.ch:~/private/ParaSanti/Output.root

- para ver path archivo
$PWD/<file>

- para agregar dir/ que contiene file a path (incluir init the terminal):
export PATH=$PATH:dir

para abrir otra ventana en screen:
ctrl+a c
para intercambiar ventanas:
ctrl+a <nro ventana>
para moverte en la terminal si estas en screen:
Ctrl+a Esc

Para instalar Deepin (tipo de escritorio):
https://linuxconfig.org/how-to-install-deepin-desktop-on-manjaro-18-linux

- buscar codigo:
    - $ which

Link dinamico:
$ln -s <path_to_file>
$unlink <path_to_file>      #quitar link, NO poner '/'

Correr programa en el fondo:
<program> &
Enumerar programas en ejecucion:
$jobs
$ps
Interrumpir proceso:
$kill %<number_process>

escribir standar error & output a log.txt:
command > log.txt 2>&1

Si durante un pacman -Syyu se colgo la compu y no instalaste el kernel.
> descargar una iso de manjaro en un pendrive.
> bootear desde ese pendrive.
> conectarse a wifi
> abrir terminal:
> $ sudo manjaro-chroot -a
> $ sudo pacman -Syyu
> $ sudo pacman -Sy linux-latest
> en grub:
    > 1. apretar 'e'
    > 2. cambiar donde diga la version de linux, por la ultima istalada.. ejemplo: 5.4 -> 5.8

Errores "no mtree":
> 

# Errores con pacman:
> pacman -Qkk

# Uninstall Orphans:
Try this when updating OS and lacking blocks.
```
pacman -Rs $(pacman -Qqdt)
```

# Security
-   Use 'chmod 600 <file>' to make a file readable by the owner only.
-   Use 'GPG' to encrypt and decrypt files.
-   Use 'ENV' variables to input them into your programs.

## GPG
It is used to encrypt and decrypt files,
you will need a private and public key,
as well as a passphrase and KeyID

-   Nice tutorial [here](https://www.howtogeek.com/427982/how-to-encrypt-and-decrypt-files-with-gpg-on-linux/)
-   [Manual](https://gnupg.org/gph/es/manual.html#INTRO)
-   Notes:
    -   the expiration is only for the public key
    - 
-   Most commands used:
    - `-r`: recipient

## Pass
-   Get gpg key:
gpg -- list-secret-keys --keyid-format LONG


## ProtonVPN - Manjaro Install (tutorial)[https://www.youtube.com/watch?v=_36XZr56dYs]
-   1. Go to protonvpn.com and download

