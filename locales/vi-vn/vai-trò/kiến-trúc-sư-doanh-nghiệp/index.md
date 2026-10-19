# Kiến trúc sư doanh nghiệp

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Kiến trúc](../../#kiến-trúc)  
**Bậc:** 8a, 8b, 8c, 8d  
**Vai trò UK GDaD PCF:** [Enterprise architect](https://understand-digital-data-roles-skills.service.gov.uk/role/enterprise-architect/)  
**Nghề nghiệp ESCO:** [enterprise architect](http://data.europa.eu/esco/occupation/2bef94db-0088-4507-982a-2ca717529adb) (ISCO-08 2511)

## Tóm tắt

Kiến trúc sư doanh nghiệp cung cấp cho tổ chức cái nhìn liền mạch về dịch vụ, thông tin, ứng dụng và công nghệ của mình, và dùng nó để chuyển chiến lược y tế và chăm sóc thành một kế hoạch thay đổi mạch lạc. Họ đề ra các nguyên tắc, tiêu chuẩn và lộ trình kiến trúc, định hướng các quyết định đầu tư, và bảo đảm thay đổi số hỗ trợ việc chăm sóc an toàn, liền mạch cho bệnh nhân giữa các tổ chức.

## Trong một tổ chức chăm sóc sức khỏe số

- Các lộ trình chăm sóc vượt qua nhiều tổ chức và hệ thống, nên kiến trúc phải hỗ trợ chia sẻ hồ sơ, kết quả và giấy giới thiệu qua các ranh giới.
- Hệ thống thường gồm các hệ thống lâm sàng tồn tại lâu, thiết bị y tế và hợp đồng nhà cung cấp khó thay đổi, nên các lộ trình phải lập kế hoạch chuyển tiếp cẩn thận.
- Các quyết định kiến trúc ảnh hưởng đến an toàn bệnh nhân, quyền riêng tư và khả năng phục hồi của các dịch vụ hoạt động suốt ngày đêm.
- Các tiêu chuẩn mở như HL7 FHIR, SNOMED CT và các hồ sơ IHE là chìa khóa để tránh bị phụ thuộc vào một nhà cung cấp và hỗ trợ khả năng tương tác.
- Nguồn tài trợ bị hạn chế và được xem xét kỹ, nên các kiến trúc sư phải chứng minh giá trị đồng tiền và việc tái sử dụng các nền tảng dùng chung khi có.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> Enterprise architects are leaders working across different levels within an organisation to translate the business strategy into business change and technical delivery.
> 
> In this role, you will:
> - identify priorities for change to enable delivery at pace
> - lead and influence the delivery of cross-cutting capabilities that enable change
> - own the enterprise architecture vision, strategy and roadmaps from a business, technology and data perspective, including ‘as is’, ‘to be’ and transitional states
> - consult and support collaboration across the business
> - understand the organisation’s ecosystem and its interdependencies, including reference architectures
> - take a strategic view across all architectural domains, portfolios and programmes
> - guide the organisation to make appropriate business, technology and data decisions by recommending reuse, sustainability and scalability, to achieve value for money and reduce risk
> - establish architectural principles, policies and standards
> - collaborate and consult with stakeholders to assure business, technology and data decisions are aligned with enterprise architecture strategy
> - develop the architecture community
> - carry out horizon scanning across industry, identifying emerging trends and their potential impact and opportunity for the organisation

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 8a | [Kiến trúc sư doanh nghiệp](#bậc-8a-kiến-trúc-sư-doanh-nghiệp) | Enterprise architect | HEO/SEO | 560 |
| 8b | [Kiến trúc sư doanh nghiệp cao cấp](#bậc-8b-kiến-trúc-sư-doanh-nghiệp-cao-cấp) | Senior enterprise architect | SEO/G7 | 622 |
| 8c | [Trưởng nhóm kiến trúc sư doanh nghiệp](#bậc-8c-trưởng-nhóm-kiến-trúc-sư-doanh-nghiệp) | Lead enterprise architect | G7/G6 | 658 |
| 8d | [Kiến trúc sư doanh nghiệp chủ chốt](#bậc-8d-kiến-trúc-sư-doanh-nghiệp-chủ-chốt) | Principal enterprise architect | G6 | 703 |

## Bậc 8a: Kiến trúc sư doanh nghiệp

**Cấp UK GDaD PCF: Enterprise architect**

> An enterprise architect supports other architects in developing the strategy.
> 
> At this role level, you will:
> - network and communicate with stakeholders across domains or enterprises, and identify opportunities for improvement
> - use best practice
> - use emerging technologies and approaches
> - learn to identify influences or risks
> - play a part in successful delivery of the team’s objectives

### Trách nhiệm

- Mô hình hóa các dịch vụ, thông tin, ứng dụng và công nghệ hiện tại và mục tiêu của tổ chức cho một lĩnh vực, như chẩn đoán hoặc chăm sóc cộng đồng.
- Cập nhật kho kiến trúc, kể cả danh mục ứng dụng và luồng dữ liệu.
- Rà soát các đề xuất theo nguyên tắc và tiêu chuẩn kiến trúc, và đưa ra khuyến nghị cho các cơ quan thẩm định thiết kế.
- Xác định nơi các hệ thống trùng lặp năng lực hoặc phụ thuộc vào công nghệ không còn được hỗ trợ, và nêu rủi ro.
- Làm việc với các kiến trúc sư giải pháp và trưởng nhóm lâm sàng để hiểu các lộ trình chăm sóc dùng hệ thống như thế nào.
- Hướng dẫn các kiến trúc sư giải pháp về việc các thiết kế phù hợp với kiến trúc của lĩnh vực như thế nào.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Thành thạo | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Thành thạo | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Vận dụng | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Vận dụng | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Enterprise architecture](../../kỹ-năng/#enterprise-architecture) | UK GDaD PCF | Vận dụng | You can:<br>• turn an organisation's goals into clear objectives, with limited direction<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives, with support |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Vận dụng | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Vận dụng | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Vận dụng | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• ghi nhận và cập nhật các rủi ro cho lĩnh vực của bạn<br>• đề xuất các biện pháp kiểm soát và theo dõi các hành động |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về kiến trúc, phân tích hoặc thiết kế kỹ thuật trong một tổ chức phức tạp, ở mức tương đương bằng thạc sĩ.
- Có kiến thức về một khung kiến trúc doanh nghiệp, như TOGAF, hoặc kinh nghiệm tương đương.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên gia về một lĩnh vực và cách quản lý lĩnh vực đó.
- **Quyền tự chủ:** Diễn giải chính sách của tổ chức cho một dịch vụ; xác định định hướng cho nhóm.
- **Phạm vi:** Một mảng dịch vụ hoặc một lĩnh vực chuyên môn trong toàn tổ chức.
- **Lãnh đạo:** Quản lý một nhóm, hoặc dẫn dắt một lĩnh vực chuyên môn mà không quản lý trực tiếp.
- **Trách nhiệm giải trình:** Một mảng dịch vụ, nhân sự và ngân sách của mảng đó.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 5 | 45 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 7 | 196 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 4 | 42 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 4 | 32 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 2 | 12 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **560** (Bậc 8a: 540–584) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 6): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8a. Kiến thức, phân tích, lập kế hoạch, chính sách và quyền tự chủ hành động được chấm theo hồ sơ Bậc 8a vì công việc định hình các kiến trúc mục tiêu và tư vấn cho các cơ quan thẩm định thiết kế của cả một lĩnh vực.

## Bậc 8b: Kiến trúc sư doanh nghiệp cao cấp

**Cấp UK GDaD PCF: Senior enterprise architect**

> A senior enterprise architect supports lead architects in ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with stakeholders across domains or enterprises
> - identify opportunities for improvement
> - support a community or team
> - use best practice
> - use emerging technologies and approaches
> - play an active part in the team and understand how to deliver the team’s objectives to meet organisational goals
> - identify influences or risks
> - play a part in successful delivery of the long-term strategy

### Trách nhiệm

- Xây dựng các kiến trúc mục tiêu và lộ trình chuyển tiếp cho một hoặc nhiều lĩnh vực của tổ chức.
- Định hình các luận chứng kinh doanh để các khoản đầu tư phù hợp với kiến trúc mục tiêu và tái sử dụng các nền tảng dùng chung.
- Dẫn dắt các đợt rà soát kiến trúc tại các cơ quan thẩm định thiết kế và đưa ra khuyến nghị về các đề xuất quan trọng.
- Lập kế hoạch thay thế hoặc ngừng sử dụng các hệ thống lâm sàng và doanh nghiệp cũ, kể cả di chuyển dữ liệu và rủi ro an toàn.
- Bảo đảm các nhu cầu về khả năng tương tác, an ninh và quản trị thông tin được tích hợp vào các lộ trình.
- Huấn luyện và hướng dẫn các kiến trúc sư doanh nghiệp và giải pháp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Thành thạo | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Thành thạo | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Vận dụng | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../kỹ-năng/#enterprise-architecture) | UK GDaD PCF | Thành thạo | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Thành thạo | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Thành thạo | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• ghi nhận và cập nhật các rủi ro cho lĩnh vực của bạn<br>• đề xuất các biện pháp kiểm soát và theo dõi các hành động |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng về kiến trúc doanh nghiệp hoặc giải pháp trên nhiều lĩnh vực.
- Có kiến thức về một khung kiến trúc doanh nghiệp, như TOGAF, hoặc kinh nghiệm tương đương.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên gia trên nhiều lĩnh vực hoặc một dịch vụ lớn.
- **Quyền tự chủ:** Định hình chính sách và chiến lược cho một mảng lớn.
- **Phạm vi:** Nhiều dịch vụ hoặc nhóm, hoặc một lĩnh vực chuyên môn ở cấp chủ chốt.
- **Lãnh đạo:** Quản lý các quản lý, hoặc là người có thẩm quyền cao nhất trong một lĩnh vực chuyên môn.
- **Trách nhiệm giải trình:** Nhiều dịch vụ, nhân sự và ngân sách của các dịch vụ đó.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 5 | 45 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 8 | 240 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 5 | 60 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 4 | 32 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 2 | 12 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **622** (Bậc 8b: 585–629) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 7): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8b. Lập kế hoạch ở mức 5 cho các lộ trình dài hạn có tác động trên toàn tổ chức; kiến thức ở mức 8 cho kiến thức về kiến trúc nghiệp vụ, thông tin, ứng dụng và công nghệ.

## Bậc 8c: Trưởng nhóm kiến trúc sư doanh nghiệp

**Cấp UK GDaD PCF: Lead enterprise architect**

> A lead enterprise architect plays a high level role in ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across enterprises, and seek opportunities for improvement
> - support at least one community or team, or a combination of both
> - find and use best practice and emerging technologies and approaches
> - lead teams including enterprise architects and help them understand how to deliver the team’s objectives to meet organisational goals
> - horizon scan for influences or risks
> - support successful delivery of the long-term strategy
> - take a leading role in the overall direction of business and digital capabilities

### Trách nhiệm

- Làm chủ kiến trúc doanh nghiệp cho một phần lớn của tổ chức, như hệ thống lâm sàng hoặc hạ tầng dùng chung.
- Chủ trì hoặc dẫn dắt cơ quan thẩm định thiết kế kiến trúc và đề ra các tiêu chuẩn mà các dự án phải đáp ứng.
- Tư vấn cho các giám đốc về ưu tiên đầu tư, chiến lược nhà cung cấp và rủi ro công nghệ.
- Làm việc với các tổ chức đối tác để điều chỉnh các kiến trúc trên các lộ trình chăm sóc và hồ sơ dùng chung.
- Dẫn dắt và phát triển các kiến trúc sư doanh nghiệp và mở rộng cộng đồng thực hành kiến trúc.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Chuyên gia | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Thành thạo | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Enterprise architecture](../../kỹ-năng/#enterprise-architecture) | UK GDaD PCF | Thành thạo | You can:<br>• design an architecture that defines the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others across the organisation to ensure your design is used to achieve the organisation’s objectives |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Chuyên gia | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Chuyên gia | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |
| [Quản lý ngân sách](../../kỹ-năng/#quản-lý-ngân-sách) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• theo dõi chi tiêu so với một ngân sách nhỏ và báo cáo chênh lệch<br>• phê duyệt chi tiêu trong hạn mức của bạn |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng về kiến trúc doanh nghiệp trong một tổ chức phức tạp.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên gia, cùng hiểu biết rộng về tổ chức và ngành.
- **Quyền tự chủ:** Đề ra chiến lược cho một chức năng; chịu trách nhiệm trước một giám đốc.
- **Phạm vi:** Một chức năng hoặc một phòng ban.
- **Lãnh đạo:** Dẫn dắt một chức năng qua nhiều tầng quản lý.
- **Trách nhiệm giải trình:** Hiệu quả hoạt động, lực lượng lao động và ngân sách của một chức năng.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 5 | 45 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 8 | 240 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 5 | 60 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 5 | 45 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 3 | 21 |
| 9 | Trách nhiệm đối với con người | 4 | 32 |
| 10 | Trách nhiệm về nguồn lực thông tin | 6 | 46 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **658** (Bậc 8c: 630–674) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 8b): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8c. Nguồn lực thông tin ở mức 6 vì công việc quản lý kiến trúc của các hệ thống thông tin trên một phần lớn của tổ chức; chính sách và con người cao hơn hồ sơ Bậc 8b vì công việc đề ra tiêu chuẩn cho mọi dự án và dẫn dắt các kiến trúc sư doanh nghiệp.

## Bậc 8d: Kiến trúc sư doanh nghiệp chủ chốt

**Cấp UK GDaD PCF: Principal enterprise architect**

> A principal enterprise architect leads at the highest level and is responsible for ensuring the strategy is developed, agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across enterprises, and actively seek opportunities for improvement
> - support multiple communities and teams
> - find and use best practice
> - find and use emerging technologies and approaches
> - inspire other enterprise architects and help them understand how to meet organisational goals
> - horizon scan for external influences or risks
> - support successful delivery of the long-term strategy
> - be responsible for the overall direction of business and digital capabilities
> - be responsible for the creation, maintenance and consumption of a Digital Twin

### Trách nhiệm

- Đề ra tầm nhìn, nguyên tắc và chiến lược kiến trúc doanh nghiệp của tổ chức, phù hợp với chiến lược y tế và chăm sóc của tổ chức.
- Tư vấn cho ban điều hành và hội đồng về kiến trúc, rủi ro và giá trị của các khoản đầu tư số lớn.
- Dẫn dắt ngành thực hành, quản trị và tiêu chuẩn kiến trúc của tổ chức.
- Đại diện tổ chức trong các diễn đàn về kiến trúc và khả năng tương tác giữa nhiều tổ chức.
- Xây dựng năng lực kiến trúc trong toàn tổ chức, kể cả tuyển dụng và lộ trình nghề nghiệp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Chuyên gia | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Thành thạo | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Chuyên gia | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Enterprise architecture](../../kỹ-năng/#enterprise-architecture) | UK GDaD PCF | Chuyên gia | You can:<br>• lead others designing architectures defining the technology, people, process and other elements needed to achieve organisation objectives<br>• work with others beyond the organisation to influence organisational structures, technology, people and processes to achieve objectives<br>• ensure organisation-wide changes align with the architectural strategy |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Chuyên gia | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Chuyên gia | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Chuyên gia | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• định hình chiến lược của tổ chức bằng hiểu biết sâu về hệ thống y tế và chăm sóc<br>• đại diện tổ chức làm việc với các đối tác và lãnh đạo y tế và chăm sóc<br>• dự đoán những thay đổi về chính sách và dịch vụ sẽ ảnh hưởng đến các dịch vụ số và việc chăm sóc như thế nào |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chính sách và chiến lược quản trị thông tin<br>• tư vấn cho hội đồng về rủi ro thông tin và việc tuân thủ<br>• đại diện tổ chức làm việc với các cơ quan quản lý và đối tác |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• dẫn dắt các quản lý và định hình văn hóa của một mảng lớn<br>• thiết kế kế hoạch nhân lực và thay đổi tổ chức<br>• huấn luyện các lãnh đạo và giải quyết các vấn đề nhân sự phức tạp |
| [Quản lý ngân sách](../../kỹ-năng/#quản-lý-ngân-sách) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• nắm giữ và quản lý một ngân sách, dự báo và giải thích các chênh lệch<br>• xây dựng một luận chứng kinh doanh với chi phí và lợi ích |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc doanh nghiệp giữa các tổ chức.

### Mô tả bậc

- **Kiến thức:** Kiến thức chiến lược trên nhiều chức năng và toàn hệ thống y tế và chăm sóc.
- **Quyền tự chủ:** Định hình chiến lược toàn tổ chức; thay mặt giám đốc khi vắng mặt.
- **Phạm vi:** Một chức năng lớn hoặc nhiều chức năng.
- **Lãnh đạo:** Dẫn dắt nhiều chức năng hoặc một phòng ban lớn.
- **Trách nhiệm giải trình:** Các chức năng lớn, ngân sách lớn và rủi ro toàn tổ chức.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 6 | 60 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 8 | 240 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 5 | 60 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 6 | 60 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 3 | 21 |
| 9 | Trách nhiệm đối với con người | 4 | 32 |
| 10 | Trách nhiệm về nguồn lực thông tin | 6 | 46 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 6 | 60 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **703** (Bậc 8d: 675–720) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 8c): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8d. Chính sách và quyền tự chủ hành động ở mức 6 vì công việc nắm trách nhiệm chung của tổ chức về tầm nhìn, nguyên tắc và chiến lược kiến trúc của tổ chức.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
