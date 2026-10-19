# -*- coding: utf-8 -*-
"""
build_sites.py - NÂNG CẤP TOÀN DIỆN VỚI FLASHCARD & SCROLLSPY
Assembles:
1. index.html (Bản desktop)
2. mobile.html (Bản mobile)
"""
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from data_b0_b1 import B0_CONTENT, B1_CONTENT
from data_b2 import B2_CONTENT
from data_b4_b5 import B4_CONTENT, B5_CONTENT
from data_b6 import B6_CONTENT

# ============================================================
# FLASHCARDS DATA CHO TỪNG BÀI
# ============================================================
FC_B1 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 1 (Chạm vào thẻ để lật mặt sau)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; BẢN CHẤT</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Cân bằng hóa học có dừng lại không?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; CÂN BẰNG ĐỘNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>KHÔNG HỀ DỪNG LẠI!</strong> vt = vn > 0. Các chất vẫn phản ứng liên tục với tốc độ bằng nhau nên nồng độ không đổi.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; HẰNG SỐ Kc</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Chất rắn có ghi vào biểu thức Kc không?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; BẪY KINH ĐIỂN</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>TUYỆT ĐỐI KHÔNG!</strong> Nồng độ chất rắn tinh khiết được coi là hằng số và bỏ qua khỏi biểu thức Kc.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; LE CHATELIER</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Tăng nhiệt độ thì cân bằng chuyển dịch theo chiều nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TĂNG THU - GIẢM TỎA</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Cân bằng dịch theo <strong>CHIỀU THU NHIỆT (&Delta;H &gt; 0)</strong> để triệt tiêu bớt lượng nhiệt vừa cấp vào.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; CHẤT XÚC TÁC</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Chất xúc tác có làm tăng hiệu suất tạo sản phẩm không?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; NGOẠI LỆ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>KHÔNG!</strong> Xúc tác chỉ làm tăng tốc độ đạt tới cân bằng, không làm chuyển dịch cân bằng và không tăng hiệu suất.</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B2 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 2 (Chạm vào thẻ để lật mặt sau)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; SỰ ĐIỆN LI</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Chất điện li mạnh gồm những loại chất nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; BỘ BA ĐIỆN LI MẠNH</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Gồm: <strong>Acid mạnh</strong> (HCl, HNO3, H2SO4...), <strong>Base mạnh</strong> (NaOH, KOH, Ba(OH)2...) và <strong>hầu hết các muối tan</strong>.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; THUYẾT BRØNSTED</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Acid là gì và Base là gì theo Brønsted?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; QUY TẮC PROTON</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>Acid:</strong> Là chất CHO proton (H+).<br><strong>Base:</strong> Là chất NHẬN proton (H+).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; TÍNH pH KIỀM</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Dung dịch NaOH 0,001 M có pH bằng mấy?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; BẪY pOH</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">[OH-] = 10^-3 M &rarr; pOH = 3.<br>&rArr; <strong>pH = 14 &minus; 3 = 11</strong> (Đứa nào bảo pH = 3 là ăn 0 điểm!).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; CHUẨN ĐỘ</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Khi nào thì dừng chuẩn độ bằng phenolphthalein?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; ĐIỂM TƯƠNG ĐƯƠNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Dừng khi dung dịch chuyển sang màu <strong>hồng nhạt bền vững trong khoảng 30 giây</strong>.</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B4 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 4 (Chạm vào thẻ để lật mặt sau)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; CẤU TẠO</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Tại sao Nitrogen lại rất trơ ở nhiệt độ thường?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; LIÊN KẾT BA</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Do phân tử N2 có <strong>liên kết ba N&equiv;N</strong> cực kỳ bền vững với năng lượng liên kết Eb = 945 kJ/mol.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; NGOẠI LỆ KIM LOẠI</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Kim loại nào phản ứng với N2 ngay ở nhiệt độ thường?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; DUY NHẤT LITHIUM</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>DUY NHẤT Lithium (Li)</strong>: 6Li + N2 &rarr; 2Li3N. Các kim loại khác (như Mg, Ca) đều phải nung nóng.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; MÀU SẮC KHÍ</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Khí NO có màu gì và NO2 có màu gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; MÀU KHÍ KINH ĐIỂN</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>NO:</strong> Không màu (hóa nâu ngoài không khí).<br><strong>NO2:</strong> Màu <strong>nâu đỏ</strong>, mùi xốc, cực độc.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; ỨNG DỤNG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Tại sao bơm khí N2 vào túi bim bim?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; BẢO QUẢN THỰC PHẨM</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">N2 rất trơ, không có oxy nên dầu mỡ không bị oxi hóa (chống ôi thiu) và đệm khí giúp bim bim không vỡ nát.</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B5 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 5 (Chạm vào thẻ để lật mặt sau)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; NGUYÊN NHÂN TÍNH BASE</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Tại sao NH3 lại có tính base?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; CẶP ELECTRON TỰ DO</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Do nguyên tử N còn <strong>1 cặp electron tự do</strong> chưa liên kết, dễ dàng nhận proton H+.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; KHÓI TRẮNG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Khói trắng xuất hiện khi nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; NH3 + HCl</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Khi để khí NH3 và khí HCl đặc gần nhau tạo các hạt tinh thể <strong>muối NH4Cl trắng</strong> bay lơ lửng.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; NHẬN BIẾT NH4+</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Dùng gì để nhận biết ion NH4+?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; DUNG DỊCH KIỀM</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Dùng dung dịch <strong>NaOH (đun nóng)</strong> &rarr; bốc khí NH3 mùi khai làm xanh quỳ tím ẩm.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; BỘT NỞ</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Muối ammonium nào dùng làm bột nở bánh bao?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; NH4HCO3</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>NH4HCO3</strong> (Amoni hidrocacbonat): khi nướng nhiệt phân thành khí NH3 + CO2 + H2O tạo độ xốp.</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B6 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 6 (Chạm vào thẻ để lật mặt sau)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; BẪY KHÍ H2</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Kim loại tác dụng với HNO3 có sinh ra khí H2 không?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TUYỆT ĐỐI KHÔNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>KHÔNG BAO GIỜ!</strong> N(+5) là chất oxi hóa mạnh hơn H+, nhận e tạo các sản phẩm khử NO, NO2, N2O, N2, NH4NO3.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; THỤ ĐỘNG HÓA</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Những kim loại nào bị thụ động hóa trong HNO3 đặc nguội?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; BỘ BA Fe, Al, Cr</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>Fe (Sắt), Al (Nhôm), Cr (Crom)</strong> tạo màng oxit bền bảo vệ kim loại, dùng thùng nhôm/thép chở HNO3 đặc nguội.</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; MƯA ACID</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Nước mưa có pH bao nhiêu thì coi là mưa acid?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; pH &lt; 5,6</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Khi <strong>pH &lt; 5,6</strong> (bình thường là khoảng 5,6 do hòa tan khí CO2).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; PHÚ DƯỠNG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Hai nguyên tố nào gây ra hiện tượng phú dưỡng?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; NITROGEN & PHOSPHORUS</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Dư thừa <strong>Nitrogen (N)</strong> từ đạm nitrate và <strong>Phosphorus (P)</strong> từ phosphate trong bột giặt.</p>
      </div>
    </div>
  </div>
