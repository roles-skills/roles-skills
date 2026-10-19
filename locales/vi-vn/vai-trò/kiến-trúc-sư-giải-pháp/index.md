# Kiến trúc sư giải pháp

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Kiến trúc](../../#kiến-trúc)  
**Bậc:** 7, 8a, 8b, 8c, 8d  
**Vai trò UK GDaD PCF:** [Solution architect](https://understand-digital-data-roles-skills.service.gov.uk/role/solution-architect/)  
**Nghề nghiệp ESCO:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511)

## Tóm tắt

Kiến trúc sư giải pháp thiết kế cách một dịch vụ mới hoặc đã thay đổi sẽ hoạt động đầu cuối, từ nhu cầu người dùng và quy trình lâm sàng đến ứng dụng, dữ liệu, tích hợp, lưu trữ và an ninh. Họ bảo đảm mỗi giải pháp phù hợp với kiến trúc của tổ chức, đáp ứng nhu cầu về an toàn, quyền riêng tư và khả năng tương tác, và có thể được xây dựng, vận hành và hỗ trợ với chi phí hợp lý.

## Trong một tổ chức chăm sóc sức khỏe số

- Các giải pháp thường kết hợp hệ thống lâm sàng mua ngoài, dịch vụ nội bộ và nền tảng dùng chung, nên các kiến trúc sư phải thiết kế xuyên qua ranh giới nhà cung cấp.
- Các lựa chọn thiết kế có thể đưa vào các mối nguy lâm sàng, như mất kết quả hoặc khớp nhầm bệnh nhân, nên thiết kế giải pháp đóng góp vào hồ sơ an toàn lâm sàng.
- Mỗi luồng dữ liệu mới về thông tin bệnh nhân cần có cơ sở pháp lý và đánh giá tác động bảo vệ dữ liệu, nên các kiến trúc sư làm việc chặt chẽ với quản trị thông tin.
- Khả năng tương tác với các tổ chức y tế và chăm sóc khác, dùng các tiêu chuẩn như HL7 FHIR, thường là yêu cầu cốt lõi.
- Một số giải pháp bao gồm phần mềm là thiết bị y tế, điều này thay đổi yêu cầu về thiết kế, đảm bảo và nhà cung cấp.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A solution architect designs solutions for problems that affect the organisation.
> 
> In this role, you will:
> - ensure a problem and the desired outcomes are properly defined
> - ensure the scope of a solution meets the organisation's requirements
> - stay up to date on technology trends and approaches
> - understand organisational objectives and external drivers, for example, legislation or financial constraints
> - work with others to develop business and technical strategies
> - work within business and technical constraints
> - design and document solutions so they can be implemented by the organisation
> - comply with standards and governance
> - communicate and work effectively with stakeholders
> - manage risks and decisions in a transparent way

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 7 | [Kiến trúc sư giải pháp trợ lý](#bậc-7-kiến-trúc-sư-giải-pháp-trợ-lý) | Associate solution architect | HEO/SEO | 483 |
| 8a | [Kiến trúc sư giải pháp](#bậc-8a-kiến-trúc-sư-giải-pháp) | Solution architect | SEO/G7 | 560 |
| 8b | [Kiến trúc sư giải pháp cao cấp](#bậc-8b-kiến-trúc-sư-giải-pháp-cao-cấp) | Senior solution architect | G7 | 604 |
| 8c | [Trưởng nhóm kiến trúc sư giải pháp](#bậc-8c-trưởng-nhóm-kiến-trúc-sư-giải-pháp) | Lead solution architect | G7/G6 | 655 |
| 8d | [Kiến trúc sư giải pháp chủ chốt](#bậc-8d-kiến-trúc-sư-giải-pháp-chủ-chốt) | Principal solution architect | G6 | 699 |

## Bậc 7: Kiến trúc sư giải pháp trợ lý

**Cấp UK GDaD PCF: Associate solution architect**

> An associate solution architect supports other solution architects to design solutions. You will usually work under supervision.
> 
> At this role level, you will:
> - support the design of solutions by working with stakeholders
> - help your team achieve its objectives

### Trách nhiệm

- Thu thập yêu cầu từ các nhóm sản phẩm, bác sĩ lâm sàng và nhà cung cấp để làm căn cứ cho thiết kế giải pháp.
- Vẽ sơ đồ hiện trạng và trạng thái mục tiêu, như các góc nhìn về ngữ cảnh, luồng dữ liệu và tích hợp.
- Soạn thảo các phần của thiết kế giải pháp và hồ sơ quyết định dưới sự giám sát.
- Kiểm tra thiết kế theo các tiêu chuẩn kiến trúc, yêu cầu về an ninh và quản trị thông tin.
- Giúp chuẩn bị thiết kế để rà soát tại các cơ quan thẩm định thiết kế.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Nhận biết | You can:<br>• identify relevant information that can inform your architectural work, such as strategies, roadmaps, policies and technical trends<br>• understand how your work supports the team in enabling change​ |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Vận dụng | You can:<br>• listen to the needs of technical and business stakeholders<br>• create and use different architecture representations to communicate effectively, achieving agreement with technical and non-technical stakeholders<br>• provide support in discussions about architectural topics within a multidisciplinary team |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Nhận biết | You can:<br>• show an awareness of government commercial processes<br>• show an awareness of legal and compliance rules |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Nhận biết | You can:<br>• understand the work of others and the importance of team dynamics, collaboration and feedback |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Nhận biết | You can:<br>• describe the reasoning behind architectural design decisions<br>• gather information to inform decisions<br>• understand architectural governance and assurance relevant to your work |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Vận dụng | You can:<br>• help to frame a problem characterised by managed levels of complexity, complication, or risk so that a solution can be created<br>• help to create options for solving problems at an appropriate level of detail |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Nhận biết | You can:<br>• explain how organisational objectives link to designing strategy<br>• describe the purpose and application of strategy, standards, patterns, policies, roadmaps, vision, and mission statements |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Vận dụng | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |

### Trình độ và kinh nghiệm thông thường

- Có kiến thức chuyên sâu về thiết kế giải pháp, ở trình độ thạc sĩ hoặc kinh nghiệm tương đương.
- Có kinh nghiệm về phân tích, phát triển hoặc thiết kế kỹ thuật.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên sâu ở mức cao, thường tương đương trình độ thạc sĩ hoặc kinh nghiệm tương đương.
- **Quyền tự chủ:** Làm việc theo chính sách của tổ chức; tự quyết định cách đạt kết quả; là chuyên gia mà người khác tham vấn.
- **Phạm vi:** Một số sản phẩm hoặc dịch vụ, hoặc một chức năng chuyên môn.
- **Lãnh đạo:** Dẫn dắt một nhóm hoặc một lĩnh vực thực hành chuyên môn.
- **Trách nhiệm giải trình:** Việc cung cấp một dịch vụ hoặc chức năng chuyên môn, và ngân sách nếu được giao.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 4 | 32 |
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
| | **Tổng** | | **483** (Bậc 7: 466–539) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 6): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 7. Kiến thức được chấm ở trình độ thạc sĩ hoặc tương đương, vì công việc thiết kế xuyên qua ứng dụng, dữ liệu, tích hợp và an ninh.

## Bậc 8a: Kiến trúc sư giải pháp

**Cấp UK GDaD PCF: Solution architect**

> A solution architect is responsible for a single solution. They usually work independently on solutions where risk is low. They also often support or contribute to work led by more senior solution architects.
> 
> At this role level, you will:
> - build relationships with stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - follow best practice for solution design
> - use emerging technologies and approaches
> - help your team achieve its objective

### Trách nhiệm

- Thiết kế các giải pháp đầu cuối cho các dịch vụ rủi ro thấp hơn, như công cụ cho nhân viên hoặc các dịch vụ đơn giản hướng tới bệnh nhân.
- So sánh các phương án, gồm mua, xây dựng và tái sử dụng nền tảng dùng chung, và đề xuất một phương án với lý do rõ ràng.
- Thiết kế các tích hợp, luồng dữ liệu, và danh tính và truy cập cho giải pháp, dùng các tiêu chuẩn mở khi có.
- Đóng góp vào việc nhận diện mối nguy và đánh giá tác động bảo vệ dữ liệu cho giải pháp.
- Trình bày thiết kế cho các cơ quan thẩm định thiết kế và hỗ trợ các nhóm triển khai qua giai đoạn xây dựng và đưa vào vận hành.
- Huấn luyện và rà soát công việc của các kiến trúc sư giải pháp trợ lý.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Vận dụng | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Thành thạo | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Vận dụng | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Vận dụng | You can:<br>• contribute to the work of others<br>• motivate and empower teams<br>• create the right environment for teams to work in, and can identify the best team makeup depending on the situation<br>• recognise and deal with issues |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Vận dụng | You can:<br>• work with others to make architectural design decisions characterised by managed levels of risk and complexity<br>• identify and address architectural risks relevant to your team or domain, for example, business, data, or security<br>• engage with architectural governance and assurance to effectively manage decisions and risks, with support |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Thành thạo | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Vận dụng | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Vận dụng | You can:<br>• create technical designs characterised by managed levels of risk, impact, and complexity<br>• provide guidance and support to teams using technical designs throughout the life cycle<br>• adapt a technical design if needed during delivery<br>• work with well-understood technology and identify appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tạo, thay đổi và xóa tài khoản người dùng và quyền truy cập<br>• kiểm tra quyền truy cập theo các quy tắc truy cập dựa trên vai trò |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về thiết kế giải pháp hoặc kỹ thuật phần mềm, ở mức tương đương bằng thạc sĩ.

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

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 7): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8a. Lập kế hoạch, chính sách và quyền tự chủ hành động được chấm cao hơn hồ sơ Bậc 7 vì công việc làm chủ các thiết kế đầu cuối và đề xuất phương án cho các cơ quan thẩm định thiết kế.

## Bậc 8b: Kiến trúc sư giải pháp cao cấp

**Cấp UK GDaD PCF: Senior solution architect**

> A senior solution architect is responsible for a single, more complex, solution. They usually work on solutions where the risk is moderate. They may lead and coach other solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across different business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects
> - find and use emerging technologies and approaches
> - support others to follow best practice for solution architecture

### Trách nhiệm

- Thiết kế các giải pháp phức tạp có rủi ro vừa phải, như hệ thống lâm sàng hoặc dịch vụ được dùng trên nhiều tổ chức.
- Dẫn dắt đánh giá kỹ thuật các sản phẩm của nhà cung cấp trong các gói mua sắm, gồm khả năng tương tác, an ninh và an toàn.
- Thiết kế cho khả năng phục hồi và duy trì hoạt động kinh doanh khi giải pháp hỗ trợ chăm sóc suốt ngày đêm.
- Làm việc với cán bộ an toàn lâm sàng để các quyết định thiết kế và biện pháp kiểm soát rủi ro được ghi lại trong hồ sơ an toàn.
- Huấn luyện và rà soát công việc của các kiến trúc sư giải pháp khác.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Vận dụng | You can:<br>• align your work with the work being done by other architects and technical professionals<br>• track emerging issues, strategies, roadmaps, patterns and technologies over time to assess opportunities and risks to your work<br>• identify how other teams contribute to delivering outcomes through change |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Thành thạo | You can:<br>• lead the communication of complicated, complex or risky architecture topics with technical and non-technical stakeholders<br>• communicate with senior stakeholders across your organisation<br>• adapt your message and communication techniques to your audience<br>• advocate on behalf of a team to other stakeholders<br>• manage stakeholder expectations effectively |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Vận dụng | You can:<br>• understand commercial processes and the appropriate internal contacts within a government department<br>• understand different sourcing strategies and when to apply them |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Thành thạo | You can:<br>• frame a problem characterised by medium complexity, complication, or risk so that a solution can be created<br>• produce architectural representations that enable different teams to have a shared understanding of problems throughout the life cycle<br>• describe options for solving problems so that appropriate delivery methods can be decided |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Vận dụng | You can:<br>• support the development of a strategy or vision that aligns with organisational objectives<br>• challenge requirements and assumptions, and identify opportunities to develop strategy<br>• support the implementation of a strategy or vision, for example, by using a roadmap or plan<br>• use architectural principles, patterns, and constraints when appropriate |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Thành thạo | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tạo, thay đổi và xóa tài khoản người dùng và quyền truy cập<br>• kiểm tra quyền truy cập theo các quy tắc truy cập dựa trên vai trò |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích rằng một số phần mềm y tế bị quản lý như thiết bị y tế<br>• biết hỏi ai khi một sản phẩm có thể là thiết bị y tế |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• ghi nhận và cập nhật các rủi ro cho lĩnh vực của bạn<br>• đề xuất các biện pháp kiểm soát và theo dõi các hành động |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc thiết kế các giải pháp phức tạp trên nhiều ngành, ở mức vượt bằng thạc sĩ.

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
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 2 | 12 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **604** (Bậc 8b: 585–629) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 8a): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8b. Kiến thức được chấm ở mức 8 cho kiến thức chuyên sâu trên nhiều ngành, như ứng dụng, dữ liệu, tích hợp, an ninh và an toàn lâm sàng.

## Bậc 8c: Trưởng nhóm kiến trúc sư giải pháp

**Cấp UK GDaD PCF: Lead solution architect**

> A lead solution architect is responsible for a group of solution architecture projects, or a single more complex area. They may lead teams of more junior solution architects.
> 
> At this role level, you will:
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation
> - be proactive in identifying opportunities to improve the organisation
> - support multiple architecture projects or programmes
> - find and use emerging technologies and approaches
> - develop best practice for solution architecture

### Trách nhiệm

- Dẫn dắt kiến trúc giải pháp cho một chương trình hoặc một mảng phức tạp, như thay thế hồ sơ bệnh nhân điện tử.
- Bảo đảm các giải pháp trên toàn chương trình nhất quán, có khả năng tương tác và phù hợp với kiến trúc mục tiêu.
- Tư vấn cho các ban chương trình về rủi ro thiết kế, các phụ thuộc, lựa chọn nhà cung cấp và chi phí.
- Đảm bảo thiết kế của các kiến trúc sư giải pháp khác tại các cơ quan thẩm định thiết kế.
- Dẫn dắt và phát triển một nhóm các kiến trúc sư giải pháp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Thành thạo | You can:<br>• work to support wider organisational objectives beyond your immediate goals​<br>• track emerging internal and external issues over time that could affect the work of teams across the organisation<br>• take action to solve or mitigate problems by influencing colleagues across the organisation |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Thành thạo | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Thành thạo | You can:<br>• work collaboratively in a group, actively networking with others<br>• adapt feedback to ensure it’s effective and lasting<br>• use your initiative to identify problems or issues in the team dynamic and rectify them<br>• identify issues through Agile ‘health checks’ with the team, and help to stimulate the right responses |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• make and guide architectural design decisions characterised by medium risk and complexity<br>• identify and address architectural risks that affect multiple teams or domains<br>• use architectural governance and assurance to make design decisions and manage technical risks at the appropriate level<br>• contribute to the development of architectural governance and assurance |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Chuyên gia | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Thành thạo | You can:<br>• define strategies or visions across teams that align with organisational objectives<br>• direct the implementation of a strategy or vision, for example, by creating roadmaps or plans<br>• define architectural principles and patterns<br>• develop or maintain strategy in response to feedback and findings |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Chuyên gia | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc giải pháp cho các chương trình phức tạp.

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
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **655** (Bậc 8c: 630–674) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 8b): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8c. Lập kế hoạch, chính sách và con người được chấm cao hơn hồ sơ Bậc 8b vì công việc lập kế hoạch kiến trúc của cả một chương trình và dẫn dắt một nhóm các kiến trúc sư giải pháp.

## Bậc 8d: Kiến trúc sư giải pháp chủ chốt

**Cấp UK GDaD PCF: Principal solution architect**

> A principal solution architect can be responsible for a large programme or group of solution architecture projects, or a single, very complex or critical business area.
> 
> At this role level, you will:
> - lead teams of more junior solution architects
> - lead multiple architecture projects or programmes
> - build relationships with senior stakeholders across multiple business or technical areas in the organisation and its partners
> - be proactive in identifying opportunities to improve the organisation and its partners
> - work with technology partners to inform their roadmaps
> - take a leading role in the overall direction of business and digital capabilities
> - inspire other architects and help them understand how to meet organisational goals

### Trách nhiệm

- Dẫn dắt kiến trúc giải pháp cho các chương trình lớn nhất hoặc quan trọng nhất của tổ chức.
- Đề ra tiêu chuẩn, mẫu thiết kế và phương pháp kiến trúc giải pháp cho tổ chức.
- Tư vấn cho các giám đốc và tổ chức đối tác về thiết kế các dịch vụ y tế và chăm sóc dùng chung, quan trọng.
- Giải quyết các xung đột thiết kế khó nhất giữa các chương trình, nhà cung cấp và tổ chức đối tác.
- Dẫn dắt ngành thực hành kiến trúc giải pháp và phát triển con người trong ngành này.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Architect for the whole context](../../kỹ-năng/#architect-for-the-whole-context) | UK GDaD PCF | Chuyên gia | You can:<br>• assess how trends in society and industry practices might impact the organisation<br>• work with people outside of your organisation to inform policies, strategies and standards<br>• anticipate changes to policy and build resilience through your architectural work<br>• coach others in identifying important trends |
| [Architecture communication](../../kỹ-năng/#architecture-communication) | UK GDaD PCF | Chuyên gia | You can:<br>• communicate with technical and non-technical stakeholders at all levels, and across organisations, using architecture communication techniques​<br>• mediate between people in difficult architectural discussions<br>• gain support from business and technical stakeholders for architectural initiatives with high levels of risk, impact and complexity<br>• coach and support others in architecture communication |
| [Commercial perspective](../../kỹ-năng/#commercial-perspective) | UK GDaD PCF | Thành thạo | You can:<br>• identify appropriate contractual frameworks and approaches<br>• identify, evaluate and select appropriate suppliers |
| [Community collaboration](../../kỹ-năng/#community-collaboration) | UK GDaD PCF | Chuyên gia | You can:<br>• solve and unblock issues between teams or departments at the highest level<br>• coach the organisation on team dynamics and conflict resolution, while also building and growing the community |
| [Making architectural decisions](../../kỹ-năng/#making-architectural-decisions) | UK GDaD PCF | Chuyên gia | You can:<br>• make and guide architectural design decisions characterised by high levels of risk and complexity<br>• identify and address architectural risks across the organisation or wider government<br>• lead and evolve architectural governance and assurance<br>• represent architectural governance as part of wider governance, for example, legal or commercial |
| [Problem definition and shaping](../../kỹ-năng/#problem-definition-and-shaping) | UK GDaD PCF | Chuyên gia | You can:<br>• lead the framing of a problem characterised by high complexity, complication, or risk so that a solution can be created<br>• coach others in defining problems and describing appropriate options for solutions<br>• help others challenge requirements and assumptions, and identify opportunities when defining problems and solution options |
| [Strategy design](../../kỹ-năng/#strategy-design) | UK GDaD PCF | Chuyên gia | You can:<br>• define and connect strategies or visions across the organisation or wider government<br>• enable the implementation of strategies or visions across the organisation or wider government, for example, by advocating for resources and removing blockers |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Chuyên gia | You can:<br>• create technical designs characterised by high risk, impact, and complexity<br>• lead and guide others in creating technical designs that achieve organisational objectives<br>• use feedback to optimise and refine standards for technical designs throughout the life cycle |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• định hình chiến lược của tổ chức bằng hiểu biết sâu về hệ thống y tế và chăm sóc<br>• đại diện tổ chức làm việc với các đối tác và lãnh đạo y tế và chăm sóc<br>• dự đoán những thay đổi về chính sách và dịch vụ sẽ ảnh hưởng đến các dịch vụ số và việc chăm sóc như thế nào |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chính sách và chiến lược quản trị thông tin<br>• tư vấn cho hội đồng về rủi ro thông tin và việc tuân thủ<br>• đại diện tổ chức làm việc với các cơ quan quản lý và đối tác |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |
| [Quản lý ngân sách](../../kỹ-năng/#quản-lý-ngân-sách) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• theo dõi chi tiêu so với một ngân sách nhỏ và báo cáo chênh lệch<br>• phê duyệt chi tiêu trong hạn mức của bạn |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc giải pháp trên nhiều chương trình hoặc tổ chức.

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
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 5 | 45 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 4 | 32 |
| 9 | Trách nhiệm đối với con người | 4 | 32 |
| 10 | Trách nhiệm về nguồn lực thông tin | 6 | 46 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 6 | 60 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **699** (Bậc 8d: 675–720) |

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 8c): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8d. Quyền tự chủ hành động ở mức 6 vì công việc đề ra tiêu chuẩn kiến trúc giải pháp của tổ chức; nguồn lực tài chính và con người ở mức 4 vì dẫn dắt ngành thực hành và ngân sách của nó.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
