-   ABRIR MULTIPLES ARCHIVOS EN VENTANAS HORIZONTALES SIMULTANEAMENTE
```shell
$vim -o file1 file2 ..
```

-   SELECCIONAR COLUMNAS (Normal mode)
`$Ctrl+v`

-   VER DIFERENCIAS ENTRE VENTANAS
`:windo difft`


#====== OPERATORS =======
`c`       change
`d`       delete 
`y`       yank into register 
`~`       swape case
`gu gU`   make lowercase / Upercase
`gd`      `<you're step on a method>` go to definition
`!`       filter external program
`< >`     shift left / right
`=`       indent

#====== TEXT OBJECTS =======
`a`      'a' #as a single 
`i`      inside or inner
`w W`    word / WORD (includes non alphabetic characters)
`p`      paragraph
`b`      bracket
`t`      tag block

#====== MOTIONS ======
`]m      go to beginning of next method.
`+       down to first non-blank char of line 
`%       jump to match of next paren or bracket
 
#====== MARKS ======
# it's use to MARK relevant parts of your working flow.

m{a-z or A-Z}       sets a mark
`{mark}             go to mark
:marks              shows all marks
:delmarks {mark}    deletes mark

#====== SNIPPETS ======
<file_name>.snippets            create a file.snippets to store your snippets
:SnipMateLoadScope <file_name>  add this file to buffer so it can be read.
:SnipMateOpenSnippetFiles       list all files.snippets that is reading from

#===== Spell mistakes =====
:set spell spelllang=<lang>     <lang> = en_us or es
:set nospell                    disable
zg                              (NORMAL mode) adds word to dict
