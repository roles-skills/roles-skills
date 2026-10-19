# Kỹ sư tích hợp (khả năng tương tác của y tế)

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Phát triển phần mềm](../../#phát-triển-phần-mềm)  
**Bậc:** 5, 6, 7, 8a  
**Vai trò UK GDaD PCF:** không có (tài liệu tham khảo này tự xác định vai trò)  
**Nghề nghiệp ESCO:** [integration engineer](http://data.europa.eu/esco/occupation/07e60525-1aad-4099-aaf3-2c7014c92212) (ISCO-08 2511); [database developer](http://data.europa.eu/esco/occupation/b11e1742-5e28-4270-b081-b0193d85ee7d) (ISCO-08 2521)

## Tóm tắt

Kỹ sư tích hợp kết nối các hệ thống lâm sàng và nghiệp vụ của tổ chức để thông tin y tế và chăm sóc chảy an toàn đến nơi cần thiết. Họ thiết kế, xây dựng, kiểm thử và hỗ trợ các giao diện, API và luồng thông điệp dùng các tiêu chuẩn như HL7 FHIR và HL7 phiên bản 2, ánh xạ dữ liệu và mã lâm sàng giữa các hệ thống, và giữ cho các tích hợp hoạt động trong dịch vụ đang vận hành.

## Trong một tổ chức chăm sóc sức khỏe số

- Một thông điệp bị mất, chậm, trùng lặp hoặc khớp nhầm, như kết quả xét nghiệm hoặc giấy giới thiệu, có thể trực tiếp dẫn đến tổn hại, nên công việc tích hợp tuân theo quy trình quản lý rủi ro lâm sàng.
- Các tích hợp mang khối lượng lớn thông tin y tế bí mật giữa các tổ chức, nên mỗi luồng cần có cơ sở pháp lý, truyền tải an toàn và kiểm toán.
- Các hệ thống y tế dùng nhiều tiêu chuẩn và phiên bản, từ thông điệp HL7 phiên bản 2 đến API HL7 FHIR và các hồ sơ IHE, thường có các biến thể địa phương.
- Ý nghĩa lâm sàng phải được giữ nguyên trong suốt hành trình, nên các kỹ sư ánh xạ đúng các bộ thuật ngữ lâm sàng như SNOMED CT và khớp bệnh nhân một cách đáng tin cậy.
- Nhiều tích hợp hỗ trợ chăm sóc suốt ngày đêm, nên chúng cần giám sát, cảnh báo và các đường xử lý rõ ràng cho thông điệp lỗi.

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 5 | [Kỹ sư tích hợp sơ cấp](#bậc-5-kỹ-sư-tích-hợp-sơ-cấp) | — | — | 335 |
| 6 | [Kỹ sư tích hợp](#bậc-6-kỹ-sư-tích-hợp) | — | — | 418 |
| 7 | [Kỹ sư tích hợp cao cấp](#bậc-7-kỹ-sư-tích-hợp-cao-cấp) | — | — | 477 |
| 8a | [Trưởng nhóm kỹ sư tích hợp](#bậc-8a-trưởng-nhóm-kỹ-sư-tích-hợp) | — | — | 551 |

## Bậc 5: Kỹ sư tích hợp sơ cấp

Kỹ sư tích hợp sơ cấp xây dựng, kiểm thử và hỗ trợ các tích hợp giữa các hệ thống y tế và chăm sóc, làm việc theo đặc tả và với sự hướng dẫn của các kỹ sư có kinh nghiệm hơn.

### Trách nhiệm

- Xây dựng và thay đổi các phép ánh xạ thông điệp, biến đổi và lệnh gọi API từ các đặc tả đã thống nhất.
- Kiểm thử các tích hợp theo đặc tả và thông điệp mẫu, kể cả các trường hợp lỗi và biên.
- Giám sát luồng thông điệp, điều tra các thông điệp lỗi hoặc bị từ chối, và khắc phục hoặc báo lên cấp trên.
- Xử lý dữ liệu y tế một cách an toàn, theo các quy tắc quản trị thông tin cho dữ liệu thật và dữ liệu kiểm thử.
- Ghi lại các thay đổi và kết quả kiểm thử để chúng có thể dùng làm bằng chứng an toàn lâm sàng.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Vận dụng | You can:<br>• build and test simple interfaces between systems<br>• work on more complex integration as part of a wider team |
| [Programming and build (software engineering)](../../kỹ-năng/#programming-and-build-software-engineering) | UK GDaD PCF | Vận dụng | You can:<br>• design, code, test, correct and document simple programs or scripts under the direction of others |
| [Testing](../../kỹ-năng/#testing) | UK GDaD PCF | Vận dụng | You can:<br>• review requirements and specifications, and define test conditions<br>• identify issues and risks associated with work<br>• analyse and report test activities and results |
| [Service support](../../kỹ-năng/#service-support) | UK GDaD PCF | Vận dụng | You can:<br>• help fix service faults following agreed procedures<br>• carry out maintenance tasks on service support infrastructure |
| [Information security](../../kỹ-năng/#information-security) | UK GDaD PCF | Nhận biết | You can:<br>• explain information security and the security controls available to protect solutions and services |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• đọc và sử dụng các tài nguyên, hồ sơ cấu hình và API của FHIR<br>• xây dựng hoặc kiểm thử các tích hợp đơn giản dưới sự hướng dẫn<br>• kiểm tra thông điệp so với đặc tả |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích sự khác nhau giữa bộ thuật ngữ lâm sàng và bảng phân loại<br>• nhận biết các bộ thuật ngữ phổ biến như SNOMED CT và ICD |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• giải thích hệ thống CNTT y tế có thể gây hại cho bệnh nhân như thế nào, ví dụ qua thông tin sai, thiếu hoặc chậm<br>• báo cáo một vấn đề an toàn lâm sàng có thể xảy ra qua đúng kênh |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Nhận biết | Bạn có thể:<br>• mô tả các bộ phận chính của hệ thống y tế và chăm sóc cùng các dịch vụ mà tổ chức hỗ trợ<br>• giải thích vì sao an toàn và bảo mật cho bệnh nhân quan trọng trong công việc của bạn |

### Trình độ và kinh nghiệm thông thường

- Có bằng đại học về máy tính hoặc một ngành liên quan, đã hoàn thành chương trình học nghề, hoặc kinh nghiệm tương đương.

### Mô tả bậc

- **Kiến thức:** Kiến thức chuyên môn hoặc kỹ thuật, thường có từ bằng đại học hoặc kinh nghiệm tương đương.
- **Quyền tự chủ:** Làm việc theo các mục tiêu chung trong khuôn khổ chuẩn mực nghề nghiệp; tự lập kế hoạch công việc.
- **Phạm vi:** Công việc chuyên môn của bản thân trong một nhóm hoặc sản phẩm.
- **Lãnh đạo:** Có thể hướng dẫn và kiểm tra công việc của nhân viên hỗ trợ và học viên học nghề.
- **Trách nhiệm giải trình:** Chất lượng công việc chuyên môn của bản thân.

### Đánh giá công việc (minh họa)

| # | Yếu tố | Mức | Điểm |
| --- | --- | --- | --- |
| 1 | Kỹ năng giao tiếp và xây dựng quan hệ | 4 | 32 |
| 2 | Kiến thức, đào tạo và kinh nghiệm | 5 | 120 |
| 3 | Kỹ năng phân tích và đánh giá | 3 | 27 |
| 4 | Kỹ năng lập kế hoạch và tổ chức | 2 | 15 |
| 5 | Kỹ năng thể chất | 3 | 27 |
| 6 | Trách nhiệm chăm sóc bệnh nhân và khách hàng | 1 | 4 |
| 7 | Trách nhiệm phát triển chính sách và dịch vụ | 2 | 12 |
| 8 | Trách nhiệm về nguồn lực tài chính và vật chất | 1 | 5 |
| 9 | Trách nhiệm đối với con người | 1 | 5 |
| 10 | Trách nhiệm về nguồn lực thông tin | 4 | 24 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 3 | 21 |
| 13 | Nỗ lực thể chất | 2 | 7 |
| 14 | Nỗ lực trí tuệ | 3 | 12 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **335** (Bậc 5: 326–395) |

## Bậc 6: Kỹ sư tích hợp

Kỹ sư tích hợp thiết kế, xây dựng và hỗ trợ độc lập các tích hợp giữa các hệ thống y tế và chăm sóc, và giúp xác định cách các hệ thống nên trao đổi dữ liệu.

### Trách nhiệm

- Thiết kế và xây dựng các tích hợp, API và luồng thông điệp bằng HL7 FHIR, HL7 phiên bản 2 và các mẫu thông điệp.
- Phân tích các hệ thống nguồn và đích và viết đặc tả giao diện và ánh xạ dữ liệu, kể cả mã lâm sàng.
- Xây dựng việc khớp bệnh nhân, kiểm định và xử lý lỗi để thông tin đến đúng hồ sơ.
- Tham gia các buổi làm việc về mối nguy và tích hợp các biện pháp kiểm soát an toàn vào các tích hợp, như cảnh báo cho các thông điệp lỗi hoặc chậm.
- Làm việc với nhà cung cấp và các tổ chức đối tác để kiểm thử và đưa vào vận hành các kết nối mới.
- Điều tra và khắc phục sự cố trong các tích hợp đang vận hành, và kèm cặp các kỹ sư tích hợp sơ cấp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Thành thạo | You can:<br>• define the integration build<br>• co-ordinate build activities across systems<br>• understand how to undertake and support integration testing activities |
| [Programming and build (software engineering)](../../kỹ-năng/#programming-and-build-software-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../kỹ-năng/#systems-design) | UK GDaD PCF | Vận dụng | You can:<br>• translate logical designs into physical designs<br>• produce detailed designs<br>• effectively document all work using required standards, methods and tools, including prototyping tools where appropriate<br>• design systems characterised by managed levels of risk, manageable business and technical complexity, and meaningful impact<br>• work with well understood technology and identify appropriate patterns |
| [Service support](../../kỹ-năng/#service-support) | UK GDaD PCF | Thành thạo | You can:<br>• identify, locate and fix service faults |
| [Information security](../../kỹ-năng/#information-security) | UK GDaD PCF | Vận dụng | You can:<br>• use information security practices and available security controls to contribute to protecting solutions and services |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tìm và dùng đúng mã cho một mục dữ liệu hoặc biểu mẫu<br>• sử dụng trình duyệt thuật ngữ và các tập tham chiếu |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• áp dụng các nguyên tắc bảo vệ dữ liệu vào công việc của bạn<br>• đóng góp vào các đánh giá tác động bảo vệ dữ liệu<br>• xử lý đúng các yêu cầu về thông tin và hồ sơ |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |

### Trình độ và kinh nghiệm thông thường

- Có bằng đại học về máy tính hoặc một ngành liên quan, hoặc kinh nghiệm tương đương.
- Có kinh nghiệm xây dựng và hỗ trợ các tích hợp giữa các hệ thống đang vận hành.

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
| 9 | Trách nhiệm đối với con người | 2 | 12 |
| 10 | Trách nhiệm về nguồn lực thông tin | 4 | 24 |
| 11 | Trách nhiệm nghiên cứu và phát triển | 2 | 12 |
| 12 | Quyền tự chủ hành động | 4 | 32 |
| 13 | Nỗ lực thể chất | 1 | 3 |
| 14 | Nỗ lực trí tuệ | 4 | 18 |
| 15 | Nỗ lực cảm xúc | 1 | 5 |
| 16 | Điều kiện làm việc | 2 | 7 |
| | **Tổng** | | **418** (Bậc 6: 396–465) |

## Bậc 7: Kỹ sư tích hợp cao cấp

Kỹ sư tích hợp cao cấp dẫn dắt thiết kế và triển khai các tích hợp phức tạp trên nhiều hệ thống và tổ chức, và đề ra tiêu chuẩn tích hợp cho lĩnh vực của mình.

### Trách nhiệm

- Dẫn dắt thiết kế kỹ thuật của các tích hợp phức tạp, như hồ sơ chăm sóc dùng chung, kết quả và giấy giới thiệu giữa các tổ chức.
- Viết và duy trì các hồ sơ cấu hình FHIR, hướng dẫn triển khai và tiêu chuẩn giao diện cho tổ chức.
- Thiết kế các tích hợp an toàn, có khả năng phục hồi và có thể quan sát, với các đường xử lý lỗi rõ ràng.
- Làm việc với cán bộ an toàn lâm sàng để nhận diện các mối nguy của tích hợp và bảo đảm các biện pháp kiểm soát được thiết kế sẵn và kiểm thử.
- Bảo đảm mỗi luồng dữ liệu có cơ sở pháp lý và thỏa thuận chia sẻ dữ liệu đã thống nhất, làm việc với các đồng nghiệp quản trị thông tin.
- Huấn luyện và phát triển các kỹ sư tích hợp trong nhóm.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Chuyên gia | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Programming and build (software engineering)](../../kỹ-năng/#programming-and-build-software-engineering) | UK GDaD PCF | Thành thạo | You can:<br>• collaborate with others when necessary to review specifications<br>• use the agreed specifications to design, code, test and document programs or scripts of medium-to-high complexity, using the right standards and tools |
| [Systems design](../../kỹ-năng/#systems-design) | UK GDaD PCF | Thành thạo | You can:<br>• design systems characterised by medium levels of risk, impact, and business or technical complexity<br>• select appropriate design standards, methods and tools, and ensure they are applied effectively<br>• review the systems designs of others to ensure the selection of appropriate technology, efficient use of resources and integration of multiple systems and technology |
| [Information security](../../kỹ-năng/#information-security) | UK GDaD PCF | Thành thạo | You can:<br>• design solutions and services with security controls included, specifically engineered to mitigate security threats |
| [Stakeholder relationship management](../../kỹ-năng/#stakeholder-relationship-management) | UK GDaD PCF | Vận dụng | You can:<br>• identify important stakeholders and communicate with them clearly and regularly<br>• tailor communication to stakeholders' needs and work with them to build relationships while meeting user needs<br>• build and reach consensus with stakeholders<br>• work to improve stakeholder relationships using evidence to explain decisions |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế mô hình dữ liệu và tập tham chiếu bằng các bộ thuật ngữ lâm sàng<br>• ánh xạ giữa các bộ thuật ngữ và bảng phân loại, và giải thích giới hạn của một phép ánh xạ<br>• tư vấn cho các nhóm về việc dùng thuật ngữ trong sản phẩm và phân tích |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý danh tính và truy cập](../../kỹ-năng/#quản-lý-danh-tính-và-truy-cập) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tạo, thay đổi và xóa tài khoản người dùng và quyền truy cập<br>• kiểm tra quyền truy cập theo các quy tắc truy cập dựa trên vai trò |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về thiết kế và hỗ trợ các tích hợp y tế hoặc phức tạp khác, ở mức tương đương bằng thạc sĩ.

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

## Bậc 8a: Trưởng nhóm kỹ sư tích hợp

Trưởng nhóm kỹ sư tích hợp dẫn dắt kỹ thuật tích hợp của tổ chức, đề ra định hướng kỹ thuật và tiêu chuẩn, và đảm bảo các tích hợp quan trọng trên nhiều hệ thống.

### Trách nhiệm

- Dẫn dắt kỹ thuật tích hợp trong toàn tổ chức, đề ra định hướng, mẫu thiết kế và tiêu chuẩn.
- Đảm bảo thiết kế của các tích hợp quan trọng, như những tích hợp mang kết quả, thuốc hoặc cảnh báo.
- Định hình lộ trình nền tảng tích hợp cùng kiến trúc sư, quản lý sản phẩm và nhà cung cấp.
- Đại diện tổ chức trong công việc về khả năng tương tác và tiêu chuẩn giữa nhiều tổ chức.
- Quản lý trực tiếp hoặc dẫn dắt các kỹ sư tích hợp và mở rộng cộng đồng thực hành tích hợp.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Systems integration](../../kỹ-năng/#systems-integration) | UK GDaD PCF | Chuyên gia | You can:<br>• establish standards and procedures across a service product life cycle, including the development product life cycle, and can ensure that practitioners adhere to these<br>• manage resources to ensure that the systems integration function works effectively |
| [Systems design](../../kỹ-năng/#systems-design) | UK GDaD PCF | Chuyên gia | You can:<br>• design systems characterised by high levels of risk, impact, and business or technical complexity<br>• control system design practice within an enterprise or industry architecture<br>• influence industry-based models for the development of new technology applications<br>• develop effective implementation and procurement strategies, consistent with business needs<br>• ensure adherence to relevant technical strategies, policies, standards and practices |
| [Technical design throughout the life cycle](../../kỹ-năng/#technical-design-throughout-the-life-cycle) | UK GDaD PCF | Thành thạo | You can:<br>• create technical designs characterised by medium risk, impact, and complexity<br>• maintain appropriate quality and architectural coherence of a technical design in response to change<br>• use feedback to optimise and refine technical designs throughout the life cycle |
| [Stakeholder relationship management](../../kỹ-năng/#stakeholder-relationship-management) | UK GDaD PCF | Thành thạo | You can:<br>• work with the team to develop and maintain an understanding of stakeholders<br>• work with the team to develop and implement stakeholder communications strategies<br>• identify and resolve issues, influence stakeholders and manage relationships effectively<br>• build long-term strategic relationships and communicate clearly and regularly with stakeholders |
| [Leadership and guidance](../../kỹ-năng/#leadership-and-guidance) | UK GDaD PCF | Thành thạo | You can:<br>• make decisions characterised by medium levels of risk and complexity and recommend decisions as risk and complexity increase<br>• build consensus between services or independent stakeholders<br>• identify problems or issues in the team dynamic and rectify them<br>• engage in varying types of feedback, choosing the right type at the appropriate time and ensuring the discussion and decision stick<br>• bring people together to form a motivated team and help create the right environment for a team to work in<br>• facilitate the best team makeup depending on the situation |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế mô hình dữ liệu và tập tham chiếu bằng các bộ thuật ngữ lâm sàng<br>• ánh xạ giữa các bộ thuật ngữ và bảng phân loại, và giải thích giới hạn của một phép ánh xạ<br>• tư vấn cho các nhóm về việc dùng thuật ngữ trong sản phẩm và phân tích |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kỹ thuật tích hợp cho các hệ thống y tế hoặc chăm sóc phức tạp.

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


---

*Contains public sector information from the UK Government Digital and Data Profession Capability Framework (https://understand-digital-data-roles-skills.service.gov.uk/), licensed under the Open Government Licence v3.0. © Crown copyright.*  
*Contains ESCO v1.2.1 data (https://esco.ec.europa.eu/). © European Union. Reuse authorised under Commission Decision 2011/833/EU.*
