import requests

def retorna_dados_cep(cep):

    url=('https://viacep.com.br/ws/{}/json/'.format(cep))
    response =requests.get(url)
    print(response.status_code)
    print(response.json())
    dados_cep=response.json()

    print (dados_cep['logradouro'])
    print(dados_cep['bairro'])


if __name__ == '__main__':
    retorna_dados_cep('29018260')
