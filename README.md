# Linux_files
Collection of scripts and files I use in my system that I like but don't particularly want to have to remake from scratch...

``` bash
set_prompt(){
 local ps_start="\n\[\033[1;37m\]\342\224\214"
 local ps_date="|\[\033[01;34m\]\@ \d\[\033[1;37m\]|"
 local ps_dash="\342\224\200"
 local ps_dir="|\[\033[1;34m\]\w\[\033[1;37m\]|"
 local ps_newline="\[\033[1;37m\]\n\342\224\224\342\224\200|"
 local ps_user_at_host="\[\033[01;32m\]\u@\h\[\033[1;37m\]|"
 local ps_end="\342\224\200> \[\033[0m\]"

 PS1=$ps_start$ps_date$ps_dash$ps_dir$ps_newline$ps_user_at_host$ps_end
}

set_prompt

```
Adding this to .bashrc makes your PS1 look like this:
``` bash
┌|TIME DATE|─|DIRECTORY|
└─|USER@HOSTNAME|─> 
```