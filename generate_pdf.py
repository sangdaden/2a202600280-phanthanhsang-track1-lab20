# -*- coding: utf-8 -*-
"""
Socratic AI — Milestone 1 Investor Package
Sinh ra file PhanThanhSang_Milestone1_InvestorPackage.pdf (9 trang)
Cấu trúc:
  Trang 1: Cover + Twitter Pitch
  Trang 2-5: Pitch Memo + Market + PRD
  Trang 6-7: Financial + Unit Economics
  Trang 8: Roadmap + OKRs
  Trang 9: Dependency + Critical Path
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable
)

# ---- Đăng ký font Arial (hỗ trợ tiếng Việt đầy đủ) ----
pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", "C:/Windows/Fonts/ariali.ttf"))
pdfmetrics.registerFont(TTFont("Arial-BoldItalic", "C:/Windows/Fonts/arialbi.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                   italic="Arial-Italic", boldItalic="Arial-BoldItalic")

# ---- Bảng màu ----
NAVY = colors.HexColor("#0F2A44")
TEAL = colors.HexColor("#0E7C86")
ACCENT = colors.HexColor("#E63946")
LIGHT = colors.HexColor("#F4F6F8")
BORDER = colors.HexColor("#D9DEE3")
MUTED = colors.HexColor("#5A6470")

# ---- Styles ----
styles = getSampleStyleSheet()

def S(name, **kw):
    base = dict(fontName="Arial", fontSize=10, leading=14, textColor=colors.black,
                alignment=TA_LEFT, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, **base)

H_TITLE   = S("H_TITLE", fontName="Arial-Bold", fontSize=28, leading=32,
              textColor=NAVY, alignment=TA_CENTER, spaceAfter=8)
H_SUB     = S("H_SUB", fontName="Arial-Italic", fontSize=14, leading=18,
              textColor=TEAL, alignment=TA_CENTER, spaceAfter=18)
H1        = S("H1", fontName="Arial-Bold", fontSize=18, leading=22,
              textColor=NAVY, spaceBefore=4, spaceAfter=10)
H2        = S("H2", fontName="Arial-Bold", fontSize=13, leading=17,
              textColor=TEAL, spaceBefore=8, spaceAfter=6)
H3        = S("H3", fontName="Arial-Bold", fontSize=11, leading=14,
              textColor=NAVY, spaceBefore=6, spaceAfter=3)
BODY      = S("BODY", alignment=TA_JUSTIFY)
BODY_TIGHT= S("BODY_TIGHT", alignment=TA_JUSTIFY, spaceAfter=3)
BULLET    = S("BULLET", leftIndent=14, bulletIndent=4, spaceAfter=3)
QUOTE     = S("QUOTE", fontName="Arial-Italic", fontSize=11, leading=15,
              textColor=NAVY, leftIndent=14, rightIndent=10,
              borderPadding=8, spaceAfter=8)
SMALL     = S("SMALL", fontSize=8, leading=11, textColor=MUTED)
META      = S("META", fontSize=10, leading=13, textColor=MUTED, alignment=TA_CENTER)
TWITTER   = S("TWITTER", fontName="Arial-Bold", fontSize=14, leading=20,
              textColor=NAVY, alignment=TA_CENTER, spaceAfter=6,
              leftIndent=12, rightIndent=12)
CLOSING   = S("CLOSING", fontName="Arial-BoldItalic", fontSize=13, leading=18,
              textColor=ACCENT, alignment=TA_CENTER, spaceBefore=10, spaceAfter=4)

# ---- Helpers ----
def hr():
    return HRFlowable(width="100%", thickness=0.6, color=BORDER,
                      spaceBefore=4, spaceAfter=6)

def bullets(items, style=BULLET):
    return [Paragraph(f"• {t}", style) for t in items]

def boxed(flowables, bg=LIGHT, border=BORDER, pad=8):
    """Đặt 1 nhóm flowables vào trong khung có nền nhẹ."""
    t = Table([[flowables]], colWidths=[16.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.5, border),
        ("LEFTPADDING", (0,0), (-1,-1), pad),
        ("RIGHTPADDING", (0,0), (-1,-1), pad),
        ("TOPPADDING", (0,0), (-1,-1), pad),
        ("BOTTOMPADDING", (0,0), (-1,-1), pad),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
    ]))
    return t

def page_header_footer(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1]-1.3*cm, A4[0], 1.3*cm, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Arial-Bold", 10)
    canvas.drawString(2*cm, A4[1]-0.85*cm, "Socratic AI — Milestone 1 Investor Package")
    canvas.setFont("Arial", 9)
    canvas.drawRightString(A4[0]-2*cm, A4[1]-0.85*cm,
                           "Phan Thanh Sang · 2A202600280")
    # Footer
    canvas.setFillColor(MUTED)
    canvas.setFont("Arial", 8)
    canvas.drawString(2*cm, 1.0*cm, "From asking AI  →  to thinking with AI")
    canvas.drawRightString(A4[0]-2*cm, 1.0*cm, f"Trang {doc.page} / 9")
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.4)
    canvas.line(2*cm, 1.4*cm, A4[0]-2*cm, 1.4*cm)
    canvas.restoreState()

def cover_page(canvas, doc):
    """Trang 1 không có header bar — vẽ riêng."""
    canvas.saveState()
    # Khối màu nền trên cùng
    canvas.setFillColor(NAVY)
    canvas.rect(0, A4[1]-9*cm, A4[0], 9*cm, stroke=0, fill=1)
    # Footer line
    canvas.setStrokeColor(BORDER)
    canvas.line(2*cm, 1.4*cm, A4[0]-2*cm, 1.4*cm)
    canvas.setFillColor(MUTED)
    canvas.setFont("Arial", 8)
    canvas.drawString(2*cm, 1.0*cm, "Confidential — Milestone 1 Investor Package · 2026")
    canvas.drawRightString(A4[0]-2*cm, 1.0*cm, "Trang 1 / 9")
    canvas.restoreState()

# ===================================================================
#                              NỘI DUNG
# ===================================================================
story = []

# ============================ TRANG 1 =============================
story.append(Spacer(1, 1.4*cm))
story.append(Paragraph("SOCRATIC AI", ParagraphStyle(
    "Cover", fontName="Arial-Bold", fontSize=44, leading=52,
    textColor=colors.white, alignment=TA_CENTER)))
story.append(Paragraph("From asking AI &nbsp;→&nbsp; to thinking with AI",
    ParagraphStyle("CoverSub", fontName="Arial-Italic", fontSize=16, leading=22,
                   textColor=colors.HexColor("#A8D8DC"), alignment=TA_CENTER,
                   spaceBefore=10)))
story.append(Spacer(1, 0.6*cm))
story.append(Paragraph("AI learning coach cá nhân cho sinh viên IT",
    ParagraphStyle("CoverTag", fontName="Arial", fontSize=12, leading=16,
                   textColor=colors.white, alignment=TA_CENTER)))
story.append(Spacer(1, 4*cm))

# Twitter Pitch
story.append(Paragraph("TWITTER PITCH", H2))
story.append(hr())
story.append(boxed([
    Paragraph("Most people use AI to get answers.<br/>"
              "We help them <b>think</b>.", TWITTER),
    Spacer(1, 4),
    Paragraph("Socratic AI dẫn dắt người học bằng câu hỏi gợi mở thay vì "
              "đưa đáp án — giúp sinh viên IT hiểu sâu vấn đề và tự giải "
              "được bài biến thể.", QUOTE),
], bg=colors.HexColor("#FAFAFA")))
story.append(Spacer(1, 0.6*cm))

# Meta block
meta_tbl = Table([
    ["Tác giả",   "Phan Thanh Sang — 2A202600280"],
    ["Track",     "Track 1 — AI Product Builder"],
    ["Phiên bản", "Milestone 1 Package · v1.0"],
    ["Ngày",      "06/05/2026"],
], colWidths=[3.2*cm, 13.3*cm])
meta_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 10),
    ("FONT", (0,0), (0,-1), "Arial-Bold", 10),
    ("TEXTCOLOR", (0,0), (0,-1), NAVY),
    ("TEXTCOLOR", (1,0), (1,-1), colors.black),
    ("BACKGROUND", (0,0), (0,-1), LIGHT),
    ("LINEBELOW", (0,0), (-1,-2), 0.3, BORDER),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(meta_tbl)
story.append(PageBreak())

# ============================ TRANG 2 =============================
# Pitch Memo + Market Analysis
story.append(Paragraph("Trang 2 · Pitch Memo + Market Analysis", H1))
story.append(hr())

story.append(Paragraph("1. Vấn đề và cơ hội", H2))
story.append(Paragraph(
    "Sinh viên IT năm 1–2 tại Việt Nam có dư tài nguyên học (YouTube, ChatGPT, "
    "tài liệu online) nhưng <b>thiếu một vòng lặp phản hồi giúp họ kiểm tra mức "
    "hiểu thật</b> — không có ai hỏi ngược lại, chỉ ra điểm mù và dẫn dắt từng "
    "bước. Hệ quả: vòng lặp <i>“copy đáp án → không nhớ → fail bài tương tự”</i> "
    "lặp lại mỗi tuần, GPA không cải thiện dù dùng AI nhiều.", BODY))

story.append(Paragraph("2. Founding belief", H2))
story.append(boxed([
    Paragraph("Học bền vững đến từ quá trình tự suy luận và đối mặt với điểm "
              "mù, không phải từ việc xem lời giải mẫu. Não bộ ghi nhớ qua nỗ "
              "lực nhận thức (cognitive effort), không qua sao chép.", QUOTE)
]))

story.append(Paragraph("3. Cơ hội sản phẩm", H2))
story.append(Paragraph(
    "Không phải <b>“AI trả lời nhanh hơn”</b>, mà là <b>“AI coach”</b> — cá "
    "nhân hóa theo hồ sơ hiểu biết từng người, phát hiện lỗ hổng kiến thức "
    "có hệ thống, và dẫn dắt qua Socratic dialogue cho đến khi người học tự "
    "suy ra được. Đo thành công bằng <b>khả năng tự giải bài biến thể</b>, "
    "không phải số câu trả lời đúng.", BODY))

story.append(Paragraph("4. Thị trường (TAM / SAM / SOM)", H2))
mkt_cell = S("mkt", fontSize=8.5, leading=11)
mkt_head = S("mkth", fontSize=9, leading=11, fontName="Arial-Bold",
             textColor=colors.white, alignment=TA_CENTER)
mkt = [
    [Paragraph("Layer", mkt_head), Paragraph("Quy mô", mkt_head),
     Paragraph("Cách tính (rút gọn)", mkt_head), Paragraph("Confidence", mkt_head)],
    [Paragraph("<b>TAM</b>", mkt_cell),
     Paragraph("~20–55M USD/năm", mkt_cell),
     Paragraph("≈2M sinh viên IT/CS tại VN+SEA · 15–20% có nhu cầu edtech AI · ARPU 3–6 USD/tháng", mkt_cell),
     Paragraph("low", mkt_cell)],
    [Paragraph("<b>SAM</b>", mkt_cell),
     Paragraph("~3–7M USD/năm", mkt_cell),
     Paragraph("200–300k sinh viên IT năm 1–3 tại VN · 10–15% sẵn sàng trả phí · ARPU 4–6 USD/tháng", mkt_cell),
     Paragraph("med", mkt_cell)],
    [Paragraph("<b>SOM</b>", mkt_cell),
     Paragraph("150–400k USD ARR (18–24 tháng)", mkt_cell),
     Paragraph("5–10k MAU cuối năm 1 · conversion 5–8% · ARPU ~4 USD/tháng", mkt_cell),
     Paragraph("low", mkt_cell)],
]
mkt_tbl = Table(mkt, colWidths=[1.6*cm, 3.8*cm, 8.8*cm, 2.3*cm])
mkt_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (0,1), (0,-1), "CENTER"),
    ("ALIGN", (-1,1), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("BACKGROUND", (0,1), (-1,-1), colors.white),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("LEFTPADDING", (0,0), (-1,-1), 5),
    ("RIGHTPADDING", (0,0), (-1,-1), 5),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
story.append(mkt_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<i>Lưu ý:</i> Bottom-up từ behavior segment (sinh viên IT VN năm 1–2) — "
    "đáng tin hơn top-down. Proxy benchmark: ELSA Speak (~1M user, conversion "
    "5–8%). Cần validate WTP và retention trong pilot 4–6 tuần trước khi "
    "build full product.", SMALL))
story.append(PageBreak())

# ============================ TRANG 3 =============================
# Customer + Pain (Need Map từ Day 16)
story.append(Paragraph("Trang 3 · Customer + Pain (Need Map)", H1))
story.append(hr())

story.append(Paragraph("Customer Segment Card", H2))
story.append(Paragraph(
    "<b>Đối tượng:</b> Sinh viên IT năm 1–2 tại các trường đại học Việt Nam "
    "đang học môn nền tảng (Programming, DSA, Database). Early adopters: năm 1, "
    "học kỳ 2 trở đi.", BODY))
story.append(Paragraph(
    "<b>Pain moment:</b> Xảy ra <i>sau khi nộp bài hoặc thi xong</i> — làm "
    "được bài cũ nhưng fail bài biến thể trong quiz; thi gặp dạng quen mà "
    "không giải được vì không hiểu cơ chế bên dưới.", BODY))
story.append(Paragraph(
    "<b>Why now:</b> (1) AI đã đủ phổ biến — barrier adoption gần bằng zero; "
    "(2) thói quen <i>“hỏi ChatGPT lấy đáp án”</i> đã tạo ra pain mới: điểm "
    "không cải thiện dù dùng AI nhiều.", BODY))
story.append(Paragraph(
    "<b>Access path:</b> CLB học thuật IT (PTIT, HUST, UET, VNU-HCM, UIT); "
    "nhóm học theo môn trên Zalo/Discord/Facebook; giảng viên trợ giảng làm "
    "early partner pilot trong lớp.", BODY))

story.append(Paragraph("3 Need ưu tiên (JTBD)", H2))

needs = [
    ("Need #1 — Scaffolded problem-solving",
     "Khi bị kẹt ở bài lập trình, sinh viên muốn nhận gợi ý theo từng nấc "
     "<b>không bị lộ đáp án ngay</b>, để tự suy ra được bước tiếp và ghi "
     "nhớ cách tư duy.",
     "ChatGPT/Copilot tối ưu cho tốc độ ra đáp án; không có incentive thiết "
     "kế để AI <i>từ chối trả lời</i> hoặc hỏi ngược lại."),
    ("Need #2 — Personalized knowledge-gap diagnosis",
     "Khi ôn thi 3–7 ngày, sinh viên muốn biết <b>chính xác mình hổng ở "
     "đâu</b> để ưu tiên đúng phần yếu, không tốn thời gian ôn lại phần "
     "đã vững.",
     "LMS phổ biến (Moodle, Google Classroom) cung cấp nội dung tĩnh, không "
     "có adaptive diagnosis theo thời gian thực."),
    ("Need #3 — Concept-to-application bridge",
     "Sau khi học xong khái niệm mới, sinh viên muốn được hỏi ngược để "
     "<b>tự diễn giải lại bằng lời của mình</b> và thử áp dụng ngay vào "
     "bối cảnh khác.",
     "Nội dung online phong phú nhưng one-way; Khan Academy có interactive "
     "exercise nhưng không có conversational AI điều chỉnh theo gap."),
]
need_rows = [["#", "Statement (JTBD)", "Why underserved"]]
for title, jtbd, gap in needs:
    need_rows.append([
        Paragraph(f"<b>{title}</b>", S("nt", fontSize=9, leading=11)),
        Paragraph(jtbd, S("nb", fontSize=9, leading=11)),
        Paragraph(gap, S("ng", fontSize=9, leading=11)),
    ])
need_tbl = Table(need_rows, colWidths=[4.0*cm, 6.5*cm, 6.0*cm])
need_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 10),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(need_tbl)
story.append(PageBreak())

# ============================ TRANG 4 =============================
# Solution + PRD Summary
story.append(Paragraph("Trang 4 · Solution + PRD Summary", H1))
story.append(hr())

story.append(Paragraph("Core Idea", H2))
story.append(boxed([
    Paragraph("AI <b>không trả lời ngay</b> — AI <b>hỏi ngược</b> để dẫn "
              "dắt người học suy luận, sau đó tóm lại insight và để người "
              "học tự diễn giải lại bằng lời của mình.", QUOTE)
]))

story.append(Paragraph("5 Core Features (PRD Day 17) — RICE prioritized", H2))

rice = [
    ["Feature", "Reach", "Impact", "Conf.", "Effort", "Score", "Phase"],
    ["Socratic Questioning Engine", "1000", "3", "0.8", "2", "1200", "NOW"],
    ["Use-case Templates",          "1200", "1", "0.9", "1", "1080", "NOW"],
    ["Insight Summary",             "900",  "1", "0.8", "1", "720",  "NOW"],
    ["Adaptive Depth Mode",         "800",  "2", "0.7", "2", "560",  "NEXT"],
    ["Conversation Memory",         "600",  "2", "0.6", "3", "240",  "LATER"],
]
rice_tbl = Table(rice, colWidths=[5.4*cm, 1.5*cm, 1.5*cm, 1.5*cm, 1.5*cm, 1.7*cm, 1.7*cm])
rice_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("ALIGN", (0,1), (0,-1), "LEFT"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("FONT", (5,1), (5,-1), "Arial-Bold", 9),
    ("TEXTCOLOR", (5,1), (5,-1), ACCENT),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
]))
story.append(rice_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>Formula:</b> Score = (Reach × Impact × Confidence) ÷ Effort &nbsp;·&nbsp; "
    "<b>Quick win:</b> Use-case Templates &nbsp;·&nbsp; "
    "<b>Strategic bet:</b> Socratic Questioning Engine.", SMALL))

story.append(Paragraph("Value Proposition", H2))
for t in [
    "<b>Clear thinking:</b> chuyển từ <i>“làm được bài”</i> sang <i>“hiểu được cơ chế”</i>.",
    "<b>Better decisions:</b> phát hiện điểm mù trước khi nộp bài.",
    "<b>Faster problem solving:</b> tự giải bài biến thể độc lập, không cần lời giải mẫu.",
]:
    story.append(Paragraph(f"• {t}", BULLET))

story.append(Paragraph("Aha Moment", H2))
story.append(boxed([
    Paragraph("<i>“Tôi hiểu vấn đề rõ hơn chỉ sau 1 session”</i> — đo qua "
              "khả năng diễn giải lại khái niệm bằng lời của mình và giải "
              "bài biến thể không nhìn gợi ý.", QUOTE)
], bg=colors.HexColor("#FFF6E6")))
story.append(PageBreak())

# ============================ TRANG 5 =============================
# Differentiation + Strategy + Moat
story.append(Paragraph("Trang 5 · Strategy + Differentiation + Moat", H1))
story.append(hr())

story.append(Paragraph("Strategy Statement", H2))
story.append(Paragraph(
    "<b>For</b> sinh viên IT năm 1–2 tại Việt Nam đang học các môn nền "
    "tảng (Programming, DSA, Database), <b>who struggle with</b> việc hiểu "
    "nông và lệ thuộc vào đáp án mẫu, <b>our product helps them</b> chuyển "
    "từ <i>“làm được bài”</i> sang <i>“hiểu được cơ chế”</i> — đo được qua "
    "khả năng tự giải bài biến thể và giải thích lại bằng lời của mình, "
    "<b>through</b> Socratic AI coaching: hỏi gợi mở nhiều nấc thay vì đưa "
    "đáp án, chẩn đoán knowledge gap theo từng chủ đề trong curriculum, và "
    "cá nhân hóa lộ trình ôn tập, <b>unlike</b> chatbot AI phổ thông tối ưu "
    "cho tốc độ trả lời, <b>because</b> chúng tôi leverage dữ liệu chuỗi "
    "tương tác học tập theo workflow môn IT cụ thể.", BODY))

# Differentiation table
story.append(Paragraph("Differentiation", H2))
diff = [
    ["", "ChatGPT / Copilot", "Socratic AI"],
    ["Mục tiêu UX", "Tốc độ ra đáp án", "Tốc độ ra <b>insight</b>"],
    ["Phản hồi", "One-way: trả lời", "Two-way: hỏi ngược + dẫn dắt"],
    ["Cá nhân hóa", "Per-prompt context", "Per-user knowledge gap"],
    ["Đo thành công", "User satisfaction", "Khả năng giải bài biến thể"],
    ["Bối cảnh", "Generic", "Curriculum IT VN cụ thể"],
]
diff_rows = [[Paragraph(c, S("d", fontSize=9, leading=11,
                             alignment=TA_CENTER if i==0 else TA_LEFT,
                             fontName="Arial-Bold" if i==0 else "Arial"))
              for c in r] for i, r in enumerate(diff)]
diff_tbl = Table(diff_rows, colWidths=[3.4*cm, 6.6*cm, 6.5*cm])
diff_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("BACKGROUND", (0,1), (0,-1), LIGHT),
    ("FONT", (0,1), (0,-1), "Arial-Bold", 9),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("ROWBACKGROUNDS", (1,1), (-1,-1), [colors.white, colors.HexColor("#F9FBFC")]),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(diff_tbl)

story.append(Paragraph("Moat Hypothesis", H2))
story.append(Paragraph(
    "<b>Cơ chế:</b> Pedagogical interaction dataset + domain-specific "
    "knowledge graph cho curriculum IT Việt Nam. Sau 1,000+ phiên học, hệ "
    "thống học được:", BODY_TIGHT))
for t in [
    "Câu hỏi nào ở mức khó nào <b>kích hoạt suy luận thật</b> vs gây frustration.",
    "Pattern <i>“sai bài JOIN vì không vững relational algebra”</i> — chỉ xuất hiện từ chuỗi tương tác dài.",
    "Tỷ lệ chuyển đổi <i>“hỏi đáp → tự giải bài biến thể”</i> — feedback loop measurable.",
]:
    story.append(Paragraph(f"• {t}", BULLET))
story.append(boxed([
    Paragraph("ChatGPT/Gemini có thể copy Socratic UX trong vài tháng, nhưng "
              "<b>không có dataset hành vi học theo curriculum VN</b> để "
              "calibrate — đây là lag thực sự.", QUOTE)
], bg=colors.HexColor("#FFF6E6")))
story.append(PageBreak())

# ============================ TRANG 6 =============================
# Financial Model
story.append(Paragraph("Trang 6 · Financial Model", H1))
story.append(hr())

story.append(Paragraph("Revenue Model", H2))
for t in [
    "<b>Freemium:</b> 3 session miễn phí/ngày — cover use-case ôn thi nhanh.",
    "<b>Paid Pro:</b> $5–10/tháng — unlimited sessions + knowledge-gap dashboard + revision plan.",
    "<b>B2B2C (NEXT):</b> partnership với CLB IT / khoa CNTT — 1 license sỉ cho 100–300 sinh viên/lớp.",
]:
    story.append(Paragraph(f"• {t}", BULLET))

story.append(Paragraph("Assumptions (early stage, 6 tháng)", H2))
fin = [
    ["Metric", "Giá trị", "Ghi chú"],
    ["MAU (cuối tháng 6)", "1,000",     "Acquisition qua CLB IT + Zalo group"],
    ["Conversion free → paid", "5%",   "Benchmark từ ELSA / edtech VN"],
    ["Paid users", "50",                "1,000 × 5%"],
    ["ARPU", "$7 / tháng",              "Trung bình giữa $5 và $10 tier"],
    ["MRR", "≈ $350",                   "50 × $7"],
    ["ARR (run-rate)", "≈ $4,200",      "MRR × 12"],
    ["Cost per session (LLM)", "$0.015","Cache + multi-provider fallback"],
    ["Sessions/paid user/tháng", "30",  "≈ 1 session/ngày"],
    ["COGS / paid user / tháng", "$0.45", "30 × $0.015"],
    ["Gross margin", "~94%",            "($7 − $0.45) / $7"],
]
fin_tbl = Table(fin, colWidths=[5.6*cm, 3.2*cm, 7.7*cm])
fin_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (1,1), (1,-1), "CENTER"),
    ("FONT", (1,1), (1,-1), "Arial-Bold", 9),
    ("TEXTCOLOR", (1,1), (1,-1), NAVY),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(fin_tbl)

story.append(Paragraph("CAC (Customer Acquisition Cost)", H2))
for t in [
    "<b>Organic (NOW):</b> $0–$2/user — qua CLB IT, Zalo group, giảng viên đối tác.",
    "<b>Paid (NEXT):</b> $3–$5/user — Facebook ads target sinh viên IT năm 1–2.",
    "<b>Blended CAC dự kiến:</b> $2 trong 6 tháng đầu (80% organic / 20% paid test).",
]:
    story.append(Paragraph(f"• {t}", BULLET))

story.append(Paragraph("Payback Period", H2))
story.append(boxed([
    Paragraph("<b>Payback ≈ &lt; 1 tháng</b> ở giai đoạn organic "
              "(CAC $2 / ARPU $7 × 94% margin = $6.6 lợi nhuận tháng 1).", QUOTE)
], bg=colors.HexColor("#E8F5E9")))
story.append(PageBreak())

# ============================ TRANG 7 =============================
# Unit Economics
story.append(Paragraph("Trang 7 · Unit Economics", H1))
story.append(hr())

story.append(Paragraph("LTV (Lifetime Value)", H2))
ltv = [
    ["Tham số", "Giá trị", "Logic"],
    ["ARPU", "$7 / tháng",        "Tier paid trung bình"],
    ["Gross margin", "94%",       "Cost LLM thấp nhờ cache"],
    ["Avg lifetime", "~10 tháng", "1 / churn rate 10% / tháng"],
    ["LTV (gross)", "$70",        "$7 × 10"],
    ["LTV (contribution)", "≈ $66", "$70 × 94%"],
]
ltv_tbl = Table(ltv, colWidths=[5.0*cm, 3.5*cm, 8.0*cm])
ltv_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (1,1), (1,-1), "CENTER"),
    ("FONT", (1,4), (1,5), "Arial-Bold", 9),
    ("TEXTCOLOR", (1,4), (1,5), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(ltv_tbl)

story.append(Paragraph("Retention Targets (NorthStar)", H2))
ret = [
    ["Cohort", "Mục tiêu", "Ý nghĩa"],
    ["W1 retention",  "≥ 30%", "User quay lại sau session đầu — validate aha moment"],
    ["W4 retention",  "≥ 20%", "Habit formation — thói quen học cùng AI"],
    ["M3 retention",  "≥ 12%", "Long-term value — sẵn sàng convert paid"],
    ["NPS",           "≥ 40",  "Chất lượng trải nghiệm tư duy"],
]
ret_tbl = Table(ret, colWidths=[3.6*cm, 2.8*cm, 10.1*cm])
ret_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (1,1), (1,-1), "CENTER"),
    ("FONT", (1,1), (1,-1), "Arial-Bold", 9),
    ("TEXTCOLOR", (1,1), (1,-1), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(ret_tbl)

story.append(Paragraph("LTV / CAC Ratio", H2))
ratio = [
    ["Phase",            "LTV", "CAC", "Ratio",  "Đánh giá"],
    ["Organic (NOW)",    "$66", "$2",  "33×",    "Excellent — push growth"],
    ["Mixed (NEXT)",     "$66", "$5",  "13×",    "Strong — vẫn rất tốt"],
    ["Paid scale (LATER)", "$66", "$15", "4.4×", "Healthy — benchmark > 3×"],
]
ratio_tbl = Table(ratio, colWidths=[4.0*cm, 2.0*cm, 2.0*cm, 2.0*cm, 6.5*cm])
ratio_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,-1), "Arial", 9),
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (1,1), (3,-1), "CENTER"),
    ("FONT", (3,1), (3,-1), "Arial-Bold", 10),
    ("TEXTCOLOR", (3,1), (3,-1), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(ratio_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<i>Lưu ý:</i> Retention 10%/tháng là <b>assumption cần validate</b> "
    "trong pilot 6 tuần đầu — nếu thực tế lifetime thấp hơn (e.g., 5 tháng), "
    "LTV giảm còn $33 và Ratio paid-scale chỉ còn 2.2× → cần tăng ARPU "
    "hoặc giảm CAC.", SMALL))
story.append(PageBreak())

# ============================ TRANG 8 =============================
# Roadmap + OKRs
story.append(Paragraph("Trang 8 · Roadmap (Now / Next / Later) + OKRs Q1", H1))
story.append(hr())

story.append(Paragraph("Roadmap", H2))
roadmap = [
    [Paragraph("<b>NOW</b> — Quick Wins", S("rh", fontName="Arial-Bold", fontSize=11, leading=14,
              textColor=colors.white, alignment=TA_CENTER)),
     Paragraph("<b>NEXT</b> — Strategic Bets", S("rh", fontName="Arial-Bold", fontSize=11, leading=14,
              textColor=colors.white, alignment=TA_CENTER)),
     Paragraph("<b>LATER</b> — Vision", S("rh", fontName="Arial-Bold", fontSize=11, leading=14,
              textColor=colors.white, alignment=TA_CENTER))],
    [Paragraph("• User không biết bắt đầu — thiếu entry point<br/>"
               "• User overload AI nhưng không extract được insight<br/>"
               "• User không thấy giá trị ngay lần đầu (aha moment)",
               S("rb", fontSize=9, leading=13)),
     Paragraph("• User không duy trì flow suy nghĩ qua nhiều bước<br/>"
               "• Socratic questioning chưa context-aware<br/>"
               "• User không nhận ra tiến bộ tư duy của mình",
               S("rb", fontSize=9, leading=13)),
     Paragraph("• AI chưa thành thinking partner lâu dài<br/>"
               "• Chưa đo được “thinking quality” — measurable asset<br/>"
               "• Chưa có thinking model riêng",
               S("rb", fontSize=9, leading=13))],
]
roadmap_tbl = Table(roadmap, colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
roadmap_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,0), colors.HexColor("#1B7A3F")),
    ("BACKGROUND", (1,0), (1,0), colors.HexColor("#C9881B")),
    ("BACKGROUND", (2,0), (2,0), colors.HexColor("#A93226")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("BACKGROUND", (0,1), (-1,-1), LIGHT),
]))
story.append(roadmap_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<i>Strategy narrative:</i> Giải bài toán onboarding + immediate value "
    "trước → build adaptive thinking systems → trở thành long-term thinking "
    "partner.", SMALL))

story.append(Paragraph("OKRs · Quarter 1", H2))
story.append(boxed([
    Paragraph("<b>Objective:</b> Help users experience their first <i>aha "
              "moment</i> with Socratic AI — shifting from <b>asking for "
              "answers</b> to <b>thinking clearly</b>.", QUOTE)
], bg=colors.HexColor("#EAF4F5")))

okr = [
    ["KR",   "Loại",     "Chỉ số mục tiêu",                                    "Ý nghĩa"],
    ["KR1",  "Leading",  "40% new users hoàn thành ≥1 full Socratic session\n(≥ 3 lượt back-and-forth) trong lần đầu",
                         "User có dùng đúng cách"],
    ["KR2",  "Lagging",  "1,000 MAU + 5% convert paid (hoặc waitlist intent)",
                         "Có demand thật"],
    ["KR3",  "Quality",  "30% W1 retention + NPS ≥ 40",
                         "Sản phẩm có tạo value"],
]
okr_rows = [okr[0]] + [
    [Paragraph(c, S("ok", fontSize=9, leading=12)) if isinstance(c, str) else c
     for c in r] for r in okr[1:]
]
okr_tbl = Table(okr_rows, colWidths=[1.2*cm, 2.0*cm, 8.5*cm, 4.8*cm])
okr_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,0), "Arial-Bold", 10),
    ("FONT", (0,1), (-1,-1), "Arial", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("ALIGN", (0,1), (1,-1), "CENTER"),
    ("FONT", (0,1), (0,-1), "Arial-Bold", 10),
    ("TEXTCOLOR", (0,1), (0,-1), ACCENT),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(okr_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph("<i>One-liner:</i> If users don’t experience better "
    "thinking in the first session, nothing else matters.", SMALL))
story.append(PageBreak())

# ============================ TRANG 9 =============================
# Dependency Map + Critical Path
story.append(Paragraph("Trang 9 · Dependency Map + Critical Path", H1))
story.append(hr())

story.append(Paragraph("External Dependencies (có thể “giết” dự án trong 30 ngày)", H2))
dep = [
    ["#", "Dependency", "Worst-case", "Plan B (≤ 7 ngày)", "Cost B"],
    ["1", "LLM Provider\n(OpenAI / Anthropic)",
     "Tăng giá / rate limit → cost vượt kiểm soát",
     "Multi-provider fallback (Anthropic / Ollama) + cache response",
     "5–7 ngày · $200–500"],
    ["2", "User Acquisition\n(FB Group / Reddit / Discord)",
     "Bị ban / reach giảm → không có user mới",
     "Landing page + waitlist + viral invite loop",
     "3–5 ngày · $50–200"],
    ["3", "UX Adoption Risk\n(user không quen bị hỏi ngược)",
     "User thấy “bị làm phiền” → churn lần đầu",
     "Guided mode (gợi ý + giải thích) + switch sang direct answer",
     "5–7 ngày · $0–100"],
]
dep_rows = [dep[0]] + [
    [Paragraph(c, S("dp", fontSize=8.5, leading=11)) if isinstance(c, str) else c
     for c in r] for r in dep[1:]
]
dep_tbl = Table(dep_rows, colWidths=[0.7*cm, 3.5*cm, 4.0*cm, 5.0*cm, 3.3*cm])
dep_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,0), "CENTER"),
    ("FONT", (0,1), (0,-1), "Arial-Bold", 11),
    ("TEXTCOLOR", (0,1), (0,-1), ACCENT),
    ("ALIGN", (0,1), (0,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING", (0,0), (-1,-1), 5),
    ("RIGHTPADDING", (0,0), (-1,-1), 5),
]))
story.append(dep_tbl)

story.append(Paragraph("Critical Path · Goal: User có aha moment lần đầu", H2))
cp = [
    ["#", "Task", "Blocks", "Trên Critical Path?"],
    ["1", "Define core Socratic loop (Q → A → deeper Q)", "toàn bộ",     "YES"],
    ["2", "Onboarding + use-case templates",              "3, 4, 5",     "YES"],
    ["3", "Implement Socratic Questioning Engine v1",     "4",           "—"],
    ["4", "Basic UI (chat + guided prompts)",             "6",           "YES"],
    ["5", "Insight Summary (end of session)",             "improves 7",  "—"],
    ["6", "Launch to 100 early users (manual)",           "—",           "YES"],
    ["7", "Collect feedback + iterate loop",              "—",           "YES"],
]
cp_tbl = Table(cp, colWidths=[0.8*cm, 8.5*cm, 4.0*cm, 3.2*cm])
cp_tbl.setStyle(TableStyle([
    ("FONT", (0,0), (-1,0), "Arial-Bold", 9),
    ("FONT", (0,1), (-1,-1), "Arial", 9),
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("ALIGN", (1,1), (1,-1), "LEFT"),
    ("FONT", (-1,1), (-1,-1), "Arial-Bold", 11),
    ("TEXTCOLOR", (-1,1), (-1,-1), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, BORDER),
    ("TOPPADDING", (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
]))
story.append(cp_tbl)
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<b>Critical path:</b> &nbsp; 1 → 2 → 4 → 6 → 7 &nbsp; "
    "(Define loop → onboarding → UI → launch → feedback). "
    "<i>Speed to first “thinking value” matters more than perfect AI.</i>",
    BODY_TIGHT))

# Closing
story.append(Spacer(1, 0.4*cm))
story.append(boxed([
    Paragraph("We are not building a better chatbot.<br/>"
              "We are building a <b>better way to think</b>.", CLOSING)
], bg=colors.HexColor("#0F2A44"), border=NAVY))

# Phụ lục
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Phụ lục", H3))
for t in [
    "Day 17 PRD đầy đủ: <i>day_16_submission.md</i> + <i>rice_matrix.md</i> (cùng repo).",
    "Day 18 Financial Excel: <i>(link bổ sung khi sẵn sàng)</i>.",
    "Roadmap chi tiết: <i>roadmap_nnl.md</i> · OKRs: <i>okrs.md</i> · Dependency: <i>dependency_map.md</i>.",
]:
    story.append(Paragraph(f"• {t}", S("apx", fontSize=8.5, leading=11, textColor=MUTED)))

# ===================================================================
#                              BUILD PDF
# ===================================================================
out_path = r"d:\VinUni\source_code\bai_giang\2A202600280-PhanThanhSang-Track1-Lab20\PhanThanhSang_Milestone1_InvestorPackage.pdf"

doc = SimpleDocTemplate(
    out_path, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=1.9*cm, bottomMargin=1.7*cm,
    title="Socratic AI — Milestone 1 Investor Package",
    author="Phan Thanh Sang — 2A202600280",
)

def first_page(canvas, doc):
    cover_page(canvas, doc)

def later_pages(canvas, doc):
    page_header_footer(canvas, doc)

doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
print(f"OK -> {out_path}")
