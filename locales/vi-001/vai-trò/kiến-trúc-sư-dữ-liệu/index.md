# Kiến trúc sư dữ liệu

> Đây là hồ sơ tham khảo mang tính minh họa cho một tổ chức chăm sóc sức khỏe số nói chung. Đây không phải là bản mô tả công việc chính thức của bất kỳ nhà tuyển dụng nào, và điểm đánh giá công việc không phải là một đánh giá chính thức.

> Bản dịch này được trợ lý AI dịch từ tiếng Anh và chưa được người bản ngữ rà soát. Các đoạn trích từ UK GDaD PCF (Khung năng lực nghề nghiệp kỹ thuật số và dữ liệu của Chính phủ Anh) và ESCO được giữ nguyên bằng tiếng Anh.

**Nhóm:** [Kiến trúc](../../#kiến-trúc)  
**Bậc:** 8a, 8b, 8c  
**Vai trò UK GDaD PCF:** [Data architect](https://understand-digital-data-roles-skills.service.gov.uk/role/data-architect/)  
**Nghề nghiệp ESCO:** [database designer](http://data.europa.eu/esco/occupation/8d9ec84d-cf2d-4179-87bc-335cda54a427) (ISCO-08 2521); [data warehouse designer](http://data.europa.eu/esco/occupation/1562c7a3-c7d9-419d-b9b6-db26610bcf84) (ISCO-08 2521)

## Tóm tắt

Kiến trúc sư dữ liệu thiết kế cách tổ chức cấu trúc, lưu trữ, di chuyển và quản trị dữ liệu y tế và chăm sóc của mình, để dữ liệu có thể được dùng an toàn cho chăm sóc trực tiếp, lập kế hoạch dịch vụ và nghiên cứu. Họ thiết kế mô hình dữ liệu, nền tảng dữ liệu và luồng dữ liệu, đề ra tiêu chuẩn dữ liệu, và bảo đảm ý nghĩa lâm sàng, chất lượng và tính bảo mật được giữ từ đầu đến cuối.

## Trong một tổ chức chăm sóc sức khỏe số

- Dữ liệu y tế phải giữ được ý nghĩa lâm sàng của nó, nên các mô hình dữ liệu dùng các bộ thuật ngữ lâm sàng như SNOMED CT và các bảng phân loại như ICD.
- Dữ liệu dùng cho chăm sóc trực tiếp và dữ liệu dùng cho lập kế hoạch hoặc nghiên cứu có cơ sở pháp lý khác nhau, nên các kiến trúc sư thiết kế để tách biệt, loại bỏ định danh và kiểm soát truy cập.
- Dữ liệu đến từ nhiều hệ thống lâm sàng và chăm sóc có chất lượng khác nhau, nên các kiến trúc sư thiết kế để kiểm tra chất lượng dữ liệu, khớp bệnh nhân và truy vết nguồn gốc.
- Hồ sơ chăm sóc dùng chung và trao đổi dữ liệu phụ thuộc vào các mô hình chung như tài nguyên HL7 FHIR và các bộ dữ liệu quốc gia hoặc quốc tế đã thống nhất.
- Hồ sơ phải được giữ trong thời hạn lưu giữ dài, nên các thiết kế phải lập kế hoạch cho việc lưu trữ và truy cập dữ liệu lịch sử.

## Mô tả vai trò UK GDaD PCF (bản gốc tiếng Anh)

> A data architect sets the vision for the organisation’s use of data, through data design, to ensure that data is managed properly and meets the organisation’s needs.

## Các cấp của vai trò

| Bậc | Chức danh | Cấp UK GDaD PCF | Ngạch công chức | Điểm đánh giá công việc |
| --- | --- | --- | --- | --- |
| 8a | [Kiến trúc sư dữ liệu](#bậc-8a-kiến-trúc-sư-dữ-liệu) | Data architect | SEO/G7 | 560 |
| 8b | [Kiến trúc sư dữ liệu cao cấp](#bậc-8b-kiến-trúc-sư-dữ-liệu-cao-cấp) | Senior data architect | G7/G6 | 613 |
| 8c | [Kiến trúc sư dữ liệu trưởng](#bậc-8c-kiến-trúc-sư-dữ-liệu-trưởng) | Chief data architect | G6 | 662 |

## Bậc 8a: Kiến trúc sư dữ liệu

**Cấp UK GDaD PCF: Data architect**

> A data architect designs and builds data models to fulfil the strategic data needs of the organisation, as defined by chief data architects.
> 
> At this role level, you will:
> - design, support and provide guidance for the upgrade, management, decommission and archive of data in compliance with data policy
> - provide input into data dictionaries
> - define and maintain the data technology architecture, including metadata, integration and business intelligence or data warehouse architecture

### Trách nhiệm

- Thiết kế mô hình dữ liệu logic và vật lý cho dữ liệu lâm sàng và vận hành, dùng các bộ thuật ngữ lâm sàng khi cần.
- Thiết kế luồng dữ liệu và các thành phần nền tảng dữ liệu, như kho dữ liệu, kho dữ liệu hồ và các lớp tích hợp.
- Xác định siêu dữ liệu, các mục từ điển dữ liệu và nguồn gốc dữ liệu cho các bộ dữ liệu trong lĩnh vực của bạn.
- Thiết kế việc loại bỏ định danh và kiểm soát truy cập để dữ liệu chỉ được dùng cho mục đích hợp pháp của nó.
- Làm việc với các đồng nghiệp về chất lượng dữ liệu và mã hóa lâm sàng để khắc phục nguyên nhân cấu trúc của dữ liệu kém.
- Hướng dẫn các kỹ sư dữ liệu và chuyên viên phân tích về mô hình và tiêu chuẩn dữ liệu.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Vận dụng | You can:<br>• communicate effectively with technical and non-technical stakeholders<br>• support and host discussions within a multidisciplinary team, with potentially difficult dynamics<br>• be an advocate for the team externally<br>• manage differing stakeholder perspectives |
| [Communicating data](../../kỹ-năng/#communicating-data) | UK GDaD PCF | Nhận biết | You can:<br>• show an awareness that data needs to be aligned to the needs of the end user<br>• create basic visuals and presentations |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Vận dụng | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../kỹ-năng/#data-governance-data-architect) | UK GDaD PCF | Vận dụng | You can:<br>• understand what data governance is required<br>• take responsibility for the assurance of data solutions and make recommendations to ensure compliance |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Nhận biết | You can:<br>• develop a basic understanding of an unfamiliar or emerging technology, or a familiar technology in a new data context, with guidance<br>• share what you learn with colleagues, including how it could help deliver more value from data |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Vận dụng | You can:<br>• explain the concepts and principles of data modelling<br>• produce, maintain and update relevant data models for an organisation’s specific needs<br>• reverse-engineer data models from a live system |
| [Data standards](../../kỹ-năng/#data-standards) | UK GDaD PCF | Vận dụng | You can:<br>• use data policies, processes and standards effectively<br>• work with subject matter experts to develop standards, policies and guidance to protect data<br>• monitor compliance with policies and standards in a team and take action if needed<br>• analyse the impact if a standard is breached |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Vận dụng | You can:<br>• use metadata repositories to complete complex tasks such as data and systems integration impact analysis<br>• maintain a metadata repository to ensure information remains accurate and up to date |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Vận dụng | You can:<br>• initiate and monitor actions to investigate patterns and trends to resolve problems<br>• effectively consult specialists where required<br>• determine the appropriate resolution and assist with its implementation<br>• determine preventative measures |
| [Strategic thinking](../../kỹ-năng/#strategic-thinking) | UK GDaD PCF | Nhận biết | You can:<br>• explain the strategic context of your work and why it is important<br>• support strategic planning in an administrative capacity |
| [Turning business problems into data design](../../kỹ-năng/#turning-business-problems-into-data-design) | UK GDaD PCF | Vận dụng | You can:<br>• design data architecture by dealing with specific business problems and aligning it to enterprise-wide standards and principles<br>• work within the context of well understood architecture, and identify appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giải thích các quy trình lâm sàng và chăm sóc mà công việc của bạn hỗ trợ<br>• dùng đúng các thuật ngữ y tế thông dụng với đồng nghiệp lâm sàng và chăm sóc<br>• nhận biết khi một thay đổi có thể ảnh hưởng đến việc chăm sóc bệnh nhân và báo lên |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tìm và dùng đúng mã cho một mục dữ liệu hoặc biểu mẫu<br>• sử dụng trình duyệt thuật ngữ và các tập tham chiếu |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý chất lượng dữ liệu](../../kỹ-năng/#quản-lý-chất-lượng-dữ-liệu) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• chạy các kiểm tra chất lượng dữ liệu và sửa lỗi<br>• giải thích các báo cáo chất lượng dữ liệu cho đồng nghiệp |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm dày dặn về mô hình hóa dữ liệu và thiết kế nền tảng dữ liệu, ở mức tương đương bằng thạc sĩ.

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

Được xếp bậc cao hơn gợi ý ngạch của UK GDaD PCF (Bậc 7): các tin tuyển dụng trong ngành y tế xếp vai trò này ở Bậc 8a. Lập kế hoạch, chính sách và quyền tự chủ hành động được chấm cao hơn hồ sơ Bậc 7 vì công việc thiết kế các nền tảng dữ liệu và kiểm soát được dùng trên nhiều dịch vụ.

## Bậc 8b: Kiến trúc sư dữ liệu cao cấp

**Cấp UK GDaD PCF: Senior data architect**

> A senior data architect delivers the vision for the organisation as set by the chief data architect.
> 
> At this role level, you will:
> - design data models and metadata systems
> - help chief data architects to interpret an organisation’s needs
> - provide oversight and advice to other data architects who are designing and producing data artefacts
> - design and support the management of data dictionaries
> - make sure that your teams are working to the standards set for the organisation by the chief data architects
> - work with technical architects to make sure that an organisation’s systems are designed in accordance with the appropriate data architecture

### Trách nhiệm

- Thiết kế kiến trúc dữ liệu cho một lĩnh vực lớn, như hồ sơ chăm sóc dùng chung hoặc nền tảng phân tích.
- Bảo đảm các thiết kế dữ liệu trên các nhóm tuân theo các tiêu chuẩn và mô hình dữ liệu của tổ chức.
- Thiết kế cách dữ liệu được chia sẻ với các tổ chức đối tác, kể cả tiêu chuẩn, biện pháp kiểm soát và thỏa thuận chia sẻ dữ liệu.
- Tư vấn cho các đồng nghiệp về quản trị thông tin và an toàn lâm sàng về các rủi ro dữ liệu của các thiết kế mới.
- Rà soát và hướng dẫn công việc của các kiến trúc sư dữ liệu.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Thành thạo | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../kỹ-năng/#communicating-data) | UK GDaD PCF | Vận dụng | You can:<br>• understand the appropriate media to communicate findings<br>• shape communications for the audience |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Vận dụng | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../kỹ-năng/#data-governance-data-architect) | UK GDaD PCF | Thành thạo | You can:<br>• evolve and define data governance<br>• take responsibility for supporting and collaborating around wider governance<br>• assure and integrate data services to meet the needs of multiple business services<br>• work proactively to ensure the organisation designs architecture that considers data |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Vận dụng | You can:<br>• experiment with unfamiliar and emerging technologies, or familiar technologies in new data contexts, with guidance<br>• share what you learn with the team, explaining potential benefits, risks, and practical considerations<br>• identify opportunities to apply technology to improve data processes or outcomes in an operational setting or the wider organisation |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Thành thạo | You can:<br>• produce relevant data models across multiple subject areas<br>• explain which models to use for which purpose<br>• understand industry-recognised data modelling patterns and standards, and when to apply them<br>• compare and align different data models |
| [Data standards](../../kỹ-năng/#data-standards) | UK GDaD PCF | Thành thạo | You can:<br>• create data standards for different subjects and ensure senior leaders understand them<br>• work with subject matter experts across the organisation to introduce data standards best practice<br>• monitor compliance with policies and standards in the organisation<br>• make recommendations about how the organisation should resolve breaches of standards |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Thành thạo | You can:<br>• design an appropriate metadata repository<br>• suggest changes to improve current metadata repositories<br>• understand a range of tools for storing and working with metadata<br>• advise less experienced members of the team about metadata management |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Thành thạo | You can:<br>• ensure that the right actions are taken to investigate, resolve and anticipate problems<br>• co-ordinate the team to investigate problems, implement solutions and take preventive measures |
| [Strategic thinking](../../kỹ-năng/#strategic-thinking) | UK GDaD PCF | Vận dụng | You can:<br>• work within a strategic context and communicate how activities meet strategic goals<br>• contribute to the development of strategy and policies |
| [Turning business problems into data design](../../kỹ-năng/#turning-business-problems-into-data-design) | UK GDaD PCF | Thành thạo | You can:<br>• design data architecture that deals with problems spanning different business areas<br>• identify links between problems to devise common solutions<br>• work across multiple subject areas, or a single large or complicated subject area<br>• produce appropriate patterns |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• phân tích một dịch vụ khớp với các lộ trình chăm sóc giữa các tổ chức như thế nào<br>• phối hợp với bác sĩ lâm sàng, nhân viên chăm sóc và bệnh nhân để định hình các dịch vụ số<br>• giải thích tác động của các quyết định số đối với việc chăm sóc, an toàn và khối lượng công việc của nhân viên |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế mô hình dữ liệu và tập tham chiếu bằng các bộ thuật ngữ lâm sàng<br>• ánh xạ giữa các bộ thuật ngữ và bảng phân loại, và giải thích giới hạn của một phép ánh xạ<br>• tư vấn cho các nhóm về việc dùng thuật ngữ trong sản phẩm và phân tích |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế và xây dựng các tích hợp bằng FHIR, HL7 phiên bản 2 và các mẫu thông điệp<br>• viết và lập hồ sơ cấu hình cho các tài nguyên FHIR và hướng dẫn triển khai<br>• giải quyết các vấn đề phức tạp về ánh xạ và chất lượng dữ liệu giữa các hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt các đánh giá tác động bảo vệ dữ liệu và các thỏa thuận chia sẻ thông tin<br>• tư vấn cho các nhóm về cơ sở pháp lý, sự đồng ý, bảo mật và thời hạn lưu giữ<br>• điều tra sự cố và đề xuất cải tiến |
| [Quản lý chất lượng dữ liệu](../../kỹ-năng/#quản-lý-chất-lượng-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• xác định các quy tắc và thước đo chất lượng dữ liệu<br>• phối hợp với các bên cung cấp dữ liệu để khắc phục nguyên nhân gốc của chất lượng kém |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• tham gia các buổi làm việc về mối nguy và đóng góp vào nhật ký mối nguy<br>• tuân theo quy trình quản lý rủi ro lâm sàng cho công việc của bạn<br>• cung cấp bằng chứng cho hồ sơ an toàn lâm sàng, như kết quả kiểm thử |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Vận dụng | Bạn có thể:<br>• giám sát công việc hằng ngày và đưa ra phản hồi<br>• tham gia tuyển dụng và hướng dẫn nhân viên mới<br>• tổ chức các buổi trao đổi riêng định kỳ |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng về kiến trúc dữ liệu cho các tổ chức phức tạp.

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

## Bậc 8c: Kiến trúc sư dữ liệu trưởng

**Cấp UK GDaD PCF: Chief data architect**

> A chief data architect sets the vision for the organisation’s use of data as directed by the appropriate governance body.
> 
> At this role level, you will:
> - oversee the design of multiple data models and have a broad understanding of how each model fulfils the needs of the organisation
> - be accountable for supporting and aligning to the organisation’s data strategy
> - champion data architecture both internally and through collaborating and communicating at the most senior levels across government
> - set the standards and ways of working for the data architecture community
> - be accountable for assuring data models at the level of a project or enterprise
> - provide advice to project teams and oversee the management of the full data product life cycle
> - be responsible for ensuring that the organisation’s systems are designed in accordance with the enterprise data architecture

### Trách nhiệm

- Đề ra tầm nhìn và lộ trình kiến trúc dữ liệu của tổ chức, phù hợp với chiến lược dữ liệu của tổ chức.
- Làm chủ mô hình dữ liệu doanh nghiệp, các tiêu chuẩn dữ liệu và từ điển dữ liệu của tổ chức.
- Tư vấn cho ban điều hành và các cơ quan quản trị dữ liệu về kiến trúc dữ liệu, rủi ro và đầu tư.
- Đại diện tổ chức trong công việc về tiêu chuẩn dữ liệu và khả năng tương tác giữa nhiều tổ chức.
- Dẫn dắt ngành thực hành kiến trúc dữ liệu và phát triển con người trong ngành này.

### Kỹ năng

| Kỹ năng | Nguồn | Mức kỳ vọng | Ý nghĩa của mức này |
| --- | --- | --- | --- |
| [Communicating between the technical and non-technical](../../kỹ-năng/#communicating-between-the-technical-and-non-technical) | UK GDaD PCF | Thành thạo | You can:<br>• listen to and interpret the needs of technical and non-technical stakeholders, and manage their expectations<br>• manage active and reactive communication<br>• support or host difficult discussions within the team or with diverse senior stakeholders |
| [Communicating data](../../kỹ-năng/#communicating-data) | UK GDaD PCF | Thành thạo | You can:<br>• turn complex data into clear and well understood solutions, which can be acted upon<br>• share data communication skills with the team and organisation<br>• understand and communicate different options, taking into account risks and uncertainties |
| [Data analysis and synthesis](../../kỹ-năng/#data-analysis-and-synthesis) | UK GDaD PCF | Vận dụng | You can:<br>• undertake data profiling and source system analysis<br>• present clear insights to colleagues to support the end use of the data |
| [Data governance (data architect)](../../kỹ-năng/#data-governance-data-architect) | UK GDaD PCF | Chuyên gia | You can:<br>• ensure data governance supports changes to the organisational strategy<br>• align data governance with wider governance (for example, budget)<br>• assure corporate services by understanding important risks and providing mitigation through assurance mechanisms |
| [Data innovation](../../kỹ-năng/#data-innovation) | UK GDaD PCF | Thành thạo | You can:<br>• test and evaluate the feasibility of unfamiliar and emerging technologies, or familiar technologies in new data contexts<br>• share what you learn with the organisation, explaining potential benefits, risks, and practical considerations<br>• recommend, design and implement innovative data solutions based on organisation objectives, user needs, and operational constraints |
| [Data modelling](../../kỹ-năng/#data-modelling) | UK GDaD PCF | Chuyên gia | You can:<br>• understand the concepts and principles of data modelling and can produce relevant data models<br>• work across government and industry, recognising opportunities for the reuse and alignment of data models in different organisations<br>• design the method to categorise data models within an organisation |
| [Data standards](../../kỹ-năng/#data-standards) | UK GDaD PCF | Chuyên gia | You can:<br>• create data standards for the organisation<br>• advocate for, and oversee compliance with, data policies and standards<br>• decide where standards need to be set across the organisation, and how to set them in the wider context of government |
| [Metadata management](../../kỹ-năng/#metadata-management) | UK GDaD PCF | Chuyên gia | You can:<br>• identify how metadata repositories can support different areas of the organisation<br>• communicate the value of metadata repositories<br>• set up robust governance processes to keep repositories up to date |
| [Problem management](../../kỹ-năng/#problem-management) | UK GDaD PCF | Chuyên gia | You can:<br>• anticipate problems and defend against them at the right time<br>• understand how a problem fits into the larger picture<br>• identify and describe problems, and help others to describe them<br>• build problem-solving capabilities in others |
| [Strategic thinking](../../kỹ-năng/#strategic-thinking) | UK GDaD PCF | Thành thạo | You can:<br>• define strategies and policies, providing guidance to others on working in the strategic context<br>• evaluate current strategies to ensure business requirements are being met and exceeded where possible |
| [Turning business problems into data design](../../kỹ-năng/#turning-business-problems-into-data-design) | UK GDaD PCF | Chuyên gia | You can:<br>• design data architecture that deals with problems across the enterprise<br>• work across all organisational subject areas and internal and external programmes |
| [Hiểu biết về các dịch vụ y tế và chăm sóc](../../kỹ-năng/#hiểu-biết-về-các-dịch-vụ-y-tế-và-chăm-sóc) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• định hình chiến lược của tổ chức bằng hiểu biết sâu về hệ thống y tế và chăm sóc<br>• đại diện tổ chức làm việc với các đối tác và lãnh đạo y tế và chăm sóc<br>• dự đoán những thay đổi về chính sách và dịch vụ sẽ ảnh hưởng đến các dịch vụ số và việc chăm sóc như thế nào |
| [Thuật ngữ và phân loại lâm sàng](../../kỹ-năng/#thuật-ngữ-và-phân-loại-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• thiết kế mô hình dữ liệu và tập tham chiếu bằng các bộ thuật ngữ lâm sàng<br>• ánh xạ giữa các bộ thuật ngữ và bảng phân loại, và giải thích giới hạn của một phép ánh xạ<br>• tư vấn cho các nhóm về việc dùng thuật ngữ trong sản phẩm và phân tích |
| [Khả năng tương tác của dữ liệu y tế](../../kỹ-năng/#khả-năng-tương-tác-của-dữ-liệu-y-tế) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra tiêu chuẩn và chiến lược về khả năng tương tác cho tổ chức<br>• dẫn dắt công việc về tiêu chuẩn ở cấp quốc gia hoặc giữa nhiều tổ chức<br>• đảm bảo thiết kế của các tích hợp quan trọng trên nhiều hệ thống |
| [Quản trị thông tin và bảo vệ dữ liệu](../../kỹ-năng/#quản-trị-thông-tin-và-bảo-vệ-dữ-liệu) | Tài liệu tham khảo này | Chuyên gia | Bạn có thể:<br>• đề ra chính sách và chiến lược quản trị thông tin<br>• tư vấn cho hội đồng về rủi ro thông tin và việc tuân thủ<br>• đại diện tổ chức làm việc với các cơ quan quản lý và đối tác |
| [Quản lý chất lượng dữ liệu](../../kỹ-năng/#quản-lý-chất-lượng-dữ-liệu) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• xác định các quy tắc và thước đo chất lượng dữ liệu<br>• phối hợp với các bên cung cấp dữ liệu để khắc phục nguyên nhân gốc của chất lượng kém |
| [Quản lý rủi ro lâm sàng](../../kỹ-năng/#quản-lý-rủi-ro-lâm-sàng) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• dẫn dắt việc nhận diện mối nguy và đánh giá rủi ro cho một sản phẩm hoặc thay đổi<br>• viết và duy trì nhật ký mối nguy và báo cáo hồ sơ an toàn lâm sàng<br>• thống nhất các biện pháp kiểm soát rủi ro với các nhóm sản phẩm và kiểm tra hiệu quả của chúng<br>• tư vấn cho các nhóm về việc áp dụng các tiêu chuẩn quản lý rủi ro lâm sàng |
| [Quản lý nhân sự](../../kỹ-năng/#quản-lý-nhân-sự) | Tài liệu tham khảo này | Thành thạo | Bạn có thể:<br>• trực tiếp quản lý một nhóm, đặt mục tiêu và tiến hành đánh giá<br>• hỗ trợ sức khỏe tinh thần và quản lý chuyên cần, hiệu quả công việc và hành vi<br>• lập kế hoạch phát triển và kế nhiệm cho nhóm |

### Trình độ và kinh nghiệm thông thường

- Có kinh nghiệm sâu rộng trong việc dẫn dắt kiến trúc dữ liệu giữa các tổ chức.

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
