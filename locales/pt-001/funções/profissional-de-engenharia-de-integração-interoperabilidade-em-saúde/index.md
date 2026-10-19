# Profissional de engenharia de integração (interoperabilidade em saúde)

> Este é um perfil de referência ilustrativo para uma organização de saúde digital genérica. Não é uma descrição de funções oficial de nenhum empregador, e as pontuações da avaliação de funções não constituem uma avaliação formal.

> Esta tradução foi feita a partir do inglês por um assistente de IA e ainda não foi revisada por um falante nativo. As citações do UK GDaD PCF (Quadro de Competências Digitais e de Dados do Governo do Reino Unido) e do ESCO mantêm-se em inglês.

**Família:** [Desenvolvimento de software](../../#desenvolvimento-de-software)  
**Faixas:** 5, 6, 7, 8a  
**Função do UK GDaD PCF:** nenhuma (esta referência define a função)  
**Profissões ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Resumo

Os profissionais de engenharia de integração conectam os sistemas clínicos e de negócios da organização para que as informações de saúde e de cuidados fluam com segurança até onde são necessárias. Projetam, constroem, testam e dão suporte a interfaces, APIs e fluxos de mensagens usando padrões como o HL7 FHIR e o HL7 versão 2, mapeiam dados e códigos clínicos entre sistemas e mantêm as integrações funcionando em serviço.

## Em uma organização de saúde digital

- Uma mensagem perdida, atrasada, duplicada ou associada ao paciente errado, como o resultado de um exame ou um encaminhamento, pode causar dano direto, por isso o trabalho de integração segue o processo de gestão de riscos clínicos.
- As integrações transportam grandes volumes de informações de saúde confidenciais entre organizações, por isso cada fluxo precisa de base legal, transporte seguro e auditoria.
- Os sistemas de saúde usam muitos padrões e versões, de mensagens HL7 versão 2 a APIs HL7 FHIR e perfis IHE, muitas vezes com variações locais.
- O significado clínico deve sobreviver à jornada, por isso as pessoas engenheiras mapeiam corretamente terminologias clínicas como a SNOMED CT e associam pacientes de forma confiável.
- Muitas integrações apoiam o cuidado 24 horas por dia, por isso precisam de monitoramento, alertas e caminhos claros para resolver mensagens com falha.

## Níveis da função

| Faixa | Título | Nível do UK GDaD PCF | Categorias do serviço público | Pontos da avaliação de funções |
| --- | --- | --- | --- | --- |
| 5 | [Profissional de engenharia de integração júnior](#faixa-5-profissional-de-engenharia-de-integração-júnior) | — | — | 335 |
| 6 | [Profissional de engenharia de integração](#faixa-6-profissional-de-engenharia-de-integração) | — | — | 418 |
| 7 | [Profissional de engenharia de integração sênior](#faixa-7-profissional-de-engenharia-de-integração-sênior) | — | — | 477 |
| 8a | [Profissional de engenharia de integração líder](#faixa-8a-profissional-de-engenharia-de-integração-líder) | — | — | 551 |

## Faixa 5: Profissional de engenharia de integração júnior

Uma pessoa engenheira de integração júnior constrói, testa e dá suporte a integrações entre sistemas de saúde e de cuidados, trabalhando a partir de especificações e com a orientação de profissionais mais experientes.

### Responsabilidades

- Construir e alterar mapeamentos de mensagens, transformações e chamadas de API a partir de especificações acordadas.
- Testar as integrações em relação às especificações e a mensagens de exemplo, incluindo casos de erro e casos-limite.
- Monitorar os fluxos de mensagens, investigar mensagens com falha ou rejeitadas e resolvê-las ou escalá-las.
- Tratar os dados de saúde com segurança, seguindo as regras de governança da informação para dados reais e de teste.
- Registrar mudanças e resultados de testes para que possam servir de evidência de segurança clínica.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Systems integration](../../competências/#systems-integration) | UK GDaD PCF | Aplicação | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../competências/#programming-and-build-software-engineering) | UK GDaD PCF | Aplicação | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../competências/#testing) | UK GDaD PCF | Aplicação | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../competências/#service-support) | UK GDaD PCF | Aplicação | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../competências/#information-security) | UK GDaD PCF | Noção | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Aplicação | Você pode:<br>• ler e usar recursos, perfis e APIs FHIR<br>• construir ou testar integrações simples com orientação<br>• verificar mensagens em relação a uma especificação |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Noção | Você pode:<br>• explicar a diferença entre uma terminologia clínica e uma classificação<br>• reconhecer terminologias comuns, como SNOMED CT e CID |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Aplicação | Você pode:<br>• aplicar os princípios de proteção de dados ao seu trabalho<br>• contribuir para avaliações de impacto sobre a proteção de dados<br>• tratar corretamente pedidos de informações e registros |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Noção | Você pode:<br>• explicar como os sistemas de TI em saúde podem prejudicar pacientes, por exemplo com informações erradas, ausentes ou atrasadas<br>• comunicar um possível problema de segurança clínica pelo canal adequado |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Noção | Você pode:<br>• descrever as principais partes do sistema de saúde e de cuidados e os serviços que a organização apoia<br>• explicar por que a segurança e a confidencialidade dos pacientes importam no seu trabalho |

### Qualificações e experiência habituais

- Graduação em computação ou em área afim, programa de aprendizagem profissional concluído ou experiência equivalente.

### Descrição da faixa

- **Conhecimentos:** Conhecimento profissional ou técnico, em geral adquirido em curso de graduação ou experiência equivalente.
- **Autonomia:** Trabalha para objetivos amplos, dentro das normas profissionais; planeja o próprio trabalho.
- **Âmbito:** O próprio trabalho profissional dentro de uma equipe ou produto.
- **Liderança:** Pode orientar e conferir o trabalho de pessoal de apoio e de aprendizes.
- **Responsabilização:** Qualidade do próprio trabalho profissional.

### Avaliação de funções (ilustrativa)

| # | Fator | Nível | Pontos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicação e de relacionamento | 4 | 32 |
| 2 | Conhecimentos, formação e experiência | 5 | 120 |
| 3 | Habilidades analíticas e de julgamento | 3 | 27 |
| 4 | Habilidades de planejamento e de organização | 2 | 15 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidade pelo cuidado de pacientes e clientes | 1 | 4 |
| 7 | Responsabilidade pela política e pelo desenvolvimento de serviços | 2 | 12 |
| 8 | Responsabilidade por recursos financeiros e físicos | 1 | 5 |
| 9 | Responsabilidade por pessoas | 1 | 5 |
| 10 | Responsabilidade por recursos de informação | 4 | 24 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 3 | 21 |
| 13 | Esforço físico | 2 | 7 |
| 14 | Esforço mental | 3 | 12 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **335** (Faixa 5: 326–395) |

## Faixa 6: Profissional de engenharia de integração

Uma pessoa engenheira de integração projeta, constrói e dá suporte de forma independente a integrações entre sistemas de saúde e de cuidados e ajuda a definir como os sistemas devem trocar dados.

### Responsabilidades

- Projetar e construir integrações, APIs e fluxos de mensagens usando HL7 FHIR, HL7 versão 2 e padrões de mensageria.
- Analisar os sistemas de origem e de destino e escrever especificações de interface e mapeamentos de dados, incluindo códigos clínicos.
- Construir associação de pacientes, validação e tratamento de erros para que a informação chegue ao registro correto.
- Participar de oficinas de perigos e incorporar controles de segurança às integrações, como alertas para mensagens com falha ou atrasadas.
- Trabalhar com fornecedores e organizações parceiras para testar e colocar em operação novas conexões.
- Investigar e corrigir problemas em integrações em operação e orientar profissionais de engenharia de integração júnior.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Systems integration](../../competências/#systems-integration) | UK GDaD PCF | Domínio | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../competências/#programming-and-build-software-engineering) | UK GDaD PCF | Domínio | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../competências/#systems-design) | UK GDaD PCF | Aplicação | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../competências/#service-support) | UK GDaD PCF | Domínio | You can:<br>• identify, locate and fix service faults |
| [Information security](../../competências/#information-security) | UK GDaD PCF | Aplicação | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Domínio | Você pode:<br>• projetar e construir integrações usando FHIR, HL7 versão 2 e padrões de mensageria<br>• escrever e perfilar recursos FHIR e guias de implementação<br>• resolver problemas complexos de mapeamento e de qualidade de dados entre sistemas |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Aplicação | Você pode:<br>• encontrar e usar os códigos certos para um item de dados ou formulário<br>• usar navegadores de terminologia e conjuntos de referência |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Aplicação | Você pode:<br>• aplicar os princípios de proteção de dados ao seu trabalho<br>• contribuir para avaliações de impacto sobre a proteção de dados<br>• tratar corretamente pedidos de informações e registros |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Aplicação | Você pode:<br>• participar de oficinas de identificação de perigos e contribuir para um registro de perigos<br>• seguir o processo de gestão de riscos clínicos no seu trabalho<br>• fornecer evidências para um dossiê de segurança clínica, como resultados de testes |
| [Compreensão dos serviços de saúde e de cuidados](../../competências/#compreensão-dos-serviços-de-saúde-e-de-cuidados) | Esta referência | Aplicação | Você pode:<br>• explicar os fluxos de trabalho clínicos e de cuidados que o seu trabalho apoia<br>• usar corretamente termos comuns de saúde com colegas clínicos e de cuidados<br>• reconhecer quando uma mudança pode afetar o cuidado de pacientes e levar o assunto adiante |

### Qualificações e experiência habituais

- Graduação em computação ou em área afim, ou experiência equivalente.
- Experiência na construção e no suporte de integrações entre sistemas em produção.

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
| 9 | Responsabilidade por pessoas | 2 | 12 |
| 10 | Responsabilidade por recursos de informação | 4 | 24 |
| 11 | Responsabilidade por pesquisa e desenvolvimento | 2 | 12 |
| 12 | Liberdade de ação | 4 | 32 |
| 13 | Esforço físico | 1 | 3 |
| 14 | Esforço mental | 4 | 18 |
| 15 | Esforço emocional | 1 | 5 |
| 16 | Condições de trabalho | 2 | 7 |
| | **Total** | | **418** (Faixa 6: 396–465) |

## Faixa 7: Profissional de engenharia de integração sênior

Uma pessoa engenheira de integração sênior lidera o projeto e a entrega de integrações complexas entre muitos sistemas e organizações e define os padrões de integração da sua área.

### Responsabilidades

- Liderar o projeto técnico de integrações complexas, como prontuários compartilhados, resultados e encaminhamentos entre organizações.
- Escrever e manter perfis FHIR, guias de implementação e padrões de interface da organização.
- Projetar integrações seguras, resilientes e observáveis, com caminhos claros para resolver falhas.
- Trabalhar com os responsáveis pela segurança clínica para identificar os perigos das integrações e garantir que os controles sejam projetados e testados.
- Garantir que cada fluxo de dados tenha uma base legal e acordos de compartilhamento de dados definidos, trabalhando com colegas de governança da informação.
- Orientar e desenvolver os profissionais de engenharia de integração da equipe.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Systems integration](../../competências/#systems-integration) | UK GDaD PCF | Especialista | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../competências/#programming-and-build-software-engineering) | UK GDaD PCF | Domínio | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../competências/#systems-design) | UK GDaD PCF | Domínio | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../competências/#information-security) | UK GDaD PCF | Domínio | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../competências/#stakeholder-relationship-management) | UK GDaD PCF | Aplicação | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Domínio | Você pode:<br>• projetar e construir integrações usando FHIR, HL7 versão 2 e padrões de mensageria<br>• escrever e perfilar recursos FHIR e guias de implementação<br>• resolver problemas complexos de mapeamento e de qualidade de dados entre sistemas |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Domínio | Você pode:<br>• projetar modelos de dados e conjuntos de referência usando terminologias clínicas<br>• mapear entre terminologias e classificações e explicar os limites de um mapeamento<br>• orientar as equipes sobre o uso de terminologias em produtos e em análises |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Domínio | Você pode:<br>• liderar avaliações de impacto sobre a proteção de dados e acordos de compartilhamento de informações<br>• orientar as equipes sobre base legal, consentimento, confidencialidade e retenção<br>• investigar incidentes e recomendar melhorias |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Aplicação | Você pode:<br>• participar de oficinas de identificação de perigos e contribuir para um registro de perigos<br>• seguir o processo de gestão de riscos clínicos no seu trabalho<br>• fornecer evidências para um dossiê de segurança clínica, como resultados de testes |
| [Gestão de identidades e acessos](../../competências/#gestão-de-identidades-e-acessos) | Esta referência | Aplicação | Você pode:<br>• criar, alterar e remover contas de usuário e direitos de acesso<br>• verificar os acessos em relação às regras de acesso baseado em papéis |

### Qualificações e experiência habituais

- Experiência substancial no projeto e no suporte de integrações de saúde ou de outras integrações complexas, em nível equivalente ao de mestrado.

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

## Faixa 8a: Profissional de engenharia de integração líder

Uma pessoa engenheira de integração líder conduz a engenharia de integração da organização, define sua direção técnica e seus padrões e dá garantia a integrações críticas entre muitos sistemas.

### Responsabilidades

- Liderar a engenharia de integração em toda a organização, definindo direção, padrões e modelos.
- Dar garantia ao projeto de integrações críticas, como as que transportam resultados, medicamentos ou alertas.
- Dar forma ao roteiro da plataforma de integração com arquitetos, gerentes de produto e fornecedores.
- Representar a organização em trabalhos de interoperabilidade e de padronização entre organizações.
- Chefiar ou liderar profissionais de engenharia de integração e ampliar a comunidade de prática de integração.

### Competências

| Competência | Fonte | Nível esperado | O que este nível significa |
| --- | --- | --- | --- |
| [Systems integration](../../competências/#systems-integration) | UK GDaD PCF | Especialista | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../competências/#systems-design) | UK GDaD PCF | Especialista | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../competências/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Domínio | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../competências/#stakeholder-relationship-management) | UK GDaD PCF | Domínio | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../competências/#leadership-and-guidance) | UK GDaD PCF | Domínio | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Interoperabilidade de dados de saúde](../../competências/#interoperabilidade-de-dados-de-saúde) | Esta referência | Especialista | Você pode:<br>• definir os padrões e a estratégia de interoperabilidade da organização<br>• liderar trabalhos de padronização nacionais ou entre organizações<br>• dar garantia ao projeto de integrações críticas entre muitos sistemas |
| [Terminologia e classificação clínicas](../../competências/#terminologia-e-classificação-clínicas) | Esta referência | Domínio | Você pode:<br>• projetar modelos de dados e conjuntos de referência usando terminologias clínicas<br>• mapear entre terminologias e classificações e explicar os limites de um mapeamento<br>• orientar as equipes sobre o uso de terminologias em produtos e em análises |
| [Governança da informação e proteção de dados](../../competências/#governança-da-informação-e-proteção-de-dados) | Esta referência | Domínio | Você pode:<br>• liderar avaliações de impacto sobre a proteção de dados e acordos de compartilhamento de informações<br>• orientar as equipes sobre base legal, consentimento, confidencialidade e retenção<br>• investigar incidentes e recomendar melhorias |
| [Gestão de riscos clínicos](../../competências/#gestão-de-riscos-clínicos) | Esta referência | Domínio | Você pode:<br>• liderar a identificação de perigos e a avaliação de riscos de um produto ou de uma mudança<br>• redigir e manter registros de perigos e relatórios de dossiês de segurança clínica<br>• acordar controles de risco com as equipes de produto e verificar se funcionam<br>• orientar as equipes na aplicação das normas de gestão de riscos clínicos |
| [Gestão de pessoas](../../competências/#gestão-de-pessoas) | Esta referência | Domínio | Você pode:<br>• chefiar uma equipe, definindo objetivos e conduzindo avaliações de desempenho<br>• apoiar o bem-estar e gerir a assiduidade, o desempenho e a conduta<br>• planejar o desenvolvimento e a sucessão da equipe |

### Qualificações e experiência habituais

- Ampla experiência na liderança da engenharia de integração de sistemas de saúde ou de cuidados complexos.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
