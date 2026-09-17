# Source fixture rules

`official-sources.demo.json` là **schema demo**, không chứa deadline hay chính sách thật.

Trước CP3, người phụ trách source phải:

1. Lấy mỗi thông báo từ đầu mối/nguồn chính thức được xác minh.
2. Chỉ lưu phần trích tối thiểu cần để trả lời, cùng `source_id`, URL, thời điểm hiệu lực và phạm vi.
3. Đặt `official: true` chỉ sau khi một thành viên khác kiểm tra lại.
4. Không thêm tin nhắn Discord của học viên, PII, token hoặc toàn bộ data pack vào fixture.

Nếu không có record `official=true`, `status=active` và excerpt khớp claim, bot phải `ASK_CLARIFY` hoặc `HANDOFF_TA`.
