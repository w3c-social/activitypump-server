# activitypump-server / minipump
Server implementation of the activitypump API

This is a MINIMAL implementation of the activitypump API.  It's
designed for readability over good production designs.  For example,
it uses an in-process-memory database.

However, it *should* be pretty easy to follow.  It uses
[flask](http://flask.pocoo.org/) for maximum simplicity.

# Install / Run

You need to install Python, version 3.3 or higher.  (2.7 works too but
we're aiming for 3.3 and up).

Set up like so:

`$ virtualenv . --python=python3.3  # or 3.4 or whatever`
`$ ./bin/python setup.py develop`

Sweet, you've now installed all dependencies.  You can run the server
like so:

`$ ./bin/python run.py`