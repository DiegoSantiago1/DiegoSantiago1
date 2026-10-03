<div align="center">

<img src="assets/banner.svg" alt="Diego Santiago — Dados, Backend e Automação com IA" width="100%" />

<br/>

[![Portfólio](https://img.shields.io/badge/Portf%C3%B3lio-EA580C?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/diego-freitas-santiago)
[![E-mail](https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:freitasdiego140@gmail.com)

</div>

## Sobre mim

Sou **Analista Administrativo de Vendas** em uma concessionária Honda, em Recife, e estudo **Análise e Desenvolvimento de Sistemas** na FBV Wyden. No dia a dia lido com dados de vendas, controle de entrada e saída de veículos e conferência de informações. Estou transformando essa vivência em carreira de **Dados**: SQL, Python, Power BI e, mais adiante, Engenharia de Dados.

Minha base é o desenvolvimento web (HTML, CSS, JavaScript, Node.js, Express, TypeScript, React e Tailwind). Por isso consigo fazer o caminho inteiro: **modelar o banco, escrever a consulta, expor a API e construir o painel** em que a resposta aparece.

- 📊 **Foco:** Análise de Dados com SQL, Python (Pandas e NumPy) e Power BI
- ⚙️ **Diferencial:** Backend com Node.js, Express e TypeScript
- 🤖 **Em estudo:** automação e IA aplicada (APIs de LLM, tool calling)
- 🐳 **Infra:** Docker nos projetos, AWS em aprendizado

## Stack

<img src="assets/stack.svg" alt="Stack por área. Dados: SQL, PostgreSQL, Python, Excel, Pandas, NumPy e Power BI. Backend: Node.js, Express, TypeScript e APIs REST. Front-end: HTML, CSS, JavaScript, Tailwind CSS e React. Infra: Docker, Git, GitHub e AWS." width="100%" />

## Projeto em destaque: Painel de Vendas Honda

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

## Controle de Materiais e Cautela

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

## Customer Analytics: Varejo Online

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

## Pipeline das Bicicletas de Londres

<a href="https://diegosantiago1.github.io/london-cycle-hire-pipeline/">
  <img src="https://raw.githubusercontent.com/DiegoSantiago1/london-cycle-hire-pipeline/main/docs/img/mapa_fluxos.png" alt="Mapa dos fluxos de bicicletas às 8h em Londres: as maiores ligações saem da estação de Waterloo para a City" width="100%" />
</a>

<br/><br/>

**Dados reais e públicos** das bicicletas de Londres (TfL Santander Cycles), num pipeline em que **o dado não para de chegar**: onde as estações ficam vazias ou cheias, quando, e onde a operação deve agir primeiro.

- **Coleta ao vivo:** as cerca de 800 estações a cada 15 minutos, com o dado bruto guardado intocado e um registro de cada execução
- **Carga incremental:** 41 milhões de viagens em 148 arquivos com 6 formatos de cabeçalho, lidas pelo nome da coluna; rodar duas vezes não duplica
- **dbt:** 17 modelos e 47 testes; demanda perdida estimada por estação e hora
- **Todo dia:** o banco é recriado do zero no GitHub Actions e a página se atualiza sozinha, com a saúde do próprio pipeline

[![Abrir o projeto](https://img.shields.io/badge/%E2%96%B6%20Abrir%20o%20projeto-EA580C?style=for-the-badge)](https://diegosantiago1.github.io/london-cycle-hire-pipeline/)
[![Ver o código](https://img.shields.io/badge/Ver%20o%20c%C3%B3digo-1F2937?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DiegoSantiago1/london-cycle-hire-pipeline)
[![Ver no portfólio](https://img.shields.io/badge/Ver%20no%20portf%C3%B3lio-1F2937?style=for-the-badge&logo=googlechrome&logoColor=white)](https://diegosantiago1.github.io/Portifolio/#projetos)

## Atividade

<div align="center">
  <img src="https://streak-stats.demolab.com/?user=DiegoSantiago1&locale=pt_BR&background=0F0B0B&border=2A1E1E&stroke=2A1E1E&ring=F97316&fire=EF4444&currStreakNum=FFFFFF&sideNums=FFFFFF&currStreakLabel=FB923C&sideLabels=D1D5DB&dates=9CA3AF&border_radius=14" alt="Sequência de contribuições no GitHub" width="495" />
</div>

## Próximos projetos

- 🤖 **AI Business Analyst:** LLM consultando o banco com tool calling e limites de segurança

---

<div align="center">

Aberto a conversar sobre oportunidades em **Análise de Dados** e **Backend**.

</div>
