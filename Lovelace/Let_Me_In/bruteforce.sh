#!/bin/bash

FILE="10-million-password-list-top-1000000.txt"

a=($(wc "$FILE"))
lines=${a[0]}
words=${a[1]}
chars=${a[2]}

while read password; do
    unrar x -p$password account.5a52b336da78.rar >/dev/null 2>/dev/null
    if [ -e flag.txt ]; then
        echo " "
        echo "Password is: $password"
        exit
    fi
    printf "\rDoing $lines"
    lines=$((lines-1))
done < "$FILE"