</div>
"""

# ============================================================
# CSS FLASHCARD DÙNG CHUNG
# ============================================================
FLASHCARD_CSS = """
/* FLASHCARD DECK */
.flashcard-deck {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin: 14px 0 20px;
}
.flashcard {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 16px;
  cursor: pointer;
  transition: transform 0.25s, border-color 0.25s, background 0.25s;
  user-select: none;
  min-height: 125px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.flashcard:hover {
  border-color: var(--accent-blue);
  transform: translateY(-2px);
}
.flashcard.flipped {
  background: rgba(105,240,174,0.08);
  border-color: var(--accent-green);
}
"""

# ============================================================
# JAVASCRIPT CHUNG NÂNG CẤP VỚI FLIP CARD & SCROLLSPY
# ============================================================
COMMON_JS = """
// Quản lý Accordion
function toggleAcc(btn) {
  btn.classList.toggle('open');
  var content = btn.nextElementSibling;
  content.classList.toggle('open');
}

// Ẩn/hiện đáp án
function toggleAnswer(btn) {
  var ans = btn.nextElementSibling;
  ans.classList.toggle('visible');
  if (ans.classList.contains('visible')) {
    btn.innerText = '🙈 Thu gọn lời giải';
  } else {
    btn.innerText = '🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!';
  }
}

// Lật thẻ Flashcard
function flipCard(card) {
  card.classList.toggle('flipped');
  var front = card.querySelector('.fc-front');
  var back = card.querySelector('.fc-back');
  if (card.classList.contains('flipped')) {
    front.style.display = 'none';
    back.style.display = 'block';
  } else {
    front.style.display = 'block';
    back.style.display = 'none';
  }
}

// Modal xem ảnh SGK
function openSgkModal(filename) {
  var modal = document.getElementById('img-modal');
  var img = document.getElementById('img-modal-img');
  img.src = filename;
  modal.classList.add('open');
}

// Chọn Đúng / Sai
function selectTF(btn, val) {
  var parent = btn.parentElement;
  var btns = parent.querySelectorAll('.tf-btn');
  btns.forEach(function(b) { b.classList.remove('selected'); });
  btn.classList.add('selected');
  parent.dataset.selected = val;
}

// Chấm điểm Quiz cho từng bài
function gradeQuiz(lessonId) {
  var section = document.getElementById(lessonId + '-quiz');
  if (!section) return;

  var questions = section.querySelectorAll('.quiz-q');
  var score = 0;
  var total = questions.length;

  questions.forEach(function(q) {
    var type = q.dataset.type;
    var correctAns = q.dataset.ans;
    var explain = q.querySelector('.quiz-explain');

    if (type === 'mc') {
      var selected = q.querySelector('input[type="radio"]:checked');
      var options = q.querySelectorAll('.quiz-option');
      options.forEach(function(opt) {
        var radio = opt.querySelector('input');
        if (radio.value === correctAns) {
          opt.classList.add('correct');
        }
      });
      if (selected) {
        if (selected.value === correctAns) {
          score++;
        } else {
          selected.parentElement.classList.add('wrong');
        }
      }
      if (explain) explain.classList.add('show');
    } 
    else if (type === 'tf') {
      var tfContainer = q.querySelector('.tf-options');
      var userVal = tfContainer ? tfContainer.dataset.selected : null;
      var tfBtns = q.querySelectorAll('.tf-btn');
      tfBtns.forEach(function(b) {
        if (b.innerText.trim() === (correctAns === 'T' ? 'Đúng' : 'Sai')) {
          b.classList.add('correct');
        }
      });
      if (userVal === correctAns) {
        score++;
      } else if (userVal) {
        tfBtns.forEach(function(b) {
          if (b.classList.contains('selected') && !b.classList.contains('correct')) {
            b.classList.add('wrong');
          }
        });
      }
      if (explain) explain.classList.add('show');
    }
    else if (q.classList.contains('quiz-essay')) {
      var txt = q.querySelector('textarea');
      var sample = q.querySelector('.sample-answer');
      if (txt && txt.value.trim().length > 10) {
        score++;
      }
      if (sample) sample.classList.add('show');
    }
  });

  var badge = document.getElementById(lessonId + '-score');
  if (badge) {
    badge.style.display = 'inline-block';
    badge.innerText = 'Điểm của bạn: ' + score + '/' + total;
    if (score >= 12) {
      badge.style.background = 'rgba(105,240,174,0.2)';
      badge.style.borderColor = 'var(--accent-green)';
      alert('🎉 ĐỈNH CỦA CHÓP! Mày đạt ' + score + '/' + total + ' điểm. Mất gốc cái nỗi gì, trình độ này đủ sức gánh cả lớp rồi!');
    } else if (score >= 8) {
      badge.style.background = 'rgba(255,213,79,0.2)';
      badge.style.borderColor = 'var(--accent-yellow)';
      alert('⚡ ỔN ÁP! Mày được ' + score + '/' + total + ' điểm. Đọc kĩ lại mấy câu giải thích màu đỏ để không bị lừa khi đi thi thật nhé!');
    } else {
      badge.style.background = 'rgba(255,82,82,0.2)';
      badge.style.borderColor = 'var(--accent-red)';
      alert('⚠️ HƠI NGUY HIỂM! Mới được ' + score + '/' + total + ' điểm thôi. Xem lại mấy chỗ giải thích bị sai, đừng nản, làm lại lần nữa là nhớ ngay!');
    }
  }
}

// Đổi Theme Dark/Light
var currentTheme = localStorage.getItem('hoa11_theme') || 'dark';
document.documentElement.setAttribute('data-theme', currentTheme);

function toggleTheme() {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  localStorage.setItem('hoa11_theme', currentTheme);
  updateThemeIcon();
}

function updateThemeIcon() {
  var btns = document.querySelectorAll('#theme-toggle, .btn-theme');
  btns.forEach(function(btn) {
    if (btn) btn.innerText = currentTheme === 'dark' ? '☀️' : '🌙';
  });
}
updateThemeIcon();

var tBtn = document.getElementById('theme-toggle');
if (tBtn) tBtn.addEventListener('click', toggleTheme);

// Progress Bar
window.addEventListener('scroll', function() {
  var h = document.documentElement;
  var b = document.body;
  var st = 'scrollTop';
  var sh = 'scrollHeight';
  var percent = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
  var pb = document.getElementById('progress-bar');
  if (pb) pb.style.width = percent + '%';
});

// ScrollSpy cho Sticky TOC trên Desktop
window.addEventListener('scroll', function() {
  var sections = document.querySelectorAll('.lesson-section');
  var scrollPos = window.scrollY + 140;
  var currentId = '';
  sections.forEach(function(sec) {
    if (sec.offsetTop <= scrollPos && (sec.offsetTop + sec.offsetHeight) > scrollPos) {
      currentId = sec.id;
    }
  });
  if (currentId) {
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(function(item) {
      if (item.getAttribute('href') === '#' + currentId) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }
});
"""

# ============================================================
# LẮP RÁP INDEX.HTML (DESKTOP)
# ============================================================
def build_index_html():
    css_and_head = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hóa Học 11 – Kết Nối Tri Thức | Ôn Thi Siêu Tốc Cứu Nạn Mất Gốc</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
/* CSS VARIABLES */
:root {
  --bg-primary: #0f1117;
  --bg-secondary: #1a1d27;
  --bg-card: #1e2233;
  --bg-hover: #252840;
  --text-primary: #e8eaf6;
  --text-secondary: #9fa8da;
  --text-muted: #5c6bc0;
  --accent-blue: #5c6fff;
  --accent-blue-light: #7986ff;
  --accent-yellow: #ffd54f;
  --accent-yellow-dark: #f9a825;
  --accent-red: #ff5252;
  --accent-green: #69f0ae;
  --accent-purple: #ce93d8;
  --accent-orange: #ffab40;
  --border-color: #2d3256;
  --border-bright: #3d4280;
  --shadow: 0 4px 24px rgba(0,0,0,0.5);
  --shadow-lg: 0 8px 40px rgba(0,0,0,0.7);
  --radius: 12px;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --sidebar-width: 290px;
  --font-main: 'Be Vietnam Pro', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --transition: all 0.25s ease;
}

[data-theme="light"] {
  --bg-primary: #f0f2ff;
  --bg-secondary: #e8eaf6;
  --bg-card: #ffffff;
  --bg-hover: #e3e6ff;
  --text-primary: #1a1d3a;
  --text-secondary: #3949ab;
  --text-muted: #7986cb;
  --accent-blue: #3f51b5;
  --accent-blue-light: #5c6fff;
  --accent-yellow: #f57f17;
  --accent-yellow-dark: #e65100;
  --accent-red: #c62828;
  --accent-green: #2e7d32;
  --accent-purple: #7b1fa2;
  --accent-orange: #e65100;
  --border-color: #c5cae9;
  --border-bright: #9fa8da;
  --shadow: 0 4px 24px rgba(63,81,181,0.12);
  --shadow-lg: 0 8px 40px rgba(63,81,181,0.18);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--font-main);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.75;
  overflow-x: hidden;
  transition: background 0.3s, color 0.3s;
}

#progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple), var(--accent-yellow));
  width: 0%; z-index: 9999;
}

.page-wrapper { display: flex; min-height: 100vh; }

/* SIDEBAR TOC */
#sidebar {
  position: fixed; top: 0; left: 0;
  width: var(--sidebar-width); height: 100vh;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  overflow-y: auto; z-index: 1000;
  transition: transform 0.3s ease;
  display: flex; flex-direction: column;
}
#sidebar.collapsed { transform: translateX(calc(-1 * var(--sidebar-width))); }

.sidebar-header {
  padding: 20px 16px 12px;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-card);
  position: sticky; top: 0; z-index: 1;
}
.sidebar-logo {
  font-size: 0.75rem; font-weight: 700; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;
}
.sidebar-title {
  font-size: 0.95rem; font-weight: 800; color: var(--accent-blue-light); line-height: 1.3;
}
.sidebar-nav { padding: 12px 0; flex: 1; }
.nav-section-label {
  padding: 8px 16px 4px; font-size: 0.65rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 2px; color: var(--text-muted);
}
.nav-item {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 16px; color: var(--text-secondary);
  text-decoration: none; font-size: 0.82rem; font-weight: 500;
  border-left: 3px solid transparent; transition: var(--transition);
}
.nav-item:hover { background: var(--bg-hover); color: var(--text-primary); border-left-color: var(--accent-blue); }
.nav-item.active { background: var(--bg-hover); color: var(--accent-blue-light); border-left-color: var(--accent-blue-light); font-weight: 700; }
.sidebar-footer { padding: 12px 16px; border-top: 1px solid var(--border-color); }

/* MAIN CONTENT */
#main-content {
  margin-left: var(--sidebar-width); flex: 1; min-width: 0;
  transition: margin-left 0.3s ease; padding: 0 0 80px;
}
#main-content.expanded { margin-left: 0; }

#topbar {
  position: sticky; top: 0; z-index: 900;
  background: var(--bg-secondary); border-bottom: 1px solid var(--border-color);
  padding: 12px 24px; display: flex; align-items: center; gap: 12px;
  backdrop-filter: blur(12px);
}
.topbar-title { font-size: 0.9rem; font-weight: 700; color: var(--text-primary); flex: 1; }
.btn-icon {
  width: 36px; height: 36px; border-radius: var(--radius-sm);
  border: 1px solid var(--border-color); background: var(--bg-card);
  color: var(--text-primary); cursor: pointer; display: flex;
  align-items: center; justify-content: center; font-size: 1.1rem;
  transition: var(--transition); flex-shrink: 0;
}
.btn-icon:hover { background: var(--accent-blue); border-color: var(--accent-blue); color: white; transform: scale(1.05); }

/* HERO */
.hero {
  background: linear-gradient(135deg, #0f1117 0%, #1a1040 40%, #0d1a3a 100%);
  padding: 60px 40px; text-align: center; border-bottom: 1px solid var(--border-color);
}
[data-theme="light"] .hero {
  background: linear-gradient(135deg, #e8eaf6 0%, #c5cae9 40%, #bbdefb 100%);
}
.hero-emoji { font-size: 3.5rem; margin-bottom: 14px; display: block; }
.hero h1 {
  font-size: 2.2rem; font-weight: 800;
  background: linear-gradient(135deg, var(--accent-blue-light), var(--accent-purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 12px; line-height: 1.25;
}
.hero p { font-size: 1rem; color: var(--text-secondary); max-width: 650px; margin: 0 auto 24px; }
.hero-tags { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.hero-tag {
  padding: 4px 14px; border-radius: 999px; font-size: 0.75rem; font-weight: 600;
  border: 1px solid;
}
.hero-tag.blue { background: rgba(92,111,255,0.15); border-color: var(--accent-blue); color: var(--accent-blue-light); }
.hero-tag.yellow { background: rgba(255,213,79,0.15); border-color: var(--accent-yellow); color: var(--accent-yellow); }
.hero-tag.green { background: rgba(105,240,174,0.15); border-color: var(--accent-green); color: var(--accent-green); }
.hero-tag.red { background: rgba(255,82,82,0.15); border-color: var(--accent-red); color: var(--accent-red); }

.content-area { max-width: 900px; margin: 0 auto; padding: 32px 24px; }
.lesson-section { margin-bottom: 60px; }
.lesson-header {
  display: flex; align-items: flex-start; gap: 16px; margin-bottom: 28px;
  padding-bottom: 20px; border-bottom: 2px solid var(--border-color);
}
.lesson-number {
  min-width: 56px; height: 56px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-radius: var(--radius); display: flex; align-items: center;
  justify-content: center; font-size: 1.4rem; font-weight: 800; color: white;
  box-shadow: 0 4px 16px rgba(92,111,255,0.4); flex-shrink: 0;
}
.lesson-meta h2 { font-size: 1.6rem; font-weight: 800; color: var(--text-primary); margin-bottom: 6px; }
.lesson-meta .lesson-sub { font-size: 0.82rem; color: var(--text-muted); font-weight: 500; }
.lesson-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 8px; }
.lesson-tag {
  padding: 2px 10px; border-radius: 999px; font-size: 0.7rem; font-weight: 600;
  background: var(--bg-hover); color: var(--text-secondary); border: 1px solid var(--border-color);
}

/* BOXES */
.box { border-radius: var(--radius); padding: 20px 24px; margin-bottom: 20px; border-left: 4px solid; }
.box-theory { background: rgba(92,111,255,0.08); border: 1px solid rgba(92,111,255,0.25); border-left: 4px solid var(--accent-blue); }
.box-theory .box-title { color: var(--accent-blue-light); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-formula { background: rgba(255,213,79,0.07); border: 1px solid rgba(255,213,79,0.3); border-left: 4px solid var(--accent-yellow); }
.box-formula .box-title { color: var(--accent-yellow); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-warning { background: rgba(255,82,82,0.07); border: 1px solid rgba(255,82,82,0.3); border-left: 4px solid var(--accent-red); }
.box-warning .box-title { color: var(--accent-red); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-story { background: rgba(105,240,174,0.07); border: 1px solid rgba(105,240,174,0.25); border-left: 4px solid var(--accent-green); }
.box-story .box-title { color: var(--accent-green); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-recall { background: rgba(206,147,216,0.07); border: 1px solid rgba(206,147,216,0.3); border-left: 4px solid var(--accent-purple); border-radius: var(--radius); }
.box-recall .box-title { color: var(--accent-purple); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }
.box-combo { background: rgba(255,171,64,0.07); border: 1px solid rgba(255,171,64,0.3); border-left: 4px solid var(--accent-orange); border-radius: var(--radius); }
.box-combo .box-title { color: var(--accent-orange); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; }

/* FORMULA DISPLAY & MATH */
sub, sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sub { bottom: -0.25em; }
sup { top: -0.5em; }

.fraction {
  display: inline-flex;
  flex-direction: column;
  vertical-align: middle;
  text-align: center;
  padding: 0 4px;
  line-height: 1.15;
  font-size: 0.95em;
}
.fraction .num {
  border-bottom: 2px solid currentColor;
  padding-bottom: 3px;
  margin-bottom: 2px;
  display: block;
}
.fraction .den {
  padding-top: 2px;
  display: block;
}

.formula-display {
  background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm);
  padding: 16px 20px; margin: 12px 0; font-family: var(--font-mono); font-size: 1.05rem;
  font-weight: 600; color: var(--accent-yellow); text-align: center;
  overflow-x: auto;
}
.formula-label { font-size: 0.72rem; color: var(--text-muted); text-align: center; margin-top: -8px; margin-bottom: 8px; font-weight: 500; }

/* ACCORDION */
.accordion-item { border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 8px; overflow: hidden; }
.accordion-trigger {
  width: 100%; background: var(--bg-card); border: none; padding: 14px 18px;
  color: var(--text-primary); font-family: var(--font-main); font-size: 0.9rem;
  font-weight: 600; text-align: left; cursor: pointer; display: flex;
  align-items: center; justify-content: space-between; gap: 12px;
}
.accordion-trigger:hover { background: var(--bg-hover); }
.accordion-trigger .acc-icon { font-size: 0.8rem; color: var(--text-muted); transition: transform 0.3s; }
.accordion-trigger.open .acc-icon { transform: rotate(180deg); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; background: var(--bg-secondary); }
.accordion-content.open { max-height: 2500px; }
.accordion-inner { padding: 16px 18px; }

/* TOOLTIP */
.tooltip { position: relative; cursor: help; border-bottom: 1px dashed var(--accent-blue); color: var(--accent-blue-light); font-weight: 600; }
.tooltip::after {
  content: attr(data-tip); position: absolute; bottom: calc(100% + 8px); left: 50%;
  transform: translateX(-50%); background: var(--bg-card); border: 1px solid var(--border-bright);
  color: var(--text-primary); padding: 8px 12px; border-radius: var(--radius-sm);
  font-size: 0.78rem; font-weight: 400; width: 220px; white-space: normal;
  text-align: center; box-shadow: var(--shadow); z-index: 100; opacity: 0;
  pointer-events: none; transition: opacity 0.2s; line-height: 1.5;
}
.tooltip:hover::after { opacity: 1; }

h3.sec-title { font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 28px 0 14px; display: flex; align-items: center; gap: 10px; }
h3.sec-title::before { content: ''; width: 4px; height: 20px; background: linear-gradient(180deg, var(--accent-blue), var(--accent-purple)); border-radius: 2px; }
h4.sub-title { font-size: 1rem; font-weight: 700; color: var(--text-secondary); margin: 20px 0 10px; padding-left: 12px; border-left: 3px solid var(--accent-blue); }

/* TABLE */
.tbl-wrap { overflow-x: auto; margin: 16px 0; border-radius: var(--radius-sm); }
table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
thead { background: var(--bg-hover); }
th { padding: 10px 14px; text-align: left; font-weight: 700; color: var(--text-secondary); font-size: 0.78rem; text-transform: uppercase; border-bottom: 2px solid var(--border-bright); }
td { padding: 9px 14px; border-bottom: 1px solid var(--border-color); color: var(--text-primary); }
tr:hover td { background: var(--bg-hover); }

.compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }
.compare-card { background: var(--bg-card); border-radius: var(--radius-sm); padding: 16px; border: 1px solid var(--border-color); }
.compare-card h5 { font-size: 0.85rem; font-weight: 700; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 1px solid var(--border-color); }
.compare-card.left h5 { color: var(--accent-blue-light); }
.compare-card.right h5 { color: var(--accent-orange); }
.compare-card ul { list-style: none; }
.compare-card li { padding: 4px 0; font-size: 0.85rem; color: var(--text-secondary); display: flex; gap: 8px; }
.compare-card li::before { content: '▸'; color: var(--accent-blue); }

/* STEP SOLVER */
.step-solver { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; margin: 16px 0; }
.step-solver-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 12px 18px; font-weight: 700; font-size: 0.9rem; color: white; }
.step-solver-body { padding: 16px 18px; }
.step { display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }
.step-num { min-width: 28px; height: 28px; background: var(--accent-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 800; color: white; }
.step-content { flex: 1; }
.step-content strong { color: var(--text-primary); font-size: 0.9rem; }
.step-content p { color: var(--text-secondary); font-size: 0.85rem; margin-top: 4px; }

.btn-reveal {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none;
  padding: 8px 20px; border-radius: 999px; font-family: var(--font-main); font-size: 0.82rem;
  font-weight: 700; cursor: pointer; transition: var(--transition); display: inline-flex; align-items: center; gap: 6px; margin-top: 10px;
}
.btn-reveal:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(92,111,255,0.5); }
.answer-content { display: none; margin-top: 12px; padding: 14px; background: rgba(105,240,174,0.08); border: 1px solid rgba(105,240,174,0.25); border-radius: var(--radius-sm); font-size: 0.88rem; line-height: 1.7; }
.answer-content.visible { display: block; }

/* SGK VIEWER */
.sgk-viewer { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0; }
.sgk-btn {
  padding: 6px 14px; background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: var(--radius-sm); color: var(--text-secondary); font-family: var(--font-main);
  font-size: 0.78rem; font-weight: 600; cursor: pointer; transition: var(--transition);
  display: flex; align-items: center; gap: 6px;
}
.sgk-btn:hover { background: var(--accent-blue); border-color: var(--accent-blue); color: white; transform: translateY(-1px); }

/* MODALS */
#img-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 9998; align-items: center; justify-content: center; padding: 20px; }
#img-modal.open { display: flex; }
#img-modal img { max-width: 90vw; max-height: 90vh; border-radius: var(--radius); box-shadow: var(--shadow-lg); object-fit: contain; }
#img-modal-close { position: fixed; top: 20px; right: 20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 50%; color: white; font-size: 1.2rem; cursor: pointer; display: flex; align-items: center; justify-content: center; }

#cheatsheet-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9997; overflow-y: auto; padding: 20px; }
#cheatsheet-modal.open { display: block; }
.cheatsheet-container { max-width: 700px; margin: 0 auto; background: var(--bg-card); border-radius: var(--radius-lg); border: 1px solid var(--border-color); overflow: hidden; }
.cheatsheet-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; color: white; }
.cheatsheet-header h3 { font-size: 1.1rem; font-weight: 800; }
.cheatsheet-header p { font-size: 0.78rem; opacity: 0.8; margin-top: 2px; }
.cheatsheet-body { padding: 20px 24px; }
.cheatsheet-section { margin-bottom: 20px; }
.cheatsheet-section h4 { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border-color); }
.cs-formula { display: flex; align-items: flex-start; gap: 12px; padding: 8px 0; border-bottom: 1px solid var(--border-color); font-size: 0.85rem; }
.cs-f { font-family: var(--font-mono); color: var(--accent-yellow); font-weight: 600; min-width: 200px; }
.cs-d { color: var(--text-secondary); flex: 1; }
.btn-print { padding: 8px 18px; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); border-radius: var(--radius-sm); color: white; font-family: var(--font-main); font-size: 0.8rem; font-weight: 600; cursor: pointer; }

/* QUIZ */
.quiz-section { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px; margin-top: 32px; }
.quiz-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border-color); }
.quiz-icon { font-size: 1.8rem; }
.quiz-title { font-size: 1.1rem; font-weight: 800; color: var(--text-primary); }
.quiz-sub { font-size: 0.78rem; color: var(--text-muted); }
.quiz-score-badge { margin-left: auto; padding: 6px 14px; background: rgba(105,240,174,0.15); border: 1px solid var(--accent-green); border-radius: 999px; font-size: 0.82rem; font-weight: 700; color: var(--accent-green); display: none; }
.quiz-q { margin-bottom: 20px; padding: 16px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
.quiz-q-text { font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; line-height: 1.6; }
.quiz-q-num { font-size: 0.7rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
.quiz-options { display: flex; flex-direction: column; gap: 6px; }
.quiz-option { display: flex; align-items: center; gap: 10px; padding: 9px 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); cursor: pointer; font-size: 0.86rem; color: var(--text-secondary); background: var(--bg-card); transition: var(--transition); }
.quiz-option:hover { border-color: var(--accent-blue); color: var(--text-primary); background: rgba(92,111,255,0.08); }
.quiz-option.correct { border-color: var(--accent-green) !important; background: rgba(105,240,174,0.15) !important; color: var(--accent-green) !important; font-weight: 600; }
.quiz-option.wrong { border-color: var(--accent-red) !important; background: rgba(255,82,82,0.15) !important; color: var(--accent-red) !important; }
.quiz-explain { display: none; margin-top: 10px; padding: 10px 14px; background: rgba(105,240,174,0.08); border-radius: var(--radius-sm); font-size: 0.83rem; color: var(--text-secondary); border-left: 3px solid var(--accent-green); line-height: 1.6; }
.quiz-explain.show { display: block; }
.tf-options { display: flex; gap: 10px; }
.tf-btn { flex: 1; padding: 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-card); color: var(--text-secondary); font-family: var(--font-main); font-size: 0.86rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
.tf-btn.selected { border-color: var(--accent-blue); background: rgba(92,111,255,0.12); color: var(--text-primary); }
.tf-btn.correct { border-color: var(--accent-green) !important; background: rgba(105,240,174,0.15) !important; color: var(--accent-green) !important; font-weight: 700; }
.tf-btn.wrong { border-color: var(--accent-red) !important; background: rgba(255,82,82,0.15) !important; color: var(--accent-red) !important; }
.quiz-essay textarea { width: 100%; min-height: 100px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 12px; color: var(--text-primary); font-family: var(--font-main); font-size: 0.86rem; resize: vertical; }
.quiz-essay .sample-answer { display: none; margin-top: 10px; padding: 12px; background: rgba(92,111,255,0.08); border-radius: var(--radius-sm); font-size: 0.84rem; color: var(--text-secondary); border-left: 3px solid var(--accent-blue); line-height: 1.6; }
.quiz-essay .sample-answer.show { display: block; }
.quiz-submit-btn { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none; border-radius: var(--radius); font-family: var(--font-main); font-size: 1rem; font-weight: 700; cursor: pointer; transition: var(--transition); margin-top: 20px; }
.quiz-submit-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(92,111,255,0.5); }

/* MINDMAP */
.mindmap { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); padding: 20px; margin: 16px 0; }
.mindmap-center { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; padding: 8px 18px; border-radius: 999px; font-weight: 700; display: inline-block; font-size: 0.82rem; }
.mindmap-branches { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; margin-top: 14px; }
.mindmap-branch { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 10px 12px; }
.mindmap-branch h5 { font-size: 0.78rem; font-weight: 700; margin-bottom: 6px; }
.mindmap-branch ul { list-style: none; }
.mindmap-branch li { font-size: 0.76rem; color: var(--text-secondary); padding: 2px 0; }
.mindmap-branch li::before { content: '• '; color: var(--accent-blue); }

.reaction-box { background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm); padding: 14px 18px; margin: 10px 0; font-family: var(--font-mono); font-size: 0.92rem; color: var(--text-primary); line-height: 1.9; }
.reaction-box .reactant { color: var(--accent-blue-light); }
.reaction-box .product { color: var(--accent-green); }
.reaction-box .arrow { color: var(--text-muted); }

ul.content-list { list-style: none; }
ul.content-list li { padding: 5px 0 5px 20px; position: relative; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.65; }
ul.content-list li::before { content: '▸'; position: absolute; left: 0; color: var(--accent-blue); }

ol.content-ol { padding-left: 20px; }
ol.content-ol li { padding: 5px 0; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.65; }

.hl-blue { color: var(--accent-blue-light); font-weight: 600; }
.hl-yellow { color: var(--accent-yellow); font-weight: 600; }
.hl-red { color: var(--accent-red); font-weight: 600; }
.hl-green { color: var(--accent-green); font-weight: 600; }
.hl-orange { color: var(--accent-orange); font-weight: 600; }
.hl-purple { color: var(--accent-purple); font-weight: 600; }
p { margin-bottom: 10px; font-size: 0.93rem; color: var(--text-secondary); }
strong { color: var(--text-primary); }

.fab-group { position: fixed; bottom: 28px; right: 24px; display: flex; flex-direction: column; gap: 10px; z-index: 800; }
.fab { width: 48px; height: 48px; border-radius: 50%; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; box-shadow: var(--shadow); transition: var(--transition); }
.fab:hover { transform: scale(1.1) translateY(-2px); }
.fab-cheat { background: linear-gradient(135deg, var(--accent-yellow-dark), var(--accent-orange)); color: white; }
.fab-top { background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-primary); }
""" + FLASHCARD_CSS + """
</style>
</head>
<body>
<div id="progress-bar"></div>

<!-- Modal SGK -->
<div id="img-modal">
  <button id="img-modal-close" onclick="document.getElementById('img-modal').classList.remove('open')">✕</button>
  <img id="img-modal-img" src="" alt="Trang Sách Giáo Khoa">
</div>

<!-- Modal Cheat Sheet -->
<div id="cheatsheet-modal">
  <div class="cheatsheet-container">
    <div class="cheatsheet-header">
      <div>
        <h3>📋 Cheat Sheet Hóa 11 – Tất Tần Tật Công Thức Trọng Tâm</h3>
        <p>Bài 1 &rarr; Bài 6 · Nhìn phát hiểu liền, cứu vớt điểm thi!</p>
      </div>
      <div style="display:flex;gap:8px;align-items:center;">
        <button class="btn-print" onclick="window.print()">🖨️ In trang</button>
        <button class="btn-icon" onclick="document.getElementById('cheatsheet-modal').classList.remove('open')" style="background:rgba(255,255,255,0.1);border-color:rgba(255,255,255,0.2);color:white;">✕</button>
      </div>
    </div>
    <div class="cheatsheet-body">
      <div class="cheatsheet-section">
        <h4>⚖️ Bài 1: Cân Bằng Hóa Học</h4>
        <div class="cs-formula"><span class="cs-f">Kc = [C]ᶜ[D]ᵈ / [A]ᵃ[B]ᵇ</span><span class="cs-d">Chất rắn KHÔNG tính; Kc > 1 thuận ưu thế</span></div>
        <div class="cs-formula"><span class="cs-f">v_thuận = v_nghịch</span><span class="cs-d">Điều kiện cân bằng động; nồng độ không đổi</span></div>
        <div class="cs-formula"><span class="cs-f">Le Chatelier</span><span class="cs-d">Tăng gì giảm nấy; Tăng Thu - Giảm Tỏa; Xúc tác không đổi cân bằng</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>💧 Bài 2: Cân Bằng Dung Dịch Nước</h4>
        <div class="cs-formula"><span class="cs-f">pH = &minus;log[H⁺]</span><span class="cs-d">Acid: pH &lt; 7; Trung tính: pH = 7; Base: pH &gt; 7 (ở 25°C)</span></div>
        <div class="cs-formula"><span class="cs-f">Kw = [H⁺][OH⁻] = 10⁻¹⁴</span><span class="cs-d">Tích số ion của nước; pH + pOH = 14</span></div>
        <div class="cs-formula"><span class="cs-f">[H⁺] = 10⁻ᵖᴴ</span><span class="cs-d">Nồng độ H⁺ từ pH</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>🌿 Bài 4: Nitrogen</h4>
        <div class="cs-formula"><span class="cs-f">N≡N (Eb = 945 kJ/mol)</span><span class="cs-d">Liên kết ba cực bền &rarr; rất trơ ở nhiệt độ thường</span></div>
        <div class="cs-formula"><span class="cs-f">6Li + N₂ &rarr; 2Li₃N</span><span class="cs-d">Li là kim loại duy nhất phản ứng ngay ở nhiệt độ thường!</span></div>
        <div class="cs-formula"><span class="cs-f">N₂ + O₂ ⇌ 2NO</span><span class="cs-d">3000°C hoặc tia sét đánh &rarr; sấm sét đẻ ra đạm</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>🧪 Bài 5: Ammonia & Muối Ammonium</h4>
        <div class="cs-formula"><span class="cs-f">NH₃ + H₂O ⇌ NH₄⁺ + OH⁻</span><span class="cs-d">Base yếu do cặp e tự do trên nguyên tử N</span></div>
        <div class="cs-formula"><span class="cs-f">NH₄⁺ + OH⁻ &rarr; NH₃↑ + H₂O</span><span class="cs-d">Nhận biết ion NH₄⁺: mùi khai làm xanh quỳ tím ẩm</span></div>
        <div class="cs-formula"><span class="cs-f">NH₄HCO₃ &rarr; NH₃ + CO₂ + H₂O</span><span class="cs-d">Bột nở làm bánh bao xốp mềm</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>⚡ Bài 6: HNO₃ & Hợp Chất Nitrogen-Oxygen</h4>
        <div class="cs-formula"><span class="cs-f">Cu + 4HNO₃(đ) &rarr; NO₂↑</span><span class="cs-d">HNO₃ đặc &rarr; Khí NO₂ màu nâu đỏ</span></div>
        <div class="cs-formula"><span class="cs-f">3Cu + 8HNO₃(l) &rarr; 2NO↑</span><span class="cs-d">HNO₃ loãng &rarr; Khí NO không màu hóa nâu</span></div>
        <div class="cs-formula"><span class="cs-f">Fe, Al, Cr</span><span class="cs-d">BỊ THỤ ĐỘNG HÓA trong HNO₃ đặc nguội!</span></div>
        <div class="cs-formula"><span class="cs-f">nHNO₃ = 2nNO₂ + 4nNO...</span><span class="cs-d">Công thức tính nhanh mol acid phản ứng</span></div>
      </div>
    </div>
  </div>
</div>

<div class="page-wrapper">
  <!-- SIDEBAR TOC -->
  <nav id="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-logo">⚗️ Hóa Học 11</div>
      <div class="sidebar-title">Kết Nối Tri Thức<br>Gia Sư Cứu Mất Gốc</div>
    </div>
    <div class="sidebar-nav">
      <div class="nav-section-label">MỤC LỤC BÀI HỌC</div>
      <a class="nav-item" href="#b0"><span>🧱</span> Tầng 0: Nền Tảng Mất Gốc</a>
      <a class="nav-item" href="#b1"><span>⚖️</span> Bài 1: Cân Bằng Hóa Học</a>
      <a class="nav-item" href="#b1-kc" style="padding-left:32px;font-size:0.78rem;">↳ Hằng số Kc & Bẫy</a>
      <a class="nav-item" href="#b1-lechatelier" style="padding-left:32px;font-size:0.78rem;">↳ Nguyên lí Le Chatelier</a>
      <a class="nav-item" href="#b1-quiz" style="padding-left:32px;font-size:0.78rem;">↳ Kiểm Tra Bài 1 (15 câu)</a>
      <a class="nav-item" href="#b2"><span>💧</span> Bài 2: Cân Bằng Dung Dịch</a>
      <a class="nav-item" href="#b2-dieli" style="padding-left:32px;font-size:0.78rem;">↳ Sự điện li mạnh/yếu</a>
      <a class="nav-item" href="#b2-ph" style="padding-left:32px;font-size:0.78rem;">↳ Thang pH & Bẫy pOH</a>
      <a class="nav-item" href="#b2-quiz" style="padding-left:32px;font-size:0.78rem;">↳ Kiểm Tra Bài 2 (15 câu)</a>
      <a class="nav-item" href="#b4"><span>🌿</span> Bài 4: Đơn Chất Nitrogen</a>
      <a class="nav-item" href="#b4-quiz" style="padding-left:32px;font-size:0.78rem;">↳ Kiểm Tra Bài 4 (15 câu)</a>
      <a class="nav-item" href="#b5"><span>🧪</span> Bài 5: Ammonia & NH₄⁺</a>
      <a class="nav-item" href="#b5-quiz" style="padding-left:32px;font-size:0.78rem;">↳ Kiểm Tra Bài 5 (15 câu)</a>
      <a class="nav-item" href="#b6"><span>⚡</span> Bài 6: HNO₃ & Hợp Chất</a>
      <a class="nav-item" href="#b6-quiz" style="padding-left:32px;font-size:0.78rem;">↳ Kiểm Tra Bài 6 (15 câu)</a>
      <div class="nav-section-label" style="margin-top:10px;">CÔNG CỤ HỖ TRỢ</div>
      <a class="nav-item" href="#" onclick="document.getElementById('cheatsheet-modal').classList.add('open');return false;"><span>📋</span> Mở Cheat Sheet Đầy Đủ</a>
      <a class="nav-item" href="mobile.html"><span>📱</span> Chuyển Bản Cho Điện Thoại</a>
    </div>
    <div class="sidebar-footer">
      <small style="color:var(--text-muted);font-size:0.72rem;">Dành riêng cho học sinh mất gốc cày điểm 9-10</small>
    </div>
  </nav>

  <!-- MAIN CONTENT AREA -->
  <main id="main-content">
    <div id="topbar">
      <button class="btn-icon" id="toggle-sidebar-btn" onclick="document.getElementById('sidebar').classList.toggle('collapsed');document.getElementById('main-content').classList.toggle('expanded');" title="Ẩn/Hiện Menu">☰</button>
      <span class="topbar-title">Hóa Học 11 – Kết Nối Tri Thức</span>
      <button class="btn-icon" id="theme-toggle" title="Đổi nền sáng/tối">🌙</button>
      <button class="btn-icon" onclick="document.getElementById('cheatsheet-modal').classList.add('open')" title="Xem Cheat Sheet">📋</button>
      <a href="mobile.html" class="btn-icon" style="text-decoration:none;font-size:0.75rem;font-weight:700;padding:0 12px;width:auto;" title="Bản Mobile">📱 Mobile</a>
    </div>

    <div class="hero">
      <span class="hero-emoji">⚗️</span>
      <h1>Hóa Học 11 – Kết Nối Tri Thức</h1>
      <p>Băm nát mọi định nghĩa SGK sang thứ tiếng người bình dân nhất. Mổ xẻ công thức đến tận gốc rễ, chỉ rõ bẫy thi học kì để đứa học dốt nhất cũng tự tin lấy lại gốc!</p>
      <div class="hero-tags">
        <span class="hero-tag blue">⚖️ Cân bằng hóa học</span>
        <span class="hero-tag blue">💧 Dung dịch nước & pH</span>
        <span class="hero-tag green">🌿 Nitrogen</span>
        <span class="hero-tag yellow">🧪 Ammonia</span>
        <span class="hero-tag red">⚡ Axit Nitric HNO3</span>
      </div>
    </div>

    <div class="content-area">
"""
    # Chèn Flashcard trước phần Quiz của mỗi bài
    b1_with_fc = B1_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 1 -->', FC_B1 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 1 -->')
    b2_with_fc = B2_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 2 -->', FC_B2 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 2 -->')
    b4_with_fc = B4_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 4 -->', FC_B4 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 4 -->')
    b5_with_fc = B5_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 5 -->', FC_B5 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 5 -->')
    b6_with_fc = B6_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 6 -->', FC_B6 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 6 -->')

    footer = """
    </div><!-- End content-area -->
  </main>
</div><!-- End page-wrapper -->

<!-- FLOATING ACTION BUTTONS -->
<div class="fab-group">
  <button class="fab fab-cheat" onclick="document.getElementById('cheatsheet-modal').classList.add('open')" title="Mở Cheat Sheet">📋</button>
  <button class="fab fab-top" onclick="window.scrollTo({top:0,behavior:'smooth'})" title="Lên đầu trang">⬆️</button>
</div>

<script>
""" + COMMON_JS + """
</script>
</body>
</html>
"""
    full_html = css_and_head + B0_CONTENT + b1_with_fc + b2_with_fc + b4_with_fc + b5_with_fc + b6_with_fc + footer
    with open(r"C:\Users\Admin\Desktop\hoa\index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("DONE: Generated index.html successfully! Size:", len(full_html), "bytes")

# ============================================================
# LẮP RÁP MOBILE.HTML (BẢN ĐIỆN THOẠI)
# ============================================================
def build_mobile_html():
    mobile_head = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Hóa 11 Mobile – Kết Nối Tri Thức</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
/* CSS VARIABLES FOR MOBILE */
:root {
  --bg-primary: #0f1117;
  --bg-secondary: #161822;
  --bg-card: #1c1f2e;
  --bg-hover: #262a3e;
  --text-primary: #f0f2ff;
  --text-secondary: #a2abcf;
  --text-muted: #657099;
  --accent-blue: #5c6fff;
  --accent-blue-light: #7986ff;
  --accent-yellow: #ffd54f;
  --accent-yellow-dark: #f9a825;
  --accent-red: #ff5252;
  --accent-green: #69f0ae;
  --accent-purple: #ce93d8;
  --accent-orange: #ffab40;
  --border-color: #2b3047;
  --border-bright: #3d4366;
  --radius: 12px;
  --radius-sm: 8px;
  --font-main: 'Be Vietnam Pro', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

[data-theme="light"] {
  --bg-primary: #f4f6fc;
  --bg-secondary: #eaedf7;
  --bg-card: #ffffff;
  --bg-hover: #e0e5f5;
  --text-primary: #15182e;
  --text-secondary: #3b4566;
  --text-muted: #727ea6;
  --accent-blue: #3f51b5;
  --accent-blue-light: #5c6fff;
  --accent-yellow: #f57f17;
  --accent-yellow-dark: #e65100;
  --accent-red: #c62828;
  --accent-green: #2e7d32;
  --accent-purple: #7b1fa2;
  --accent-orange: #e65100;
  --border-color: #c9d0e8;
  --border-bright: #a4afd4;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
html { scroll-behavior: smooth; font-size: 15px; }
body {
  font-family: var(--font-main);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.65;
  padding-top: 56px;
  padding-bottom: 70px;
  overflow-x: hidden;
}

#progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple), var(--accent-yellow));
  width: 0%; z-index: 9999;
}

/* TOP APP BAR */
.mobile-appbar {
  position: fixed; top: 0; left: 0; right: 0; height: 56px;
  background: var(--bg-secondary); border-bottom: 1px solid var(--border-color);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 16px; z-index: 1000; backdrop-filter: blur(10px);
}
.appbar-title { font-size: 0.95rem; font-weight: 800; color: var(--accent-blue-light); display: flex; align-items: center; gap: 8px; }
.appbar-actions { display: flex; align-items: center; gap: 8px; }
.btn-m-icon {
  width: 38px; height: 38px; border-radius: var(--radius-sm);
  background: var(--bg-card); border: 1px solid var(--border-color);
  color: var(--text-primary); font-size: 1.1rem; display: flex;
  align-items: center; justify-content: center; cursor: pointer;
}

/* BOTTOM NAVIGATION BAR */
.mobile-bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0; height: 60px;
  background: var(--bg-secondary); border-top: 1px solid var(--border-color);
  display: flex; align-items: center; justify-content: space-around;
  z-index: 1000; padding: 4px 6px;
}
.m-nav-tab {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  color: var(--text-muted); text-decoration: none; font-size: 0.65rem; font-weight: 600;
  padding: 4px 8px; border-radius: var(--radius-sm); transition: all 0.2s; flex: 1;
}
.m-nav-tab .tab-icon { font-size: 1.2rem; margin-bottom: 2px; }
.m-nav-tab:hover, .m-nav-tab.active { color: var(--accent-blue-light); background: var(--bg-hover); }

/* SLIDING DRAWER MENU */
#drawer {
  position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 2000;
  opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
#drawer.open { opacity: 1; pointer-events: auto; }
.drawer-content {
  position: absolute; top: 0; left: 0; bottom: 0; width: 280px;
  background: var(--bg-secondary); border-right: 1px solid var(--border-color);
  transform: translateX(-100%); transition: transform 0.3s cubic-bezier(0.1, 0.9, 0.2, 1);
  display: flex; flex-direction: column; padding: 20px 16px; overflow-y: auto;
}
#drawer.open .drawer-content { transform: translateX(0); }
.drawer-header { display: flex; align-items: center; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color); margin-bottom: 14px; }
.drawer-item {
  display: flex; align-items: center; gap: 10px; padding: 10px 12px;
  border-radius: var(--radius-sm); color: var(--text-secondary);
  text-decoration: none; font-size: 0.88rem; font-weight: 600; margin-bottom: 4px;
}
.drawer-item:hover, .drawer-item.active { background: var(--bg-hover); color: var(--accent-blue-light); }

