import pandas as pd

i = 0

#username
while True:
    try:
        nm_user = input(f"Olá, qual o seu nome? ")
        
    except ValueError:
        print(f"Desculpe, pode repetir? (Apenas texto!)")
        continue
        
    if nm_user.isalpha() == True:
        break
        
    else:
        print(f"Desculpe, pode repetir? (Apenas texto!)")
        continue
        

#age check
while True:
    try:
        idade = input(f"Você é maior de Idade?(s/n) ")
        
    except ValueError:
        print(f"Desculpe, proibido o consumo para menores de 18 anos!")
        continue
        
    if idade == "s":
        break
        
    else:
        print(f"Desculpe, proibido o consumo para menores de 18 anos!")
        continue

print("Bem vindo(a)", nm_user,"!\n")


#getting the csv file data with pandas
df = pd.read_csv('cervejas_ambev.csv',encoding='ISO-8859-1')

while True:
    try:
        nm_cerveja = input(f"Gostaria de saber mais sobre a sua cerveja favorita? Digite o nome dela: ")
        cervejas_filtro = df[df['nome_comp'].str.contains(nm_cerveja, na = False)]
        n_linhas = cervejas_filtro.shape[0]
        
    except ValueError:
        print(f"Desculpe, não achamos o item.")
        del cervejas_filtro
        continue
        
    if n_linhas == 1:
        print(cervejas_filtro.iloc[0]['nome_comp'])
        print(cervejas_filtro.iloc[0]['tipo'])
        print(f"Teor alcoólico: {cervejas_filtro.iloc[0]['%teor_alc']}")
        print(f"IBU: {cervejas_filtro.iloc[0]['IBU_amargor']}")
        print(f"Ingredientes:{cervejas_filtro.iloc[0]['ingredientes']}")
        print(f"{cervejas_filtro.iloc[0]['descr']}")
        break
        
    elif n_linhas == 0:
        print(f"Desculpe, não achamos o item.")
        del cervejas_filtro
        continue
        
    elif n_linhas > 1:
        while i < n_linhas:
            print(cervejas_filtro.iloc[i]['nome_comp'])
            i = i + 1
        print(f"Por favor seja mais específico, qual desses itens você escolheu?")

