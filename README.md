#Slacktex

**Tiny bot for LaTeX equation rendering.**

This bot will take any message in the form of inline math e.g

```latex
$\frac{\pi}{2}$
```

and respond with an embedded gif rendered by [codecogs.com](http://www.codecogs.com/latex/eqneditor.php).

## Using Slacktex

To use Slacktex, this code needs to be hosted on your platform of choice (I run the code using `screen` on a raspberry pi I have sitting around at home). You'll also need a bot access token, which you can get by following the instructions [here](https://ucldqt.slack.com/apps/new/A0F7YS25R-bots). Make sure you pick 'slacktex' as the username. 

Once you have both, replace the contents of secret.txt with your key, run bot.py, and then invite your bot to a channel by running `/invite slacktex`.
