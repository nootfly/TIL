# jupyterthemes

1. `pip install jupyterthemes`

2. Select a theme

   ```sh
      # list available themes
      # onedork | grade3 | oceans16 | chesterish | monokai | solarizedl | solarizedd
      jt -l
      
      # select theme...
      jt -t chesterish
      
      # restore default theme
      # NOTE: Need to delete browser cache after running jt -r
      # If this doesn't work, try starting a new notebook session.
      jt -r
      
      # toggle toolbar ON and notebook name ON
      jt -t grade3 -T -N
   ```

## Reference

[https://github.com/dunovank/jupyter-themes](https://github.com/dunovank/jupyter-themes)