/* MOBILE CONTENT STYLING */
.mobile-container { padding: 16px 14px; }
.hero-m {
  background: linear-gradient(135deg, rgba(92,111,255,0.15), rgba(206,147,216,0.1));
  border: 1px solid var(--border-color); border-radius: var(--radius);
  padding: 20px 16px; text-align: center; margin-bottom: 20px;
}
.hero-m h1 { font-size: 1.35rem; font-weight: 800; color: var(--accent-blue-light); margin-bottom: 6px; }
.hero-m p { font-size: 0.82rem; color: var(--text-secondary); margin-bottom: 12px; }

.lesson-section { margin-bottom: 40px; }
.lesson-header { display: flex; gap: 12px; align-items: center; margin-bottom: 18px; padding-bottom: 14px; border-bottom: 2px solid var(--border-color); }
.lesson-number { width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; color: white; flex-shrink: 0; }
.lesson-meta h2 { font-size: 1.15rem; font-weight: 800; color: var(--text-primary); line-height: 1.3; }
.lesson-meta .lesson-sub { font-size: 0.75rem; color: var(--text-muted); }

.box { border-radius: var(--radius); padding: 14px 16px; margin-bottom: 16px; border-left: 4px solid; }
.box-theory { background: rgba(92,111,255,0.08); border: 1px solid rgba(92,111,255,0.2); border-left: 4px solid var(--accent-blue); }
.box-theory .box-title { color: var(--accent-blue-light); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-formula { background: rgba(255,213,79,0.07); border: 1px solid rgba(255,213,79,0.25); border-left: 4px solid var(--accent-yellow); }
.box-formula .box-title { color: var(--accent-yellow); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-warning { background: rgba(255,82,82,0.07); border: 1px solid rgba(255,82,82,0.25); border-left: 4px solid var(--accent-red); }
.box-warning .box-title { color: var(--accent-red); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-story { background: rgba(105,240,174,0.07); border: 1px solid rgba(105,240,174,0.2); border-left: 4px solid var(--accent-green); }
.box-story .box-title { color: var(--accent-green); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-recall { background: rgba(206,147,216,0.07); border: 1px solid rgba(206,147,216,0.25); border-left: 4px solid var(--accent-purple); border-radius: var(--radius); }
.box-recall .box-title { color: var(--accent-purple); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; }
.box-combo { background: rgba(255,171,64,0.07); border: 1px solid rgba(255,171,64,0.25); border-left: 4px solid var(--accent-orange); border-radius: var(--radius); }
.box-combo .box-title { color: var(--accent-orange); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; }

/* MATH & FRACTION FOR MOBILE */
sub, sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sub { bottom: -0.25em; }
sup { top: -0.5em; }

.fraction {
  display: inline-flex;
  flex-direction: column;
  vertical-align: middle;
  text-align: center;
  padding: 0 4px;
  line-height: 1.15;
  font-size: 0.95em;
}
.fraction .num {
  border-bottom: 2px solid currentColor;
  padding-bottom: 2px;
  margin-bottom: 2px;
  display: block;
}
.fraction .den {
  padding-top: 2px;
  display: block;
}

.formula-display {
  background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm);
  padding: 12px 14px; margin: 10px 0; font-family: var(--font-mono); font-size: 0.92rem;
  font-weight: 600; color: var(--accent-yellow); text-align: center; overflow-x: auto;
}
.formula-label { font-size: 0.68rem; color: var(--text-muted); text-align: center; margin-top: -6px; margin-bottom: 6px; }

.accordion-item { border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 8px; overflow: hidden; }
.accordion-trigger {
  width: 100%; background: var(--bg-card); border: none; padding: 12px 14px;
  color: var(--text-primary); font-family: var(--font-main); font-size: 0.84rem;
  font-weight: 600; text-align: left; cursor: pointer; display: flex;
  align-items: center; justify-content: space-between; gap: 8px;
}
.accordion-trigger.open .acc-icon { transform: rotate(180deg); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; background: var(--bg-secondary); }
.accordion-content.open { max-height: 3500px; }
.accordion-inner { padding: 12px 14px; }

.tooltip { position: relative; border-bottom: 1px dashed var(--accent-blue); color: var(--accent-blue-light); font-weight: 600; }
.tooltip::after {
  content: attr(data-tip); position: absolute; bottom: calc(100% + 6px); left: 50%;
  transform: translateX(-50%); background: var(--bg-card); border: 1px solid var(--border-bright);
  color: var(--text-primary); padding: 6px 10px; border-radius: var(--radius-sm);
  font-size: 0.72rem; font-weight: 400; width: 190px; white-space: normal;
  text-align: center; box-shadow: 0 4px 16px rgba(0,0,0,0.6); z-index: 100; opacity: 0;
  pointer-events: none; transition: opacity 0.2s;
}
.tooltip:active::after, .tooltip:hover::after { opacity: 1; }

h3.sec-title { font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin: 22px 0 10px; display: flex; align-items: center; gap: 8px; }
h3.sec-title::before { content: ''; width: 3px; height: 16px; background: var(--accent-blue); border-radius: 2px; }
h4.sub-title { font-size: 0.92rem; font-weight: 700; color: var(--text-secondary); margin: 16px 0 8px; padding-left: 8px; border-left: 3px solid var(--accent-blue); }

.tbl-wrap { overflow-x: auto; margin: 12px 0; -webkit-overflow-scrolling: touch; border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
table { width: 100%; border-collapse: collapse; font-size: 0.8rem; }
thead { background: var(--bg-hover); }
th { padding: 8px 10px; text-align: left; font-weight: 700; color: var(--text-secondary); font-size: 0.7rem; text-transform: uppercase; white-space: nowrap; }
td { padding: 8px 10px; border-bottom: 1px solid var(--border-color); color: var(--text-primary); }

.compare-grid { display: flex; flex-direction: column; gap: 10px; margin: 12px 0; }
.compare-card { background: var(--bg-card); border-radius: var(--radius-sm); padding: 12px; border: 1px solid var(--border-color); }
.compare-card h5 { font-size: 0.82rem; font-weight: 700; margin-bottom: 8px; padding-bottom: 6px; border-bottom: 1px solid var(--border-color); }
.compare-card.left h5 { color: var(--accent-blue-light); }
.compare-card.right h5 { color: var(--accent-orange); }
.compare-card ul { list-style: none; }
.compare-card li { padding: 3px 0; font-size: 0.8rem; color: var(--text-secondary); }

.step-solver { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; margin: 14px 0; }
.step-solver-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 10px 14px; font-weight: 700; font-size: 0.85rem; color: white; }
.step-solver-body { padding: 12px 14px; }
.step { display: flex; gap: 10px; margin-bottom: 12px; align-items: flex-start; }
.step-num { min-width: 24px; height: 24px; background: var(--accent-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 800; color: white; flex-shrink: 0; }
.step-content strong { color: var(--text-primary); font-size: 0.85rem; }
.step-content p { color: var(--text-secondary); font-size: 0.8rem; margin-top: 3px; }

.btn-reveal {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none;
  padding: 8px 16px; border-radius: 999px; font-family: var(--font-main); font-size: 0.78rem;
  font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; margin-top: 8px;
}
.answer-content { display: none; margin-top: 10px; padding: 12px; background: rgba(105,240,174,0.08); border: 1px solid rgba(105,240,174,0.25); border-radius: var(--radius-sm); font-size: 0.82rem; line-height: 1.6; }
.answer-content.visible { display: block; }

.sgk-viewer { display: flex; gap: 6px; flex-wrap: wrap; margin: 12px 0; }
.sgk-btn {
  padding: 5px 10px; background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: var(--radius-sm); color: var(--text-secondary); font-size: 0.72rem;
  font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 4px;
}

/* QUIZ MOBILE */
.quiz-section { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); padding: 16px; margin-top: 24px; }
.quiz-header { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid var(--border-color); }
.quiz-title { font-size: 0.95rem; font-weight: 800; color: var(--text-primary); }
.quiz-sub { font-size: 0.7rem; color: var(--text-muted); }
.quiz-score-badge { margin-left: auto; padding: 4px 10px; background: rgba(105,240,174,0.15); border: 1px solid var(--accent-green); border-radius: 999px; font-size: 0.75rem; font-weight: 700; color: var(--accent-green); display: none; }
.quiz-q { margin-bottom: 16px; padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
.quiz-q-num { font-size: 0.65rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; margin-bottom: 4px; }
.quiz-q-text { font-size: 0.84rem; font-weight: 600; color: var(--text-primary); margin-bottom: 10px; line-height: 1.5; }
.quiz-options { display: flex; flex-direction: column; gap: 6px; }
.quiz-option { display: flex; align-items: flex-start; gap: 8px; padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); cursor: pointer; font-size: 0.8rem; color: var(--text-secondary); background: var(--bg-card); }
.quiz-option.correct { border-color: var(--accent-green) !important; background: rgba(105,240,174,0.15) !important; color: var(--accent-green) !important; font-weight: 600; }
.quiz-option.wrong { border-color: var(--accent-red) !important; background: rgba(255,82,82,0.15) !important; color: var(--accent-red) !important; }
.quiz-explain { display: none; margin-top: 8px; padding: 8px 10px; background: rgba(105,240,174,0.08); border-radius: var(--radius-sm); font-size: 0.78rem; color: var(--text-secondary); border-left: 3px solid var(--accent-green); }
.quiz-explain.show { display: block; }
.tf-options { display: flex; gap: 8px; }
.tf-btn { flex: 1; padding: 8px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-card); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer; }
.tf-btn.correct { border-color: var(--accent-green) !important; background: rgba(105,240,174,0.15) !important; color: var(--accent-green) !important; }
.tf-btn.wrong { border-color: var(--accent-red) !important; background: rgba(255,82,82,0.15) !important; color: var(--accent-red) !important; }
.quiz-essay textarea { width: 100%; min-height: 80px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 8px; color: var(--text-primary); font-size: 0.8rem; font-family: var(--font-main); }
.quiz-essay .sample-answer { display: none; margin-top: 8px; padding: 10px; background: rgba(92,111,255,0.08); border-radius: var(--radius-sm); font-size: 0.78rem; color: var(--text-secondary); border-left: 3px solid var(--accent-blue); }
.quiz-essay .sample-answer.show { display: block; }
.quiz-submit-btn { display: block; width: 100%; padding: 12px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none; border-radius: var(--radius); font-size: 0.9rem; font-weight: 700; cursor: pointer; margin-top: 14px; }

/* MODALS */
#img-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 9998; align-items: center; justify-content: center; padding: 10px; }
#img-modal.open { display: flex; }
#img-modal img { max-width: 95vw; max-height: 90vh; border-radius: var(--radius-sm); object-fit: contain; }
#img-modal-close { position: fixed; top: 12px; right: 12px; width: 36px; height: 36px; background: rgba(255,255,255,0.15); border: none; border-radius: 50%; color: white; font-size: 1.1rem; cursor: pointer; display: flex; align-items: center; justify-content: center; }

#cheatsheet-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.88); z-index: 9997; overflow-y: auto; padding: 16px 10px 70px; }
#cheatsheet-modal.open { display: block; }
.cheatsheet-container { background: var(--bg-card); border-radius: var(--radius); border: 1px solid var(--border-color); overflow: hidden; }
.cheatsheet-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 14px 16px; display: flex; align-items: center; justify-content: space-between; color: white; }
.cheatsheet-header h3 { font-size: 0.95rem; font-weight: 800; }
.cheatsheet-body { padding: 14px 16px; }
.cheatsheet-section { margin-bottom: 16px; }
.cheatsheet-section h4 { font-size: 0.72rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 6px; padding-bottom: 4px; border-bottom: 1px solid var(--border-color); }
.cs-formula { display: flex; flex-direction: column; gap: 2px; padding: 6px 0; border-bottom: 1px solid var(--border-color); font-size: 0.8rem; }
.cs-f { font-family: var(--font-mono); color: var(--accent-yellow); font-weight: 600; }
.cs-d { color: var(--text-secondary); font-size: 0.75rem; }

.mindmap { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); padding: 14px; margin: 12px 0; }
.mindmap-center { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; padding: 6px 14px; border-radius: 999px; font-weight: 700; display: inline-block; font-size: 0.75rem; }
.mindmap-branches { display: flex; flex-direction: column; gap: 8px; margin-top: 10px; }
.mindmap-branch { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 8px 10px; }
.mindmap-branch h5 { font-size: 0.72rem; font-weight: 700; margin-bottom: 4px; }
.mindmap-branch ul { list-style: none; }
.mindmap-branch li { font-size: 0.72rem; color: var(--text-secondary); padding: 1px 0; }

