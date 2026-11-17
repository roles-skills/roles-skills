# Ingeniero de integración (interoperabilidad sanitaria)

> Este es un perfil de referencia ilustrativo para una organización genérica de atención sanitaria digital. No es una descripción de puesto oficial de ningún empleador, y sus puntuaciones de valoración de puestos no son una valoración formal.

> Este texto ha sido traducido del inglés por un asistente de inteligencia artificial y todavía no lo ha revisado un hablante nativo de español. Las citas del Marco de Capacidades de la Profesión Digital y de Datos del Gobierno del Reino Unido (UK GDaD PCF) y de ESCO se mantienen en inglés.

**Familia:** [Desarrollo de software](../../#desarrollo-de-software)  
**Bandas:** 5, 6, 7, 8a  
**Rol del UK GDaD PCF:** Ninguno (esta referencia define el rol)  
**Ocupaciones de ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Resumen

Los ingenieros de integración conectan los sistemas clínicos y de gestión de la organización para que la información de salud y asistencia llegue con seguridad a donde se necesita. Diseñan, crean, prueban y dan soporte a interfaces, API y flujos de mensajes con estándares como HL7 FHIR y HL7 versión 2, mapean datos y códigos clínicos entre sistemas, y mantienen las integraciones en funcionamiento en producción.

## En una organización de atención sanitaria digital

- Un mensaje perdido, retrasado, duplicado o asociado al paciente equivocado, como un resultado de una prueba o una derivación, puede causar daño directamente, por lo que el trabajo de integración sigue el proceso de gestión del riesgo clínico.
- Las integraciones transportan grandes volúmenes de información sanitaria confidencial entre organizaciones, por lo que cada flujo necesita una base jurídica, un transporte seguro y auditoría.
- Los sistemas sanitarios usan muchos estándares y versiones, desde los mensajes HL7 versión 2 hasta las API HL7 FHIR y los perfiles IHE, a menudo con variantes locales.
- El significado clínico debe llegar intacto, por lo que los ingenieros mapean correctamente terminologías clínicas como SNOMED CT y asocian a los pacientes de forma fiable.
- Muchas integraciones apoyan la atención a todas horas, por lo que necesitan monitorización, alertas y vías claras para resolver los mensajes fallidos.

## Niveles de rol

| Banda | Título | Nivel del UK GDaD PCF | Grados de la función pública del Reino Unido | Puntos de valoración del puesto |
| --- | --- | --- | --- | --- |
| 5 | [Ingeniero de integración júnior](#banda-5-ingeniero-de-integración-júnior) | — | — | 335 |
| 6 | [Ingeniero de integración](#banda-6-ingeniero-de-integración) | — | — | 418 |
| 7 | [Ingeniero de integración sénior](#banda-7-ingeniero-de-integración-sénior) | — | — | 477 |
| 8a | [Ingeniero de integración líder](#banda-8a-ingeniero-de-integración-líder) | — | — | 551 |

## Banda 5: Ingeniero de integración júnior

El ingeniero de integración júnior crea, prueba y da soporte a integraciones entre sistemas de salud y asistencia, a partir de especificaciones y con la orientación de ingenieros con más experiencia.

### Responsabilidades

- Crear y modificar mapeos de mensajes, transformaciones y llamadas a API a partir de especificaciones acordadas.
- Probar las integraciones frente a las especificaciones y mensajes de ejemplo, incluidos los casos de error y los casos límite.
- Monitorizar los flujos de mensajes, investigar los mensajes fallidos o rechazados, y resolverlos o escalarlos.
- Tratar los datos sanitarios de forma segura, siguiendo las normas de gobernanza de la información para los datos reales y de prueba.
- Registrar los cambios y los resultados de las pruebas para que puedan usarse como evidencia de seguridad clínica.

### Habilidades

| Habilidad | Fuente | Nivel esperado | Qué significa este nivel |
| --- | --- | --- | --- |
| [Systems integration](../../habilidades/#systems-integration) | UK GDaD PCF | Operativo | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../habilidades/#programming-and-build-software-engineering) | UK GDaD PCF | Operativo | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../habilidades/#testing) | UK GDaD PCF | Operativo | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../habilidades/#service-support) | UK GDaD PCF | Operativo | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../habilidades/#information-security) | UK GDaD PCF | Conocimiento básico | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Interoperabilidad de datos sanitarios](../../habilidades/#interoperabilidad-de-datos-sanitarios) | Esta referencia | Operativo | Puede:<br>• leer y usar recursos, perfiles y API de FHIR<br>• crear o probar integraciones sencillas con orientación<br>• comprobar los mensajes frente a una especificación |
| [Terminología y clasificación clínicas](../../habilidades/#terminología-y-clasificación-clínicas) | Esta referencia | Conocimiento básico | Puede:<br>• explicar la diferencia entre una terminología clínica y una clasificación<br>• reconocer terminologías habituales como SNOMED CT y la CIE |
| [Gobernanza de la información y protección de datos](../../habilidades/#gobernanza-de-la-información-y-protección-de-datos) | Esta referencia | Operativo | Puede:<br>• aplicar los principios de protección de datos a su trabajo<br>• contribuir a las evaluaciones de impacto relativas a la protección de datos<br>• tramitar correctamente las solicitudes de información y los registros |
| [Gestión del riesgo clínico](../../habilidades/#gestión-del-riesgo-clínico) | Esta referencia | Conocimiento básico | Puede:<br>• explicar cómo los sistemas de TI sanitarios pueden causar daño a los pacientes, por ejemplo con información errónea, ausente o tardía<br>• notificar un posible problema de seguridad clínica por la vía adecuada |
| [Comprensión de los servicios de salud y asistencia](../../habilidades/#comprensión-de-los-servicios-de-salud-y-asistencia) | Esta referencia | Conocimiento básico | Puede:<br>• describir las partes principales del sistema de salud y asistencia y los servicios que apoya la organización<br>• explicar por qué la seguridad de los pacientes y la confidencialidad importan en su trabajo |

### Cualificaciones y experiencia habituales

- Un grado en informática o una materia afín, un programa de aprendizaje completado o experiencia equivalente.

### Descripción de la banda

- **Conocimientos:** Conocimiento profesional o técnico, normalmente mediante un grado universitario o experiencia equivalente.
- **Autonomía:** Trabaja hacia objetivos amplios dentro de las normas profesionales; planifica su propio trabajo.
- **Alcance:** Su propio trabajo profesional dentro de un equipo o producto.
- **Liderazgo:** Puede orientar y revisar el trabajo del personal de apoyo y de los aprendices.
- **Rendición de cuentas:** La calidad de su propio trabajo profesional.

### Valoración del puesto (ilustrativa)

| # | Factor | Nivel | Puntos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicación y relación | 4 | 32 |
| 2 | Conocimientos, formación y experiencia | 5 | 120 |
| 3 | Habilidades analíticas y de juicio | 3 | 27 |
| 4 | Habilidades de planificación y organización | 2 | 15 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidad en la atención a pacientes y usuarios | 1 | 4 |
| 7 | Responsabilidad en el desarrollo de políticas y servicios | 2 | 12 |
| 8 | Responsabilidad sobre recursos financieros y materiales | 1 | 5 |
| 9 | Responsabilidad sobre personas | 1 | 5 |
| 10 | Responsabilidad sobre recursos de información | 4 | 24 |
| 11 | Responsabilidad en investigación y desarrollo | 2 | 12 |
| 12 | Libertad de actuación | 3 | 21 |
| 13 | Esfuerzo físico | 2 | 7 |
| 14 | Esfuerzo mental | 3 | 12 |
| 15 | Esfuerzo emocional | 1 | 5 |
| 16 | Condiciones de trabajo | 2 | 7 |
| | **Total** | | **335** (Banda 5: 326–395) |

## Banda 6: Ingeniero de integración

El ingeniero de integración diseña, crea y da soporte de forma independiente a integraciones entre sistemas de salud y asistencia, y ayuda a definir cómo deben intercambiar datos los sistemas.

### Responsabilidades

- Diseñar y crear integraciones, API y flujos de mensajes con HL7 FHIR, HL7 versión 2 y patrones de mensajería.
- Analizar los sistemas de origen y de destino y redactar especificaciones de interfaz y mapeos de datos, incluidos los códigos clínicos.
- Crear la asociación de pacientes, la validación y la gestión de errores para que la información llegue a la historia correcta.
- Participar en talleres de peligros e incorporar controles de seguridad a las integraciones, como alertas de mensajes fallidos o retrasados.
- Trabajar con proveedores y organizaciones socias para probar y poner en marcha nuevas conexiones.
- Investigar y corregir problemas en las integraciones en producción, y ser mentor de los ingenieros de integración júnior.

### Habilidades

| Habilidad | Fuente | Nivel esperado | Qué significa este nivel |
| --- | --- | --- | --- |
| [Systems integration](../../habilidades/#systems-integration) | UK GDaD PCF | Profesional | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../habilidades/#programming-and-build-software-engineering) | UK GDaD PCF | Profesional | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../habilidades/#systems-design) | UK GDaD PCF | Operativo | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../habilidades/#service-support) | UK GDaD PCF | Profesional | You can:<br>• identify, locate and fix service faults |
| [Information security](../../habilidades/#information-security) | UK GDaD PCF | Operativo | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Interoperabilidad de datos sanitarios](../../habilidades/#interoperabilidad-de-datos-sanitarios) | Esta referencia | Profesional | Puede:<br>• diseñar y crear integraciones con FHIR, HL7 versión 2 y patrones de mensajería<br>• redactar y perfilar recursos FHIR y guías de implementación<br>• resolver problemas complejos de mapeo y de calidad de datos entre sistemas |
| [Terminología y clasificación clínicas](../../habilidades/#terminología-y-clasificación-clínicas) | Esta referencia | Operativo | Puede:<br>• encontrar y usar los códigos adecuados para un dato o un formulario<br>• usar navegadores de terminología y conjuntos de referencia |
| [Gobernanza de la información y protección de datos](../../habilidades/#gobernanza-de-la-información-y-protección-de-datos) | Esta referencia | Operativo | Puede:<br>• aplicar los principios de protección de datos a su trabajo<br>• contribuir a las evaluaciones de impacto relativas a la protección de datos<br>• tramitar correctamente las solicitudes de información y los registros |
| [Gestión del riesgo clínico](../../habilidades/#gestión-del-riesgo-clínico) | Esta referencia | Operativo | Puede:<br>• participar en talleres de peligros y contribuir a un registro de peligros<br>• seguir el proceso de gestión del riesgo clínico en su trabajo<br>• aportar pruebas para un caso de seguridad clínica, como resultados de pruebas |
| [Comprensión de los servicios de salud y asistencia](../../habilidades/#comprensión-de-los-servicios-de-salud-y-asistencia) | Esta referencia | Operativo | Puede:<br>• explicar los flujos de trabajo clínicos y asistenciales que apoya su trabajo<br>• usar correctamente los términos sanitarios habituales con colegas clínicos y asistenciales<br>• reconocer cuándo un cambio podría afectar a la atención a los pacientes y comunicarlo |

### Cualificaciones y experiencia habituales

- Un grado en informática o una materia afín, o experiencia equivalente.
- Experiencia en la creación y el soporte de integraciones entre sistemas en producción.

### Descripción de la banda

- **Conocimientos:** Conocimiento especializado de diversos procedimientos, adquirido mediante formación adicional o experiencia.
- **Autonomía:** Trabaja con independencia; interpreta la política para su área; pide consejo en cuestiones complejas.
- **Alcance:** Un producto, servicio o línea de trabajo.
- **Liderazgo:** Puede dirigir un equipo pequeño o ser mentor de sus colegas.
- **Rendición de cuentas:** Los resultados de su línea de trabajo y la calidad del asesoramiento que da.

### Valoración del puesto (ilustrativa)

| # | Factor | Nivel | Puntos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicación y relación | 4 | 32 |
| 2 | Conocimientos, formación y experiencia | 6 | 156 |
| 3 | Habilidades analíticas y de juicio | 4 | 42 |
| 4 | Habilidades de planificación y organización | 3 | 27 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidad en la atención a pacientes y usuarios | 1 | 4 |
| 7 | Responsabilidad en el desarrollo de políticas y servicios | 2 | 12 |
| 8 | Responsabilidad sobre recursos financieros y materiales | 1 | 5 |
| 9 | Responsabilidad sobre personas | 2 | 12 |
| 10 | Responsabilidad sobre recursos de información | 4 | 24 |
| 11 | Responsabilidad en investigación y desarrollo | 2 | 12 |
| 12 | Libertad de actuación | 4 | 32 |
| 13 | Esfuerzo físico | 1 | 3 |
| 14 | Esfuerzo mental | 4 | 18 |
| 15 | Esfuerzo emocional | 1 | 5 |
| 16 | Condiciones de trabajo | 2 | 7 |
| | **Total** | | **418** (Banda 6: 396–465) |

## Banda 7: Ingeniero de integración sénior

El ingeniero de integración sénior dirige el diseño y la entrega de integraciones complejas entre muchos sistemas y organizaciones, y fija las normas de integración de su área.

### Responsabilidades

- Dirigir el diseño técnico de integraciones complejas, como las historias clínicas compartidas, los resultados y las derivaciones entre organizaciones.
- Redactar y mantener perfiles FHIR, guías de implementación y normas de interfaz para la organización.
- Diseñar las integraciones para que sean seguras, resilientes y observables, con vías claras para resolver los fallos.
- Trabajar con los responsables de seguridad clínica para identificar los peligros de integración y asegurarse de que los controles se diseñan desde el principio y se prueban.
- Asegurarse de que cada flujo de datos tiene una base jurídica y unos acuerdos de intercambio de datos acordados, trabajando con los colegas de gobernanza de la información.
- Orientar y desarrollar a los ingenieros de integración del equipo.

### Habilidades

| Habilidad | Fuente | Nivel esperado | Qué significa este nivel |
| --- | --- | --- | --- |
| [Systems integration](../../habilidades/#systems-integration) | UK GDaD PCF | Experto | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../habilidades/#programming-and-build-software-engineering) | UK GDaD PCF | Profesional | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../habilidades/#systems-design) | UK GDaD PCF | Profesional | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../habilidades/#information-security) | UK GDaD PCF | Profesional | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../habilidades/#stakeholder-relationship-management) | UK GDaD PCF | Operativo | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Interoperabilidad de datos sanitarios](../../habilidades/#interoperabilidad-de-datos-sanitarios) | Esta referencia | Profesional | Puede:<br>• diseñar y crear integraciones con FHIR, HL7 versión 2 y patrones de mensajería<br>• redactar y perfilar recursos FHIR y guías de implementación<br>• resolver problemas complejos de mapeo y de calidad de datos entre sistemas |
| [Terminología y clasificación clínicas](../../habilidades/#terminología-y-clasificación-clínicas) | Esta referencia | Profesional | Puede:<br>• diseñar modelos de datos y conjuntos de referencia con terminologías clínicas<br>• mapear entre terminologías y clasificaciones, y explicar los límites de un mapeo<br>• asesorar a los equipos sobre el uso de la terminología en productos y analítica |
| [Gobernanza de la información y protección de datos](../../habilidades/#gobernanza-de-la-información-y-protección-de-datos) | Esta referencia | Profesional | Puede:<br>• dirigir evaluaciones de impacto relativas a la protección de datos y acuerdos de intercambio de información<br>• asesorar a los equipos sobre la base jurídica, el consentimiento, la confidencialidad y la conservación<br>• investigar incidentes y recomendar mejoras |
| [Gestión del riesgo clínico](../../habilidades/#gestión-del-riesgo-clínico) | Esta referencia | Operativo | Puede:<br>• participar en talleres de peligros y contribuir a un registro de peligros<br>• seguir el proceso de gestión del riesgo clínico en su trabajo<br>• aportar pruebas para un caso de seguridad clínica, como resultados de pruebas |
| [Gestión de identidades y accesos](../../habilidades/#gestión-de-identidades-y-accesos) | Esta referencia | Operativo | Puede:<br>• crear, modificar y eliminar cuentas de usuario y derechos de acceso<br>• comprobar los accesos frente a las normas de acceso basado en roles |

### Cualificaciones y experiencia habituales

- Experiencia sustancial en el diseño y el soporte de integraciones sanitarias u otras integraciones complejas, a un nivel equivalente a un máster.

### Descripción de la banda

- **Conocimientos:** Conocimiento especializado muy desarrollado, normalmente de nivel de máster o experiencia equivalente.
- **Autonomía:** Trabaja según la política de la organización; decide cómo se logran los resultados; es la persona experta a la que otros consultan.
- **Alcance:** Varios productos o servicios, o una función especializada.
- **Liderazgo:** Dirige un equipo o un área de práctica profesional.
- **Rendición de cuentas:** La prestación de un servicio o función especializada, y su presupuesto si lo tiene.

### Valoración del puesto (ilustrativa)

| # | Factor | Nivel | Puntos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicación y relación | 4 | 32 |
| 2 | Conocimientos, formación y experiencia | 7 | 196 |
| 3 | Habilidades analíticas y de juicio | 4 | 42 |
| 4 | Habilidades de planificación y organización | 3 | 27 |
| 5 | Habilidades físicas | 3 | 27 |
| 6 | Responsabilidad en la atención a pacientes y usuarios | 1 | 4 |
| 7 | Responsabilidad en el desarrollo de políticas y servicios | 3 | 21 |
| 8 | Responsabilidad sobre recursos financieros y materiales | 1 | 5 |
| 9 | Responsabilidad sobre personas | 2 | 12 |
| 10 | Responsabilidad sobre recursos de información | 5 | 34 |
| 11 | Responsabilidad en investigación y desarrollo | 2 | 12 |
| 12 | Libertad de actuación | 4 | 32 |
| 13 | Esfuerzo físico | 1 | 3 |
| 14 | Esfuerzo mental | 4 | 18 |
| 15 | Esfuerzo emocional | 1 | 5 |
| 16 | Condiciones de trabajo | 2 | 7 |
| | **Total** | | **477** (Banda 7: 466–539) |

## Banda 8a: Ingeniero de integración líder

El ingeniero de integración líder dirige la ingeniería de integración de la organización, fija su dirección técnica y sus normas, y garantiza las integraciones críticas entre muchos sistemas.

### Responsabilidades

- Dirigir la ingeniería de integración en toda la organización, fijando la dirección, los patrones y las normas.
- Garantizar el diseño de las integraciones críticas, como las que transportan resultados, medicamentos o alertas.
- Dar forma a la hoja de ruta de la plataforma de integración con arquitectos, gestores de producto y proveedores.
- Representar a la organización en el trabajo interorganizativo de interoperabilidad y de estándares.
- Gestionar o dirigir a los ingenieros de integración y hacer crecer la comunidad de práctica de integración.

### Habilidades

| Habilidad | Fuente | Nivel esperado | Qué significa este nivel |
| --- | --- | --- | --- |
| [Systems integration](../../habilidades/#systems-integration) | UK GDaD PCF | Experto | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../habilidades/#systems-design) | UK GDaD PCF | Experto | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../habilidades/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Profesional | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../habilidades/#stakeholder-relationship-management) | UK GDaD PCF | Profesional | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../habilidades/#leadership-and-guidance) | UK GDaD PCF | Profesional | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Interoperabilidad de datos sanitarios](../../habilidades/#interoperabilidad-de-datos-sanitarios) | Esta referencia | Experto | Puede:<br>• fijar los estándares y la estrategia de interoperabilidad de la organización<br>• dirigir el trabajo de estándares nacional o entre organizaciones<br>• garantizar el diseño de integraciones críticas entre muchos sistemas |
| [Terminología y clasificación clínicas](../../habilidades/#terminología-y-clasificación-clínicas) | Esta referencia | Profesional | Puede:<br>• diseñar modelos de datos y conjuntos de referencia con terminologías clínicas<br>• mapear entre terminologías y clasificaciones, y explicar los límites de un mapeo<br>• asesorar a los equipos sobre el uso de la terminología en productos y analítica |
| [Gobernanza de la información y protección de datos](../../habilidades/#gobernanza-de-la-información-y-protección-de-datos) | Esta referencia | Profesional | Puede:<br>• dirigir evaluaciones de impacto relativas a la protección de datos y acuerdos de intercambio de información<br>• asesorar a los equipos sobre la base jurídica, el consentimiento, la confidencialidad y la conservación<br>• investigar incidentes y recomendar mejoras |
| [Gestión del riesgo clínico](../../habilidades/#gestión-del-riesgo-clínico) | Esta referencia | Profesional | Puede:<br>• dirigir la identificación de peligros y la evaluación de riesgos de un producto o cambio<br>• redactar y mantener registros de peligros e informes de casos de seguridad clínica<br>• acordar controles de riesgos con los equipos de producto y comprobar que funcionan<br>• asesorar a los equipos sobre la aplicación de las normas de gestión del riesgo clínico |
| [Gestión de personas](../../habilidades/#gestión-de-personas) | Esta referencia | Profesional | Puede:<br>• gestionar directamente un equipo, fijando objetivos y realizando evaluaciones del desempeño<br>• apoyar el bienestar y gestionar la asistencia, el rendimiento y la conducta<br>• planificar el desarrollo y la sucesión del equipo |

### Cualificaciones y experiencia habituales

- Amplia experiencia en la dirección de la ingeniería de integración de sistemas complejos de salud o asistencia.

### Descripción de la banda

- **Conocimientos:** Conocimiento experto de una disciplina y de su gestión.
- **Autonomía:** Interpreta la política de la organización para un servicio; marca la dirección del equipo.
- **Alcance:** Un área de servicio o una disciplina en toda la organización.
- **Liderazgo:** Gestiona un equipo, o dirige una disciplina sin gestión directa de personas.
- **Rendición de cuentas:** Un área de servicio, su personal y su presupuesto.

### Valoración del puesto (ilustrativa)

| # | Factor | Nivel | Puntos |
| --- | --- | --- | --- |
| 1 | Habilidades de comunicación y relación | 5 | 45 |
| 2 | Conocimientos, formación y experiencia | 7 | 196 |
| 3 | Habilidades analíticas y de juicio | 5 | 60 |
| 4 | Habilidades de planificación y organización | 4 | 42 |
| 5 | Habilidades físicas | 2 | 15 |
| 6 | Responsabilidad en la atención a pacientes y usuarios | 1 | 4 |
| 7 | Responsabilidad en el desarrollo de políticas y servicios | 4 | 32 |
| 8 | Responsabilidad sobre recursos financieros y materiales | 2 | 12 |
| 9 | Responsabilidad sobre personas | 3 | 21 |
| 10 | Responsabilidad sobre recursos de información | 5 | 34 |
| 11 | Responsabilidad en investigación y desarrollo | 2 | 12 |
| 12 | Libertad de actuación | 5 | 45 |
| 13 | Esfuerzo físico | 1 | 3 |
| 14 | Esfuerzo mental | 4 | 18 |
| 15 | Esfuerzo emocional | 1 | 5 |
| 16 | Condiciones de trabajo | 2 | 7 |
| | **Total** | | **551** (Banda 8a: 540–584) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
