# Webscraping no Linkedin

O projeto consiste em pegar vagas (publicamente disponíveis) do Linkedin por
webscraping e gerar um mapa de calor com as vagas a partir de que estado estão
disponibilizadas. Possivelmente, serão feitas outras análises também. 

## Instalação

O projeto está sendo feito dentro de um venv. É possível rodar sem utilizá-lo,
mas isso traz o risco de atrapalhar a instalação do sistema, sobretudo em
sistemas Unix. Para criar um, rode o seguinte comando dentro da pasta depois 
de clonar o projeto:  

```bash
python -m venv .

# No Windows, possivelmente será necessário especificar o endereço do
# interpretador (ex.: `C:\Python3\python`).  
```

Em seguida, será necessário ativar o `venv`. Utilize o comando correspondente 
ao seu sistema/shell:  

```bash
source ./bin/activate      # bash/zsh
source ./bin/activate.fish # fish
source ./bin/activate.csh  # csh
.\Scripts\activate.ps1     # Windows (Powershell) 
.\Scripts\activate.bat     # Windows (cmd.exe)
```

E finalmente, instale os pacotes necessários. Caso esteja utilizando um venv,
rode o primeiro comando, senão, instale os pacotes diretamente:  
```bash
python -m pip install -r requirements.txt
pip install selenium matplotlib numpy pandas geopandas
```

## Execução

Execute `python main.py "\<nome-da-vaga\> \[tempo_scrolling\]". Se a vaga
desejada possuir espaços (por exemplo, "engenheiro civil"), insira-a entre
aspas duplas. Não inserir uma vaga ou inserir vagas adicionais retornará um 
erro na versão atual.  

`tempo_scrolling` corresponde ao tempo que o script irá avançar o scroll 
infinito da página antes de coletar os resultados.  

## Próximos passos

- [x] Escrever o script pra pegar uma busca no linkedin
- [x] Transformar cada busca em dados armazenados (json, csv, etc)
- [x] Permitir que a vaga seja passada como parâmetro
- [x] Ampliar busca para retornar mais vagas
- [x] Escapar strings retornadas com vírgula (considerando o retorno em CSV)
- [x] Visualizar (mapa de calor)
- [x] Parametrizar tempo de scraping
- [ ] Alterar pra pegar várias buscas simultaneamente no csv
- [ ] Corrigir valores inválidos no .csv
- [ ] Refinar mapa de calor (especialmente cor de resultados zero)