.reaction-box { background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm); padding: 10px 12px; margin: 8px 0; font-family: var(--font-mono); font-size: 0.82rem; line-height: 1.7; word-break: break-all; }
ul.content-list { list-style: none; }
ul.content-list li { padding: 4px 0 4px 16px; position: relative; font-size: 0.84rem; color: var(--text-secondary); line-height: 1.55; }
ul.content-list li::before { content: '▸'; position: absolute; left: 0; color: var(--accent-blue); }
ol.content-ol { padding-left: 18px; }
ol.content-ol li { padding: 4px 0; font-size: 0.84rem; color: var(--text-secondary); line-height: 1.55; }

.hl-blue { color: var(--accent-blue-light); font-weight: 600; }
.hl-yellow { color: var(--accent-yellow); font-weight: 600; }
.hl-red { color: var(--accent-red); font-weight: 600; }
.hl-green { color: var(--accent-green); font-weight: 600; }
.hl-orange { color: var(--accent-orange); font-weight: 600; }
.hl-purple { color: var(--accent-purple); font-weight: 600; }
p { margin-bottom: 8px; font-size: 0.86rem; color: var(--text-secondary); }
strong { color: var(--text-primary); }
""" + FLASHCARD_CSS + """
</style>
</head>
<body>
<div id="progress-bar"></div>

