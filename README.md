## Webscraping no Linkedin

O projeto consiste em pegar vagas (publicamente disponíveis) do Linkedin por
webscraping e gerar um mapa de calor com as vagas a partir de que estado estão
disponibilizadas. Possivelmente, serão feitas outras análises também. 

### Execução 

O projeto está sendo feito dentro de um venv. É possível rodar sem utilizá-lo,
mas isso traz o risco de atrapalhar a instalação do sistema, sobretudo em
sistemas Unix. Para criar um, rode o seguinte comando dentro da pasta depois 
de clonar o projeto:  

```bash
python -m venv .

# No Windows, possivelmente será necessário especificar o endereço do
# interpretador (ex.: `C:\Python3\python`).  
```

Em seguida, será necessário ativar o `venv` Utilize o comando correspondente 
ao seu sistema/shell:  

```bash
source ./bin/activate      # bash/zsh
source ./bin/activate.fish # fish
source ./bin/activate.csh  # csh
.\Scripts\activate.ps1     # Windows (Powershell) 
.\Scripts\activate.bat     # Windows (cmd.exe)
```

E finalmente, instale os pacotes necessários:  
```bash
pip install selenium bs4 matplotlib numpy pandas geopandas
```

### Próximos passos

- [x] Escrever o script pra pegar uma busca no linkedin
- [x] Transformar cada busca em dados armazenados (json, csv, etc)
- [x] Permitir que a vaga seja passada como parâmetro
- [x] Ampliar busca para retornar mais vagas
- [x] Escapar strings retornadas com vírgula (considerando o retorno em CSV)
- [x] Visualizar (mapa de calor)
- [ ] Alterar pra pegar várias buscas simultaneamente no csv
- [ ] Refinar mapa de calor
