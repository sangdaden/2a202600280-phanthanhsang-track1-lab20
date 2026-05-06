# 🧩 Socratic AI — Dependency Map (NOW)

## ⚠️ External Dependencies (có thể “giết” dự án trong 30 ngày)

---

### 1. LLM Provider (OpenAI / Anthropic)

**Worst-case scenario:**  
API bị tăng giá mạnh hoặc bị rate limit → app không dùng được hoặc cost vượt kiểm soát

**Plan B (deploy ≤ 7 ngày):**  
Chuyển sang multi-provider fallback (Anthropic / open-source qua Ollama hoặc API khác) + cache response cho use-case phổ biến

**Cost của Plan B:**  
- Time: ~5–7 ngày  
- Money: $200–$500 (infra + testing)

---

### 2. User Acquisition Channel (Facebook Groups / Reddit / Discord)

**Worst-case scenario:**  
Bị ban / reach giảm mạnh → không có user mới

**Plan B (deploy ≤ 7 ngày):**  
Chuyển sang landing page + waitlist + build-in sharing (invite link, viral loop nhẹ)

**Cost của Plan B:**  
- Time: ~3–5 ngày  
- Money: $50–$200 (domain + tool + ads test nhẹ)

---

### 3. UX Adoption Risk (User không quen bị hỏi ngược)

**Worst-case scenario:**  
User thấy “bị làm phiền” → churn ngay lần đầu

**Plan B (deploy ≤ 7 ngày):**  
Thêm “Guided mode” (gợi ý câu hỏi + explain tại sao hỏi) + option switch sang “direct answer”

**Cost của Plan B:**  
- Time: ~5–7 ngày  
- Money: ~$0–$100

---

# 🧭 Critical Path (NOW)

## 🎯 Goal: User có “aha moment” trong lần dùng đầu

---

### Task Flow (có dependency)

1. **Define core Socratic loop (question → answer → deeper question)**  
   → nền tảng logic sản phẩm

2. **Design onboarding + use-case templates** *(blocks 3,4,5)*  
   → giúp user bắt đầu nhanh

3. **Implement Socratic Questioning Engine (v1)** *(blocks 4)*  
   → core differentiation

4. **Build basic UI (chat + guided prompts)** *(blocks 5)*  
   → để user trải nghiệm

5. **Add Insight Summary (end of session)** *(blocks 4)*  
   → tạo “aha moment”

6. **Launch to 100 early users (manual distribution)** *(blocks none)*  
   → validate thực tế

7. **Collect feedback + iterate loop** *(blocks none)*  
   → improve retention

---

## 🔗 Blocking Relationships

- (1) → blocks toàn bộ  
- (2) → blocks (4) & (6)  
- (3) → blocks (5)  
- (4) → blocks (6)  
- (5) → improves (7)

---

## 🔥 Critical Path

> **1 → 2 → 4 → 6 → 7**

👉 Đây là chuỗi dài nhất quyết định tốc độ ra market

---

# ⚡ Strategy Insight

> Speed to first “thinking value” matters more than perfect AI.

---

# 🎤 Investor-ready line

> We have identified key external risks and built fast fallback plans, while focusing execution on a tight critical path to deliver user value within days, not months.