<!-- TOP APP BAR -->
<header class="mobile-appbar">
  <div class="appbar-title">
    <button class="btn-m-icon" onclick="document.getElementById('drawer').classList.add('open')">☰</button>
    <span>⚗️ Hóa 11 KNTT</span>
  </div>
  <div class="appbar-actions">
    <button class="btn-m-icon btn-theme" onclick="toggleTheme()">🌙</button>
    <button class="btn-m-icon" onclick="document.getElementById('cheatsheet-modal').classList.add('open')">📋</button>
    <a href="index.html" class="btn-m-icon" style="text-decoration:none;font-size:0.7rem;font-weight:700;width:auto;padding:0 8px;">💻 PC</a>
  </div>
</header>

<!-- DRAWER MENU -->
<div id="drawer" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="drawer-content">
    <div class="drawer-header">
      <strong style="color:var(--accent-blue-light);font-size:1rem;">Mục Lục Bài Học</strong>
      <button class="btn-m-icon" onclick="document.getElementById('drawer').classList.remove('open')" style="width:30px;height:30px;">✕</button>
    </div>
    <a class="drawer-item" href="#b0" onclick="document.getElementById('drawer').classList.remove('open')">🧱 Tầng 0: Mất Gốc Lớp 10</a>
    <a class="drawer-item" href="#b1" onclick="document.getElementById('drawer').classList.remove('open')">⚖️ Bài 1: Cân Bằng Hóa Học</a>
    <a class="drawer-item" href="#b2" onclick="document.getElementById('drawer').classList.remove('open')">💧 Bài 2: Cân Bằng Dung Dịch</a>
    <a class="drawer-item" href="#b4" onclick="document.getElementById('drawer').classList.remove('open')">🌿 Bài 4: Đơn Chất Nitrogen</a>
    <a class="drawer-item" href="#b5" onclick="document.getElementById('drawer').classList.remove('open')">🧪 Bài 5: Ammonia & NH₄⁺</a>
    <a class="drawer-item" href="#b6" onclick="document.getElementById('drawer').classList.remove('open')">⚡ Bài 6: HNO₃ & Hợp Chất</a>
    <hr style="border:none;border-top:1px solid var(--border-color);margin:12px 0;">
    <a class="drawer-item" href="#" onclick="document.getElementById('cheatsheet-modal').classList.add('open');document.getElementById('drawer').classList.remove('open');return false;">📋 Mở Cheat Sheet</a>
    <a class="drawer-item" href="index.html">💻 Chuyển Bản Desktop</a>
  </div>
