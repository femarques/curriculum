# Curriculum Vitae

<img src="../me.JPG" alt="me" width="200"/>

## Sobre mim

Olá! Meu nome é Felipe Marques da Silva, tenho 29 anos, e moro com minha namorada e nossos dois gatos em São Paulo/SP.
Embora tenha me formado Engenheiro Eletricista, eu trabalho como Desenvolvedor de Software e áreas correlatas desde
que me graduei. A maioria dos meus conhecimentos em Engenharia de Software foi adquirida sendo auto-didata, e também
aprendi muito com cada uma das experiências profissionais que tive. Escuto, escrevo e leio em inglês muito bem, e tenho
um pouco de dificuldade para falar.

Tenho experiência em projetar arquiteturas de software resilientes e evoluíveis, e em produzir códigos simples,
testáveis, e manuteníveis em Python. Tenho sólidas habilidades com liderança técnica, orientação a objetos, princípios
SOLID, versionamento de software Git, Clean Code, serviços de nuvem AWS, testes unitários e de integração, APIs HTTP.

### Meus contatos

**Celular:** +55 16 99172-2315

**Email:** femarques01@gmail.com

## Educação

#### Capacitação em Arquitetura de Software (2021)

Programa de formação de Arquitetos de Software promovido pela Experian, com aulas ministradas pelo Elemar Jr.

#### Universidade de São Paulo (2018)

Bacharel em Engenharia Elétrica com ênfase em Eletrônica, Escola de Engenharia de São Carlos.

## Experiência profissional

### **Engenheiro de software sênior** - *Itaú Unibanco* (05/2022 - hoje)

Fui líder técnico de um projeto de modernização do cálculo do resultado financeiro diário de parte das operações da
Tesouraria, para acompanhamento e conferência dos operadores.

> Anteriormente, este processo era feito por um conjunto de planilhas Excel e seus principais problemas eram a falta
> de robustez, a lentidão para executar o processo (+5h/dia), a dependência de pessoas para executá-lo e a limitação de
> recursos tecnológicos para lidar com o grande volume de dados.
>
> O processo foi dividido em +50 rotinas, que poderiam ser acionadas dinamicamente por endpoints HTTP expostos em um
> SwaggerUI. Projetamos uma API monolítica, orientada a casos de uso e dividida em camadas, atingindo 85% de cobertura
> de testes unitários, com baixíssima manutenção e suporte ao usuário no dia-a-dia.
>
> Ao final do projeto as rotinas diárias eram executadas automaticamente em menos de 1h (-80%) com enorme
> confiança e robustez devido à extensa cobertura de testes. Os relatórios eram consumidos pelo Excel, proporcionado
> alta adesão do usuário e eliminando a necessidade da criação de um front-end.

**Tecnologias:** *Python3, Pytest, Pandas, FastAPI, SQLServer, SOAP, HTTP, Docker, Kubernetes, AWS*

Durante o período de atuação na empresa, fui reconhecido por alto desempenho, e também recebi um aumento salarial.

### **Desenvolvedor Backend** (Pleno e Sênior) - *Experian* (01/2021 - 05/2022)

Fui líder técnico de um projeto para alterar a exibição das ofertas de acordo do Serasa Limpa Nome, adicionando um
banner "Baixou R$ X" caso a oferta se enquadrasse em determinadas regras de negócio.

> As principais complexidades do projeto eram: o alto volume de requisições (10k-40k reqs/min); e a adição do banner
> não deveria onerar o carregamento da página de ofertas de acordo.
>
> Criamos uma arquitetura CQRS (2 serviços) para gerar os banners e consultá-los separadamente, possibilitamos
> a configuração de testes A/B e de roll-out em tempo real da funcionalidade. Aplicamos testes de carga para dimensionar
> os serviços e criamos um dashboard para monitorar o tempo de execução da geração e consulta dos banners. Cada etapa do
> processo emitia eventos para posteriores análises estatísticas.
>
> Como resultado, o aparato conseguiu cumprir todos os requisitos funcionais e não-funcionais utilizando poucos recursos
> computacionais, garantindo uma experiência do usuário fluida. Todo o projeto levou aproximadamente 5 meses para ser
> colocado em produção, sendo considerado um sucesso.

**Tecnologias:** *Python3, FastAPI, Flagr, Locust, ElasticSearch, Redis, Amazon SQS, Amazon SNS, Splunk, Kubernetes,
Docker, AWS*

Durante o período trabalhado na empresa fui promovido para nível Sênior, e também recebi um aumento salarial.

### **Desenvolvedor Backend** (Jr e Pleno) - *QI Tech* (11/2019 - 01/2021)

Desenvolvi um serviço para ofertar consultas SCR aos clientes da empresa, controlar as autorizações das pessoas
consultadas, e a quantidade de consultas realizadas pelos clientes no mês para fins de cobrança.

> As complexidades do projeto eram: realizar a integração junto ao BACEN para fazer a consulta; e garantir
> que a consulta só poderia ser realizada caso a pessoa consultada assinasse digitalmente um documento dando anuência.
>
> O projeto envolveu: criar templates HTML de documentos e populá-los programaticamente; realizar integrações com o
> serviço gerador de documentos, o de assinatura digital e com o BACEN propriamente dito, enviando requisições e
> recebendo webhooks; controlar o estado do processo todo para dar visibilidade ao cliente e para permitir uma
> automação.
>
> Ao final, todo o processo ficou automatizado, mais um serviço pôde ser ofertado pela QI Tech, e nossos clientes
> obtiveram os dados necessários para realizar uma boa análise de risco de crédito em seus funis.

**Tecnologias**: *Python 3, Falcon, FastAPI, GCP, Google PubSub, Google Storage, MySQL, Kubernetes, Docker*

Durante o tempo trabalhado na empresa fui reconhecido por alto desempenho, e depois recebi um aumento salarial.

### **Cientista de Dados** (Estágiário e Jr) - *brain4care* (03/2018 - 11/2019)

Desenvolvi diversos algoritmos para aquisição, processamento, e análise de sinais vitais de pacientes de hospitais
parceiros.

> Construí uma rede neural do tipo auto-encoder para reduzir dimensionalidade das séries temporais de pulsos de pressão
> arterial, pressão intra-craniana padrão-ouro, e pressão intra-craniana não-invasiva. Com isso pudemos extrair features
> dos sinais, clusterizá-los e até compará-los nesse espaço de menor dimensionalidade.
>
> Realizei análises estatísticas para estudos clínicos conduzidos pela empresa em parceria com diversos pesquisadores e
> hospitais, destacando-se um estudo de reprodutibilidade e repetibilidade do sensor para aprovação no FDA e um estudo
> para checar a hipótese de que os sinais provenientes do sensor não-invasivo poderiam ajudar a identificar pessoas 
> portadoras de diabetes *mellitus* tipo II.
> 
> Criei uma API REST para visualização dos sinais vitais capturados, destacando-se a criação de um algoritmo para 
> compressão (redução) dos dados, preservando as formas de onda dos sinais. 

**Tecnologias:** *Python 2, Flask, AWS, Keras, Tensorflow, Pandas, Scipy, SKLearn, Numpy*