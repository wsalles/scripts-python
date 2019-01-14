import os, sys, glob, time, datetime

path = 'C:\\Temp\\Instrucoes_Gaveta\\'

files = glob.glob(path + '*.*')

filename = []

ultimoArquivo = max(files, key=os.path.getmtime)

statbuf = os.stat(ultimoArquivo)

print(ultimoArquivo)
print("Modification time: {}".format(statbuf.st_mtime))
print("Modification time: %s" % statbuf.st_mtime)
r = datetime.datetime.fromtimestamp(os.path.getmtime(ultimoArquivo))
print(r)


#bash
#nomeUltimoArq = os.system("ls -tr | tail -n1")
#dataUltimoArq = os.system("ls -trl --full-time | tail -n1 | awk '{print $6" "$7}' | cut -d"." -f1")
#find /tmp/fileteste/ -type f -iname "*.txt" -delete -print >> "$tmpfile"
#find /tmp/fileteste/ -type f -iname "*.txt" -print -exec rm -f "{}" \; >> "$tmpfile"

#NOW=$(date '+%Y-%m-%d %H:%M:%S')

#alias echo='echo $NOW' >> "$tmpfile"
#echo "Lista de arquivos deletados:" >> "$tmpfile"