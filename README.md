<div align="center">

<img src="assets/banner.svg" alt="Diego Santiago — Dados, Backend e IA aplicada" width="100%" />

<br/>

[![Portfólio](https://img.shields.io/badge/Portf%C3%B3lio-EA580C?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/diego-freitas-santiago)
[![E-mail](https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:freitasdiego140@gmail.com)

</div>

## Sobre mim

Sou **Analista de Dados I** na Autoline Honda, em Recife, e estudo **Análise e Desenvolvimento de Sistemas** na FBV Wyden. No dia a dia trabalho com dados de vendas, controle de entrada e saída de veículos e conferência de informações, e desenvolvi o painel de vendas que hoje está em uso em concessionárias Honda de Recife. Meu foco é **Dados** (SQL, Python, Power BI, dbt) e **Engenharia de Dados** (PySpark, Delta Lake, pipelines idempotentes).

Minha base é o desenvolvimento web (HTML, CSS, JavaScript, Node.js, Express, TypeScript, React e Tailwind). Por isso consigo fazer o caminho inteiro: **modelar o banco, escrever a consulta, expor a API e construir o painel** em que a resposta aparece.

- 📊 **Dados:** SQL, Python (Pandas), Power BI e dbt
- 🏗️ **Engenharia de Dados:** PySpark, Delta Lake e Databricks; pipelines incrementais e idempotentes
- ☁️ **Nuvem:** AWS com Terraform (Lambda, S3, EventBridge, IAM, CloudWatch e OIDC), Docker e GitHub Actions
- 🤖 **IA aplicada:** LLM com tool calling, saída estruturada e avaliação de respostas
- ⚙️ **Diferencial:** Backend com Node.js, Express e TypeScript

## Stack

<img src="assets/stack.svg" alt="Stack por área. Dados: SQL, PostgreSQL, Python, Pandas, NumPy, Power BI, dbt, PySpark, Delta Lake, Excel e Databricks. IA aplicada: LLM com tool calling, saída estruturada (zod) e avaliação de IA. Backend: Node.js, Express, TypeScript e APIs REST. Front-end: React, Vite, Tailwind CSS, HTML, CSS e JavaScript. Infra: Docker, GitHub Actions, Git e GitHub, Render, pytest e node:test, AWS e Terraform." width="100%" />

## Projetos

Engenharia de dados e IA primeiro. Todos têm página com os resultados e código aberto.

### Lakehouse do Financiamento Imobiliário (EUA)

<a href="https://diegosantiago1.github.io/us-mortgage-lakehouse/">
  <img src="https://diegosantiago1.github.io/Portifolio/assets/images/us-mortgage-lakehouse.png" alt="Página do lakehouse do financiamento imobiliário dos EUA: mapa do valor do imóvel dividido pela renda por estado em 2021 e a série nacional de 2018 a 2025" width="100%" />
</a>

<br/><br/>

**Engenharia de dados com dados reais e públicos do governo dos EUA (HMDA):** 222,7 milhões de pedidos de financiamento imobiliário de 2018 a 2025, num lakehouse em **PySpark + Delta Lake**. Quem consegue financiar a casa, e quanto o próprio dado do governo muda entre as versões que ele publica.

- **Bronze → silver → gold:** carga idempotente (SHA-256 e `replaceWhere`), CHECK constraints e `RESTORE` se a contagem não bate; nenhuma linha perdida
- **Versões sem chave:** o governo publica cada ano 3 vezes e o dado não tem ID do empréstimo; comparo como multiconjuntos por hash, provado contra o `exceptAll` do Spark
- **Conferido contra o governo:** estado × resultado na API oficial e registros por banco; taxas de negativa a 0,06 p.p. do relatório do CFPB
- **Achados:** o refinanciamento caiu 98% com a alta dos juros de 2022; ~5% das linhas mudam entre versões, mas as métricas nacionais quase não
- **Catálogo e Databricks:** tabelas registradas num metastore Hive e no Unity Catalog do Databricks; o `EXPLAIN` mostra que o filtro por ano lê só a pasta do ano (14 de 109 arquivos), e o Databricks deu os mesmos números do Spark local; um Z-ORDER por estado, medido numa cópia, cortou de 14 para 2 os arquivos lidos

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/us-mortgage-lakehouse/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/us-mortgage-lakehouse)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### Pipeline das Bicicletas de Londres

<a href="https://diegosantiago1.github.io/london-cycle-hire-pipeline/">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/london-cycle-hire-pipeline/main/docs/img/mapa_fluxos.png" alt="Mapa dos fluxos de bicicletas às 8h em Londres: as maiores ligações saem da estação de Waterloo para a City" width="100%" />
</a>

<br/><br/>

**Dados reais e públicos** das bicicletas de Londres (TfL Santander Cycles), num pipeline em que **o dado não para de chegar**: onde as estações ficam vazias ou cheias, quando, e onde a operação deve agir primeiro.

- **Coleta ao vivo na AWS:** as cerca de 800 estações a cada 15 minutos, numa Lambda disparada pelo EventBridge que grava o bruto intocado no S3; infraestrutura toda em Terraform e o GitHub Actions entrando na AWS por OIDC, sem chave guardada
- **Carga incremental:** 41 milhões de viagens em 148 arquivos com 6 formatos de cabeçalho, lidas pelo nome da coluna; rodar duas vezes não duplica
- **dbt:** 17 modelos e 47 testes; demanda perdida estimada por estação e hora
- **Todo dia:** o banco é recriado do zero no GitHub Actions e a página se atualiza sozinha, com a saúde do próprio pipeline

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/london-cycle-hire-pipeline/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/london-cycle-hire-pipeline)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### AI Business Analyst

<a href="https://diegosantiago1.github.io/Portifolio/projetos/ai-business-analyst/">
  <img src="https://diegosantiago1.github.io/Portifolio/assets/images/ai-business-analyst.png" alt="Página do AI Business Analyst: o gerente pergunta em português e a IA consulta o banco e mostra a conta; 28 de 32 perguntas certas e 95% dos números conferidos no banco" width="100%" />
</a>

<br/><br/>

**IA aplicada a dados:** o gerente de uma rede de concessionárias pergunta em português e um LLM com **tool calling** consulta o PostgreSQL **só para leitura**, respondendo com números conferíveis, cada um com o SQL que o gerou (dados 100% fictícios).

- **Métricas oficiais:** a IA escolhe a métrica e a API monta SQL parametrizado; o SQL livre é só reserva
- **Segurança em 4 camadas:** o usuário da IA só tem SELECT em 7 views; ataques testados um a um
- **Avaliação:** 36 perguntas com resposta certa conhecida, incluindo pedidos hostis e injeção pelo dado
- **Números conferidos:** cada valor citado é procurado no resultado do banco; o que a IA calculou sozinha é marcado

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/Portifolio/projetos/ai-business-analyst/)
[![Pergunte à IA ao vivo](https://img.shields.io/badge/%F0%9F%92%AC%20Pergunte%20%C3%A0%20IA%20ao%20vivo-C5F03A?style=for-the-badge)](https://ai-business-analyst-f85s.onrender.com)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/ai-business-analyst)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### Clínicas-escola em dados

<a href="https://diegosantiago1.github.io/clinicas-escola-indicadores/">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/clinicas-escola-indicadores/main/site/powerbi/img/01_visao_geral.png" alt="Relatório no Power BI das clínicas-escola: faturamento, consultas realizadas, taxa de faltas e espera, com quem veio, faltou e desmarcou por mês e a taxa de faltas por clínica" width="100%" />
</a>

<br/><br/>

**Análise de dados de saúde e educação:** um ano de atendimentos de uma rede de clínicas-escola (Odontologia, Fisioterapia, Psicologia e Nutrição) em Recife, Olinda e Jaboatão, com dados fictícios. Planilhas preenchidas à mão, exportações do sistema e o tablet da recepção viram indicadores confiáveis.

- **Padronização:** 20 regras em Python (situação escrita de 15 jeitos, datas como texto, duplicatas entre exportações, prontuário em branco recuperado só quando o nome é único); cada correção registrada com arquivo, aba e linha, e provada linha a linha contra a verdade da simulação
- **Power BI:** 8 páginas (faturamento, faltas, motivos, espera na recepção, agenda e fila, alunos, qualidade), Power Query, modelo estrela e 36 medidas DAX, todas conferidas contra o Python no motor do Power BI
- **Painel animado:** faturamento, motivos de falta e espera na recepção, com filtro por unidade e um assistente de perguntas que responde com os dados
- **Looker Studio:** a mesma base, já agregada, com os campos calculados prontos
- **Achados:** 20,3% das consultas terminam em falta (16.515 horas de prática perdidas); 27,6% na segunda de manhã; quem esperou mais de 60 dias na fila falta 41% à primeira consulta; as faltas de quem pagaria custaram R$ 240 mil

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/clinicas-escola-indicadores/)
[![Ver o Power BI](https://img.shields.io/badge/Ver%20o%20Power%20BI-2B2D33?style=for-the-badge&logo=powerbi&logoColor=F2C811)](https://diegosantiago1.github.io/clinicas-escola-indicadores/powerbi/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/clinicas-escola-indicadores)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### Customer Analytics: Varejo Online

<a href="https://diegosantiago1.github.io/customer-analytics-online-retail/">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/customer-analytics-online-retail/main/docs/img/powerbi_segmentos.png" alt="Relatório no Power BI: segmentos RFM, com clientes, receita, clientes em risco e valor previsto por segmento" width="100%" />
</a>

<br/><br/>

**Dados reais e públicos** de uma loja online do Reino Unido que vende presentes e utilidades, com muitos clientes lojistas: 1 milhão de linhas de vendas em dois anos (UCI Online Retail II). Respondi as quatro perguntas de um time de CRM e **conferi cada resposta contra o que de fato aconteceu depois**.

- **Melhores clientes:** segmentação RFM em SQL. Os Campeões são 24% dos clientes e trazem 69% da receita
- **Quem está indo embora:** regra de churn testada numa data passada. 1.376 clientes em risco, com £838 mil de receita no último ano, e quase metade disso está em clientes leais que pararam
- **Retenção e valor do cliente:** coortes com window functions e CLV de 6 meses, que ganhou de um modelo ingênuo sazonal
- **Engenharia:** limpeza e análise em SQL versionado no PostgreSQL, 18 checagens de qualidade, 280 testes e Power BI com cada número conferido contra o SQL

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/customer-analytics-online-retail/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/customer-analytics-online-retail)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### Controle de Materiais e Cautela

<a href="https://github.com/DiegoSantiago1/controle-materiais-cautela">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/controle-materiais-cautela/main/docs/img/app_inicio.png" alt="Sistema de controle de material: ações de balcão, posses vencidas e últimas movimentações" width="49%" />
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/controle-materiais-cautela/main/docs/img/powerbi_estoque.png" alt="Relatório no Power BI: estoque agora, com a situação de cada material" width="49%" />
</a>

<br/><br/>

Projeto **real**: desenvolvi o **sistema de controle de cautelas** da seção de material em que trabalhei na **Força Aérea**, que segue em uso, e os relatórios de estoque apresentados nas reuniões com os superiores. O repositório é a versão reconstruída para portfólio, com dados 100% fictícios e sem nenhuma informação da organização.

- **Banco:** PostgreSQL com as regras de negócio em funções, histórico de movimentações imutável e concorrência tratada (`FOR UPDATE SKIP LOCKED`)
- **Análises:** conferência de planilha, atrasos, ociosidade e ruptura de estoque, em SQL (CTEs, window functions) e Python (Pandas)
- **Power BI:** dois relatórios em modelo estrela, versionados como código (PBIP), com cada número conferido contra o SQL
- **Sistema web:** retirada, devolução, posse e estoque, com perfis de acesso, auditoria e 700+ testes automatizados

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/Portifolio/projetos/controle-materiais/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/controle-materiais-cautela)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

### Painel de Vendas Honda

<a href="https://diegosantiago1.github.io/Portifolio/projetos/painel-vendas/">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/analise-vendas-concessionaria/main/docs/screenshots/painel.png" alt="Painel de vendas com metas por loja, ranking de vendedores e calendário de vendas" width="100%" />
</a>

<br/><br/>

Projeto **real, pedido no meu trabalho e em uso em algumas concessionárias Honda de Recife**. O repositório é a versão reconstruída para portfólio, com dados 100% fictícios e sem nenhuma informação da empresa.

<img src="assets/pipeline.svg" alt="Fluxo: Python gera os dados, PostgreSQL em Docker armazena, API REST em Express expõe e o painel em Chart.js exibe" width="100%" />

- **Banco:** modelagem relacional no PostgreSQL, com chaves, views e índices, e agregações escritas em SQL, sem ORM
- **API:** REST em Node.js, Express e TypeScript, com validação e tratamento central de erros
- **Painel:** filtro por loja, metas, ranking de vendedores, mix de modelos e calendário de vendas
- **Detalhes que importam:** fuso horário tratado no banco e gerente derivado do vendedor, para evitar erro de cadastro

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/Portifolio/projetos/painel-vendas/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/analise-vendas-concessionaria)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

## Atividade

<div align="center">
  <img src="https://streak-stats.demolab.com/?user=DiegoSantiago1&locale=pt_BR&background=0A0B0E&border=2A2620&stroke=2A2620&ring=F59E0B&fire=EA580C&currStreakNum=FFFFFF&sideNums=FFFFFF&currStreakLabel=FBBF24&sideLabels=E7E5E4&dates=A8A29E&border_radius=14" alt="Sequência de contribuições no GitHub" width="495" />
</div>

---

<div align="center">

Aberto a conversar sobre oportunidades em **Análise de Dados**, **Engenharia de Dados** e **Backend**.

</div>
