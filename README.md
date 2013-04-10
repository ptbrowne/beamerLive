Greetings everyone
==================

Pandoc + Markdown + Beamer + ImageMagick + Flask + EpicEditor = BeamerLive

This is an attempt at making Beamer presentations really easy to make. All the
credit goes to the makers of the different programs/libraries I used since it
is only a mashup.

Thanks also to John Hammersley and John Lees-Miller and their [awesome website](http://writelatex.com)
for the original idea of making Latex easier to use.

In this little demo are used 5 CLI programs :

* Pandoc
* Markdown
* Latex
* ImageMagick

... 1 Latex package :

* Beamer

... 2 Python libraries :

* sh
* Flask

.. and 2 JS libraries :

* EpicEditor
* JQuery

How to use it
=============

    sudo apt-get install imagemagick pandoc texlive texlive-xetex
    sudo pip install flask sh

    git clone git@github.com/phisto/beamerLive.git
    cd beamerLive
    python server.py

And then goes to your favorite browser at localhost:8000 and start editing.
The presentation will be rendered when you stop typing for 5 seconds.
You can see the pdf version of the presentation in the directory where you
started the server as temp.pdf

TODO
====

Add uploading of images, themes etc...
