# SecureJournal
A Python library for encrypting a journal

To get started, clone the repo. 

There are a couple of meta-dependencies.

`python` is one of those (version 3.8.5 recommended). 
`pip` is the second meta-dependency.

On Ubuntu (Focal Fossa):
```
# sudo apt-get install python3
# sudo apt-get install python3-pip
```
Now using pip:

`pip install pygobject`

`pip install cryptography` 

That _should_ do it. 
To get started, open up mySecureJournal in your favourite text editor, and type away!

Once you are done:

`python script.py mySecureJournal`

Your journal will be safely encrypted. When you are ready to journal again, run:

`python script.py mySecureJournal`

And the script figures out the rest.

Happy journalling! :-)
