#!/usr/bin/env bash

awk 'BEGIN{FS=";"} /^[0-9]/{if ($4 != "/bin/false\r") print($1)}' sample.txt