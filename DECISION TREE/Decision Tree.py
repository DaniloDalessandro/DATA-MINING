# ARVORE DE DECISÃO
# DATA MINING

# IMPORTANDO BIBLIOTECA PANDAS
import pandas as pd
# IMPORTANDO BIBLIOTECA P/ PLOTAGEM DE GRAFICOS
import matplotlib.pyplot as plt
# IMPORTANDO BIBLIOTECA P/ TRABALHAR COM ARVORES
from sklearn.tree import DecisionTreeClassifier

# FUNÇÃO P/ PLOTAGEM DE GRAFICOS
def graf(dataset):
    dataset['CLASSE'].value_counts().plot(kind='pie')
    plt.axis('equal')
    plt.title('DISTRIBUIÇÃO DE DADOS PELO DATASET')
    plt.show()

# FUNÇÃO PARA INFORMAR TAMANHO DO DATASET
def tam(dataset):
    print("LINHAS: {}, COLUNAS: {}".format(len(dataset), len(dataset.columns)))

# FUNÇÃO PARA INFORMAR RESULTADO DAS INFORMAÇÕES
def arvoreresul ():
    resul = classifier_dt.predict([ex1])
    print(resul)

# NOME DAS FLORES
names = ['SEPAL(COMPRIMENTO)', 'SEPAL(LARGURA)',
         'PETALA(COMPRIMENTO)', 'PETALA(LARGURA)',
         'CLASSE']

#IMPORTANDO O DATASET
dataset = pd.read_csv('/home/kyra/Downloads/Texto.csv', names=names)


# CRIANDO AS CARACTERISTICAS
dataset['SepalArea'] = dataset['SEPAL(COMPRIMENTO)'] * dataset['SEPAL(LARGURA)']
dataset['PetalArea'] = dataset['PETALA(COMPRIMENTO)'] * dataset['PETALA(LARGURA)']

dataset['SepalLengthAboveMean'] = dataset['SEPAL(COMPRIMENTO)'] > dataset['SEPAL(COMPRIMENTO)'].mean()
dataset['SepalWidthAboveMean'] = dataset['SEPAL(LARGURA)'] > dataset['SEPAL(LARGURA)'].mean()

dataset['PetalLengthAboveMean'] = dataset['PETALA(COMPRIMENTO)'] > dataset['PETALA(COMPRIMENTO)'].mean()
dataset['PetalWidthAboveMean'] = dataset['PETALA(LARGURA)'] > dataset['PETALA(LARGURA)'].mean()

# PREPARAÇÃO DE DADOS
caracte = dataset.columns.difference(['CLASSE'])

X = dataset[caracte].values
y = dataset['CLASSE'].values

# CLASSIFICANDO NA ARVORE
classifier_dt = DecisionTreeClassifier(random_state=1986, criterion='entropy', max_depth=3)
classifier_dt.fit(X, y)

# TESTES DE FUNCIONAMENTO
ex1 = [1.0, 2.0, 3.5, 1.0, 10.0, 3.5, False, False, False, False]  # P/ Iris-setosa
ex2 = [5.0, 3.5, 1.3, 0.2, 17.8, 0.2, False, True, False, False]   # P/ Iris-versicolor
ex3 = [7.9, 8.0, 2.0, 1.8, 19.7, 9.1, True, False, True, True]     # P/ Iris-virginica

print('============= ARVORE DE DECISÃO ==============')
print('PARA RESULTADO DA ARVORE DIGITE 1.')
print('PARA GRAFICO DO DATASET DIGITE 2.')
print('PARA TAMANHO DO DATASET DIGITE 3.')
op = int(input())

if op == 1:
    arvoreresul()
elif op == 2:
    graf(dataset)
elif op ==3:
    tam(dataset)





