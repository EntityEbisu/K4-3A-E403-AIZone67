# BẬT NHẬT KÝ KHAI THÁC DỮ LIỆU & BẰNG CHỨNG THỰC TẾ (MINING LOG)
**Track B · Đề tài B1 — Trợ lý Discord (Hỏi đáp & Tra cứu Thông báo Chính thức)**
*Tài liệu đính kèm phục vụ minh chứng cho `spec.md` (§1. User & Job và §2. Impact)*

---

## 1. Nguồn dữ liệu khai thác (Data Sources)

1. **Chuẩn B (Chatlog thực tế):** `data/discord-pack/k4_messages.csv`
   - Thu thập từ 2 server Discord cộng đồng Khóa 4 (`K4-L2-3` và `K4-L3-4`) từ ngày 12/09/2026 06:57 đến 14/09/2026 23:54 (giờ VN).
   - Tổng cộng: **1.092 tin nhắn** (đã ẩn danh mã hoá theo quy chuẩn của Ban Tổ Chức).
2. **Chuẩn A (Khảo sát người dùng thực tế):** Khảo sát trực tiếp qua Google Forms
   - Quy mô mẫu: $n = 9$ học viên Khóa 4 ngoài nhóm (thực hiện ngày 16–17/09/2026).

---

## 2. Số liệu Mining tổng thể (Quantitative Metrics)

### 2.1 Thống kê Chatlog Discord (`k4_messages.csv`)
- **Tổng số tin nhắn:** 1.092 tin nhắn.
  - Tin nhắn từ người dùng (học viên/mentor/TA): **779 tin** (71.3%).
  - Tin nhắn từ Bot hệ thống: **313 tin** (28.7%).
- **Tin nhắn thắc mắc / hỏi đáp Logistics & Quy định:** **391 tin** (chiếm **50.2%** tổng số tin nhắn của học viên).
- **Tình trạng trôi tin / Bỏ sót câu hỏi:**
  - **108 câu hỏi (27.6%)** hoàn toàn không nhận được phản hồi trực tiếp (bị trôi tin do thảo luận khác đè lên).
  - **283 câu hỏi (72.4%)** được trả lời nhưng thời gian chờ đợi phản hồi trung bình là **18.3 phút**.
  - Độ trễ phản hồi lớn nhất ghi nhận: **1.149 phút (~19.1 giờ)** (gửi từ nửa đêm nhưng sang ngày hôm sau mới có người trả lời).
- **Phân bổ thắc mắc theo 4 nhóm chủ đề chính:**
  1. **Team / Ghép nhóm / Phoenix:** 135 tin (34.5%)
  2. **Daily Standup / Form / Link nộp:** 108 tin (27.6%)
  3. **Bài tập / Lab / VLearn / Deadline:** 99 tin (25.3%)
  4. **Lịch học / Workshop / Xin nghỉ / Điểm danh:** 73 tin (18.7%)

### 2.2 Thống kê Khảo sát thực tế ($n = 9$)
- **100% (9/9 học viên)** xác nhận thường xuyên bị trôi tin hoặc phát hiện muộn các thông báo quan trọng trên Discord.
- **55.6% (5/9 học viên)** chỉ ra nỗi đau lặp lại nghiêm trọng nhất hàng ngày: **Bỏ lỡ hoặc quên điền link Daily Standup & Daily Request**.

---

## 3. Top 5 Ví dụ / Trích dẫn thực tế từ Chatlog (5 Evidence Cases)

Dưới đây là 5 trường hợp điển hình được khai thác trực tiếp từ file `k4_messages.csv`, minh họa rõ nét các vấn đề về trôi tin, thông tin sai lệch và ranh giới thẩm quyền:

---

### Case 1: Học viên nhận câu trả lời SAI LỆCH từ thành viên khác do không có nguồn chính thức
- **Message ID:** `M83358`
- **Thời gian:** `2026-09-12 18:55` | **Kênh:** `channel_02` | **Server:** `K4-L2-3`
- **Tác giả:** `D1224` (Học viên)
- **Nội dung nguyên văn:**
  > *"cho mình hỏi một team bao nhiêu bạn ?"*
- **Phản hồi nhận được (`M1224` lúc 19:01 từ `D3694`):**
  > *"5 nhé , trên web vào sẽ thấy có 5 slot ở phần lập đôi thôi"*
- **Phân tích vấn đề (Lớp ① - Nguồn sự thật):**
  - **Thực tế quy chế:** Thông báo onboarding chính thức (`M49744`) quy định rõ: Mỗi nhóm gồm **3–4 thành viên**.
  - **Hậu quả:** Học viên nhận thông tin sai lệch từ người khác (đoán mò là 5 người), gây hỗn loạn trong quá trình lập team nếu không có Bot đối soát từ nguồn thông báo chính thức.

---

### Case 2: Trôi tin nghiêm trọng — Câu hỏi quy chế bị bỏ quên hoàn toàn
- **Message ID:** `M69081`
- **Thời gian:** `2026-09-12 12:04` | **Kênh:** `channel_02` | **Server:** `K4-L2-3`
- **Tác giả:** `D2313` (Học viên)
- **Nội dung nguyên văn:**
  > *"có điểm danh ws không ạ"*
- **Phản hồi nhận được:** **Không có bất kỳ phản hồi nào** trong toàn bộ chatlog (Trôi tin 100%).
- **Phân tích vấn đề (Lớp ② - Mơ hồ & Trôi tin):**
  - Học viên hỏi cộc lốc về điểm danh workshop ngay trước giờ diễn ra. Tin nhắn bị các trao đổi khác cuốn trôi, khiến học viên không nắm được thông tin điểm danh.

