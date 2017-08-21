#!/bin/bash

ARGS="$@"
if [ $# -eq 0 ]; then
    ARGS=/usr/sbin/init
fi

# Make sure we're not confused by old, incompletely-shutdown httpd
# context after restarting the container.  httpd won't start correctly
# if it thinks it is already running.
rm -rf /run/httpd/* /tmp/httpd*

exec ${ARGS}
