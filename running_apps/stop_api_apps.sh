#!/bin/bash

PIDn="$(pgrep -f noti_app:noti_app)"
PIDi="$(pgrep -f import_app:import_app)"
if [[ -n "$PIDn" ]]
then
    PGID="$(ps --no-headers -p $PIDn -o pgid)"
    kill -SIGINT -- -${PGID// /}
fi

if [[ -n "$PIDi" ]]
then
    PGID="$(ps --no-headers -p $PIDi -o pgid)"
    kill -SIGINT -- -${PGID// /}
fi
