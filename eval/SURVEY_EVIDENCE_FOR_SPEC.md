# TỔNG HỢP BẰNG CHỨNG KHẢO SÁT & IMPACT (DÀNH CHO SPEC.MD §1 - §2)
**Khối R1 (15 Điểm) — Chuẩn Bằng Chứng Thực Tế Khóa 4**

---

## 1. Nội dung dán vào `spec.md` — Mục §1. User & Job

### Evidence chuẩn A (Khảo sát thực tế từ người học K4)
- **Quy mô mẫu:** $n = 9$ học viên Khóa 4 ngoài nhóm (khảo sát qua Google Forms ngày 16–17/09/2026).
- **Tỷ lệ xác nhận vấn đề (Pain Rate):** **100% (9/9 bạn)** xác nhận thường xuyên bị trôi, bỏ lỡ hoặc phát hiện muộn các thông tin quan trọng do có quá nhiều kênh Discord và tin nhắn bị trôi.
- **Phát hiện trọng điểm (Core Insight):** **55.6% (5/9 học viên)** chỉ đích danh nỗi đau lớn nhất và lặp đi lặp lại hàng ngày là: **Bỏ lỡ / Quên điền Daily Standup & Daily Request** do thông báo và link form bị trôi giữa các kênh chat.
- **$\ge 5$ Trích dẫn nguyên văn từ học viên (Quotes):**
  1. *"Nộp daily request"* — (Học viên K4)
  2. *"Điền daily hằng ngày"* — (Học viên K4)
  3. *"Bỏ điền daily standup"* — (Học viên K4)
  4. *"Quên k nộp standup"* — (Học viên K4)
  5. *"Nhiều thông tin quá dẫn đến bị miss thông tin quan trọng"* — (Học viên K4)
  6. *"Rất nhiều á / có nhìu lắm k nhớ nổi"* — (Học viên K4)

### Evidence chuẩn B (Khai thác dữ liệu Chatlog thật `k4_messages.csv`)
- **Tập dữ liệu:** 1.092 tin nhắn (779 tin người gửi, 313 tin bot) tại 2 server Discord cộng đồng K4 giai đoạn Onboarding.
- **Số liệu đếm:** Có 293 tin nhắn mang tính chất hỏi đáp / thắc mắc logistics, trong đó các câu hỏi liên quan đến lịch trình, quy định lập team, nộp bài chiếm phần lớn. Nhiều câu hỏi bị trôi từ 2–4 tiếng không có người giải đáp (ví dụ các tin `M83358`, `M13014`, `M63574`).

---

## 2. Nội dung dán vào `spec.md` — Mục §2. Impact & Quyết định chọn

### Bảng so sánh Impact giữa 3 ứng viên bài toán:

| Ứng viên bài toán | Số người gặp ($N$) | Tần suất ($F$) | Thiệt hại mỗi lần ($C$) | Tính khả thi build | Điểm Impact ($N \times F \times C$) | Quyết định |
|---|---|---|---|:---:|:---:|:---:|
| **1. Trợ lý tra cứu Deadline Lab & Thông báo chính thức (Kèm Daily Standup)** | ~1.000 học viên khoá 4 | **Hàng ngày** (Daily standup) & Hàng tuần (Lab) | Trừ điểm chuyên cần, trễ hạn nộp bài, quá tải cho TA trả lời lặp | Cao (Conditional Bot + RAG nguồn chính thức) | **CAO NHẤT** (Bằng chứng 55.6% học viên phản ánh) | **CHỌN** ✅ |
| **2. Bot gom nhóm tự động tìm bạn làm bài tập** | ~200 học viên chưa có team | Chỉ diễn ra tuần đầu Onboarding (1-2 lần) | Tốn 1-2 tiếng tìm người, không ảnh hưởng trực tiếp đến điểm số | Trung bình | Thấp (Tần suất thấp, chỉ dùng 1 lần rồi bỏ) | **LOẠI** ❌ |
| **3. Bot tóm tắt toàn bộ tin nhắn chém gió trong ngày** | ~500 học viên theo dõi kênh chung | Hàng ngày | Đọc tin rác mất thời gian nhưng không gây hậu quả mất điểm | Khó (Dữ liệu chém gió nhiễu, nguy cơ hallucination cao) | Trung bình (Không giải quyết trực tiếp rủi ro học tập) | **LOẠI** ❌ |

- **Lý do CHỌN Ứng viên 1:** Tần suất xảy ra mỗi ngày (Daily Standup), thiệt hại trực tiếp vào điểm số của học viên, và có bằng chứng xác thực từ 55.6% học viên trong khảo sát.
