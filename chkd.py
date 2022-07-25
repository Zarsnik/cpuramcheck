#!/usr/bin/python3 
from subprocess import check_output as bash_outp
from syslog import syslog as log

def human_read(num, suffix="B"):
  for unit in ["Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
    if abs(round(num)) < 1024.0:
      return f"{num:3.1f}{unit}{suffix}"
    num /= 1024.0
  return f"{num:.1f}Yi{suffix}"

while True:
  ram=int(bash_outp("vmstat 1 2 | tail -1 | awk '{printf $4}'",shell=True).decode('utf-8'))
  val=(bash_outp("vmstat 1 2 | tail -1 | awk '{printf $14}'",shell=True).decode('utf-8'))
  crit_val=float(75)
  if float(val) > crit_val:
    log(2,"["+str(val)+"%] Utilisation CRITIQUE du CPU \n ["+human_read(ram)+"] RAM libre")
    sleep(300)
