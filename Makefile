install:
	cp mateAppletExample.py	/usr/local/bin/
	cp mateAppletExample.server /usr/lib/matecomponent/servers/

uninstall:
	rm /usr/local/bin/mateAppletExample.py
	rm /usr/lib/matecomponent/servers/mateAppletExample.server
