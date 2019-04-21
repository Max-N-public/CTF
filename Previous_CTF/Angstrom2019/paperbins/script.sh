#!/bin/bash
FILES=/mnt/c/Users/^Water_Bear/Desktop/angstrom/paperbins/*
for f in $FILES
do
  # take action on each file. $f store current file name
  strings $f | grep "a c t"
done