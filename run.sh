#/bin/sh
gunicorn -D -w 4 -b unix:/tmp/mnemonic.sock mnemonic.wsgi
