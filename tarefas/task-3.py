import re, nltk
from unidecode import unidecode

# nltk.download('rslp')

with open('texto-task-3.txt') as f:
    texto = f.read()

# 1. Tudo para maiusculas

# uppercase = texto.upper()
# print(uppercase)

# 2. Tudo para minusculas

# lowercase = texto.lower()
# print(lowercase)

# 3. Remover pontuacoes

# nopunct = re.sub('[\S\W]', '', texto)
# print(nopunct)

# 4. Remover acentuacao grafica

# noaccents = unidecode(texto)
# print(noaccents)

# 5. Dividir entre frases

# sentences = re.split('[\?\.!]+\s', texto)
# print(sentences)

# 6. Dividir entre paragrafos

# paragraphs = texto.readlines()
# print(paragraphs)

# 7. Remover stopwords

stopwords = "a, agora, ainda, alguém, algum, alguma, algumas, alguns, ampla, amplas, amplo, amplos, ante, antes, ao, aos, após, aquela, aquelas, aquele, aqueles, aquilo, as, até, através, cada, coisa, coisas, com, como, contra, contudo, da, daquele, daqueles, das, de, dela, delas, dele, deles, depois, dessa, dessas, desse, desses, desta, destas, deste, deste, destes, deve, devem, devendo, dever, deverá, deverão, deveria, deveriam, devia, deviam, disse, disso, disto, dito, diz, dizem, do, dos, e, é, ela, elas, ele, eles, em, enquanto, entre, era, essa, essas, esse, esses, esta, está, estamos, estão, estas, estava, estavam, estávamos, este, estes, estou, eu, fazendo, fazer, feita, feitas, feito, feitos, foi, for, foram, fosse, fossem, grande, grandes, há, isso, isto, já, la, lá, lhe, lhes, lo, mas, me, mesma, mesmas, mesmo, mesmos, meu, meus, minha, minhas, muita, muitas, muito, muitos, na, não, nas, nem, nenhum, nessa, nessas, nesta, nestas, ninguém, no, nos, nós, nossa, nossas, nosso, nossos, num, numa, nunca, o, os, ou, outra, outras, outro, outros, para, pela, pelas, pelo, pelos, pequena, pequenas, pequeno, pequenos, per, perante, pode, pude, podendo, poder, poderia, poderiam, podia, podiam, pois, por, porém, porque, posso, pouca, poucas, pouco, poucos, primeiro, primeiros, própria, próprias, próprio, próprios, quais, qual, quando, quanto, quantos, que, quem, são, se, seja, sejam, sem, sempre, sendo, será, serão, seu, seus, si, sido, só, sob, sobre, sua, suas, talvez, também, tampouco, te, tem, tendo, tenha, ter, teu, teus, ti, tido, tinha, tinham, toda, todas, todavia, todo, todos, tu, tua, tuas, tudo, última, últimas, último, últimos, um, uma, umas, uns, vendo, ver, vez, vindo, vir, vos, vós"
stopwords = stopwords.split(', ')

def prepare(input):
   tokens = input.lower()
   tokens = re.sub('[()]', '', tokens)
   tokens = re.sub('[^\s\w]+\s', ' ', tokens)
   return tokens.split()

print(texto)
print('\n')
texto_lista = prepare(texto)
tokens = [word for word in texto_lista if word not in stopwords]
print(tokens)
print('\n')

# 8. _Stemming_ - encontrar o radical das palavras

# stemmer = nltk.RSLPStemmer()
# tokens = map(stemmer.stem, tokens)
# print(list(tokens))

# 9. _Lemmatization_ formas flexionadas da mesma palavra

# 10. Achar e separar hashtags e URLs

hashtags = re.findall('https?://\S+(\.\S+)+', texto)
urls = re.findall('#\w+[\s\.\n]', texto)
# 
# print(f'HASHTAGS: {hashtags}') 
# print(f'URLS: {urls}') 

# 11. Achar e remover hashtags e URLs

# delinked = re.remove('#\w+[\s\.\n]', texto)

# 12. A forma em que os exercicios foram dispostos e a melhor? Ordem seguiria?

'''
De modo geral, sim, apesar de nem todos os exercicios fazerem 
sentido em cadeia. Os exercicios 10 e 11 poderiam ser executados antes
do stemming e lemmatization.
''' 
