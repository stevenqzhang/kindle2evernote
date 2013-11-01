kindle2evernote
===============

Python script to parse notes in Evernote using Kindle clippings.

Only works for windows.

Clippings with the same merged are merged



Instructions
============
Put your Kindle's `clippings.txt` in the same directory as `kindle2evernote.py`

Run `kindle2evernote.py`

A sample note should look something like this:

```
- Highlight Loc. 12-13 | Added on Saturday, September 22, 2012, 06:55 AM

independent variables are normally distributed, which is a fundamental assumption of the LDA method.

====- Highlight Loc. 2 | Added on Saturday, September 22, 2012, 06:57 AM

Linear discriminant analysis
```


Alternatives
======
[Clippingsconverter.com](http://Clippingsconverter.com) is more stable, but two reasons to use this solution instead:

1. You prefer plaintext notes in Evernote (clippingsconverter.com generates notes with tables

2. You prefer not to authorize third party apps to access your Evernote cloud data. clippingsconverter uses the Evernote cloud API to create notes directly in your account.
