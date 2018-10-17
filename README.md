# rocregrev.github.io
Website for the Rochester Reggae Revival

This website serves as a resource for the musicians involved with the event.

If you have a problem with your music being represented on my site, please don't hesitate to contact me.


steps to generate static website yourself:

install virtualenvwrapper

sudo apt-get install virtualenvwrapper

mkvirtualenv -p $(which python3) rocregrev

pip install jinja2

python generator.py
