import pandas as pd

i = 0

#username
while True:
    try:
        nm_user = input("Olá, qual o seu nome?\n")
        
    except ValueError:
        print("Desculpe, pode repetir? (Apenas texto!)\n")
        continue
        
    if nm_user.isalpha() == True:
        break
        
    else:
        print("Desculpe, pode repetir? (Apenas texto!)\n")
        continue
        

#age check
while True:
    try:
        idade = input("Você é maior de Idade?(s/n)\n")
        
    except ValueError:
        print("Desculpe, proibido o consumo para menores de 18 anos!\n")
        continue
        
    if idade == "s":
        break
        
    else:
        print("Desculpe, proibido o consumo para menores de 18 anos!\n")
        continue

print("Bem vindo(a)", nm_user,"!\n")


#getting the csv file data with pandas
df = pd.read_csv('cervejas_ambev.csv',encoding='ISO-8859-1')

while True:
    try:
        nm_cerveja = input("Gostaria de saber mais sobre a sua cerveja favorita? Digite o nome dela:\n")
        cervejas_filtro = df[df['nome_comp'].str.contains(nm_cerveja, na = False)]
        n_linhas = cervejas_filtro.shape[0]
        
    except ValueError:
        print("Desculpe, não achamos o item.")
        del cervejas_filtro
        continue
        
    if n_linhas == 1:
        print('\n')
        print(cervejas_filtro.iloc[0]['nome_comp'],"\n")
        print(cervejas_filtro.iloc[0]['tipo'],"\n")
        print('\n')
        print("Teor alcoólico: ", cervejas_filtro.iloc[0]['%teor_alc'],"%\n")
        print("IBU: ", cervejas_filtro.iloc[0]['IBU_amargor'],"\n")
        print("Ingredientes:", cervejas_filtro.iloc[0]['ingredientes'],"\n")
        print('\n')
        print(cervejas_filtro.iloc[0]['descr'],"\n")
        break
        
    elif n_linhas == 0:
        print('\n')
        print("Desculpe, não achamos o item.")
        del cervejas_filtro
        continue
        
    elif n_linhas > 1:
        print('\n')
        print("Por favor seja mais específico, qual desses itens você escolheu?")
        print('\n')
        while i < n_linhas:
            print(cervejas_filtro.iloc[i]['nome_comp'])
            i = i + 1
            print('\n')