</div>

<!-- SGK MODAL -->
<div id="img-modal">
  <button id="img-modal-close" onclick="document.getElementById('img-modal').classList.remove('open')">✕</button>
  <img id="img-modal-img" src="" alt="Trang Sách">
</div>

<!-- CHEAT SHEET MODAL -->
<div id="cheatsheet-modal">
  <div class="cheatsheet-container">
    <div class="cheatsheet-header">
      <h3>📋 Cheat Sheet Hóa 11</h3>
      <button class="btn-m-icon" onclick="document.getElementById('cheatsheet-modal').classList.remove('open')" style="color:white;background:rgba(255,255,255,0.2);border:none;">✕</button>
    </div>
    <div class="cheatsheet-body">
      <div class="cheatsheet-section">
        <h4>⚖️ Bài 1: Cân Bằng Hóa Học</h4>
        <div class="cs-formula"><span class="cs-f">Kc = [C]ᶜ[D]ᵈ / [A]ᵃ[B]ᵇ</span><span class="cs-d">Chất rắn KHÔNG tính; Kc > 1 thuận ưu thế</span></div>
        <div class="cs-formula"><span class="cs-f">Le Chatelier</span><span class="cs-d">Tăng Thu - Giảm Tỏa; Tăng P dịch về ít mol khí</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>💧 Bài 2: Cân Bằng Dung Dịch</h4>
        <div class="cs-formula"><span class="cs-f">pH = &minus;log[H⁺]</span><span class="cs-d">pH &lt; 7 Acid; pH = 7 Trung tính; pH &gt; 7 Base</span></div>
        <div class="cs-formula"><span class="cs-f">Kw = [H⁺][OH⁻] = 10⁻¹⁴</span><span class="cs-d">pH + pOH = 14 (ở 25°C)</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>🌿 Bài 4: Nitrogen</h4>
        <div class="cs-formula"><span class="cs-f">N≡N (945 kJ/mol)</span><span class="cs-d">Liên kết ba cực bền &rarr; rất trơ ở t° thường</span></div>
        <div class="cs-formula"><span class="cs-f">6Li + N₂ &rarr; 2Li₃N</span><span class="cs-d">Phản ứng ngay ở nhiệt độ thường</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>🧪 Bài 5: Ammonia & Muối NH₄⁺</h4>
        <div class="cs-formula"><span class="cs-f">NH₃ + H₂O ⇌ NH₄⁺ + OH⁻</span><span class="cs-d">Base yếu do cặp e tự do nhận H⁺</span></div>
        <div class="cs-formula"><span class="cs-f">NH₄⁺ + OH⁻ &rarr; NH₃↑</span><span class="cs-d">Khí mùi khai làm xanh quỳ tím ẩm</span></div>
      </div>
      <div class="cheatsheet-section">
        <h4>⚡ Bài 6: HNO₃</h4>
        <div class="cs-formula"><span class="cs-f">HNO₃ đặc &rarr; NO₂↑</span><span class="cs-d">Khí màu nâu đỏ, cực độc</span></div>
        <div class="cs-formula"><span class="cs-f">HNO₃ loãng &rarr; NO↑</span><span class="cs-d">Khí không màu hóa nâu ngoài không khí</span></div>
        <div class="cs-formula"><span class="cs-f">Fe, Al thụ động</span><span class="cs-d">Không tan trong HNO₃ đặc nguội</span></div>
      </div>
    </div>
  </div>
