#!/bin/bash

socat -dd -T60 TCP-LISTEN:8000,reuseaddr,fork,keepalive,su=StackSmasher EXEC:/home/StackSmasher/prog,stderr
