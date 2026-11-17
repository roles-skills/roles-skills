# Profissional de engenharia de dados

> Este é um perfil de referência ilustrativo para uma organização de saúde digital genérica. Não é uma descrição de funções oficial de nenhum empregador, e as pontuações da avaliação de funções não constituem uma avaliação formal.

> Esta tradução foi feita a partir do inglês por um assistente de IA e ainda não foi revisada por um falante nativo. As citações do UK GDaD PCF (Quadro de Competências Digitais e de Dados do Governo do Reino Unido) e do ESCO mantêm-se em inglês.

**Família:** [Dados](../../#dados)  
**Faixas:** 6, 7, 8a, 8b  
**Função do UK GDaD PCF:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**Profissões ESCO:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## Resumo

Os profissionais de engenharia de dados constroem e operam os pipelines e as plataformas que levam os dados de saúde e de cuidados dos sistemas clínicos e operacionais a lugares onde podem ser analisados e usados com segurança. Projetam fluxos de dados, integram fontes que usam padrões diferentes e garantem que os dados sejam exatos, atuais, seguros e acessíveis somente às pessoas que devem vê-los.

## Em uma organização de saúde digital

- Os sistemas de origem incluem prontuários eletrônicos, sistemas de laboratório, de imagem e de farmácia, que usam padrões como HL7 versão 2, HL7 FHIR, SNOMED CT e CID.
- Os pipelines costumam transportar dados identificáveis de pacientes, por isso as pessoas engenheiras incorporam desde o início a pseudonimização, o controle de acesso e a auditoria.
- Alguns fluxos de dados apoiam o cuidado direto, como alertas ou listas de pacientes, por isso um pipeline com falha ou atrasado pode afetar pacientes e precisa de avaliação de segurança clínica.
- Os dados muitas vezes precisam ser vinculados entre ambientes de cuidado, o que depende de uma associação confiável de pacientes e de identificadores consistentes.

## Descrição da função do UK GDaD PCF (original em inglês)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## Níveis da função

| Faixa | Título | Nível do UK GDaD PCF | Categorias do serviço público | Pontos da avaliação de funções |
| --- | --- | --- | --- | --- |
| 6 | [Profissional de engenharia de dados](#faixa-6-profissional-de-engenharia-de-dados) | Data engineer | HEO/SEO | 421 |
| 7 | [Profissional de engenharia de dados sênior](#faixa-7-profissional-de-engenharia-de-dados-sênior) | Senior data engineer | SEO/G7 | 477 |
| 8a | [Profissional de engenharia de dados líder](#faixa-8a-profissional-de-engenharia-de-dados-líder) | Lead data engineer | G7 | 551 |
| 8b | [Chefia de engenharia de dados](#faixa-8b-chefia-de-engenharia-de-dados) | Head of data engineering | G7/G6 | 589 |

## Faixa 6: Profissional de engenharia de dados

**Nível do UK GDaD PCF: Data engineer**

> A data engineer delivers the designs set by more senior members of the data engineering community.
> 
> At this role level, you will:
> - implement data flows to connect operational systems, data for analytics and business intelligence (BI) systems
> - document source-to-target mappings
> - re-engineer manual data flows to enable scaling and repeatable use
> - support the build of data streaming systems
> - write ETL (extract, transform, load) scripts and code to ensure the ETL process performs optimally
> - develop business intelligence reports that can be reused
> - build accessible data for analysis

### Responsabilidades

- Construir e manter pipelines de dados dos sistemas clínicos e operacionais até a plataforma de dados, seguindo os projetos acordados.
- Mapear os dados de origem, incluindo dados clínicos codificados, para os modelos de destino e documentar os mapeamentos.
- Incorporar aos pipelines pseudonimização, validação e verificações de qualidade de dados.
- Monitorar os pipelines e corrigir falhas, priorizando os fluxos que apoiam o cuidado direto.
- Aplicar controles de acesso e registro de auditoria que atendam às regras de governança da informação.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../competências/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Noção | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../competências/#data-analysis-and-synthesis) | UK GDaD PCF | Aplicação | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../competências/#data-compliance-and-security) | UK GDaD PCF | Aplicação | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../competências/#data-development-process) | UK GDaD PCF | Aplicação | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../competências/#data-innovation) | UK GDaD PCF | Noção | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../competências/#data-integration-design) | UK GDaD PCF | Aplicação | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../competências/#data-modelling) | UK GDaD PCF | Aplicação | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../competências/#metadata-management) | UK GDaD PCF | Aplicação | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../competências/#problem-management) | UK GDaD PCF | Noção | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../competências/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Aplicação | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Aplicação | Você pode:<br>• explicar os fluxos de trabalho clínicos e de cuidados que o seu trabalho apoia<br>• usar corretamente termos comuns de saúde com colegas clínicos e de cuidados<br>• reconhecer quando uma mudança pode afetar o cuidado de pacientes e levar o assunto adiante |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Aplicação | Você pode:<br>• aplicar os princípios de proteção de dados ao seu trabalho<br>• contribuir para avaliações de impacto sobre a proteção de dados<br>• tratar corretamente pedidos de informações e registros |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Aplicação | Você pode:<br>• ler e usar recursos, perfis e APIs FHIR<br>• construir ou testar integrações simples com orientação<br>• verificar mensagens em relação a uma especificação |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Noção | Você pode:<br>• explicar a diferença entre uma terminologia clínica e uma classificação<br>• reconhecer terminologias comuns, como SNOMED CT e CID |
| [Pseudonimização e controle de divulgação](../../competências/#pseudonimização-e-controle-de-divulgação) | Esta referência | Aplicação | Você pode:<br>• trabalhar com dados pseudonimizados e aplicar verificações de divulgação antes de liberar resultados<br>• reconhecer quando dados vinculados ou detalhados podem identificar um paciente |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Noção | Você pode:<br>• explicar como os sistemas de TI em saúde podem prejudicar pacientes, por exemplo com informações erradas, ausentes ou atrasadas<br>• comunicar um possível problema de segurança clínica pelo canal adequado |

### Qualificações e experiência habituais

- Graduação em computação ou em área afim, ou experiência equivalente.
- Experiência na construção de pipelines de dados.

### Descrição da faixa

- **Conhecimentos:** Conhecimento especializado em vários procedimentos, construído por meio de formação complementar ou da experiência.
- **Autonomia:** Trabalha com independência; interpreta a política para a própria área; busca orientação em questões complexas.
- **Âmbito:** Um produto, serviço ou frente de trabalho.
- **Liderança:** Pode liderar uma equipe pequena ou orientar colegas.
- **Responsabilização:** Resultados da própria frente de trabalho e qualidade das orientações dadas.

### Avaliação de funções (ilustrativa)

| # | Fator | Nível | Pontos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicação e de relacionamento | 4 | 32 |
| 2 | Conhecimentos, formação e experiência | 6 | 156 |
| 3 | Habilidades analíticas e de julgamento | 4 | 42 |
| 4 | Habilidades de planejamento e de organização | 3 | 27 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidade pelo cuidado de pacientes e clientes | 1 | 4 |
| 7 | Responsabilidade pela política e pelo desenvolvimento de serviços | 2 | 12 |
| 8 | Responsabilidade por recursos financeiros e físicos | 1 | 5 |
| 9 | Responsabilidade por pessoas | 1 | 5 |
| 10 | Responsabilidade por recursos de informação | 5 | 34 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 4 | 32 |
| 13 | Esforço físico | 1 | 3 |
| 14 | Esforço mental | 4 | 18 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **421** (Faixa 6: 396–465) |

## Faixa 7: Profissional de engenharia de dados sênior

**Nível do UK GDaD PCF: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### Responsabilidades

- Projetar fluxos de dados e serviços de streaming que reúnam dados de muitos sistemas de saúde e de cuidados.
- Projetar processos de associação e de vinculação de pacientes e medir seu desempenho.
- Liderar o trabalho de desempenho de bancos de dados e de plataformas para que os dados estejam disponíveis quando os serviços precisarem.
- Avaliar, com as pessoas especialistas pertinentes, os riscos de segurança clínica e de governança da informação dos fluxos de dados.
- Revisar o trabalho de outras pessoas engenheiras e orientá-las.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../competências/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Aplicação | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../competências/#data-analysis-and-synthesis) | UK GDaD PCF | Aplicação | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../competências/#data-compliance-and-security) | UK GDaD PCF | Domínio | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../competências/#data-development-process) | UK GDaD PCF | Domínio | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../competências/#data-innovation) | UK GDaD PCF | Aplicação | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../competências/#data-integration-design) | UK GDaD PCF | Domínio | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../competências/#data-modelling) | UK GDaD PCF | Domínio | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../competências/#metadata-management) | UK GDaD PCF | Domínio | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../competências/#problem-management) | UK GDaD PCF | Aplicação | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../competências/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Domínio | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Aplicação | Você pode:<br>• explicar os fluxos de trabalho clínicos e de cuidados que o seu trabalho apoia<br>• usar corretamente termos comuns de saúde com colegas clínicos e de cuidados<br>• reconhecer quando uma mudança pode afetar o cuidado de pacientes e levar o assunto adiante |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Domínio | Você pode:<br>• liderar avaliações de impacto sobre a proteção de dados e acordos de compartilhamento de informações<br>• orientar as equipes sobre base legal, consentimento, confidencialidade e retenção<br>• investigar incidentes e recomendar melhorias |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Domínio | Você pode:<br>• projetar e construir integrações usando FHIR, HL7 versão 2 e padrões de mensageria<br>• escrever e perfilar recursos FHIR e guias de implementação<br>• resolver problemas complexos de mapeamento e de qualidade de dados entre sistemas |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Aplicação | Você pode:<br>• encontrar e usar os códigos certos para um item de dados ou formulário<br>• usar navegadores de terminologia e conjuntos de referência |
| [Pseudonimização e controle de divulgação](../../competências/#pseudonimização-e-controle-de-divulgação) | Esta referência | Domínio | Você pode:<br>• projetar métodos de pseudonimização e de vinculação que mantenham os identificadores separados dos dados de análise<br>• avaliar o risco de reidentificação de um conjunto de dados ou de uma publicação e escolher controles adequados<br>• orientar as equipes sobre ambientes seguros, como os ambientes de pesquisa confiáveis |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Aplicação | Você pode:<br>• participar de oficinas de identificação de perigos e contribuir para um registro de perigos<br>• seguir o processo de gestão de riscos clínicos no seu trabalho<br>• fornecer evidências para um dossiê de segurança clínica, como resultados de testes |

### Qualificações e experiência habituais

- Experiência substancial no projeto e na construção de sistemas de dados, em nível equivalente ao de mestrado.

### Descrição da faixa

- **Conhecimentos:** Conhecimento especializado muito desenvolvido, em geral em nível de mestrado ou experiência equivalente.
- **Autonomia:** Trabalha segundo a política da organização; decide como alcançar os resultados; é a pessoa especialista que os outros consultam.
- **Âmbito:** Vários produtos ou serviços, ou uma função especializada.
- **Liderança:** Lidera uma equipe ou uma área de prática profissional.
- **Responsabilização:** Entrega de um serviço ou função especializada e, se houver, do respectivo orçamento.

### Avaliação de funções (ilustrativa)

| # | Fator | Nível | Pontos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicação e de relacionamento | 4 | 32 |
| 2 | Conhecimentos, formação e experiência | 7 | 196 |
| 3 | Habilidades analíticas e de julgamento | 4 | 42 |
| 4 | Habilidades de planejamento e de organização | 3 | 27 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidade pelo cuidado de pacientes e clientes | 1 | 4 |
| 7 | Responsabilidade pela política e pelo desenvolvimento de serviços | 3 | 21 |
| 8 | Responsabilidade por recursos financeiros e físicos | 1 | 5 |
| 9 | Responsabilidade por pessoas | 2 | 12 |
| 10 | Responsabilidade por recursos de informação | 5 | 34 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 4 | 32 |
| 13 | Esforço físico | 1 | 3 |
| 14 | Esforço mental | 4 | 18 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **477** (Faixa 7: 466–539) |

## Faixa 8a: Profissional de engenharia de dados líder

**Nível do UK GDaD PCF: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### Responsabilidades

- Liderar o projeto e a operação da plataforma de dados da organização e de seus muitos fluxos de dados.
- Definir padrões de engenharia para pipelines, testes, segurança e documentação.
- Planejar a integração de dados com parceiros de saúde e de cuidados, incluindo prontuários compartilhados e serviços regionais de dados.
- Garantir que os fluxos de dados que apoiam o cuidado direto sejam resilientes e tenham dossiês de segurança clínica.
- Coordenar as equipes de engenharia de dados e chefiar profissionais de engenharia.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../competências/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Domínio | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../competências/#data-analysis-and-synthesis) | UK GDaD PCF | Domínio | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../competências/#data-compliance-and-security) | UK GDaD PCF | Especialista | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../competências/#data-development-process) | UK GDaD PCF | Especialista | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../competências/#data-innovation) | UK GDaD PCF | Domínio | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../competências/#data-integration-design) | UK GDaD PCF | Especialista | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../competências/#data-modelling) | UK GDaD PCF | Especialista | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../competências/#metadata-management) | UK GDaD PCF | Domínio | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../competências/#problem-management) | UK GDaD PCF | Domínio | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../competências/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Domínio | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Domínio | Você pode:<br>• analisar como um serviço se encaixa nas linhas de cuidado entre organizações<br>• trabalhar com profissionais clínicos, equipes de cuidados e pacientes para dar forma aos serviços digitais<br>• explicar o efeito das decisões digitais sobre o cuidado, a segurança e a carga de trabalho das equipes |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Domínio | Você pode:<br>• liderar avaliações de impacto sobre a proteção de dados e acordos de compartilhamento de informações<br>• orientar as equipes sobre base legal, consentimento, confidencialidade e retenção<br>• investigar incidentes e recomendar melhorias |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Domínio | Você pode:<br>• projetar e construir integrações usando FHIR, HL7 versão 2 e padrões de mensageria<br>• escrever e perfilar recursos FHIR e guias de implementação<br>• resolver problemas complexos de mapeamento e de qualidade de dados entre sistemas |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Aplicação | Você pode:<br>• encontrar e usar os códigos certos para um item de dados ou formulário<br>• usar navegadores de terminologia e conjuntos de referência |
| [Pseudonimização e controle de divulgação](../../competências/#pseudonimização-e-controle-de-divulgação) | Esta referência | Domínio | Você pode:<br>• projetar métodos de pseudonimização e de vinculação que mantenham os identificadores separados dos dados de análise<br>• avaliar o risco de reidentificação de um conjunto de dados ou de uma publicação e escolher controles adequados<br>• orientar as equipes sobre ambientes seguros, como os ambientes de pesquisa confiáveis |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Aplicação | Você pode:<br>• participar de oficinas de identificação de perigos e contribuir para um registro de perigos<br>• seguir o processo de gestão de riscos clínicos no seu trabalho<br>• fornecer evidências para um dossiê de segurança clínica, como resultados de testes |
| [Gestão de pessoas](../../competências/#gestão-de-pessoas) | Esta referência | Domínio | Você pode:<br>• chefiar uma equipe, definindo objetivos e conduzindo avaliações de desempenho<br>• apoiar o bem-estar e gerir a assiduidade, o desempenho e a conduta<br>• planejar o desenvolvimento e a sucessão da equipe |

### Qualificações e experiência habituais

- Ampla experiência na liderança da engenharia de dados de sistemas complexos.

### Descrição da faixa

- **Conhecimentos:** Conhecimento de especialista em uma disciplina e na sua gestão.
- **Autonomia:** Interpreta a política da organização para um serviço; define a direção da equipe.
- **Âmbito:** Uma área de serviço ou uma disciplina em toda a organização.
- **Liderança:** Gerencia uma equipe ou lidera uma disciplina sem chefia direta.
- **Responsabilização:** Uma área de serviço, sua equipe e seu orçamento.

### Avaliação de funções (ilustrativa)

| # | Fator | Nível | Pontos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicação e de relacionamento | 5 | 45 |
| 2 | Conhecimentos, formação e experiência | 7 | 196 |
| 3 | Habilidades analíticas e de julgamento | 5 | 60 |
| 4 | Habilidades de planejamento e de organização | 4 | 42 |
| 5 | Habilidades físicas | 2 | 15 |
| 6 | Responsabilidade pelo cuidado de pacientes e clientes | 1 | 4 |
| 7 | Responsabilidade pela política e pelo desenvolvimento de serviços | 4 | 32 |
| 8 | Responsabilidade por recursos financeiros e físicos | 2 | 12 |
| 9 | Responsabilidade por pessoas | 3 | 21 |
| 10 | Responsabilidade por recursos de informação | 5 | 34 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 5 | 45 |
| 13 | Esforço físico | 1 | 3 |
| 14 | Esforço mental | 4 | 18 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **551** (Faixa 8a: 540–584) |

## Faixa 8b: Chefia de engenharia de dados

**Nível do UK GDaD PCF: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### Responsabilidades

- Definir a estratégia das plataformas de dados e dos serviços de engenharia de dados da organização.
- Liderar equipes multidisciplinares que entregam serviços de dados para equipes internas e parceiros de saúde e de cuidados.
- Aconselhar a liderança sênior sobre riscos, custos e investimentos nas plataformas de dados.
- Garantir que os serviços de dados atendam aos requisitos de governança da informação, de segurança e de segurança clínica.
- Desenvolver a capacidade de engenharia de dados por meio de recrutamento, desenvolvimento e trilhas de carreira.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../competências/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Especialista | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../competências/#data-analysis-and-synthesis) | UK GDaD PCF | Domínio | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../competências/#data-compliance-and-security) | UK GDaD PCF | Especialista | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../competências/#data-development-process) | UK GDaD PCF | Especialista | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../competências/#data-innovation) | UK GDaD PCF | Especialista | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../competências/#data-integration-design) | UK GDaD PCF | Especialista | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../competências/#data-modelling) | UK GDaD PCF | Aplicação | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../competências/#metadata-management) | UK GDaD PCF | Especialista | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../competências/#problem-management) | UK GDaD PCF | Especialista | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../competências/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Especialista | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Domínio | Você pode:<br>• analisar como um serviço se encaixa nas linhas de cuidado entre organizações<br>• trabalhar com profissionais clínicos, equipes de cuidados e pacientes para dar forma aos serviços digitais<br>• explicar o efeito das decisões digitais sobre o cuidado, a segurança e a carga de trabalho das equipes |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Domínio | Você pode:<br>• liderar avaliações de impacto sobre a proteção de dados e acordos de compartilhamento de informações<br>• orientar as equipes sobre base legal, consentimento, confidencialidade e retenção<br>• investigar incidentes e recomendar melhorias |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Especialista | Você pode:<br>• definir os padrões e a estratégia de interoperabilidade da organização<br>• liderar trabalhos de padronização nacionais ou entre organizações<br>• dar garantia ao projeto de integrações críticas entre muitos sistemas |
| [Pseudonimização e controle de divulgação](../../competências/#pseudonimização-e-controle-de-divulgação) | Esta referência | Domínio | Você pode:<br>• projetar métodos de pseudonimização e de vinculação que mantenham os identificadores separados dos dados de análise<br>• avaliar o risco de reidentificação de um conjunto de dados ou de uma publicação e escolher controles adequados<br>• orientar as equipes sobre ambientes seguros, como os ambientes de pesquisa confiáveis |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Aplicação | Você pode:<br>• participar de oficinas de identificação de perigos e contribuir para um registro de perigos<br>• seguir o processo de gestão de riscos clínicos no seu trabalho<br>• fornecer evidências para um dossiê de segurança clínica, como resultados de testes |
| [Gestão de pessoas](../../competências/#gestão-de-pessoas) | Esta referência | Domínio | Você pode:<br>• chefiar uma equipe, definindo objetivos e conduzindo avaliações de desempenho<br>• apoiar o bem-estar e gerir a assiduidade, o desempenho e a conduta<br>• planejar o desenvolvimento e a sucessão da equipe |
| [Gestão orçamentária](../../competências/#gestão-orçamentária) | Esta referência | Domínio | Você pode:<br>• administrar um orçamento, fazendo previsões e explicando desvios<br>• elaborar um business case com custos e benefícios |

### Qualificações e experiência habituais

- Ampla experiência na liderança da engenharia de dados em várias equipes.

### Descrição da faixa

- **Conhecimentos:** Conhecimento de especialista em várias disciplinas ou em um serviço de grande porte.
- **Autonomia:** Molda a política e a estratégia de uma área ampla.
- **Âmbito:** Vários serviços ou equipes, ou uma disciplina em nível principal.
- **Liderança:** Gerencia gestores ou é a principal autoridade em uma disciplina.
- **Responsabilização:** Vários serviços, suas equipes e seus orçamentos.

### Avaliação de funções (ilustrativa)

| # | Fator | Nível | Pontos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicação e de relacionamento | 5 | 45 |
| 2 | Conhecimentos, formação e experiência | 7 | 196 |
| 3 | Habilidades analíticas e de julgamento | 5 | 60 |
| 4 | Habilidades de planejamento e de organização | 5 | 60 |
| 5 | Habilidades físicas | 2 | 15 |
| 6 | Responsabilidade pelo cuidado de pacientes e clientes | 1 | 4 |
| 7 | Responsabilidade pela política e pelo desenvolvimento de serviços | 4 | 32 |
| 8 | Responsabilidade por recursos financeiros e físicos | 3 | 21 |
| 9 | Responsabilidade por pessoas | 4 | 32 |
| 10 | Responsabilidade por recursos de informação | 5 | 34 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 5 | 45 |
| 13 | Esforço físico | 1 | 3 |
| 14 | Esforço mental | 4 | 18 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **589** (Faixa 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
