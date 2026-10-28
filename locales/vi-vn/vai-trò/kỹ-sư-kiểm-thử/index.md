# Kỹ sư kiểm thử

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Đảm bảo chất lượng và kiểm thử](../../#đảm-bảo-chất-lượng-và-kiểm-thử)  
**Bậc:** 4, 6, 7, 8a  
**Vai trò UK GDaD PCF:** [Test engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/test-engineer/)  
**Nghề nghiệp ESCO:** [software tester](http://data.europa.eu/esco/occupation/106f79e4-6264-45f1-9e7a-297435cd684b) (ISCO-08 2519)

## Tóm tắt

Kỹ sư kiểm thử xây dựng các kiểm thử tự động, công cụ và khung giúp các nhóm kiểm thử các dịch vụ y tế số của tổ chức nhanh chóng và thường xuyên. Họ viết mã để kiểm thử chức năng, tích hợp, hiệu năng, an ninh và khả năng phục hồi, và đưa kiểm thử vào các đường ống phân phối, để các thay đổi đối với hệ thống lâm sàng và hướng tới bệnh nhân có thể được phát hành một cách an toàn.

## Trong một tổ chức chăm sóc sức khỏe số

- Các hệ thống lâm sàng quan trọng về an toàn, nên các kiểm thử hồi quy tự động bảo vệ các biện pháp kiểm soát an toàn được ghi trong nhật ký mối nguy và được giữ làm bằng chứng cho hồ sơ an toàn.
- Các tích hợp với hệ thống y tế và chăm sóc khác cần kiểm thử tự động theo các tiêu chuẩn như HL7 FHIR và HL7 phiên bản 2, thường dùng các hệ thống đối tác mô phỏng.
- Các dịch vụ lâm sàng hoạt động suốt ngày đêm và đạt đỉnh vào những thời điểm có thể dự đoán, nên kiểm thử hiệu năng và khả năng phục hồi mô hình hóa nhu cầu lâm sàng thực tế.
- Môi trường kiểm thử không được chứa dữ liệu bệnh nhân thật, nên các kỹ sư tạo dữ liệu tổng hợp thực tế, kể cả các trường hợp lâm sàng hiếm và biên.
- Phần mềm bị quản lý như thiết bị y tế cần kiểm thử có thể truy vết, lặp lại được như một phần của vòng đời theo các tiêu chuẩn như IEC 62304.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A test engineer designs, builds, automates and executes comprehensive, robust and maintainable test suites. They apply test engineering standards, perform exploratory testing and use diverse techniques to identify risks and improve testing efficiency and quality.
> 
> In this role you will:
> - maintain automated tests in continuous integration, continuous delivery (CI/CD) pipelines
> - use, develop and standardise reusable frameworks and tools following engineering practices and standards
> - analyse and test artefacts such as products, services and business processes
> - promote quality considerations throughout the development life cycle
> - support the resolution of technical issues

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 4 | [Kỹ sư kiểm thử trợ lý](#bậc-4-kỹ-sư-kiểm-thử-trợ-lý) | Associate test engineer | EO | 275 |
| 6 | [Kỹ sư kiểm thử](#bậc-6-kỹ-sư-kiểm-thử) | Test engineer | HEO/SEO | 411 |
| 7 | [Kỹ sư kiểm thử cao cấp](#bậc-7-kỹ-sư-kiểm-thử-cao-cấp) | Senior test engineer | SEO/G7 | 477 |
| 8a | [Trưởng nhóm kỹ sư kiểm thử](#bậc-8a-trưởng-nhóm-kỹ-sư-kiểm-thử) | Lead test engineer | SEO/G7/G6 | 553 |

## Bậc 4: Kỹ sư kiểm thử trợ lý

**Cấp UK GDaD PCF: Associate test engineer**

> An associate test engineer works closely with other test professionals to learn test engineering activities and techniques.
> 
> At this role level, you will:
> - contribute to and maintain technical test suites under supervision
> - follow engineering practices and standards to apply test approaches, plans and strategies under supervision
> - analyse artefacts such as user stories, prototypes, processes and designs with support
> - support the development of reports, recording of outcomes and resolution of defects
> - understand the technical tooling and engineering approach to design and execute tests

### Trách nhiệm

- Viết và duy trì các kiểm thử tự động đơn giản dưới sự giám sát, theo các tiêu chuẩn kỹ thuật của nhóm.
- Chạy các kiểm thử tự động và thủ công và ghi chính xác kết quả.
- Giúp điều tra và báo cáo lỗi, kể cả trong các tích hợp với hệ thống lâm sàng.
- Dùng dữ liệu kiểm thử tổng hợp và tuân thủ các quy tắc quản trị thông tin trong môi trường kiểm thử.
- Học các công cụ kiểm thử, thực hành viết mã và quy trình an toàn lâm sàng của nhóm.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Nhận biết | You can:<br>• explain why it's important to communicate technical concepts in non-technical language<br>• explain the types of communication that can be used with internal and external stakeholders, and their impact |
| [Designing and executing tests](../../kỹ-năng/#designing-and-executing-tests) | UK GDaD PCF | Nhận biết | You can:<br>• contribute to deciding the most appropriate test types and techniques to use<br>• follow guidance to design, build and maintain simple tests that align to user needs and requirements<br>• execute simple tests with support<br>• explain the value of automation within testing |
| [Managing, reporting and resolving defects](../../kỹ-năng/#managing-reporting-and-resolving-defects) | UK GDaD PCF | Nhận biết | You can:<br>• explain how to report and track defects<br>• follow a defect management process to report, communicate and maintain defects with appropriate information<br>• retest and escalate defects when needed |
| [Test analysis](../../kỹ-năng/#test-analysis) | UK GDaD PCF | Nhận biết | You can:<br>• describe quality characteristics and explain why they are important<br>• analyse information, such as user stories, prototypes, processes and designs, with support<br>• explain what might be a risk in achieving quality goals |
| [Test and quality planning](../../kỹ-năng/#test-and-quality-planning) | UK GDaD PCF | Nhận biết | You can:<br>• explain the value of quality testing approaches, plans and strategies<br>• explain how different delivery methodologies affect quality testing approaches, plans and strategies<br>• follow quality testing approaches, plans and strategies, with support<br>• explain how to measure the effectiveness of quality testing approaches, plans and strategies, and why it’s important |
| [Test engineering](../../kỹ-năng/#test-engineering) | UK GDaD PCF | Nhận biết | You can:<br>• explain why testing processes, environments and tools are important<br>• follow test engineering practices and standards, with support<br>• support the maintenance of automated tests and tools required for testing |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• mô tả các bộ phận chính của hệ thống y tế và chăm sóc cùng các dịch vụ mà tổ chức hỗ trợ<br>• giải thích vì sao an toàn và bảo mật cho bệnh nhân quan trọng trong công việc của bạn |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích hệ thống CNTT y tế có thể gây hại cho bệnh nhân như thế nào, ví dụ qua thông tin sai, thiếu hoặc chậm<br>• báo cáo một vấn đề an toàn lâm sàng có thể xảy ra qua đúng kênh |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• tuân theo các quy tắc của tổ chức về xử lý thông tin cá nhân và thông tin y tế<br>• nhận biết và báo cáo một vụ vi phạm dữ liệu hoặc suýt xảy ra vi phạm |

### Trình độ và kinh nghiệm thông thường

- Có một số kinh nghiệm viết mã hoặc kiểm thử, hoặc đã đăng ký chương trình học nghề liên quan, hoặc tương đương.

### Mô tả bậc

- **Kiến thức:** Hiểu biết chi tiết về lĩnh vực công việc, thường có từ bằng cao đẳng, học nghề hoặc kinh nghiệm tương đương.
- **Quyền tự chủ:** Làm việc trong khuôn khổ hướng dẫn; giải quyết hầu hết các vấn đề hằng ngày; có quản lý để xin ý kiến.
- **Phạm vi:** Công việc của bản thân và một dịch vụ hoặc quy trình được xác định.
- **Lãnh đạo:** Có thể giám sát một nhóm nhỏ hoặc điều phối công việc của người khác.
- **Trách nhiệm giải trình:** Việc thực hiện một dịch vụ hoặc quy trình được xác định.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 3 | 21 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 4 | 88 |
| 3 | Kỹ năng phân tích và đánh giá | 3 | 27 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 2 | 15 |
| 5 | Kỹ năng thể chất | 3 | 27 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 2 | 12 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 1 | 5 |
| 10 | Trách nhiệm về nguồn lực thông tin | 3 | 16 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 2 | 12 |
| 13 | Nỗ lực thể chất | 2 | 7 |
| 14 | Nỗ lực trí tuệ | 3 | 12 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **275** (Bậc 4: 271–325) |

## Bậc 6: Kỹ sư kiểm thử

**Cấp UK GDaD PCF: Test engineer**

> A test engineer develops solutions to enable more efficient testing. They follow engineering standards to design and execute appropriate technical tests.
> 
> At this role level, you will:
> - determine test scope and estimate the effort required
> - select and use the most appropriate test approaches and techniques to mitigate risk
> - use technical tooling and engineering approaches to design and execute tests
> - develop and maintain technical test suites
> - develop reports, record outcomes and support the resolution of defects
> - contribute to and follow engineering practices and standards

### Trách nhiệm

- Thiết kế và xây dựng các kiểm thử chức năng, tích hợp và API tự động cho các dịch vụ lâm sàng và hướng tới bệnh nhân.
- Xây dựng các kiểm thử kiểm tra thông điệp theo hồ sơ cấu hình HL7 FHIR và các đặc tả tương tác khác.
- Tạo dữ liệu bệnh nhân tổng hợp bao gồm các trường hợp lâm sàng thực tế và biên.
- Thêm kiểm thử vào các đường ống phân phối để các kiểm tra liên quan đến an toàn chạy trên mỗi thay đổi.
- Ước tính công sức kiểm thử, báo cáo kết quả và hỗ trợ giải quyết lỗi.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Vận dụng | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Designing and executing tests](../../kỹ-năng/#designing-and-executing-tests) | UK GDaD PCF | Vận dụng | You can:<br>• set up suitable environments with some support<br>• select appropriate test types and techniques with some support<br>• design, build, maintain and execute tests that align to user needs and requirements<br>• conduct exploratory testing<br>• research and try new test types and techniques |
| [Managing, reporting and resolving defects](../../kỹ-năng/#managing-reporting-and-resolving-defects) | UK GDaD PCF | Vận dụng | You can:<br>• collaborate with others to create a defect management process to report, communicate and resolve defects, with support<br>• critically assess dependencies, defects and risks, with support<br>• contribute to mitigation and contingency plans<br>• clearly communicate risks and the impact of defects to stakeholders |
| [Test analysis](../../kỹ-năng/#test-analysis) | UK GDaD PCF | Vận dụng | You can:<br>• work with stakeholders to determine which functional and non-functional quality characteristics add value<br>• determine what to test following an agreed approach<br>• identify and advocate for test needs, such as data, access and environments, with support<br>• analyse information to identify risks |
| [Test and quality planning](../../kỹ-năng/#test-and-quality-planning) | UK GDaD PCF | Vận dụng | You can:<br>• create or adapt quality testing approaches based on risk, with some support<br>• follow a quality testing strategy and contribute to its development<br>• contribute to continuous improvement of quality testing approaches, plans and strategies |
| [Test engineering](../../kỹ-năng/#test-engineering) | UK GDaD PCF | Vận dụng | You can:<br>• use test engineering frameworks and tools to support testing activities<br>• follow test engineering practices and standards, such as source control and continuous integration, continuous delivery (CI/CD) pipelines<br>• integrate and execute tests to ensure early testing and continuous feedback<br>• create and maintain automated tests, with some support<br>• write and review coded solutions, with some support |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |

### Trình độ và kinh nghiệm thông thường

- Có bằng đại học về máy tính hoặc một ngành liên quan, hoặc kinh nghiệm tương đương.
- Có kinh nghiệm xây dựng các kiểm thử tự động.

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
| 10 | Trách nhiệm về nguồn lực thông tin | 4 | 24 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 4 | 32 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **411** (Bậc 6: 396–465) |

## Bậc 7: Kỹ sư kiểm thử cao cấp

**Cấp UK GDaD PCF: Senior test engineer**

> A senior test engineer is responsible for test engineering in their area. They influence, coach and guide others in test engineering, sharing best practice and standards.
> 
> At this role level, you will:
> - select, use and guide others in using the most appropriate technical tooling, engineering approaches, test types and techniques to identify and address risks early
> - extend, standardise and build reusable frameworks and tools that support testing
> - communicate and document chosen approaches, tools, techniques and outcomes to the team and appropriate stakeholders
> - contribute to and agree engineering standards

### Trách nhiệm

- Dẫn dắt kỹ thuật kiểm thử cho một mảng, chọn công cụ, khung và loại kiểm thử giải quyết sớm các rủi ro của mảng đó.
- Xây dựng các khung kiểm thử và trình mô phỏng có thể tái sử dụng cho các hệ thống lâm sàng và tích hợp đối tác.
- Lập kế hoạch và thực hiện kiểm thử hiệu năng, tải và khả năng phục hồi dựa trên nhu cầu lâm sàng thực tế.
- Bảo đảm các kiểm thử tự động truy vết đến mối nguy và biện pháp kiểm soát an toàn và tạo bằng chứng cho hồ sơ an toàn.
- Huấn luyện và hướng dẫn các kỹ sư kiểm thử khác, và thống nhất tiêu chuẩn kỹ thuật với lập trình viên.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Thành thạo | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Designing and executing tests](../../kỹ-năng/#designing-and-executing-tests) | UK GDaD PCF | Thành thạo | You can:<br>• set up suitable environments<br>• influence and guide the use of appropriate test types and techniques to mitigate risk early<br>• lead others in designing, building, maintaining and executing tests that align to user needs and requirements<br>• contribute to developing and implementing standards for designing and executing tests<br>• improve test types and techniques through a structured process. |
| [Managing, reporting and resolving defects](../../kỹ-năng/#managing-reporting-and-resolving-defects) | UK GDaD PCF | Thành thạo | You can:<br>• contribute to developing standards for defect management processes<br>• manage and escalate dependencies, defects and risks across teams<br>• contribute to mitigation and contingency plans across teams<br>• use defect patterns and trends to make recommendations on testing and quality approaches, with support<br>• manage stakeholder expectations and communications during defect resolution |
| [Test analysis](../../kỹ-năng/#test-analysis) | UK GDaD PCF | Thành thạo | You can:<br>• lead work with stakeholders across teams to determine which functional and non-functional quality characteristics add value<br>• determine if an approach needs to change based on effort and risk<br>• ensure test needs are implemented early<br>• use multiple techniques to analyse complex information to identify risks<br>• coach others in test analysis |
| [Test and quality planning](../../kỹ-năng/#test-and-quality-planning) | UK GDaD PCF | Thành thạo | You can:<br>• work with teams to develop and implement appropriate quality testing approaches, plans and strategies<br>• contribute to organisational quality testing strategies<br>• implement ways to capture data to drive continuous improvement of quality testing approaches, plans and strategies<br>• advocate for full team ownership of quality testing activities, encouraging early engagement |
| [Test engineering](../../kỹ-năng/#test-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• develop, standardise and extend reusable frameworks and tools to support a range of testing activities<br>• guide and coach others in creating and maintaining comprehensive and reliable tests that meet standards<br>• research and prepare for future testing needs, including tools, methodologies and techniques<br>• maintain and adapt continuous integration, continuous delivery (CI/CD) pipelines |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích rằng một số phần mềm y tế bị quản lý như thiết bị y tế<br>• biết hỏi ai khi một sản phẩm có thể là thiết bị y tế |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về kỹ thuật kiểm thử, ở mức tương đương bằng thạc sĩ.

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

## Bậc 8a: Trưởng nhóm kỹ sư kiểm thử

**Cấp UK GDaD PCF: Lead test engineer**

> A lead test engineer sets the strategy for test engineering and influences test engineering practices across a broad area. They develop, monitor and evaluate quality engineering standards, and make strategic improvements to quality engineering in the organisation.
> 
> At this role level, you will:
> - lead a broad area in technical tooling, engineering approaches and test types and techniques to address risks early
> - define engineering standards, enabling others to follow them
> - lead and guide teams in quality engineering strategies and practices
> - lead and guide test engineers
> - escalate risks to senior stakeholders
> - lead and implement continuous testing, identifying opportunities to test earlier

### Trách nhiệm

- Đề ra chiến lược và tiêu chuẩn kỹ thuật kiểm thử trên một mảng rộng, gồm kiểm thử liên tục trong các đường ống phân phối.
- Dẫn dắt và hướng dẫn các kỹ sư kiểm thử và các nhóm về thực hành kỹ thuật chất lượng.
- Bảo đảm việc kiểm thử phần mềm chịu quản lý và quan trọng về an toàn đáp ứng các tiêu chuẩn yêu cầu và có thể truy vết.
- Báo cáo lên cấp trên các rủi ro về chất lượng và an toàn cho các trưởng nhóm sản phẩm, lâm sàng và nhà cung cấp cấp cao.
- Tìm cơ hội kiểm thử sớm hơn và thường xuyên hơn, và đo lường tác động đối với chất lượng.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Chuyên gia | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Designing and executing tests](../../kỹ-năng/#designing-and-executing-tests) | UK GDaD PCF | Chuyên gia | You can:<br>• set standards and influence organisational decisions for test types, techniques, design and execution<br>• coach others in test types, techniques, design and execution<br>• advocate for continuous improvement and refinement of test types and techniques<br>• make strategic decisions on new or improved test types and techniques used in your area |
| [Managing, reporting and resolving defects](../../kỹ-năng/#managing-reporting-and-resolving-defects) | UK GDaD PCF | Chuyên gia | You can:<br>• lead and coach others in improving test and defect management processes<br>• support others in assessing complex and challenging defects across the organisation<br>• lead and coach others in using defect patterns and trends to make tactical and strategic recommendations<br>• influence improvements to quality processes, informed by defect patterns and trends |
| [Test analysis](../../kỹ-năng/#test-analysis) | UK GDaD PCF | Chuyên gia | You can:<br>• lead and guide multiple teams in test analysis, ensuring it is implemented early in the life cycle<br>• advocate for risk-based analysis to drive improvements across many teams<br>• set standards and principles for test analysis across the organisation |
| [Test and quality planning](../../kỹ-năng/#test-and-quality-planning) | UK GDaD PCF | Chuyên gia | You can:<br>• create and manage multiple quality testing plans, approaches and strategies<br>• lead and guide multiple teams in adopting quality testing strategy<br>• advocate for early quality testing involvement in organisational delivery processes<br>• guide teams across an organisation in optimising quality testing approaches, plans and strategies by using appropriate data |
| [Test engineering](../../kỹ-năng/#test-engineering) | UK GDaD PCF | Chuyên gia | You can:<br>• establish and lead test engineering practices, standards and behaviours<br>• influence and guide test engineering technology and tool choices across the organisation<br>• advocate for the adoption and use of appropriate testing solutions, ensuring alignment with organisational goals and quality objectives |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giám sát công việc hằng ngày và đưa ra phản hồi<br>• tham gia tuyển dụng và hướng dẫn nhân viên mới<br>• tổ chức các buổi trao đổi riêng định kỳ |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kỹ thuật kiểm thử cho các dịch vụ phức tạp.

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
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 3 | 21 |
| 10 | Trách nhiệm về nguồn lực thông tin | 5 | 34 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 3 | 21 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **553** (Bậc 8a: 540–584) |

UK GDaD PCF gợi ý SEO đến G6 cho cấp này, tương ứng với Bậc 7, cùng bậc với kỹ sư kiểm thử cao cấp. Tài liệu tham khảo này xếp nó ở Bậc 8a, vì nó đề ra chiến lược và tiêu chuẩn kỹ thuật kiểm thử trên một mảng rộng.


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
