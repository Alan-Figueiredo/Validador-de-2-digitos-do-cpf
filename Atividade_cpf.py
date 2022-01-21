cpf = '16899535009'                                    

b = 10 
maior = 0
dig1 = 0
dig2 = 0
for a in cpf[0:9]:        
    a = int(a)  
    c = a * b
    b -= 1
    maior = maior + c 
    if b < 2:
        break
cal = 11 -((maior) % 11)

if cal > 9:
    dig1 = 0
else:
    dig1 = cal

dig1 = str(dig1)

novo = cpf[0:9] + dig1

b = 11
maior2 = 0
for a in novo:        
    a = int(a)  
    c = a * b
    b -= 1
    maior2 = maior2 + c 
    if b < 2:
        break
cal = 11 -((maior2) % 11)

if cal > 9:
    dig2 = 0
else:
    dig2 = cal

dig2 = str(dig2)

novo_cpf = novo + dig2

print(novo_cpf[0:11])
if cpf == novo_cpf:   
    print('valido')
else:
    print('invalido')
