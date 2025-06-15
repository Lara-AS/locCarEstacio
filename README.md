## LocCarEstácio – Sistema de Controle de Frota

É um projeto acadêmico com fins didáticos. A estrutura foi pensada para representar um sistema real de forma simplificada, destacando a lógica de funcionamento e a organização dos dados.

Este projeto é um sistema local desenvolvido em Python com interface gráfica feita em Tkinter. Foi criado como uma possível solução para os problemas enfrentados pela empresa fictícia LocCarEstácio, que aluga veículos para motoristas de aplicativo como Uber.

O projeto faz parte de um trabalho da disciplina de Engenharia de Software, com foco em aplicar os conceitos de levantamento de requisitos, planejamento, modelagem e construção de software.

### Objetivo do Projeto

O objetivo é resolver os problemas enfrentados pela empresa como:

- Falta de controle sobre quem estava com o carro no momento de uma multa
- Pagamento atrasado de IPVA, seguro e licenciamento
- Inadimplência nos pagamentos semanais dos motoristas
- Ausência de registros sobre manutenções e movimentação dos veículos
O sistema busca oferecer uma organização básica e funcional desses dados de forma acessível.

### Tecnologias Utilizadas

- Python no VSCode
- Tkinter para a interface gráfica
- Arquivos '.txt' para armazenamento local dos dados

> Por ser uma interface simples, o uso dos arquivos '.txt' foi como uma solução simples apenas para simular um banco de dados. A ideia é ver como os dados seriam tratados em um sistema real, sem um banco de dados de verdade.

### Funcionalidades

- Cadastro de motoristas
- Cadastro de veículos
- Registro de movimentações (qual motorista está com qual veículo)
- Cadastro e atualização de contas do veículo (IPVA, seguro, licenciamento, etc.)
- Registro e visualização de multas, associando motorista e veículo

##Tela inicial
![Captura de tela 2025-06-14 213849](https://github.com/user-attachments/assets/3b74b218-079d-4f40-b37d-5f4ad083b53f)

## Motoristas
Cadastro e vizualização de motoristas
![Captura de tela 2025-06-14 214219](https://github.com/user-attachments/assets/be3ce8a9-6121-406b-84cb-0003b0199c89)
![Captura de tela 2025-06-14 214502](https://github.com/user-attachments/assets/57c68983-41f5-4c7d-aaff-e207810abcad)

## Veículos
Cadastro e vizualização de veículos
![Captura de tela 2025-06-14 215215](https://github.com/user-attachments/assets/83b9b900-33f1-48d3-ae72-728578d6d987)
![Captura de tela 2025-06-14 215246](https://github.com/user-attachments/assets/3f5524a1-911d-400f-858f-2f09174185f9)

## Movimentações de veículos
Contém uma opção para selecionar o motorista e o carro cadastrado e registra a movimentação de qual motorista está com qual carro.
![Captura de tela 2025-06-14 215510](https://github.com/user-attachments/assets/219c624a-c838-44c3-80d9-10a56384b1b6)
![Captura de tela 2025-06-14 215545](https://github.com/user-attachments/assets/cfcaa664-c81e-4d34-ba48-bd7ebe787f69)

## Contas da empresa
Faz o registro das contas fixas dos veículos da empresa (seguro, licenciamento etc).
![Captura de tela 2025-06-14 215853](https://github.com/user-attachments/assets/39a532f6-35d6-4a5f-8f6b-93e53a07e5b9)
![Captura de tela 2025-06-14 215910](https://github.com/user-attachments/assets/3d9d8dd1-3737-4fdd-b3d6-a93e42671c9d)

##Multas
Multas cometidas pelos motoristas cadastrados, seleciona a placa e o motorista, e escreve valor, data e local da multa.
![Captura de tela 2025-06-14 220500](https://github.com/user-attachments/assets/ac436ef7-aec5-48f8-ab83-fe71edccd936)
![Captura de tela 2025-06-14 220518](https://github.com/user-attachments/assets/ba4bff78-e737-4436-842c-21b028fd62eb)

