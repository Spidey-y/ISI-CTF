#!/bin/sh

echo """
           .----------------.
           |                |
           |      /||\      |
           |     /_||_\     |
           | =m==========m= |
           |   /   ||   \   |
           |  /____||____\  |
           |                |
           '----------------'

  Know the limits - even on a Autobashn

"""
echo -n "$ "
read  -r -p " " CMD


case "${CMD}" in
  ("" | *[!\(\)\'\0\1\$\<\#\\]*)
    echo >&2 "characters not allowed.";;
    #echo >&2 "Invalid command, only (\$\\01<#) characters are allowed.";;
  (*)
    # printf -v cmd '%s ' sh -c "\"${CMD}\""
    eval 'sh -c' "\"${CMD}\""
esac

