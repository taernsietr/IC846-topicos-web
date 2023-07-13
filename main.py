import sys
from scrape import scrape
from heatmap import heatmap

time_to_run = 5

if len(sys.argv) == 1: 
    print("É necessário informar pelo menos uma palavra para que a busca seja feita. O script será encerrado agora.")
    sys.exit()
elif len(sys.argv) == 3 and sys.argv[2].isdigit():
    time_to_run = int(sys.argv[2])
elif len(sys.argv) > 3:
    print("Argumentos demais! O script será encerrado agora.")

arg = sys.argv[1].replace(" ","_")

print(f'Fazendo busca para {sys.argv[1]} com intervalos de {time_to_run} para cada scroll')
scrape(arg, time_to_run)
heatmap(arg)
print("Fim")
