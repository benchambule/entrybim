# entrybim

Este repositorio contem uma colecao de exercicios dados a candidatos a vaga para area de TI no banco Millennium BIM

O ficheiro exam_1.py e a solucao do segunte problema:
À partir da matriz 
[1, 2, 2, 1]
[2, 2, 2, 1]
[1, 4, 5, 7]
[1, 2, 5, 7], encontrar colunas adjacentes verticalmente ou horizontalmente com valores iguais e substituir os seus valores por 0 (zero). Os zeros devem estar nas linhas mais acima. 

De notar que o algoritmo proposto resolve o problema horizontalmente e depois verticalmente (aplicando a matriz transposta)

Então a solução seria:
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 4, 0, 0]
[0, 2, 0, 0]