</div>

<!-- MAIN MOBILE CONTAINER -->
<div class="mobile-container">
  <div class="hero-m">
    <h1>Hóa 11 – Kết Nối Tri Thức</h1>
    <p>Bản tối ưu cảm ứng cho điện thoại. Đầy đủ lý thuyết chi tiết, bẫy thi, bài tập step-by-step và 15 câu test mỗi bài!</p>
  </div>
"""
    # Chèn Flashcard trước phần Quiz của mỗi bài
    b1_with_fc = B1_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 1 -->', FC_B1 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 1 -->')
    b2_with_fc = B2_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 2 -->', FC_B2 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 2 -->')
    b4_with_fc = B4_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 4 -->', FC_B4 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 4 -->')
    b5_with_fc = B5_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 5 -->', FC_B5 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 5 -->')
    b6_with_fc = B6_CONTENT.replace('<!-- BÀI KIỂM TRA 15 CÂU BÀI 6 -->', FC_B6 + '\n<!-- BÀI KIỂM TRA 15 CÂU BÀI 6 -->')

    mobile_footer = """
</div><!-- End mobile-container -->

<!-- BOTTOM NAVIGATION TABS -->
<nav class="mobile-bottom-nav">
  <a class="m-nav-tab active" href="#b0"><span class="tab-icon">🧱</span>Tầng 0</a>
  <a class="m-nav-tab" href="#b1"><span class="tab-icon">⚖️</span>Bài 1</a>
  <a class="m-nav-tab" href="#b2"><span class="tab-icon">💧</span>Bài 2</a>
  <a class="m-nav-tab" href="#b4"><span class="tab-icon">🌿</span>Bài 4</a>
  <a class="m-nav-tab" href="#b5"><span class="tab-icon">🧪</span>Bài 5</a>
  <a class="m-nav-tab" href="#b6"><span class="tab-icon">⚡</span>Bài 6</a>
</nav>

<script>
""" + COMMON_JS + """
// Cập nhật tab active khi cuộn trên mobile
window.addEventListener('scroll', function() {
  var sections = document.querySelectorAll('.lesson-section');
  var scrollPos = window.scrollY + 100;
  sections.forEach(function(sec) {
    if (scrollPos >= sec.offsetTop && scrollPos < sec.offsetTop + sec.offsetHeight) {
      var id = sec.id;
      document.querySelectorAll('.mobile-bottom-nav .m-nav-tab').forEach(function(tab) {
        tab.classList.remove('active');
        if (tab.getAttribute('href') === '#' + id) {
          tab.classList.add('active');
        }
      });
    }
  });
});
</script>
</body>
</html>
"""
    full_mobile = mobile_head + B0_CONTENT + b1_with_fc + b2_with_fc + b4_with_fc + b5_with_fc + b6_with_fc + mobile_footer
    with open(r"C:\Users\Admin\Desktop\hoa\mobile.html", "w", encoding="utf-8") as f:
        f.write(full_mobile)
    print("DONE: Generated mobile.html successfully! Size:", len(full_mobile), "bytes")

if __name__ == '__main__':
    build_index_html()
    build_mobile_html()
