# Curriculum Vitae

<img src="./me.JPG" alt="me" width="200"/>

## Sobre mim

Olá! Eu sou o Felipe Marques da Silva, tenho 29 anos, e moro com minha namorada e meus dois gatos em São Paulo/SP.
Embora eu tenha me formado Engenheiro Eletricista pela Universidade de São Paulo, eu trabalho como Desenvolvedor de
Software e áreas correlatas desde que me graduei. A maioria dos meus conhecimentos em Engenharia de Software foi
adquirida sendo auto-didata, e também aprendi muito com cada uma das experiências profissionais que tive. Escuto,
escrevo e leio em inglês muito bem, e tenho um pouco de dificuldade para falar.

Tenho experiência em projetar arquiteturas de software resilientes e evoluíveis, e em produzir código simples, testável,
e manutenível em Python. Tenho sólidas habilidades com orientação a objetos, princípios SOLID, versionamento de software
Git, serviços de nuvem AWS, testes unitários, APIs HTTP, e liderança técnica.

### Meus contatos

**Celular:** +55 16 99172-2315

**Email:** femarques01@gmail.com

## Educação

#### Universidade de São Paulo (2018)

Bacharel em Engenharia Elétrica com ênfase em Eletrônica, Escola de Engenharia de São Carlos.

## Experiência profissional

### **Engenheiro de software sênior** - *Itaú Unibanco* (05/2022 - hoje)

Liderei um projeto de modernização do cálculo do resultado financeiro diário de parte das operações da Tesouraria, para
acompanhamento e conferência dos operadores.

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

**Tecnologias:** *Python3, Pytest, Pandas, FastAPI, SQLServer, SOAP, HTTP, Docker, Kubernetes*

Durante o período desempenhado na empresa, fui reconhecido por alto desempenho, e também recebi um aumento 
de salário.

### **Desenvolvedor Backend** (Pleno e Sênior) - *Experian* (01/2021 - 05/2022)

Liderei um projeto para alterar a exibição das ofertas de acordo do Serasa Limpa Nome, adicionando um banner 
"Baixou R$ X" caso a oferta enquadrasse em determinadas regras de negócio.

> As principais complexidades do projeto eram: a geração on-line do banner no momento do acesso do usuário; o conteúdo
> deveria ser baseado no histórico de ofertas visualizadas de cada usuário; e a adição do banner não deveria onerar o
> carregamento da página.
>
> Criamos uma arquitetura CQRS (2 serviços) para gerar os banners e consultá-los separadamente, possibilitamos
> a configuração de testes A/B e de roll-out em tempo real da funcionalidade. Aplicamos testes de carga para dimensionar
> os serviços e criamos um dashboard para monitorar o tempo de execução da geração e consulta dos banners. Cada etapa do 
> processo emitia eventos para posteriores análises estatísticas.
>
> Como resultado, o aparato conseguiu cumprir todos os requisitos funcionais e não-funcionais utilizando 2 réplicas 
> de 0,5 vCPU e 0,5 GB RAM cada para gerar banners para um volume de 200 usuários/min, com p95 < 500ms/usuário, e 6 
> réplicas de mesmo tamanho para servir 10k consultas/min, com p95 < 200ms. Todo o projeto levou aproximadamente 5 
> meses para ser colocado em produção, sendo considerado um sucesso.

**Tecnologias:** *Python3, FastAPI, Flagr, Locust, ElasticSearch, Redis, Amazon SQS, Amazon SNS, Splunk, Kubernetes,
Docker, AWS*

Durante o período trabalhado na empresa fui promovido para nível Sênior, e depois ganhei um aumento de salário.

### **Desenvolvedor Backend** (Jr e Pleno) - *QI Tech* (11/2019 - 01/2021)

Desenvolvi um serviço para ofertar consultas SCR aos clientes, controlar as autorizações das pessoas consultadas, e 
a quantidade de consultas realizadas pelos clientes no mês para fins de cobrança.

> As complexidades do projeto eram: realizar a integração junto ao BACEN para realizar a consulta; e garantir 
> que a consulta só poderia ser realizada caso a pessoa consultada assinasse digitalmente um documento dando anuência.
> 
> O projeto envolveu: criar templates de documentos e populá-los programaticamente; realizar integrações com o serviço
> gerador de documentos, o de assinatura digital (já existentes) e com o BACEN propriamente dito, enviando requisições
> e recebendo webhooks; controlar o estado do processo todo para dar visibilidade ao cliente e para permitir uma 
> automação.
> 
> Ao final, todo o processo ficou automatizado, mais um serviço pôde ser ofertado pela QI Tech, e nossos clientes
> obtiveram os dados necessários para realizar uma boa análise de risco de crédito em seus funis.

**Tecnologias**: *Python 3, Falcon, FastAPI, GCP, Google PubSub, Google Storage, MySQL, Kubernetes, Docker* 

Durante o tempo desempenhado na empresa fui premiado por alta desempenho, e depois obtive um aumento de salário.

### **Cientista de Dados** (Estágiário e Jr) - *brain4care* (03/2018 - 11/2019)

Desenvolvimento/manutenção de:

- Sistema de aquisição e armazenamento de dados de monitores multi-paramétricos de pacientes de UTI;
- Algoritmos de processamento de sinais para os dados adquiridos (redução de ruído, identificação de pulsos,
  separação de sinais pulsáteis das tendências, etc);
- Algoritmos para clusterização e extração de features utilizando técnicas de Machine Learning;
- Análises estatísticas para produção de artigos científicos.

#### Principais realizações

- Analisei dados para um estudo de R&R para um novo sensor não-invasivo de pressão intracraniana;
- Analisei dados para um estudo conduzido pela UFSCar para identificar pacientes diabéticos utilizando o sensor de
  pressão intracraniâna não-invasivo;
- API REST para consultar os sinais dos pacientes para fins de visualização;
- Desenvolvi um algoritmo de compressão para reduzir a quantidade de dados retornados.
