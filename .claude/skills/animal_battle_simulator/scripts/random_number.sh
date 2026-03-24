#!/bin/bash

num=$(od -An -N2 -tu2 < /dev/urandom | tr -d ' ')

# Limit to 1–100
num=$((num % 100 + 1))

echo $num