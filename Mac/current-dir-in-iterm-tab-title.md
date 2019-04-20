# Show Current dirctory name in iterm tab title

```shell
# put this in your .bash_profile
if [ $ITERM_SESSION_ID ]; then
  export PROMPT_COMMAND='echo -ne "\033];${PWD##*/}\007"; ':"$PROMPT_COMMAND";
fi
```


## Reference

[https://gist.github.com/phette23/5270658](https://gist.github.com/phette23/5270658)