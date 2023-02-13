import requests

#Cabeçalho bonitinho
def main():
   print("############################################")
print("#################API ViaCEP#################")
print("############################################")

#Usuário digitar o CEP
cep_input = input("Digite o CEP para a consulta: ")
while len(cep_input) !=8:
   print("A quantidade de digitos inserida é inválida ")
   cep_input = input("Digite novamente o CEP para a consulta: ")

#"Format" é uma função usada para formatar, no caso, o cep
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
address_data = request.json() 
print(request.json())

#
if 'erro' not in address_data:
   print("CEP ENCONTRADO")

   print('CEP: {}'.format(address_data['cep']))
   print('Logradouro: {}'.format(address_data['logradouro']))
   print('Complemento: {}'.format(address_data['complemento']))
   print('Bairro: {}'.format(address_data['bairro']))
   print('Cidade: {}'.format(address_data['localidade']))
   print('Estado: {}'.format(address_data['uf']))

else:
   print('{}:CEP INVÁLIDO!', format(cep_input))

option = int(input("Deseja realizar uma nova busca?\n 1- sim \n 2- sair"))
if option == 1:
   main()
else:
   print("Finalizando programa...")

#nome do ambiente de nível superior do programa
if __name__ == '__main__':
   main()
