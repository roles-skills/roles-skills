# Kỹ sư dữ liệu

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Dữ liệu](../../#dữ-liệu)  
**Bậc:** 6, 7, 8a, 8b  
**Vai trò UK GDaD PCF:** [Data engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/data-engineer/)  
**Nghề nghiệp ESCO:** [data engineer](http://data.europa.eu/esco/occupation/2079755f-d809-49e6-8037-4de6180e54c0) (ISCO-08 2511)

## Tóm tắt

Kỹ sư dữ liệu xây dựng và vận hành các đường ống và nền tảng chuyển dữ liệu y tế và chăm sóc từ các hệ thống lâm sàng và vận hành đến nơi dữ liệu có thể được phân tích và sử dụng an toàn. Họ thiết kế luồng dữ liệu, tích hợp các nguồn dùng tiêu chuẩn khác nhau, và bảo đảm dữ liệu chính xác, kịp thời, an toàn và chỉ dành cho những người được phép xem.

## Trong một tổ chức chăm sóc sức khỏe số

- Các hệ thống nguồn gồm hồ sơ bệnh nhân điện tử, hệ thống xét nghiệm, chẩn đoán hình ảnh và dược, dùng các tiêu chuẩn như HL7 phiên bản 2, HL7 FHIR, SNOMED CT và ICD.
- Các đường ống thường mang dữ liệu bệnh nhân có thể nhận dạng, nên các kỹ sư tích hợp sẵn bút danh hóa, kiểm soát truy cập và ghi nhật ký kiểm toán ngay từ đầu.
- Một số luồng dữ liệu hỗ trợ chăm sóc trực tiếp, như cảnh báo hoặc danh sách bệnh nhân, nên một đường ống bị lỗi hoặc chậm có thể ảnh hưởng đến bệnh nhân và cần được đánh giá an toàn lâm sàng.
- Dữ liệu thường cần được liên kết giữa các môi trường chăm sóc, điều này phụ thuộc vào việc khớp bệnh nhân đáng tin cậy và mã định danh nhất quán.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A data engineer develops and constructs data products and services, and integrates them into systems and business processes.

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 6 | [Kỹ sư dữ liệu](#bậc-6-kỹ-sư-dữ-liệu) | Data engineer | HEO/SEO | 421 |
| 7 | [Kỹ sư dữ liệu cao cấp](#bậc-7-kỹ-sư-dữ-liệu-cao-cấp) | Senior data engineer | SEO/G7 | 477 |
| 8a | [Trưởng nhóm kỹ sư dữ liệu](#bậc-8a-trưởng-nhóm-kỹ-sư-dữ-liệu) | Lead data engineer | G7 | 551 |
| 8b | [Trưởng bộ phận kỹ thuật dữ liệu](#bậc-8b-trưởng-bộ-phận-kỹ-thuật-dữ-liệu) | Head of data engineering | G7/G6 | 589 |

## Bậc 6: Kỹ sư dữ liệu

**Cấp UK GDaD PCF: Data engineer**

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

### Trách nhiệm

- Xây dựng và duy trì các đường ống dữ liệu từ các hệ thống lâm sàng và vận hành đến nền tảng dữ liệu, theo các thiết kế đã thống nhất.
- Ánh xạ dữ liệu nguồn, kể cả dữ liệu lâm sàng đã mã hóa, sang các mô hình đích và ghi tài liệu các phép ánh xạ.
- Tích hợp bút danh hóa, kiểm định và kiểm tra chất lượng dữ liệu vào các đường ống.
- Giám sát các đường ống và sửa lỗi, ưu tiên các luồng dữ liệu hỗ trợ chăm sóc trực tiếp.
- Áp dụng kiểm soát truy cập và ghi nhật ký kiểm toán đáp ứng các quy tắc quản trị thông tin.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Nhận biết | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Vận dụng | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../kỹ-năng/#data-compliance-and-security) | UK GDaD PCF | Vận dụng | You can:<br>• use official data classification when authoring documents<br>• apply internal procedures, policies and technologies to ensure secure data handling<br>• identify and address ethical considerations when working with data<br>• address data compliance issues using internal processes |
| [Data development process](../../kỹ-năng/#data-development-process) | UK GDaD PCF | Vận dụng | You can:<br>• implement simple data solutions such as data pipelines, following established approaches and standards<br>• create repeatable, reliable and reusable data solutions |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Nhận biết | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data integration design](../../kỹ-năng/#data-integration-design) | UK GDaD PCF | Vận dụng | You can:<br>• design simple data exchange or integration solutions using established patterns or modelling techniques<br>• include security features in your data integration designs |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Vận dụng | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Vận dụng | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Nhận biết | You can:<br>• investigate problems in systems, processes and services, with an understanding of the level of a problem, for example, strategic, tactical or operational<br>• contribute to the implementation of remedies and preventative measures |
| [Programming and build (data and analytics engineering)](../../kỹ-năng/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Vận dụng | You can:<br>• design, code, test and deploy programs or scripts following standards and good practice<br>• write readable, maintainable code<br>• use automation to improve the software development life cycle<br>• consider and adopt appropriate security measures in your solutions |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích sự khác nhau giữa bộ thuật ngữ lâm sàng và bảng phân loại<br>• nhận biết các bộ thuật ngữ phổ biến như SNOMED CT và ICD |
| [Bút danh hóa và kiểm soát tiết lộ](../../kỹ-năng/#bút-danh-hóa-và-kiểm-soát-tiết-lộ) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• làm việc với dữ liệu đã bút danh hóa và áp dụng các kiểm tra tiết lộ trước khi công bố kết quả<br>• nhận biết khi dữ liệu được liên kết hoặc chi tiết có thể nhận dạng được một bệnh nhân |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích hệ thống CNTT y tế có thể gây hại cho bệnh nhân như thế nào, ví dụ qua thông tin sai, thiếu hoặc chậm<br>• báo cáo một vấn đề an toàn lâm sàng có thể xảy ra qua đúng kênh |

### Trình độ và kinh nghiệm thông thường

- Có bằng đại học về máy tính hoặc một ngành liên quan, hoặc kinh nghiệm tương đương.
- Có kinh nghiệm xây dựng các đường ống dữ liệu.

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
| 5 | Kỹ năng thể chất | 3 | 27 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 2 | 12 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 1 | 5 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 4 | 32 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **421** (Bậc 6: 396–465) |

## Bậc 7: Kỹ sư dữ liệu cao cấp

**Cấp UK GDaD PCF: Senior data engineer**

> A senior data engineer designs and leads the implementation of data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise opportunities to reuse existing data flows
> - lead the build of data streaming systems
> - optimise the code to ensure processes perform optimally
> - lead work on database management

### Trách nhiệm

- Thiết kế các luồng dữ liệu và dịch vụ phát trực tuyến tập hợp dữ liệu từ nhiều hệ thống y tế và chăm sóc.
- Thiết kế các quy trình khớp và liên kết bệnh nhân, và đo mức độ hiệu quả của chúng.
- Dẫn dắt công việc về hiệu năng cơ sở dữ liệu và nền tảng để dữ liệu sẵn sàng khi các dịch vụ cần.
- Đánh giá các rủi ro an toàn lâm sàng và quản trị thông tin của các luồng dữ liệu cùng các chuyên gia liên quan.
- Rà soát công việc của các kỹ sư khác và huấn luyện họ.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Vận dụng | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Vận dụng | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data compliance and security](../../kỹ-năng/#data-compliance-and-security) | UK GDaD PCF | Thành thạo | You can:<br>• consistently apply data ethics, legislation, internal procedures, policies and technologies to ensure secure data handling<br>• help ensure your team remain compliant by identifying and addressing current and potential data compliance and ethical issues<br>• guide and support others in addressing data compliance issues |
| [Data development process](../../kỹ-năng/#data-development-process) | UK GDaD PCF | Thành thạo | You can:<br>• lead the implementation of complex or large-scale data solutions<br>• apply appropriate technology and techniques to ensure data solutions are secure and scalable<br>• identify and implement continuous improvement to the operation and performance of data solutions |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Vận dụng | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data integration design](../../kỹ-năng/#data-integration-design) | UK GDaD PCF | Thành thạo | You can:<br>• select the most appropriate techniques for different integration scenarios<br>• evaluate and lead the implementation of integration using varied approaches that ensure security, efficiency and compliance |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Thành thạo | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Thành thạo | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Vận dụng | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Programming and build (data and analytics engineering)](../../kỹ-năng/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tìm và dùng đúng mã cho một mục dữ liệu hoặc biểu mẫu<br>• sử dụng trình duyệt thuật ngữ và các tập tham chiếu |
| [Bút danh hóa và kiểm soát tiết lộ](../../kỹ-năng/#bút-danh-hóa-và-kiểm-soát-tiết-lộ) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế các phương pháp bút danh hóa và liên kết giữ các mã định danh tách biệt khỏi dữ liệu phân tích<br>• đánh giá rủi ro nhận dạng lại của một tập dữ liệu hoặc ấn phẩm và chọn các biện pháp kiểm soát phù hợp<br>• tư vấn cho các nhóm về các môi trường an toàn, như môi trường nghiên cứu đáng tin cậy |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về thiết kế và xây dựng các hệ thống dữ liệu, ở mức tương đương bằng thạc sĩ.

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
| 3 | Kỹ năng phân tích và đánh giá | 4 | 42 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 3 | 27 |
| 5 | Kỹ năng thể chất | 3 | 27 |
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
| | **Tổng** | | **477** (Bậc 7: 466–539) |

## Bậc 8a: Trưởng nhóm kỹ sư dữ liệu

**Cấp UK GDaD PCF: Lead data engineer**

> A lead data engineer is responsible for the design and implementation of numerous complex data flows to connect operational systems, data for analytics and business intelligence (BI) systems.
> 
> At this role level, you will:
> - recognise and share opportunities to reuse existing data flows between teams
> - be responsible for the build of data-streaming systems
> - co-ordinate teams and set best practice and standards
> - apply knowledge of systems integration to your work
> - champion data engineering across government

### Trách nhiệm

- Dẫn dắt việc thiết kế và vận hành nền tảng dữ liệu của tổ chức và nhiều luồng dữ liệu của nó.
- Đề ra tiêu chuẩn kỹ thuật cho đường ống, kiểm thử, an ninh và tài liệu.
- Lập kế hoạch tích hợp dữ liệu với các đối tác y tế và chăm sóc, kể cả hồ sơ chăm sóc dùng chung và các dịch vụ dữ liệu khu vực.
- Bảo đảm các luồng dữ liệu hỗ trợ chăm sóc trực tiếp có khả năng phục hồi và có hồ sơ an toàn lâm sàng.
- Điều phối các nhóm kỹ thuật dữ liệu và quản lý trực tiếp các kỹ sư.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Thành thạo | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Thành thạo | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../kỹ-năng/#data-compliance-and-security) | UK GDaD PCF | Chuyên gia | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../kỹ-năng/#data-development-process) | UK GDaD PCF | Chuyên gia | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Thành thạo | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data integration design](../../kỹ-năng/#data-integration-design) | UK GDaD PCF | Chuyên gia | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Chuyên gia | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Thành thạo | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Thành thạo | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Programming and build (data and analytics engineering)](../../kỹ-năng/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• lead the design, code, testing and deployment of secure, resilient and maintainable solutions<br>• continuously improve the codebase and reliability of solutions<br>• create automation to improve the software development life cycle<br>• work with others to implement standards and good practice to ensure security, testability and maintainability of solutions |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tìm và dùng đúng mã cho một mục dữ liệu hoặc biểu mẫu<br>• sử dụng trình duyệt thuật ngữ và các tập tham chiếu |
| [Bút danh hóa và kiểm soát tiết lộ](../../kỹ-năng/#bút-danh-hóa-và-kiểm-soát-tiết-lộ) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế các phương pháp bút danh hóa và liên kết giữ các mã định danh tách biệt khỏi dữ liệu phân tích<br>• đánh giá rủi ro nhận dạng lại của một tập dữ liệu hoặc ấn phẩm và chọn các biện pháp kiểm soát phù hợp<br>• tư vấn cho các nhóm về các môi trường an toàn, như môi trường nghiên cứu đáng tin cậy |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kỹ thuật dữ liệu cho các hệ thống phức tạp.

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
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **551** (Bậc 8a: 540–584) |

## Bậc 8b: Trưởng bộ phận kỹ thuật dữ liệu

**Cấp UK GDaD PCF: Head of data engineering**

> A head of data engineering leads multi-functional delivery teams to deliver robust data services for their department, other government departments and private sector partners.
> 
> At this role level, you will:
> - inspire best practice for data products and services within your teams
> - build data engineering capability by providing technical leadership and career development for the community
> - work with other senior team members to identify, plan, develop and deliver data services

### Trách nhiệm

- Đề ra chiến lược cho các nền tảng dữ liệu và dịch vụ kỹ thuật dữ liệu của tổ chức.
- Dẫn dắt các nhóm đa ngành cung cấp dịch vụ dữ liệu cho các nhóm nội bộ và đối tác y tế và chăm sóc.
- Tư vấn cho các lãnh đạo cấp cao về rủi ro, chi phí và đầu tư của nền tảng dữ liệu.
- Bảo đảm các dịch vụ dữ liệu đáp ứng yêu cầu về quản trị thông tin, an ninh và an toàn lâm sàng.
- Xây dựng năng lực kỹ thuật dữ liệu thông qua tuyển dụng, phát triển và lộ trình nghề nghiệp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Chuyên gia | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Thành thạo | You can:<br>• understand and help teams to apply a range of techniques for data profiling<br>• source system analysis from a complex single source<br>• bring multiple data sources together in a conformed model for analysis |
| [Data compliance and security](../../kỹ-năng/#data-compliance-and-security) | UK GDaD PCF | Chuyên gia | You can:<br>• advise senior stakeholders on data security, ethical or procedural risks<br>• improve organisational awareness of data compliance and procedures<br>• lead, guide and mentor teams in implementing secure data practices and maintaining compliance |
| [Data development process](../../kỹ-năng/#data-development-process) | UK GDaD PCF | Chuyên gia | You can:<br>• establish cross-organisational data solutions that include all aspects of the data development life cycle<br>• define and promote good practices for creating repeatable, reliable and reusable data solutions |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Chuyên gia | You can:<br>• advocate for adoption of unfamiliar and emerging technologies, or familiar technologies in new data contexts, ensuring organisation objectives, user needs, and operational constraints inform decisions<br>• develop organisational capability in data innovation through leadership<br>• anticipate future technology changes and advise how to take advantage of them to realise value from data |
| [Data integration design](../../kỹ-năng/#data-integration-design) | UK GDaD PCF | Chuyên gia | You can:<br>• establish cross-organisational data integration standards and design patterns<br>• guide teams in designing secure and interoperable systems and services |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Vận dụng | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Chuyên gia | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Chuyên gia | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Programming and build (data and analytics engineering)](../../kỹ-năng/#programming-and-build-data-and-analytics-engineering) | UK GDaD PCF | Chuyên gia | You can:<br>• set standards for programming tools and techniques<br>• select appropriate development methods for a problem<br>• advise on the application of standards and methods that ensure security, maintainability and compliance<br>• take technical responsibility for all stages of a software development project, providing technical advice and guidance to stakeholders |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Bút danh hóa và kiểm soát tiết lộ](../../kỹ-năng/#bút-danh-hóa-và-kiểm-soát-tiết-lộ) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế các phương pháp bút danh hóa và liên kết giữ các mã định danh tách biệt khỏi dữ liệu phân tích<br>• đánh giá rủi ro nhận dạng lại của một tập dữ liệu hoặc ấn phẩm và chọn các biện pháp kiểm soát phù hợp<br>• tư vấn cho các nhóm về các môi trường an toàn, như môi trường nghiên cứu đáng tin cậy |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |
| [Quản lý ngân sách](../../kỹ-năng/#quản-lý-ngân-sách) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• nắm giữ và quản lý một ngân sách, dự báo và giải thích các chênh lệch<br>• xây dựng một luận chứng kinh doanh với chi phí và lợi ích |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kỹ thuật dữ liệu trên nhiều nhóm.

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
| 2 | Kiến thức, đào tạo và kinh nghiệm | 7 | 196 |
| 3 | Kỹ năng phân tích và đánh giá | 5 | 60 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 5 | 60 |
| 5 | Kỹ năng thể chất | 2 | 15 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 4 | 32 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 3 | 21 |
| 9 | Trách nhiệm đối với con người | 4 | 32 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **589** (Bậc 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
