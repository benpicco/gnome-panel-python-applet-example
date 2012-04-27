install:
	cp gnomeAppletExample.py	/usr/local/bin/
	cp gnomeAppletExample.server /usr/lib/bonobo/servers/

uninstall:
	rm /usr/local/bin/gnomeAppletExample.py
	rm /usr/lib/bonobo/servers/gnomeAppletExample.server
