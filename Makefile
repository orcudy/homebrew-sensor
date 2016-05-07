host = 104.236.12.14
port = 8080
shared_secret = d6gz3

run:
	sudo python sensor.py $(host) $(port) $(shared_secret)

clean:
	@(( \
	(rm *~ || /bin/true) && \
	(rm *.pyc || /bin/true) \
	) 2>/dev/null)

edit:
	emacs -nw sensor.py
