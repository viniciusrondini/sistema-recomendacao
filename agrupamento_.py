# -*- coding: utf-8 -*-
"""agrupamento .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RHowx7LpC4YPw8-d_Ldjjqt_ILVWIvU5
"""

#biblioteca
import numpy as np
from sklearn.cluster import KMeans

caminho_arquivo = '/content/filmes_100_usuarios.csv'
df = pd.read_csv(caminho_arquivo)
print(df.head())

#matriz com filmes assistidos
filmes_assistidos = df.drop(columns=["Unnamed: 0"]).values

#definindo o numero de clusters (grupos)
num_cluster = 2

#inicializar modelo
kmeans = KMeans(n_clusters=num_cluster, random_state=0, n_init=10)

#treinando o modelo
kmeans.fit(filmes_assistidos)

#classificando usuarios
grupos_indice = kmeans.predict(filmes_assistidos)

#exibir os dados
print("usuario pertence ao seguinte grupo:")
for i, cluster in enumerate(grupos_indice):
  print(f"usuario {i+1} pertence ao grupo {cluster+1}")

print("/nfilmes assistidos")
for i in range(len(filmes_assistidos)):
  assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
  print(f"usuario {i+1}assistiu aos filmes: {assistidos}")

#funcao recomenda filmes
def recomendar_filmes(filmes, filmes_assistidos, grupos_indice):


  filmes = np.array(filmes)
#grupo usuario com base em seu vetor de filmes assistidos
  usuario_id = len(filmes_assistidos)
  grupo_usuario = kmeans.predict([filmes]) [0]

#encontrar todos os usuarios no mesmo grupo
  usuario_no_mesmo_grupo = [i for i in range(len(grupos_indice))if grupos_indice[i] == grupo_usuario]

#filmes assistidos pelo usuario no mesmo grupo
  filmes_recomendados = set()
  for usuario in usuario_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] ==1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

#remover filmes q o usuario ja assistiu
    filmes_recomendados = filmes_recomendados - set(np.where(filmes == 1)[0])

#ajustar os indices dos filmes recomendados (de volta para 1-based)
    filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

    return sorted(filmes_recomendados)

#exemplo funcao recomendar filmes
filmes_assistidos_usuario =  [1,0,0,1,1,1,0,0,0,1]

#assistidos ex assistiu 1 e 3
filmes_recomendados = recomendar_filmes(filmes_assistidos_usuario, filmes_assistidos, grupos_indice)


print(f"\nFilmes recomendados: {filmes_recomendados}")