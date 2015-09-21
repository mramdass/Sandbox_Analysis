Minor Bug:

When creating a new user for the first time, the username
and password are collected and stored. A loop then brings
the user back to whether s/he wants to create a new user
or log in. If the new user tries to log in at this given
moment, s/he will not be able to do so. Instead the terminal
must be closed and reopened to enable the new user to log in.