#!/bin/bash

pigz -d -z --stdout download.zip > output1.zip

for i in {1..100}; do
    let j=i+1
    pigz -d -z --stdout "output$i.zip" > "output$j.zip"
    if [ $? -ne 0 ]; then
        exit
    fi
    echo "Decompressed $i times"
done