# Kỹ sư học máy

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Dữ liệu](../../#dữ-liệu)  
**Bậc:** 7, 8b  
**Vai trò UK GDaD PCF:** [Machine learning engineer](https://understand-digital-data-roles-skills.service.gov.uk/role/machine-learning-engineer/)  
**Nghề nghiệp ESCO:** [artificial intelligence engineer](http://data.europa.eu/esco/occupation/35553663-deab-4d9a-bf22-15c1625d28e8) (ISCO-08 2511)

## Tóm tắt

Kỹ sư học máy lấy các mô hình do nhà khoa học dữ liệu xây dựng, hoặc mua từ nhà cung cấp, và làm cho chúng hoạt động đáng tin cậy trong các dịch vụ y tế và chăm sóc đang vận hành. Họ xây dựng các đường ống huấn luyện, kiểm thử, triển khai và giám sát mô hình, và tích hợp chúng với các hệ thống lâm sàng và vận hành. Họ bảo đảm các mô hình luôn an toàn, bảo mật, công bằng và hiệu quả khi bệnh nhân và nhân viên thực sự dựa vào chúng.

## Trong một tổ chức chăm sóc sức khỏe số

- Các mô hình đang được sử dụng có thể trôi dạt khi nhóm dân số bệnh nhân, thực hành lâm sàng hoặc thói quen ghi chép thay đổi, nên hiệu quả được giám sát cho từng nhóm bệnh nhân và các mô hình được huấn luyện lại hoặc ngừng sử dụng khi cần.
- Một mô hình cung cấp thông tin cho chẩn đoán, phân loại hoặc điều trị có thể bị quản lý như thiết bị y tế, điều này kéo theo các yêu cầu chính thức về vòng đời phần mềm, kiểm soát thay đổi và giám sát sau khi đưa ra thị trường.
- Các hồ sơ an toàn lâm sàng cần bằng chứng về cách mô hình thất bại, cách kết quả của nó được hiển thị cho bác sĩ lâm sàng, và điều gì xảy ra khi nó không sẵn sàng.
- Các mô hình được huấn luyện trên dữ liệu bệnh nhân có thể làm rò rỉ thông tin về từng cá nhân, nên dữ liệu huấn luyện, tạo phẩm mô hình và nhật ký được bảo vệ như chính dữ liệu.
- AI tạo sinh và các mô hình ngôn ngữ lớn mang thêm các rủi ro, như nội dung bịa đặt trong ghi chú lâm sàng, cần kiểm thử cụ thể và sự giám sát của con người.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A machine learning engineer develops, assures and maintains machine learning models so they can be used in products and services.
> 
> In this role, you will:
> - be responsible for the software development and technical infrastructure needed to design, train, deploy and scale machine learning models
> - provide and maintain effective, secure and sustainable machine learning models for use in products and services
> - support all stages of the machine learning life cycle
> - help product teams evaluate and choose appropriate machine learning solutions

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 7 | [Kỹ sư học máy cao cấp](#bậc-7-kỹ-sư-học-máy-cao-cấp) | Senior machine learning engineer | SEO/G7/G6 | 495 |
| 8b | [Trưởng nhóm kỹ sư học máy](#bậc-8b-trưởng-nhóm-kỹ-sư-học-máy) | Lead machine learning engineer | G7/G6 | 595 |

## Bậc 7: Kỹ sư học máy cao cấp

**Cấp UK GDaD PCF: Senior machine learning engineer**

> A senior machine learning engineer develops machine learning models so they can be used in products and services.
> 
> At this role level, you will:
> - decide what model is most suitable for use in products and services
> - customise, optimise, re-train and maintain existing models
> - deploy models into production, testing and assuring them to ensure they meet performance requirements
> - work with others to integrate models with existing systems
> - check that models used in live products and services stay safe, secure and continue to work effectively

### Trách nhiệm

- Triển khai các mô hình vào các dịch vụ lâm sàng và vận hành đang vận hành, với kiểm thử tự động, quản lý phiên bản và quay lui.
- Xây dựng giám sát hiệu quả mô hình, sự trôi dạt và tính công bằng giữa các nhóm bệnh nhân, với cảnh báo và người phụ trách rõ ràng.
- Tích hợp các mô hình với các hệ thống lâm sàng, dùng các tiêu chuẩn mở như HL7 FHIR khi có thể.
- Lập bằng chứng về kiểm thử, thay đổi và giám sát cần cho các hồ sơ an toàn lâm sàng và hồ sơ kỹ thuật của thiết bị y tế.
- Đánh giá và điều chỉnh các mô hình của nhà cung cấp và mã nguồn mở để dùng tại địa phương, kể cả các mô hình AI tạo sinh.
- Huấn luyện các nhà khoa học dữ liệu và kỹ sư về thực hành kỹ thuật học máy.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../kỹ-năng/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | Thành thạo | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Thành thạo | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Data ethics and privacy](../../kỹ-năng/#data-ethics-and-privacy) | UK GDaD PCF | Thành thạo | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../kỹ-năng/#data-science-innovation) | UK GDaD PCF | Thành thạo | You can:<br>• demonstrate practical knowledge of data science tools and techniques<br>• develop data science solutions that maximise insight<br>• identify opportunities for how data science can improve data practices |
| [Programming and build (software engineering)](../../kỹ-năng/#programming-and-build-software-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Thành thạo | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tuân theo quy trình vòng đời phần mềm đáp ứng các tiêu chuẩn thiết bị y tế<br>• lập các hồ sơ mà quy trình đó yêu cầu |
| [AI an toàn và công bằng trong chăm sóc sức khỏe](../../kỹ-năng/#ai-an-toàn-và-công-bằng-trong-chăm-sóc-sức-khỏe) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• lập kế hoạch kiểm định, đánh giá thiên lệch và giám sát trực tiếp một mô hình cùng đồng nghiệp lâm sàng<br>• quyết định khi nào một mô hình cần được huấn luyện lại, hạn chế hoặc ngừng sử dụng<br>• tư vấn cho các nhóm về việc khi nào một mô hình có thể bị quản lý như thiết bị y tế và cần những bằng chứng nào |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về xây dựng và vận hành các hệ thống học máy trong môi trường vận hành, ở mức tương đương bằng thạc sĩ.

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
| | **Tổng** | | **495** (Bậc 7: 466–539) |

## Bậc 8b: Trưởng nhóm kỹ sư học máy

**Cấp UK GDaD PCF: Lead machine learning engineer**

> A lead machine learning engineer leads the technical development and deployment of machine learning models.
> 
> At this role level, you will:
> - lead the most complex technical work needed to develop models for use in products and services
> - co-ordinate moving a model from the research and development stage to production
> - define ways of working across the machine learning life cycle
> - identify training needs for machine learning engineers and related roles
> - help your team work with other teams and disciplines
> - assure the effectiveness of machine learning models in use across the organisation
> - define and communicate software standards and guidelines related to ethics, risk and security

### Trách nhiệm

- Dẫn dắt công việc phức tạp nhất để đưa các mô hình từ nghiên cứu vào sử dụng an toàn trong toàn tổ chức.
- Xác định vòng đời học máy, gồm các biện pháp kiểm soát cần thiết cho các mô hình chịu quản lý và quan trọng về an toàn.
- Đề ra tiêu chuẩn cho kiểm thử, giám sát, an ninh và đạo đức của mô hình, và đảm bảo các mô hình đang được sử dụng.
- Làm việc với cán bộ an toàn lâm sàng, quản trị thông tin và các chuyên gia về quy định để thống nhất cách các mô hình được đánh giá và phê duyệt.
- Xác định nhu cầu đào tạo và phát triển các kỹ sư học máy và các vai trò liên quan.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Applied maths, statistics and scientific practices](../../kỹ-năng/#applied-maths-statistics-and-scientific-practices) | UK GDaD PCF | Thành thạo | You can:<br>• apply designated quantitative techniques such as time series analysis, optimisation and simulation to create and embed appropriate models for analysis and prediction<br>• provide guidance on matching data sources with relevant applied mathematics and statistical techniques to meet analysis goals<br>• apply appropriate statistical techniques to available data to discover new relations and offer insight into research problems, helping to improve organisational processes and support decision making<br>• access and use the statistical tools available within the organisation |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Chuyên gia | You can:<br>• mediate between people and strengthen relationships, adopting the appropriate communication method with stakeholders at all levels<br>• manage stakeholder expectations and moderate difficult discussions about high risk and complex topics, even within constrained timescales<br>• speak on behalf of, and represent the community to, large audiences inside and outside the organisation |
| [Data ethics and privacy](../../kỹ-năng/#data-ethics-and-privacy) | UK GDaD PCF | Thành thạo | You can:<br>• work with stakeholders to identify and address ethical and privacy concerns<br>• demonstrate and communicate how data ethical issues fit into the wider organisational context<br>• research developments in data ethics and privacy to improve compliance and processes<br>• assess and constructively challenge proposed data ethics policies |
| [Data science innovation](../../kỹ-năng/#data-science-innovation) | UK GDaD PCF | Chuyên gia | You can:<br>• be a leader in the data science space<br>• demonstrate in-depth knowledge of data science tools and techniques, which you can use to solve problems creatively and to create opportunities for your team<br>• act as a coach, inspiring curiosity and creativity in others<br>• demonstrate in-depth knowledge of your chosen profession and keep up to date with changes in the industry<br>• challenge the status quo and always look for ways to improve data science |
| [Programming and build (software engineering)](../../kỹ-năng/#programming-and-build-software-engineering) | UK GDaD PCF | Chuyên gia | You can:<br>• advise on the right way to apply standards and methods to ensure compliance<br>• maintain technical responsibility for all the stages and iterations of a software development project<br>• provide technical advice to stakeholders and set the team-based standards for programming tools and techniques |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Chuyên gia | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quy định về phần mềm là thiết bị y tế](../../kỹ-năng/#quy-định-về-phần-mềm-là-thiết-bị-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• đánh giá một sản phẩm có phải là thiết bị y tế hay không, và phân loại có khả năng của nó<br>• lập kế hoạch công việc quy định cho một sản phẩm cùng đồng nghiệp về chất lượng và lâm sàng |
| [AI an toàn và công bằng trong chăm sóc sức khỏe](../../kỹ-năng/#ai-an-toàn-và-công-bằng-trong-chăm-sóc-sức-khỏe) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn của tổ chức về đảm bảo và giám sát AI trong chăm sóc<br>• dẫn dắt việc đảm bảo các mô hình rủi ro cao trước và sau khi triển khai<br>• đại diện tổ chức làm việc với các cơ quan quản lý và đối tác về AI an toàn và công bằng |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giám sát công việc hằng ngày và đưa ra phản hồi<br>• tham gia tuyển dụng và hướng dẫn nhân viên mới<br>• tổ chức các buổi trao đổi riêng định kỳ |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kỹ thuật học máy cho các dịch vụ phức tạp hoặc chịu quản lý.

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
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 5 | 45 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **595** (Bậc 8b: 585–629) |


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
