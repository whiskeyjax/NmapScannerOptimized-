import subprocess

#scan with nmap and saves the result in a textfile
output_file = "risultato_nmap.txt"
ip = input("inserire l'ip da scansionare: ")
subprocess.run(["nmap", "-T5", "-p-", "-oN", output_file, ip])

# reads the content of the text file

foundPorts = []
with open(output_file, 'r') as f:
    for line in f:
        if 'open' in line:
            ports = line.split('/')[0]
            foundPorts.append(ports)
            
openPorts = ""

for port in foundPorts:
    openPorts += port + ","


subprocess.run(["nmap", "-T4", "-p", openPorts, "-A", ip])

