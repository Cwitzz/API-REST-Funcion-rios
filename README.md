
Controle de Funcionários API
Esta é uma API REST feita em Python com o framework Flask, utilizando de integração com banco de dados, projetada para gerenciamento de funcionários.

Instalação
Clone este repositório em sua máquina local.
Certifique-se de ter o Python 3.11 instalado.
Instale as dependências do projeto.

ENDPOINTS::
/funcionarios [GET]
Retorna a lista de todos os funcionários cadastrados.

/funcionarios/{id} [GET]
Retorna os detalhes de um funcionário específico.

/funcionarios [POST]
Adiciona um novo funcionário à lista

/funcionarios/{id} [PUT]
Atualiza as informações de um funcionário específico.

/funcionarios/{id} [DELETE]
Remove um funcionário da lista.

Utilização
Para utilizar esta API, você pode enviar requisições HTTP para os endpoints listados acima. Por exemplo, para adicionar um novo funcionário, envie uma requisição POST com os dados do funcionário no corpo da requisição.

Aqui está um exemplo de como adicionar um novo funcionário usando o cURL:

CSS

curl --location --request POST 'http://localhost:5000/funcionarios' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "João da Silva",
    "cargo": "Desenvolvedor",
    "salario": 5000
}'

CONTRUBUINDO
Sinta-se à vontade para contribuir para este projeto! Você pode enviar um pull request com suas modificações, ou abrir uma nova issue se encontrar algum problema.
