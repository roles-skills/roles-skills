# Kiến trúc sư an ninh

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Kiến trúc](../../#kiến-trúc)  
**Bậc:** 8a, 8b, 8c  
**Vai trò UK GDaD PCF:** [Security architect](https://understand-digital-data-roles-skills.service.gov.uk/role/security-architect/)  
**Nghề nghiệp ESCO:** [ICT system architect](http://data.europa.eu/esco/occupation/e1c72b5f-4c5c-487c-a6df-e84b64a51dae) (ISCO-08 2511); [cybersecurity risk manager](http://data.europa.eu/esco/occupation/7754d570-9519-48c2-b1c9-8e165f8bca0f) (ISCO-08 2529)

## Tóm tắt

Kiến trúc sư an ninh thiết kế an ninh cho các dịch vụ y tế số của tổ chức, để thông tin bệnh nhân luôn bí mật, chính xác và sẵn sàng khi việc chăm sóc cần. Họ đề ra các mẫu và biện pháp kiểm soát an ninh, đánh giá rủi ro an ninh của các thiết kế mới và nhà cung cấp, và giúp các nhóm đưa ra quyết định dựa trên rủi ro để các dịch vụ vừa an toàn vừa dễ dùng cho bác sĩ lâm sàng và bệnh nhân.

## Trong một tổ chức chăm sóc sức khỏe số

- Các tổ chức y tế là mục tiêu thường xuyên của mã độc tống tiền và đánh cắp dữ liệu, và một cuộc tấn công có thể làm ngừng các dịch vụ lâm sàng, nên tính sẵn sàng quan trọng ngang với tính bảo mật.
- Các biện pháp kiểm soát an ninh không được cản trở việc chăm sóc khẩn cấp, nên các thiết kế cân bằng giữa xác thực mạnh và truy cập nhanh trong môi trường lâm sàng.
- Các thiết bị y tế kết nối và hệ thống lâm sàng cũ thường không thể vá nhanh, nên các kiến trúc sư thiết kế các biện pháp kiểm soát bù đắp như phân đoạn.
- Nhiều nhân viên, tổ chức đối tác và nhà cung cấp cần truy cập hồ sơ bệnh nhân, nên danh tính, truy cập theo vai trò và kiểm toán là trọng tâm.
- Thiết kế an ninh phải hỗ trợ các nghĩa vụ quản trị thông tin và các tiêu chuẩn an ninh đã công bố, như ISO/IEC 27001.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A security architect designs and builds secure solutions.

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 8a | [Kiến trúc sư an ninh](#bậc-8a-kiến-trúc-sư-an-ninh) | Security architect | HEO/SEO/G7 | 560 |
| 8b | [Trưởng nhóm kiến trúc sư an ninh](#bậc-8b-trưởng-nhóm-kiến-trúc-sư-an-ninh) | Lead security architect | G7/G6 | 613 |
| 8c | [Kiến trúc sư an ninh chủ chốt](#bậc-8c-kiến-trúc-sư-an-ninh-chủ-chốt) | Principal security architect | G6 | 662 |

## Bậc 8a: Kiến trúc sư an ninh

**Cấp UK GDaD PCF: Security architect**

> A security architect creates and designs security for a system or service, maintains security documentation and develops architecture patterns and security approaches to new technologies.
> 
> At this role level, you will:
> - recommend security controls and identify solutions that support a business objective
> - provide specialist advice and recommend approaches across teams and various stakeholders
> - communicate widely with other stakeholders
> - advise on important security-related technologies and assess the risk associated with proposed changes
> - inspire and influence others to execute security principles
> - help review other people’s work

### Trách nhiệm

- Thiết kế các biện pháp kiểm soát an ninh cho dịch vụ và hệ thống, gồm danh tính, mã hóa, ghi nhật ký và bảo vệ mạng.
- Đánh giá an ninh của các thiết kế mới và sản phẩm của nhà cung cấp, và ghi lại rủi ro và các biện pháp kiểm soát đề xuất.
- Xây dựng các mẫu an ninh mà các nhóm triển khai có thể tái sử dụng, như đăng nhập của bệnh nhân và đăng nhập một lần của nhân viên.
- Tư vấn về các biện pháp kiểm soát bù đắp cho thiết bị y tế và hệ thống lâm sàng cũ không thể cập nhật dễ dàng.
- Làm việc với các đồng nghiệp về quản trị thông tin và an toàn lâm sàng để các rủi ro về an ninh, quyền riêng tư và an toàn được đánh giá cùng nhau.
- Huấn luyện các kỹ sư an ninh và kiến trúc sư khác về thiết kế an toàn.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Analysis](../../kỹ-năng/#analysis) | UK GDaD PCF | Vận dụng | You can:<br>• apply the approach to real problems and consider all relevant information<br>• apply appropriate rigour to ensure a full solution is designed and achieves the business outcome |
| [Communication (security architect)](../../kỹ-năng/#communication-security-architect) | UK GDaD PCF | Thành thạo | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../kỹ-năng/#designing-secure-systems) | UK GDaD PCF | Vận dụng | You can:<br>• design and review system architectures through the application of patterns and principles |
| [Enabling and informing risk-based decisions](../../kỹ-năng/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | Vận dụng | You can:<br>• work with risk owners to advise and give feedback<br>• advise on risk impact and whether it's within risk tolerance<br>• describe different risk methodologies and how these are applied, as well as the proportionality of risk |
| [Research and innovation](../../kỹ-năng/#research-and-innovation) | UK GDaD PCF | Vận dụng | You can:<br>• advise on developments to security properties in technology<br>• identify new technologies and design their use in a business context |
| [Security technology](../../kỹ-năng/#security-technology) | UK GDaD PCF | Vận dụng | You can:<br>• explain the effect of vulnerabilities on current and future designs<br>• share information on a range of systems, but may specialise in one |
| [Understanding security implications of transformation](../../kỹ-năng/#understanding-security-implications-of-transformation) | UK GDaD PCF | Vận dụng | You can:<br>• interpret and apply an understanding of policy and process, business architecture, and legal and political implications to assist the development of technical solutions or controls |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và vận hành các dịch vụ danh tính và truy cập<br>• rà soát quyền truy cập định kỳ và khắc phục sự cố |
| [Quản lý lỗ hổng](../../kỹ-năng/#quản-lý-lỗ-hổng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• ưu tiên các lỗ hổng theo rủi ro, kể cả rủi ro đối với các dịch vụ bệnh nhân<br>• xác định phạm vi và quản lý các đợt kiểm thử xâm nhập và việc khắc phục |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích rằng một số phần mềm y tế bị quản lý như thiết bị y tế<br>• biết hỏi ai khi một sản phẩm có thể là thiết bị y tế |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về kiến trúc an ninh hoặc kỹ thuật an ninh, ở mức tương đương bằng thạc sĩ.
- Có bằng cấp an ninh được công nhận hoặc kinh nghiệm tương đương.

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

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 6): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8a. Phân tích và quyền tự chủ hành động được chấm cao hơn hồ sơ Bậc 7 vì công việc thiết kế an ninh cho các hệ thống lâm sàng quan trọng với ít sự giám sát.

## Bậc 8b: Trưởng nhóm kiến trúc sư an ninh

**Cấp UK GDaD PCF: Lead security architect**

> A lead security architect undertakes complex work of a high risk level, often working on several projects.
> 
> At this role level, you will:
> - interact with senior stakeholders across departments
> - reach and influence a wide range of people across larger teams and communities
> - research and apply innovative security architecture solutions to new or existing problems and be able to justify and communicate design decisions
> - develop vision, principles and strategy for security architects for one project or technology
> - work out subtle security needs
> - understand the impact of decisions, balancing requirements and deciding between approaches
> - produce particular patterns and support quality assurance
> - be the point of escalation for architects in lower grade roles
> - lead the technical design of systems and services

### Trách nhiệm

- Dẫn dắt kiến trúc an ninh cho nhiều dự án rủi ro cao hoặc một mảng lớn, như hệ thống lâm sàng hoặc lưu trữ đám mây.
- Đề ra nguyên tắc và tiêu chuẩn an ninh cho các thiết kế trong mảng của bạn và đảm bảo chúng tại các cơ quan thẩm định thiết kế.
- Tư vấn cho các chủ sở hữu rủi ro cấp cao về rủi ro an ninh và các phương án quản lý chúng.
- Thiết kế an ninh cho dữ liệu chia sẻ với các tổ chức đối tác và nhà cung cấp.
- Dẫn dắt và phát triển các kiến trúc sư an ninh.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Analysis](../../kỹ-năng/#analysis) | UK GDaD PCF | Thành thạo | You can:<br>• monitor the analysis of a technical solution and ensure analysis is reused for similar problem sets<br>• review solutions and identify areas for change<br>• drive the collection of information that is used and analysed<br>• feed back on policy and requirements |
| [Communication (security architect)](../../kỹ-năng/#communication-security-architect) | UK GDaD PCF | Thành thạo | You can:<br>• demonstrate a deep understanding of security concepts and can apply them to a technical level<br>• effectively translate and accurately communicate security and risk implications to technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations and be flexible, adapting to stakeholder reactions to reach consensus |
| [Designing secure systems](../../kỹ-năng/#designing-secure-systems) | UK GDaD PCF | Thành thạo | You can:<br>• design and review system architectures through the development of patterns and principles |
| [Enabling and informing risk-based decisions](../../kỹ-năng/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | Thành thạo | You can:<br>• work with higher impact or more complex risks, advising on the impact and whether it's within risk tolerance<br>• apply different risk methodologies in proportion to the risk |
| [Research and innovation](../../kỹ-năng/#research-and-innovation) | UK GDaD PCF | Thành thạo | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../kỹ-năng/#security-technology) | UK GDaD PCF | Chuyên gia | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../kỹ-năng/#understanding-security-implications-of-transformation) | UK GDaD PCF | Thành thạo | You can:<br>• interpret and apply understanding across a complex area<br>• start influencing policy and process, business architecture, and legal and political implications |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chiến lược danh tính và truy cập cho nhân viên, bệnh nhân và hệ thống<br>• dẫn dắt việc áp dụng các tiêu chuẩn danh tính mới |
| [Quản lý lỗ hổng](../../kỹ-năng/#quản-lý-lỗ-hổng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• ưu tiên các lỗ hổng theo rủi ro, kể cả rủi ro đối với các dịch vụ bệnh nhân<br>• xác định phạm vi và quản lý các đợt kiểm thử xâm nhập và việc khắc phục |
| [Vận hành an ninh](../../kỹ-năng/#vận-hành-an-ninh) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giám sát cảnh báo và phân loại chúng theo sổ tay vận hành<br>• thu thập bằng chứng và báo cáo lên cấp trên các sự kiện<br>• tinh chỉnh các quy tắc phát hiện đơn giản dưới sự hướng dẫn |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• vận hành quy trình rủi ro cho một ban hoặc chương trình<br>• đánh giá rủi ro theo khẩu vị rủi ro và báo cáo lên cấp trên<br>• báo cáo về rủi ro cho các ủy ban |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng về kiến trúc an ninh cho các dịch vụ phức tạp.

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

## Bậc 8c: Kiến trúc sư an ninh chủ chốt

**Cấp UK GDaD PCF: Principal security architect**

> A principal security architect works on services of high complexity and risk, making decisions to enable the business to achieve its needs.
> 
> At this role level, you will:
> - work on projects with high strategic impact, setting a strategy that can be used in the long term and across the breadth of the organisation
> - communicate with a broad range of senior stakeholders and be responsible for defining the vision, principles and strategy for security architects
> - recommend security design across several projects or technologies, up to an organisational or inter-organisational level
> - have a deep and evolving level of technical expertise, so you can act as an exemplar
> - make and influence important business and architectural decisions
> - research, identify, validate and adopt new technologies and methodologies
> - be a recognised expert and demonstrate this expertise by solving unprecedented issues and problems
> - further the profession, demonstrating and sharing best practice within and outside the organisation

### Trách nhiệm

- Đề ra tầm nhìn, nguyên tắc và chiến lược kiến trúc an ninh của tổ chức.
- Tư vấn cho ban điều hành và hội đồng về rủi ro an ninh mạng đối với việc chăm sóc bệnh nhân và dịch vụ.
- Bảo đảm khả năng phục hồi trước tấn công mạng, kể cả phục hồi sau một cuộc tấn công lớn, được thiết kế sẵn trong các dịch vụ lâm sàng quan trọng.
- Đại diện tổ chức trong các cộng đồng về an ninh mạng và tiêu chuẩn giữa nhiều tổ chức.
- Dẫn dắt ngành thực hành kiến trúc an ninh và phát triển con người trong ngành này.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Analysis](../../kỹ-năng/#analysis) | UK GDaD PCF | Chuyên gia | You can:<br>• provide direction and lead on change regarding factors that feed into analysis<br>• monitor changes in the technical environment and assess whether risks are still at acceptable levels or whether previous decisions need to be revisited<br>• direct and influence others on best practice and policy |
| [Communication (security architect)](../../kỹ-năng/#communication-security-architect) | UK GDaD PCF | Chuyên gia | You can:<br>• demonstrate expert understanding of security concepts and can apply them to a technical level, at the highest levels of risk complexity<br>• effectively translate and accurately communicate security and risk implications at the most senior levels across technical and non-technical stakeholders<br>• successfully respond to challenges<br>• manage stakeholder expectations across high risk and complexity or under constrained timescales |
| [Designing secure systems](../../kỹ-năng/#designing-secure-systems) | UK GDaD PCF | Chuyên gia | You can:<br>• lead design and review solutions to complex problems with system architectures by defining and challenging patterns and principles<br>• create precedents and set direction |
| [Enabling and informing risk-based decisions](../../kỹ-năng/#enabling-and-informing-risk-based-decisions) | UK GDaD PCF | Chuyên gia | You can:<br>• act as a point of escalation<br>• be trusted by senior risk owners as an expert in security<br>• apply risk methodologies at the most complex levels of risk |
| [Research and innovation](../../kỹ-năng/#research-and-innovation) | UK GDaD PCF | Thành thạo | You can:<br>• contribute to and inform developments on security properties in technology<br>• identify new technologies and design the use of these in the business context across the organisation<br>• engage with the broader security community |
| [Security technology](../../kỹ-năng/#security-technology) | UK GDaD PCF | Chuyên gia | You can:<br>• explain complex system architectures<br>• identify and explain how easy or difficult it will be to exploit vulnerabilities<br>• lead and influence security technology in the security industry |
| [Understanding security implications of transformation](../../kỹ-năng/#understanding-security-implications-of-transformation) | UK GDaD PCF | Chuyên gia | You can:<br>• challenge and lead changes to policy and processes to support business outcomes, business architecture, and legal and political implications |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chính sách và chiến lược quản trị thông tin<br>• tư vấn cho hội đồng về rủi ro thông tin và việc tuân thủ<br>• đại diện tổ chức làm việc với các cơ quan quản lý và đối tác |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chiến lược danh tính và truy cập cho nhân viên, bệnh nhân và hệ thống<br>• dẫn dắt việc áp dụng các tiêu chuẩn danh tính mới |
| [Quản lý lỗ hổng](../../kỹ-năng/#quản-lý-lỗ-hổng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• ưu tiên các lỗ hổng theo rủi ro, kể cả rủi ro đối với các dịch vụ bệnh nhân<br>• xác định phạm vi và quản lý các đợt kiểm thử xâm nhập và việc khắc phục |
| [Vận hành an ninh](../../kỹ-năng/#vận-hành-an-ninh) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• điều tra và ngăn chặn các sự cố an ninh<br>• viết các quy tắc phát hiện và thực hiện săn tìm mối đe dọa<br>• cải thiện sổ tay vận hành và công cụ sau các sự cố |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [Quản lý rủi ro của tổ chức](../../kỹ-năng/#quản-lý-rủi-ro-của-tổ-chức) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• thiết kế khung quản lý rủi ro và khẩu vị rủi ro của tổ chức<br>• tư vấn cho hội đồng về các rủi ro chiến lược |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc an ninh giữa các tổ chức.

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