---

### Case 3: Hỏi về việc cá nhân / Vượt thẩm quyền quy chế
- **Message ID:** `M63574`
- **Thời gian:** `2026-09-12 11:06` | **Kênh:** `channel_02` | **Server:** `K4-L2-3`
- **Tác giả:** `D3082` (Học viên)
- **Nội dung nguyên văn:**
  > *"A ơi, cho e hỏi, buổi workshop chủ nhật ngày mai thì có tính vào số buổi nghỉ ko ạ? Giả dụ sáng mai e có việc thì sao ạ?..."*
- **Phản hồi (`M3694` lúc 11:08):**
  > *"Build phase sẽ không tính vào hoạt động học trên lớp các buổi nghỉ đâu nhé. Với lại nếu sắp xếp được..."*
- **Phân tích vấn đề (Lớp ③ - Thẩm quyền & Ngoại lệ):**
  - Đây là câu hỏi về việc xin phép nghỉ cá nhân. Bot nếu trả lời tự động không được phép tự cam kết "được nghỉ" mà phải có cơ chế **HANDOFF_TA / Lab Coach** để tránh học viên ỷ lại.

---

### Case 4: Hỏi về tình trạng hệ thống — Chờ đợi phản hồi hơn 3 tiếng
- **Message ID:** `M83711`
- **Thời gian:** `2026-09-12 13:55` | **Kênh:** `channel_02` | **Server:** `K4-L2-3`
- **Tác giả:** `D1224` (Học viên)
- **Nội dung nguyên văn:**
  > *"anh [@D3694] cho e hỏi vlearn chưa up bài mới hả ?"*
- **Phản hồi nhận được lúc 17:11 (Chờ đợi 3 giờ 16 phút):**
  > *"bài mới buổi 2 up rồi nhé"*
- **Phân tích vấn đề (Lớp ① - Hệ thống bên ngoài):**
  - Học viên không biết bài lab đã lên hệ thống VLearn hay chưa và phải tag người phụ trách, đợi hơn 3 tiếng đồng hồ trong giờ tự học mới có câu trả lời.

---

### Case 5: Lo lắng về deadline nửa đêm — Chờ phản hồi hơn 8 tiếng
- **Message ID:** `M19124`
- **Thời gian:** `2026-09-13 00:25` (Nửa đêm) | **Kênh:** `channel_02` | **Server:** `K4-L2-3`
- **Tác giả:** `D9616` (Học viên)
- **Nội dung nguyên văn:**
  > *"a ơi sao deadline ghép đội tự do end sớm vậy a?"*
- **Phản hồi nhận được lúc 08:32 sáng hôm sau (Chờ đợi 8 giờ 7 phút):**
  > *"Time thì cũng sẽ limit không quá dài để theo đúng plan chương trình nè. Các bạn chưa tìm đc đồng đội..."*
- **Phân tích vấn đề (Pain Point về tính tức thời 24/7):**
  - Học viên thường tự học và làm bài vào ban đêm. Khi có thắc mắc gấp về thời hạn (deadline), đội ngũ nhân sự không thể túc trực 24/7. Trợ lý Bot tra cứu tức thì là giải pháp duy nhất giúp giải tỏa lo lắng kịp thời cho học viên.

---

## 4. Bảng tổng hợp trích dẫn nguyên văn từ khảo sát người học (Chuẩn A)

| STT | Trích dẫn nguyên văn từ học viên (Quotes) | Nguồn | Vấn đề phản ánh |
|:---:|---|---|---|
| 1 | *"Bỏ điền daily standup"* | Google Forms K4 | Quên/miss thông báo nộp báo cáo tiến độ ngày |
| 2 | *"Nộp daily request"* | Google Forms K4 | Trôi link form yêu cầu hỗ trợ kỹ thuật |
| 3 | *"Quên k nộp standup"* | Google Forms K4 | Bị trừ điểm chuyên cần do không nhớ giờ chốt |
| 4 | *"Điền daily hằng ngày"* | Google Forms K4 | Thiếu kênh nhắc nhở tập trung đúng giờ |
| 5 | *"Nhiều thông tin quá dẫn đến bị miss thông tin quan trọng"* | Google Forms K4 | Nhiễu loạn thông tin giữa các kênh chat |
| 6 | *"Rất nhiều á / có nhìu lắm k nhớ nổi"* | Google Forms K4 | Tình trạng quá tải thông tin Onboarding |

---

## 5. Kết luận áp dụng vào `spec.md`

1. **Vào §1 (User & Job):** Sử dụng số liệu **391 câu hỏi thắc mắc** (chiếm 50.2% thảo luận của học viên), tỷ lệ **27.6% trôi tin** và thời gian chờ đợi trung bình **18.3 phút** làm minh chứng đanh thép cho nhu cầu cấp thiết phải có trợ lý tra cứu tự động.
2. **Vào §2 (Impact):** Tần suất câu hỏi diễn ra **hàng ngày** (108 tin về Daily/Form, 99 tin về Deadline Lab) với chi phí thiệt hại cao (mất điểm, lỡ hạn ghép đội), chứng minh quyết định chọn bài toán **Trợ lý Discord tra cứu thông báo & Deadline chính thức** là hoàn toàn vượt trội so với các ứng viên khác.
