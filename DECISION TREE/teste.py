import pandas as pd
import matplotlib.pyplot as plt

def graf(dataset):
    dataset['Classe'].value_counts().plot(kind='pie')
    plt.axis('equal')
    plt.title('DISTRIBUIÇÃO DE DADOS PELO DATASET')
    plt.show()

names = ['Sepal(COMPRIMENTO)', 'SepalWidth',
         'PetalLength', 'PetalWidth',
         'Classe']
dataset = pd.read_csv('/home/kyra/Downloads/Texto.csv', names=names)

print("Linhas: {}, Colunas: {}".format(len(dataset), len(dataset.columns)))



graf(dataset)
