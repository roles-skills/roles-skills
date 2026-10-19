# Kiến trúc sư kỹ thuật

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Kiến trúc](../../#kiến-trúc)  
**Bậc:** 6, 7, 8a, 8b, 8c  
**Vai trò UK GDaD PCF:** [Technical architect](https://understand-digital-data-roles-skills.service.gov.uk/role/technical-architect/)  
**Nghề nghiệp ESCO:** [software architect](http://data.europa.eu/esco/occupation/d0aa0792-4345-474b-9365-686cf4869d2e) (ISCO-08 2512); [cloud architect](http://data.europa.eu/esco/occupation/2fb96c6c-8d0b-4ef0-b1ee-3e493305e4eb) (ISCO-08 2512)

## Tóm tắt

Kiến trúc sư kỹ thuật thiết kế cấu trúc kỹ thuật của các dịch vụ y tế số của tổ chức: các thành phần, nền tảng, lưu trữ, mẫu tích hợp và các chất lượng phi chức năng như an ninh, hiệu năng và khả năng phục hồi. Họ làm việc chặt chẽ với lập trình viên và kỹ sư DevOps, lãnh đạo kỹ thuật cho các nhóm triển khai, và bảo đảm các dịch vụ được xây dựng bền vững và an toàn khi vận hành.

## Trong một tổ chức chăm sóc sức khỏe số

- Các dịch vụ lâm sàng thường cần tính sẵn sàng cao và khôi phục nhanh, nên thiết kế kỹ thuật phải lập kế hoạch cho sự cố và vận hành ở chế độ suy giảm.
- Thiết kế phải bảo vệ thông tin y tế bí mật thông qua mã hóa, kiểm soát truy cập và kiểm toán theo mặc định.
- Các dịch vụ kết nối với nhiều hệ thống lâm sàng và nền tảng dùng chung, thường qua API HL7 FHIR và thông điệp, nên các mẫu tích hợp là trọng tâm của thiết kế.
- Các lựa chọn thiết kế kỹ thuật, như bộ nhớ đệm, thử lại và xử lý thời gian, có thể gây ra mối nguy lâm sàng, nên các kiến trúc sư đóng góp vào hồ sơ an toàn.
- Các hệ thống lâm sàng cũ và thiết bị y tế có thể hạn chế các lựa chọn về công nghệ, mạng và lưu trữ.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A technical architect provides technical leadership and architectural design.

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 6 | [Kiến trúc sư kỹ thuật trợ lý](#bậc-6-kiến-trúc-sư-kỹ-thuật-trợ-lý) | Associate technical architect | EO/HEO | 412 |
| 7 | [Kiến trúc sư kỹ thuật](#bậc-7-kiến-trúc-sư-kỹ-thuật) | Technical architect | SEO/G7 | 496 |
| 8a | [Kiến trúc sư kỹ thuật cao cấp](#bậc-8a-kiến-trúc-sư-kỹ-thuật-cao-cấp) | Senior technical architect | SEO/G7 | 560 |
| 8b | [Trưởng nhóm kiến trúc sư kỹ thuật](#bậc-8b-trưởng-nhóm-kiến-trúc-sư-kỹ-thuật) | Lead technical architect | G7/G6 | 613 |
| 8c | [Kiến trúc sư kỹ thuật chủ chốt](#bậc-8c-kiến-trúc-sư-kỹ-thuật-chủ-chốt) | Principal technical architect | G6 | 662 |

## Bậc 6: Kiến trúc sư kỹ thuật trợ lý

**Cấp UK GDaD PCF: Associate technical architect**

> An associate technical architect supports technical architects in putting forward designs as solutions to technology challenges, usually under supervision.
> 
> At this role level, you will:
> - work closely with developers when designing appropriate solutions
> - have an understanding of the overall strategy and how your work supports it

### Trách nhiệm

- Vẽ sơ đồ kỹ thuật và ghi tài liệu về các thành phần, lưu trữ và tích hợp của các dịch vụ hiện có.
- Nghiên cứu các phương án công nghệ và tóm tắt ưu nhược điểm của chúng, với sự hướng dẫn.
- Làm việc với lập trình viên để kiểm tra các bản dựng tuân theo thiết kế và mẫu đã thống nhất.
- Ghi lại các quyết định kỹ thuật và cập nhật tài liệu thiết kế.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Nhận biết | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Nhận biết | You can:<br>• show an awareness of different ways of creating architecture representations for a limited audience, including technical and non-technical stakeholders<br>• gather and explain information to be used in architecture representations |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Nhận biết | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Nhận biết | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Nhận biết | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Vận dụng | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• mô tả các bộ phận chính của hệ thống y tế và chăm sóc cùng các dịch vụ mà tổ chức hỗ trợ<br>• giải thích vì sao an toàn và bảo mật cho bệnh nhân quan trọng trong công việc của bạn |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• tuân theo các quy tắc của tổ chức về xử lý thông tin cá nhân và thông tin y tế<br>• nhận biết và báo cáo một vụ vi phạm dữ liệu hoặc suýt xảy ra vi phạm |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích hệ thống CNTT y tế có thể gây hại cho bệnh nhân như thế nào, ví dụ qua thông tin sai, thiếu hoặc chậm<br>• báo cáo một vấn đề an toàn lâm sàng có thể xảy ra qua đúng kênh |

### Trình độ và kinh nghiệm thông thường

- Có bằng đại học về máy tính hoặc một ngành liên quan, hoặc kinh nghiệm tương đương về kỹ thuật phần mềm hoặc hạ tầng.
- Có kiến thức chuyên sâu về thiết kế kỹ thuật, ở mức văn bằng sau đại học hoặc kinh nghiệm tương đương.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên sâu về nhiều quy trình, được xây dựng qua đào tạo thêm hoặc kinh nghiệm.
- **Quyền tự chủ:** Làm việc độc lập; diễn giải chính sách cho lĩnh vực của mình; xin ý kiến về các vấn đề phức tạp.
- **Phạm vi:** Một sản phẩm, dịch vụ hoặc mảng công việc.
- **Lãnh đạo:** Có thể dẫn dắt một nhóm nhỏ hoặc kèm cặp đồng nghiệp.
- **Trách nhiệm giải trình:** Kết quả của mảng công việc của mình và chất lượng lời khuyên đưa ra.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 4 | 32 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 6 | 156 |
| 3 | Kỹ năng phân tích và đánh giá | 4 | 42 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 3 | 27 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 3 | 21 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 1 | 5 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 4 | 32 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 3 | 12 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **412** (Bậc 6: 396–465) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 5): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 6. Kiến thức được chấm ở mức văn bằng sau đại học, và nguồn lực thông tin ở mức 5 vì công việc thiết kế các phần của các hệ thống thông tin lớn.

## Bậc 7: Kiến trúc sư kỹ thuật

**Cấp UK GDaD PCF: Technical architect**

> A technical architect is responsible for the design and build of technical architecture.
> 
> At this role level, you will:
> - undertake structured analysis of technical issues, translating this analysis into technical designs that describe a solution
> - be consulted about design and provide design patterns
> - identify deeper issues that need fixing
> - look for opportunities to collaborate and reuse components, communicating with both technical and non-technical stakeholders

### Trách nhiệm

- Thiết kế kiến trúc kỹ thuật cho một dịch vụ, gồm thành phần, lưu trữ, tích hợp và an ninh.
- Cung cấp các mẫu thiết kế cho các nhóm triển khai và rà soát thiết kế kỹ thuật và cấu trúc mã của họ.
- Xác định các yêu cầu phi chức năng, như mục tiêu về tính sẵn sàng, hiệu năng và khôi phục, cùng chủ sở hữu dịch vụ.
- Nhận diện nợ kỹ thuật và công nghệ không còn được hỗ trợ, và lập kế hoạch khắc phục.
- Nhận diện các mối nguy kỹ thuật và biện pháp kiểm soát cho hồ sơ an toàn lâm sàng.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Vận dụng | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Vận dụng | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Vận dụng | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Vận dụng | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Vận dụng | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Vận dụng | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• tuân theo các quy tắc truy cập và bảo vệ thông tin xác thực của bạn |

### Trình độ và kinh nghiệm thông thường

- Có kiến thức chuyên sâu về kiến trúc kỹ thuật, ở trình độ thạc sĩ hoặc kinh nghiệm tương đương.
- Có kinh nghiệm thiết kế hoặc xây dựng phần mềm hoặc hạ tầng đang vận hành.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên sâu ở mức cao, thường tương đương trình độ thạc sĩ hoặc kinh nghiệm tương đương.
- **Quyền tự chủ:** Làm việc theo chính sách của tổ chức; tự quyết định cách đạt kết quả; là chuyên gia mà người khác tham vấn.
- **Phạm vi:** Một số sản phẩm hoặc dịch vụ, hoặc một chức năng chuyên môn.
- **Lãnh đạo:** Dẫn dắt một nhóm hoặc một lĩnh vực thực hành chuyên môn.
- **Trách nhiệm giải trình:** Việc cung cấp một dịch vụ hoặc chức năng chuyên môn, và ngân sách nếu được giao.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 5 | 45 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 7 | 196 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 3 | 27 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 3 | 21 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 2 | 12 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 4 | 32 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **496** (Bậc 7: 466–539) |

Được xếp bậc theo gợi ý ngạch của UK GDaD PCF là Bậc 7, phù hợp với các tin tuyển dụng trong ngành y tế cho vai trò này. Kiến thức được chấm ở trình độ thạc sĩ hoặc tương đương cho kiến thức chuyên sâu trên toàn bộ phạm vi kiến trúc kỹ thuật.

## Bậc 8a: Kiến trúc sư kỹ thuật cao cấp

**Cấp UK GDaD PCF: Senior technical architect**

> A senior technical architect works on large or multiple pieces of work that are complex or risky.
> 
> At this role level, you will:
> - define strategy and be central to assuring services
> - regularly collaborate and find agreement with senior stakeholders, providing direction and challenge
> - be proactive in identifying problems and translating these into non-technical descriptions that can be widely understood
> - mentor and coach junior colleagues

### Trách nhiệm

- Dẫn dắt thiết kế kỹ thuật của các dịch vụ lớn, phức tạp hoặc rủi ro cao, như hệ thống lâm sàng và nền tảng tích hợp dùng chung.
- Đề ra định hướng kỹ thuật cho một hoặc nhiều nhóm triển khai và phản biện các thiết kế làm tăng rủi ro.
- Thiết kế cho khả năng phục hồi, khôi phục sau thảm họa và vận hành an toàn, và kiểm tra các nhóm có kiểm thử chúng.
- Giải thích các rủi ro và đánh đổi kỹ thuật cho chủ sở hữu dịch vụ, trưởng nhóm lâm sàng và các bên liên quan cấp cao bằng ngôn ngữ giản dị.
- Kèm cặp và huấn luyện các kiến trúc sư kỹ thuật và lập trình viên cao cấp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Vận dụng | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Thành thạo | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Vận dụng | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Vận dụng | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Thành thạo | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tạo, thay đổi và xóa tài khoản người dùng và quyền truy cập<br>• kiểm tra quyền truy cập theo các quy tắc truy cập dựa trên vai trò |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích rằng một số phần mềm y tế bị quản lý như thiết bị y tế<br>• biết hỏi ai khi một sản phẩm có thể là thiết bị y tế |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về thiết kế kỹ thuật cho các dịch vụ phức tạp, ở mức tương đương bằng thạc sĩ.

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

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 7): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8a. Lập kế hoạch, chính sách và quyền tự chủ hành động được chấm cao hơn hồ sơ Bậc 7 vì công việc đề ra định hướng kỹ thuật cho nhiều nhóm với ít sự giám sát.

## Bậc 8b: Trưởng nhóm kiến trúc sư kỹ thuật

**Cấp UK GDaD PCF: Lead technical architect**

> A lead technical architect works with multiple projects or teams on problems that require broad architectural thinking.
> 
> At this role level, you will:
> - be responsible for leading the technical design of systems and services, justifying and communicating design decisions
> - assure other services and system quality, ensuring the technical work fits into the broader strategy for government
> - explore the benefits of cross-government alignment
> - provide mentoring within teams
> - provide leadership to other architects

### Trách nhiệm

- Dẫn dắt kiến trúc kỹ thuật trên nhiều dịch vụ hoặc nhóm, đề ra các mẫu thiết kế và tiêu chuẩn dùng chung.
- Đảm bảo chất lượng kỹ thuật của thiết kế tại các cơ quan thẩm định thiết kế, gồm an ninh, khả năng phục hồi và khả năng tương tác.
- Định hình lộ trình công nghệ của tổ chức cùng kiến trúc sư doanh nghiệp và các trưởng nhóm kỹ thuật.
- Tư vấn cho các lãnh đạo cấp cao về lựa chọn công nghệ, đầu tư nền tảng và rủi ro kỹ thuật.
- Dẫn dắt và phát triển các kiến trúc sư kỹ thuật.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Thành thạo | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Thành thạo | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Chuyên gia | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và vận hành các dịch vụ danh tính và truy cập<br>• rà soát quyền truy cập định kỳ và khắc phục sự cố |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc kỹ thuật cho các dịch vụ phức tạp.

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
| 4 | Kỹ năng lập kế hoạch và tổ chức | 4 | 42 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 4 | 32 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 3 | 21 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **613** (Bậc 8b: 585–629) |

## Bậc 8c: Kiến trúc sư kỹ thuật chủ chốt

**Cấp UK GDaD PCF: Principal technical architect**

> A principal technical architect leads at the highest level and is responsible for making sure the strategy is agreed and followed.
> 
> At this role level, you will:
> - network and communicate with senior stakeholders across organisations
> - proactively seek opportunities for digital transformation
> - support multiple teams, finding and using best practice and emerging technologies
> - inspire other architects and help them understand how to deliver the goals of the organisation
> - be responsible for governance, solving complex and high risk issues or delivering architecture design

### Trách nhiệm

- Đề ra chiến lược, nguyên tắc và tiêu chuẩn kiến trúc kỹ thuật của tổ chức.
- Quản trị thiết kế kỹ thuật trong toàn tổ chức, kể cả cơ quan thẩm định thiết kế kỹ thuật.
- Tư vấn cho ban điều hành về các quyết định công nghệ lớn, như chiến lược lưu trữ và hợp nhất nền tảng.
- Đại diện tổ chức trong các cộng đồng kỹ thuật và tiêu chuẩn giữa nhiều tổ chức.
- Truyền cảm hứng và phát triển các kiến trúc sư trong toàn tổ chức.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Thành thạo | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Chuyên gia | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Chuyên gia | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Chuyên gia | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và vận hành các dịch vụ danh tính và truy cập<br>• rà soát quyền truy cập định kỳ và khắc phục sự cố |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc kỹ thuật trên nhiều nhóm hoặc tổ chức.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên gia, cùng hiểu biết rộng về tổ chức và ngành.
- **Quyền tự chủ:** Đề ra chiến lược cho một chức năng; chịu trách nhiệm trước một giám đốc.
- **Phạm vi:** Một chức năng hoặc một phòng ban.
- **Lãnh đạo:** Dẫn dắt một chức năng qua nhiều tầng quản lý.
- **Trách nhiệm giải trình:** Hiệu quả hoạt động, lực lượng lao động và ngân sách của một chức năng.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 6 | 60 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 8 | 240 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 5 | 60 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 5 | 45 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 3 | 21 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 6 | 46 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **662** (Bậc 8c: 630–674) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
