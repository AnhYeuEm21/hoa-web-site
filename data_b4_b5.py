# -*- coding: utf-8 -*-
"""
Module data_b4_b5.py - NÂNG CẤP TOÀN DIỆN
- Bổ sung Sơ Đồ Tư Duy Mindmap Cho Bài 4 & Bài 5
- Bổ sung 2 Bài Tập Thực Chiến Step-by-Step Cho Cả Bài 4 & Bài 5 Chuẩn 3 Bước
- Đổi nút bấm: "🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!"
"""

B4_CONTENT = """
<!-- ========================================== -->
<!-- BÀI 4: NITROGEN (SGK 29-32) -->
<!-- ========================================== -->
<section id="b4" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number">04</div>
    <div class="lesson-meta">
      <h2>Bài 4: Đơn Chất Nitrogen (N<sub>2</sub>)</h2>
      <div class="lesson-sub">SGK Hóa học 11 – Kết Nối Tri Thức (Trang 29 đến trang 32)</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Liên kết ba N&equiv;N</span>
        <span class="lesson-tag">Tính trơ hóa học</span>
        <span class="lesson-tag">Tính oxi hóa & khử</span>
        <span class="lesson-tag">Ứng dụng thực tế</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('sgk_b4_p29.png')">📖 Xem SGK Trang 29</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b4_p30_31.png')">📖 Xem SGK Trang 30-31</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b4_5_p32_33.png')">📖 Xem SGK Trang 32-33</button>
  </div>

  <!-- PHẦN 1: CẤU TẠO PHÂN TỬ NITROGEN -->
  <h3 class="sec-title" id="b4-cautao">1. Cấu Tạo Phân Tử & Tính Trơ Kì Lạ Của Nitrogen</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch SGK Sang Tiếng Người (Bí Mật Của Liên Kết Ba)</div>
    <p>Khí nitrogen (N<sub>2</sub>) chiếm tới <strong>78% thể tích không khí</strong> mà mày đang hít thở hàng ngày. Nhưng tại sao nó bao quanh chúng ta mà không thèm phản ứng với da thịt, phổi hay đồ vật trong phòng?</p>
    <p>Bí mật nằm ở cấu trúc phân tử của nó:</p>
    <div class="formula-display" style="font-size:1.3rem;letter-spacing:2px;color:var(--accent-blue-light);">
      :N &equiv; N:
    </div>
    <ul class="content-list">
      <li>Hai nguyên tử N liên kết với nhau bằng <strong>1 LIÊN KẾT BA</strong> (gồm 1 liên kết &sigma; bền vững và 2 liên kết &pi;).</li>
      <li>Năng lượng liên kết cực kỳ khủng khiếp: <strong>E<sub>b</sub> = 945 kJ/mol</strong>! Đây là một trong những liên kết cộng hóa trị bền vững nhất trong toàn bộ giới hóa học.</li>
      <li>Do liên kết ba quá trâu bò, ở nhiệt độ thường, phân tử N<sub>2</sub> cực kỳ <strong>TRƠ VỀ MẶT HÓA HỌC</strong> (ngủ đông, không thèm phản ứng với hầu hết các chất). Chỉ khi nào mày cấp nhiệt độ cực cao (hàng ngàn độ C) hoặc có tia sét đánh thì nó mới chịu thức giấc!</li>
    </ul>
  </div>

  <!-- PHẦN 2: TÍNH CHẤT HÓA HỌC -->
  <h3 class="sec-title" id="b4-tchat">2. Tính Chất Hóa Học: Vừa Oxi Hóa Vừa Khử</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Thang Số Oxi Hóa Của Nguyên Tố Nitrogen</div>
    <p>Nguyên tố N có các số oxi hóa rất phong phú:</p>
    <div style="background:var(--bg-card);padding:12px;border-radius:var(--radius-sm);text-align:center;font-family:var(--font-mono);margin:10px 0;border:1px solid var(--border-color);">
      <span style="color:var(--accent-green);">-3 (NH<sub>3</sub>)</span> &larr; 
      <strong style="color:var(--accent-yellow);font-size:1.1rem;background:rgba(255,213,79,0.15);padding:2px 8px;border-radius:4px;">0 (N<sub>2</sub>)</strong> &rarr; 
      <span style="color:var(--accent-orange);">+1 (N<sub>2</sub>O)</span> &rarr; 
      <span style="color:var(--accent-blue-light);">+2 (NO)</span> &rarr; 
      <span style="color:var(--accent-purple);">+3 (HNO<sub>2</sub>)</span> &rarr; 
      <span style="color:var(--accent-red);">+4 (NO<sub>2</sub>)</span> &rarr; 
      <span style="color:var(--accent-red-dark);">+5 (HNO<sub>3</sub>)</span>
    </div>
    <p>Vì <strong>N<sub>2</sub> có mức oxi hóa 0 ở lưng chừng</strong>:
    <br>&bull; Nó có thể giảm xuống <strong>-3</strong> &rarr; Thể hiện <strong>TÍNH OXI HÓA</strong> (Tính chất chủ yếu).
    <br>&bull; Nó có thể tăng lên các mức <strong>+1, +2, +4, +5</strong> &rarr; Thể hiện <strong>TÍNH KHỬ</strong>.</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 Các Phản Ứng Điển Hình Bắt Buộc Phải Nhớ</div>
    <p><strong>1. Tính Oxi Hóa (Tác dụng với Kim loại mạnh & H<sub>2</sub>)</strong></p>
    <div class="reaction-box">
      &bull; Với H<sub>2</sub> (Phản ứng Haber): 
      <br><strong>N<sub>2</sub>(g) + 3H<sub>2</sub>(g) &hArr; 2NH<sub>3</sub>(g)</strong> &nbsp;&nbsp; (&Delta;rH&deg; = -91,8 kJ; 450&deg;C, 200 bar, xúc tác bột Fe)
      <br>&bull; Với Kim loại mạnh (ở nhiệt độ cao tạo muối nitride):
      <br><strong>3Mg + N<sub>2</sub> &rarr;(t&deg;) Mg<sub>3</sub>N<sub>2</sub></strong> (Magnesium nitride)
    </div>
    <div class="box-warning" style="margin-top:10px;">
      <div class="box-title">🚨 ĐẶC BIỆT LƯU Ý VỀ LITHIUM (Li)</div>
      <p>Trong tất cả các kim loại trên đời, <strong>duy nhất LITHIUM (Li)</strong> phản ứng được với Nitrogen ngay ở <strong>NHIỆT ĐỘ PHÒNG (không cần đun nóng)</strong>:
      <br><code>6Li + N<sub>2</sub> &rarr; 2Li<sub>3</sub>N</code> (Đề thi rất thích hỏi câu này để gài bẫy học sinh!).</p>
    </div>

    <p style="margin-top:14px;"><strong>2. Tính Khử (Tác dụng với Oxygen O<sub>2</sub>)</strong></p>
    <div class="reaction-box">
      &bull; Ở nhiệt độ khoảng <strong>3000&deg;C</strong> hoặc có <strong>tia lửa điện (sét đánh)</strong>:
      <br><strong>N<sub>2</sub>(g) + O<sub>2</sub>(g) &hArr; 2NO(g)</strong> (Nitrogen monoxide &ndash; không màu)
      <br>&bull; Ngay sau đó ở điều kiện thường, khí NO gặp oxy trong không khí sẽ hóa nâu ngay lập tức:
      <br><strong>2NO(g) + O<sub>2</sub>(g) &rarr; 2NO<sub>2</sub>(g)</strong> (Nitrogen dioxide &ndash; màu nâu đỏ độc hại)
    </div>
  </div>

  <!-- GÓC HỒI TƯỞNG BÀI 4 -->
  <div class="accordion-item" style="margin:20px 0;">
    <button class="accordion-trigger" onclick="toggleAcc(this)">
      <span>🟣 <strong>KÝ ỨC ÙA VỀ (Ca Dao Tục Ngữ Hóa Học): Sấm Sét Đẻ Ra Phân Đạm</strong></span>
      <span class="acc-icon">▼</span>
    </button>
    <div class="accordion-content">
      <div class="accordion-inner">
        <div class="box box-recall">
          <div class="box-title">💡 Giải Thích Câu Ca Dao Dân Gian Dưới Góc Nhìn Hóa 11</div>
          <p style="font-style:italic;color:var(--accent-yellow);font-size:1.05rem;">"Lúa chiêm lấp ló đầu bờ &ndash; Hễ nghe tiếng sấm phất cờ mà lên"</p>
          <p>Tại sao sấm sét đánh đùng đùng lại giúp cây lúa tốt bời bời như được bón đạm? Chuỗi phản ứng tự nhiên diễn ra như sau:</p>
          <ol class="content-ol">
            <li>Tia sét (hàng triệu vôn, nhiệt độ ~3000&deg;C) bẻ gãy liên kết N&equiv;N: <code>N<sub>2</sub> + O<sub>2</sub> &rarr; 2NO</code></li>
            <li>NO gặp oxy hóa thành khí nâu: <code>2NO + O<sub>2</sub> &rarr; 2NO<sub>2</sub></code></li>
            <li>Nước mưa hòa tan NO<sub>2</sub> cùng oxy tạo thành axit nitric: <code>4NO<sub>2</sub> + O<sub>2</sub> + 2H<sub>2</sub>O &rarr; 4HNO<sub>3</sub></code></li>
            <li>Axit ngấm vào đất, phản ứng với các khoáng chất tạo ion nitrate: <strong>NO<sub>3</sub><sup>&minus;</sup></strong>. Đây chính là <strong>PHÂN ĐẠM NGUYÊN CHẤT MIỄN PHÍ TỪ TRỜI RƠI XUỐNG</strong> giúp lúa lớn nhanh như thổi!</li>
          </ol>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 3: ỨNG DỤNG THỰC TẾ -->
  <h3 class="sec-title" id="b4-ungdung">3. Ứng Dụng Thực Tế Trong Đời Sống</h3>
  <div class="box box-story">
    <div class="box-title">🥔 Tại Sao Gói Bim Bim Lại Phồng To Toàn Khí?</div>
    <p>Nhiều đứa bảo các hãng bim bim bán "bọc không khí kèm vài miếng khoai tây". Nhưng thực ra người ta bơm <strong>khí Nitrogen tinh khiết</strong> vào đó!</p>
    <p>&bull; <em>Lí do 1:</em> Khí N<sub>2</sub> cực kì trơ, không chứa oxy nên dầu mỡ trong khoai tây chiên không bị oxi hóa (chống hôi dầu, chống ỉu, giữ giòn rụm trong nhiều tháng mà không cần chất bảo quản độc hại).</p>
    <p>&bull; <em>Lí do 2:</em> Đệm khí căng phồng giúp các lát bim bim không bị dập nát vụn khi vận chuyển.</p>
    <p style="margin-top:8px;"><strong>Ứng dụng khác:</strong> Khí Nitrogen lỏng sôi ở <strong>-196&deg;C</strong> được dùng để bảo quản tinh trùng, phôi thụ tinh trong ống nghiệm, mẫu máu sinh học, hoặc đông lạnh siêu tốc thực phẩm tươi sống.</p>
  </div>

  <!-- SƠ ĐỒ TƯ DUY MINDMAP BÀI 4 -->
  <h3 class="sec-title">4. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Bài 4</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">ĐƠN CHẤT NITROGEN (BÀI 4)</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-blue-light);">1. CẤU TẠO PHÂN TỬ</h5>
        <ul>
          <li>N≡N (Liên kết ba rất bền)</li>
          <li>Eb = 945 kJ/mol &rarr; Rất trơ</li>
          <li>Chiếm 78% thể tích không khí</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-green);">2. TÍNH OXI HÓA</h5>
        <ul>
          <li>N2 + H2 ⇌ NH3 (450&deg;C, 200 bar, Fe)</li>
          <li>N2 + Mg &rarr;(t&deg;) Mg3N2</li>
          <li>N2 + Li &rarr; Li3N (Nhiệt độ thường!)</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-orange);">3. TÍNH KHỬ</h5>
        <ul>
          <li>N2 + O2 ⇌ 2NO (~3000&deg;C / Sấm sét)</li>
          <li>2NO + O2 &rarr; 2NO2 (Nâu đỏ)</li>
          <li>Mưa acid & Chu trình đạm</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">4. ỨNG DỤNG</h5>
        <ul>
          <li>Bảo quản thực phẩm (bim bim giòn)</li>
          <li>Bơm lốp xe ô tô / máy bay</li>
          <li>N2 lỏng (-196&deg;C) trữ mẫu sinh học</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- THỰC CHIẾN STEP BY STEP BÀI 4 (2 BÀI MẪU) -->
  <h3 class="sec-title">5. Thực Chiến: 2 Bài Tập Mẫu Step-by-Step</h3>

  <!-- BÀI MẪU 1 -->
  <div class="step-solver">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 1: Tính Hiệu Suất Tổng Hợp Ammonia (NH3)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Cho 4,958 lít khí N<sub>2</sub> và 17,353 lít khí H<sub>2</sub> (đo ở đkc) vào bình phản ứng có xúc tác bột sắt, nung nóng ở 450&deg;C. Sau một thời gian, thu được 2,479 lít khí NH<sub>3</sub> (đkc). Hãy tính hiệu suất của phản ứng tổng hợp ammonia.</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bẫy chất thiếu / chất dư</strong>
          <p>&bull; Ở đkc: chia cho <strong>24,79</strong> (chuẩn mới!).
          <br>&bull; n<sub>N<sub>2</sub></sub> = 4,958 / 24,79 = <strong>0,2 mol</strong>.
          <br>&bull; n<sub>H<sub>2</sub></sub> = 17,353 / 24,79 = <strong>0,7 mol</strong>.
          <br>&bull; <span class="hl-red">BẪY CHẾT NGƯỜI:</span> Tỉ lệ phản ứng là N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>.
          <br>So sánh: 0,2 / 1 = 0,2 &lt; 0,7 / 3 &approx; 0,233 &rArr; H<sub>2</sub> DƯ! <strong>Hiệu suất BẮT BUỘC PHẢI TÍNH THEO THẰNG THIẾU LÀ N<sub>2</sub></strong>! Đứa nào tính theo H<sub>2</sub> là ăn 0 điểm!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tóm tắt lượng lý thuyết và thực tế</strong>
          <p>&bull; n<sub>NH<sub>3</sub> thực tế thu được</sub> = 2,479 / 24,79 = <strong>0,1 mol</strong>.
          <br>&bull; Lượng N<sub>2</sub> đã phản ứng để tạo ra 0,1 mol NH<sub>3</sub>: n<sub>N<sub>2</sub> pư</sub> = 0,1 / 2 = <strong>0,05 mol</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tại sao dùng công thức này?</strong>
          <p>Hiệu suất H% = (Lượng chất thiếu phản ứng / Lượng chất thiếu ban đầu) &times; 100%:</p>
          <div class="formula-display" style="font-size:0.95rem;">
            H% = (0,05 / 0,2) &times; 100% = 25%
          </div>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ CHÍNH XÁC: H = 25%</strong>
        <p><em>Lời gia sư bình phẩm:</em> Nhớ kỹ quy tắc vàng: Khi đề cho 2 chất tham gia, luôn phải lập tỉ lệ mol chia cho hệ số phương trình xem thằng nào nhỏ hơn thì tính hiệu suất theo thằng đó!</p>
      </div>
    </div>
  </div>

  <!-- BÀI MẪU 2 -->
  <div class="step-solver" style="margin-top:16px;">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 2: Phản Ứng Kim Loại + N2 (Bẫy Nhiệt Độ Thường Của Lithium)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Cho các phát biểu sau về đơn chất Nitrogen:
      <br>(1) Khí N<sub>2</sub> tác dụng với Magnesium (Mg) ở nhiệt độ phòng tạo Mg<sub>3</sub>N<sub>2</sub>.
      <br>(2) Khí N<sub>2</sub> tác dụng với Lithium (Li) ở nhiệt độ phòng tạo Li<sub>3</sub>N.
      <br>(3) Trong phản ứng với kim loại, N<sub>2</sub> đóng vai trò là chất khử.
      <br>(4) Khí NO sinh ra từ tia sét có màu nâu đỏ ngay khi vừa hình thành.
      <br>Hỏi có bao nhiêu phát biểu ĐÚNG?</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từng phát biểu</strong>
          <p>&bull; (1) SAI: Mg tác dụng với N<sub>2</sub> bắt buộc phải <strong>nung nóng</strong> (nhiệt độ cao).
          <br>&bull; (2) ĐÚNG: Li là kim loại DUY NHẤT phản ứng ngay ở nhiệt độ phòng!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Soi tiếp số oxi hóa và màu sắc</strong>
          <p>&bull; (3) SAI: Tác dụng với kim loại thì số oxh của N giảm từ 0 xuống -3 &rarr; N<sub>2</sub> là <strong>chất oxi hóa</strong> chứ không phải chất khử!
          <br>&bull; (4) SAI: Khí NO vừa hình thành là <strong>không màu</strong>! Khi gặp O<sub>2</sub> không khí nó mới hóa nâu đỏ tạo NO<sub>2</sub>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Kết luận</strong>
          <p>Chỉ có duy nhất <strong>1 phát biểu đúng</strong> là phát biểu (2).</p>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ: Có 1 phát biểu đúng (phát biểu 2)</strong>
        <p><em>Lời gia sư bình phẩm:</em> Câu này đề thi chuyên lừa học sinh ở chữ "nhiệt độ phòng" của Mg và "màu nâu đỏ" của NO. Nhớ lấy bài học đắt giá này!</p>
      </div>
    </div>
  </div>

  <!-- BÀI KIỂM TRA 15 CÂU BÀI 4 -->
  <div class="quiz-section" id="b4-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">Bài Kiểm Tra Kiến Thức Bài 4: Đơn Chất Nitrogen</div>
        <div class="quiz-sub">Gồm 8 câu trắc nghiệm + 4 câu đúng/sai + 3 câu tự luận</div>
      </div>
      <div class="quiz-score-badge" id="b4-score">Điểm: 0/15</div>
    </div>

    <!-- TRẮC NGHIỆM 1-8 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 1 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Ở nhiệt độ thường, nitrogen khá trơ về mặt hóa học là do nguyên nhân nào sau đây?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q1" value="A"> A. Nitrogen có độ âm điện lớn.</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="B"> B. Bán kính nguyên tử nitrogen rất nhỏ.</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="C"> C. Phân tử N<sub>2</sub> có liên kết ba rất bền với năng lượng liên kết lớn.</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="D"> D. Phân tử nitrogen không phân cực.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Phân tử N2 có liên kết ba N&equiv;N cực kì bền vững (Eb = 945 kJ/mol) khiến nó trơ ở nhiệt độ thường. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Kim loại duy nhất tác dụng với nitrogen ngay ở nhiệt độ thường là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q2" value="A"> A. Li (Lithium)</label>
        <label class="quiz-option"><input type="radio" name="b4_q2" value="B"> B. Na (Sodium)</label>
        <label class="quiz-option"><input type="radio" name="b4_q2" value="C"> C. Mg (Magnesium)</label>
        <label class="quiz-option"><input type="radio" name="b4_q2" value="D"> D. Ca (Calcium)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> 6Li + N2 &rarr; 2Li3N xảy ra ngay nhiệt độ thường. Các kim loại khác đều cần đun nóng. Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Trong phản ứng N<sub>2</sub> + 3H<sub>2</sub> &hArr; 2NH<sub>3</sub>, đơn chất N<sub>2</sub> đóng vai trò là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q3" value="A"> A. Chất khử.</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="B"> B. Chất oxi hóa.</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="C"> C. Vừa là chất oxi hóa, vừa là chất khử.</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="D"> D. Chất xúc tác.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Số oxi hóa của N giảm từ 0 (trong N2) xuống -3 (trong NH3) &rarr; N2 là chất oxi hóa. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Khí NO không màu sinh ra từ phản ứng N<sub>2</sub> + O<sub>2</sub> sẽ nhanh chóng chuyển sang màu gì khi tiếp xúc với không khí?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q4" value="A"> A. Màu xanh lơ</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="B"> B. Màu vàng lục</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="C"> C. Màu tím</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="D"> D. Màu nâu đỏ (của khí NO<sub>2</sub>)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> 2NO + O2 &rarr; 2NO2 (khí màu nâu đỏ). Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Ứng dụng nào sau đây KHÔNG PHẢI của khí nitrogen?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q5" value="A"> A. Đóng gói bảo quản thực phẩm (bim bim, đồ chiên rán).</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="B"> B. Dùng để duy trì sự hô hấp cho thợ lặn dưới đáy biển.</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="C"> C. Dùng nitrogen lỏng để bảo quản mẫu sinh học.</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="D"> D. Sản xuất phân bón qua quy trình tổng hợp ammonia.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Khí duy trì sự hô hấp là Oxy (O2), Nitrogen không duy trì sự sống và không duy trì sự hô hấp. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 6 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Trong tự nhiên, phản ứng giữa N<sub>2</sub> và O<sub>2</sub> xảy ra trong điều kiện nào?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q6" value="A"> A. Khi có sấm sét (nhiệt độ &approx; 3000&deg;C hoặc phóng điện).</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="B"> B. Trong điều kiện ngày nắng gắt mùa hè (khoảng 40&deg;C).</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="C"> C. Khi có mặt khí CO<sub>2</sub> làm chất xúc tác.</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="D"> D. Xảy ra liên tục tự phát trong khí quyển.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Liên kết N&equiv;N rất bền, cần nhiệt độ &approx; 3000&deg;C hoặc tia lửa điện của sấm sét. Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 7 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Khí nitrogen chiếm khoảng bao nhiêu phần trăm thể tích của không khí Trái Đất?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q7" value="A"> A. 21%</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="B"> B. 50%</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="C"> C. 78%</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="D"> D. 90%</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Khí quyển chứa khoảng 78% N2, 21% O2 và 1% các khí khác. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 8 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Trong phản ứng: N<sub>2</sub> + O<sub>2</sub> &hArr; 2NO, nitrogen thể hiện tính chất gì?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q8" value="A"> A. Tính oxi hóa.</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="B"> B. Tính khử.</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="C"> C. Tính acid.</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="D"> D. Tính base.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Số oxi hóa của N tăng từ 0 lên +2 trong NO &rarr; N2 là chất khử. Chọn B.</div>
    </div>

    <!-- ĐÚNG SAI 9-12 -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 (Đúng / Sai)</div>
      <div class="quiz-q-text">Khí nitrogen không màu, không mùi, không vị và nhẹ hơn không khí một chút.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> M_N2 = 28 g/mol, nhẹ hơn không khí (M_kk &approx; 29 g/mol).</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 (Đúng / Sai)</div>
      <div class="quiz-q-text">Nitrogen tan rất nhiều trong nước ở điều kiện thường.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Phân tử N2 không phân cực nên rất ít tan trong nước (1 lít nước chỉ hòa tan khoảng mười mấy mL N2).</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 (Đúng / Sai)</div>
      <div class="quiz-q-text">Người ta bơm khí nitrogen vào lốp xe đua và máy bay để giảm nguy cơ cháy nổ và giữ áp suất lốp ổn định hơn không khí thường.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> N2 khô ráo, không bị oxi hóa kim loại và ít bị dãn nở vì nhiệt hơn không khí ẩm.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 (Đúng / Sai)</div>
      <div class="quiz-q-text">Trong hợp chất Mg<sub>3</sub>N<sub>2</sub>, số oxi hóa của nguyên tố nitrogen là +3.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Mg có số oxi hóa +2 &rarr; 3 &times; (+2) + 2 &times; x = 0 &rArr; x = -3 (số oxi hóa là -3 chứ không phải +3).</div>
    </div>

    <!-- TỰ LUẬN 13-15 -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 13 (Tự luận)</div>
      <div class="quiz-q-text">Tại sao khi đốt cháy than hoặc củi trong phòng kín lại dễ gây ngạt thở, nhưng dù phòng có đầy khí nitrogen (chiếm 78%) con người vẫn ngạt nếu hết oxy? Khí nitrogen có gây độc trực tiếp cho cơ thể không?</div>
      <textarea placeholder="Giải thích bản chất tác động sinh học của N2..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>1. Khí Nitrogen bản thân nó <strong>KHÔNG ĐỘC</strong> đối với cơ thể người. Nó đi vào phổi rồi lại đi ra mà không tham gia phản ứng hóa học nào.
        <br>2. Tuy nhiên, Nitrogen <strong>KHÔNG DUY TRÌ SỰ HÔ HẤP</strong>. Khi lượng oxy trong phòng kín bị tiêu hao hết (nồng độ O<sub>2</sub> hạ dưới 16%), con người sẽ bị ngạt thở do thiếu oxy để tế bào hoạt động (ngạt cơ học), chứ không phải do khí N<sub>2</sub> đầu độc.
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 (Tự luận tính toán)</div>
      <div class="quiz-q-text">Cho 7,437 lít khí N<sub>2</sub> (đkc) tác dụng với lượng dư khí H<sub>2</sub> (xúc tác Fe, đun nóng). Biết hiệu suất của phản ứng tổng hợp NH<sub>3</sub> chỉ đạt 25%. Tính thể tích khí NH<sub>3</sub> thu được ở cùng điều kiện đkc.</div>
      <textarea placeholder="Nháp bài toán hiệu suất..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>&bull; Số mol N<sub>2</sub> ban đầu: n<sub>N<sub>2</sub></sub> = 7,437 / 24,79 = 0,3 mol.
        <br>&bull; Phương trình: N<sub>2</sub> + 3H<sub>2</sub> &hArr; 2NH<sub>3</sub>
        <br>&bull; Theo lý thuyết (hiệu suất 100%): 1 mol N<sub>2</sub> &rarr; 2 mol NH<sub>3</sub> &rArr; n<sub>NH<sub>3</sub> lý thuyết</sub> = 0,3 &times; 2 = 0,6 mol.
        <br>&bull; Vì hiệu suất chỉ đạt 25%: n<sub>NH<sub>3</sub> thực tế</sub> = 0,6 &times; (25 / 100) = <strong>0,15 mol</strong>.
        <br>&bull; Thể tích NH<sub>3</sub> thu được: V = 0,15 &times; 24,79 = <strong>3,7185 lít</strong>.
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 (Tự luận vận dụng)</div>
      <div class="quiz-q-text">Hãy viết sơ đồ chuyển hóa từ đơn chất Nitrogen trong không khí thành phân bón đạm ammonium nitrate (NH<sub>4</sub>NO<sub>3</sub>) trong công nghiệp, ghi rõ điều kiện phản ứng của từng giai đoạn.</div>
      <textarea placeholder="Viết các phương trình chuỗi..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>Chuỗi phản ứng tổng hợp trong công nghiệp:
        <br>1. N<sub>2</sub> + 3H<sub>2</sub> &hArr; 2NH<sub>3</sub> (450&deg;C, 200 bar, xúc tác Fe).
        <br>2. 4NH<sub>3</sub> + 5O<sub>2</sub> &rarr; 4NO + 6H<sub>2</sub>O (850-900&deg;C, xúc tác Pt).
        <br>3. 2NO + O<sub>2</sub> &rarr; 2NO<sub>2</sub> (nhiệt độ thường).
        <br>4. 4NO<sub>2</sub> + O<sub>2</sub> + 2H<sub>2</sub>O &rarr; 4HNO<sub>3</sub>.
        <br>5. NH<sub>3</sub> + HNO<sub>3</sub> &rarr; <strong>NH<sub>4</sub>NO<sub>3</sub></strong> (Phân đạm amoni nitrat có hàm lượng N cao).
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b4')">📊 Nộp Bài & Chấm Điểm Bài 4</button>
  </div>
</section>
"""

B5_CONTENT = """
<!-- ========================================== -->
<!-- BÀI 5: AMMONIA VÀ MUỐI AMMONIUM (SGK 33-37) -->
<!-- ========================================== -->
<section id="b5" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number">05</div>
    <div class="lesson-meta">
      <h2>Bài 5: Ammonia (NH<sub>3</sub>) & Muối Ammonium (NH<sub>4</sub><sup>+</sup>)</h2>
      <div class="lesson-sub">SGK Hóa học 11 – Kết Nối Tri Thức (Trang 33 đến trang 37)</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Cặp e tự do</span>
        <span class="lesson-tag">Tính base yếu</span>
        <span class="lesson-tag">Tính khử mạnh</span>
        <span class="lesson-tag">Nhiệt phân muối NH4+</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('sgk_b4_5_p32_33.png')">📖 Xem SGK Trang 33</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b5_p34_35.png')">📖 Xem SGK Trang 34-35</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b5_p36_37.png')">📖 Xem SGK Trang 36-37</button>
  </div>

  <!-- PHẦN 1: CẤU TẠO PHÂN TỬ NH3 -->
  <h3 class="sec-title" id="b5-cautao">1. Cấu Tạo & Tính Chất Vật Lí Kì Lạ Của NH<sub>3</sub></h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch SGK Sang Tiếng Người (Vũ Khí Bí Mật Của NH3)</div>
    <p>Phân tử NH<sub>3</sub> có hình <strong>chóp tam giác</strong>, nguyên tử N nằm ở đỉnh chóp, 3 nguyên tử H nằm ở 3 đáy. Góc liên kết H&ndash;N&ndash;H khoảng 107&deg;.</p>
    <div class="formula-display" style="color:var(--accent-green);font-size:1.1rem;">
      H &ndash; N̈ &ndash; H<br><span style="font-size:0.8rem;color:var(--accent-yellow);">|</span><br>H
    </div>
    <p><strong>VŨ KHÍ TỐI THƯỢNG CỦA NH<sub>3</sub>:</strong> Trên đầu nguyên tử N vẫn còn trơ trọi <strong>1 CẶP ELECTRON TỰ DO</strong> chưa tham gia liên kết! Cặp electron này giống như một cánh tay mở rộng, cực kì háo hức đón nhận hạt proton H<sup>+</sup> để tạo thành liên kết cho-nhận. Chính điều này quyết định <strong>TÍNH BASE</strong> của NH<sub>3</sub>!</p>
  </div>

  <div class="box box-story">
    <div class="box-title">🦨 Mùi Khai Kinh Hoàng & Kỉ Lục Tan Trong Nước</div>
    <p>Chắc mày từng đi vệ sinh công cộng và ngửi thấy mùi khai nồng nặc đến xộc óc chảy cả nước mắt? Đó chính là mùi của <strong>khí Ammonia (NH<sub>3</sub>)</strong> sinh ra do vi khuẩn phân hủy urê trong nước tiểu!</p>
    <p><strong>Kỉ Lục Tan Trong Nước:</strong> Ở 20&deg;C, <strong>1 lít nước có thể hòa tan tới 700 LÍT KHÍ NH<sub>3</sub></strong>! Tại sao nó tan khủng khiếp đến thế? Vì giữa phân tử NH<sub>3</sub> và các phân tử H<sub>2</sub>O tạo được <em>liên kết hydrogen liên phân tử</em> cực mạnh, nước hút NH<sub>3</sub> như nam châm hút sắt!</p>
  </div>

  <!-- PHẦN 2: TÍNH CHẤT HÓA HỌC CỦA NH3 -->
  <h3 class="sec-title" id="b5-tchat">2. Hai Tính Chất Hóa Học Cốt Lõi Của Ammonia</h3>

  <div class="box box-theory">
    <div class="box-title">📘 1. TÍNH BASE YẾU (Do Cặp e Tự Do Của N Nhận H<sup>+</sup>)</div>
    <p><strong>a) Tác dụng với nước:</strong></p>
    <div class="reaction-box">
      NH<sub>3</sub> + H<sub>2</sub>O &hArr; NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup>
    </div>
    <p>&bull; Phản ứng thuận nghịch, sinh ra ion OH<sup>&minus;</sup> &rarr; Làm quỳ tím ẩm hóa <span class="hl-blue">XANH</span>, phenolphthalein hóa <span class="hl-purple">HỒNG</span>.</p>

    <p style="margin-top:10px;"><strong>b) Tác dụng với acid &rarr; Muối ammonium:</strong></p>
    <div class="reaction-box">
      NH<sub>3</sub>(g) + HCl(g) &rarr; NH<sub>4</sub>Cl(s) (Khói trắng!)
      <br>2NH<sub>3</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>
    </div>
    <p>&bull; <em>Thí nghiệm ảo thuật kinh điển:</em> Để 2 bình chứa HCl đặc và NH<sub>3</sub> đặc lại gần nhau, đéo cần chạm miệng bình vào nhau mà giữa không khí tự nhiên bốc lên một làn <strong>"khói trắng như mây"</strong>! Thực chất khói trắng đó là các hạt tinh thể muối NH<sub>4</sub>Cl li ti bay lơ lửng.</p>

    <p style="margin-top:10px;"><strong>c) Tác dụng với dung dịch muối của kim loại &rarr; Kết tủa Hydroxide:</strong></p>
    <div class="reaction-box">
      Al<sup>3+</sup> + 3NH<sub>3</sub> + 3H<sub>2</sub>O &rarr; Al(OH)<sub>3</sub>&darr; + 3NH<sub>4</sub><sup>+</sup> (Kết tủa keo trắng)
      <br>Fe<sup>3+</sup> + 3NH<sub>3</sub> + 3H<sub>2</sub>O &rarr; Fe(OH)<sub>3</sub>&darr; + 3NH<sub>4</sub><sup>+</sup> (Kết tủa nâu đỏ)
    </div>
    <p>&bull; <span class="hl-red">LƯU Ý:</span> Dung dịch NH<sub>3</sub> KHÔNG HÒA TAN ĐƯỢC Al(OH)<sub>3</sub> kể cả khi dùng dư NH<sub>3</sub> (khác với dung dịch kiềm mạnh NaOH sẽ hòa tan Al(OH)<sub>3</sub>!).</p>
  </div>

  <div class="box box-theory">
    <div class="box-title">📘 2. TÍNH KHỬ MẠNH (Do N Có Số Oxi Hóa Cực Tiểu -3)</div>
    <p>Trong NH<sub>3</sub>, số oxi hóa của N là <strong>-3</strong> (thấp nhất có thể có). Nó chỉ có một con đường duy nhất là <strong>TĂNG LÊN</strong> &rarr; Thể hiện tính khử mạnh mẽ.</p>
    <div class="reaction-box">
      &bull; Đốt trong khí oxygen (không xúc tác &rarr; ngọn lửa màu vàng):
      <br><strong>4NH<sub>3</sub> + 3O<sub>2</sub> &rarr;(t&deg;) 2N<sub>2</sub> + 6H<sub>2</sub>O</strong>
      <br>&bull; Đốt có xúc tác Platinum (Pt) ở 850&ndash;900&deg;C (Giai đoạn sống còn để sản xuất HNO<sub>3</sub>):
      <br><strong>4NH<sub>3</sub> + 5O<sub>2</sub> &rarr;(Pt, 850&deg;C) 4NO + 6H<sub>2</sub>O</strong>
      <br>&bull; Khử oxide kim loại (CuO đen hóa đỏ Cu):
      <br><strong>2NH<sub>3</sub> + 3CuO &rarr;(t&deg;) 3Cu + N<sub>2</sub> + 3H<sub>2</sub>O</strong>
    </div>
  </div>

  <!-- PHẦN 3: MUỐI AMMONIUM -->
  <h3 class="sec-title" id="b5-muoi">3. Muối Ammonium (Chứa Ion NH<sub>4</sub><sup>+</sup>)</h3>

  <div class="box box-formula">
    <div class="box-title">📐 2 Tính Chất Vàng Của Mọi Muối Ammonium</div>
    <p><strong>1. Tính Tan & Điện Li:</strong></p>
    <p><strong>100% các muối ammonium đều tan rất tốt trong nước và điện li hoàn toàn</strong> thành cation NH<sub>4</sub><sup>+</sup> và anion gốc acid tương ứng.</p>

    <p style="margin-top:10px;"><strong>2. Phản Ứng Tác Dụng Dung Dịch Kiềm (DÙNG ĐỂ NHẬN BIẾT ION NH<sub>4</sub><sup>+</sup>):</strong></p>
    <div class="formula-display">
      NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup> &rarr;(t&deg;) NH<sub>3</sub>&uarr; + H<sub>2</sub>O
    </div>
    <div class="formula-label">Hiện tượng: Bốc ra khí có mùi khai đặc trưng, làm xanh giấy quỳ tím ẩm đặt ở miệng ống nghiệm!</div>

    <p style="margin-top:10px;"><strong>3. Phản Ứng Kém Bền Nhiệt (Dễ Bị Nhiệt Phân):</strong></p>
    <div class="reaction-box">
      &bull; Muối gốc acid không có tính oxi hóa &rarr; phân hủy thành NH<sub>3</sub> và acid tương ứng:
      <br>NH<sub>4</sub>Cl(s) &hArr;(t&deg;) NH<sub>3</sub>(g) + HCl(g)
      <br>NH<sub>4</sub>HCO<sub>3</sub>(s) &rarr;(t&deg;) NH<sub>3</sub> + CO<sub>2</sub> + H<sub>2</sub>O <em>(Dùng làm bột nở làm bánh bao!)</em>
      <br>&bull; Muối gốc acid có tính oxi hóa &rarr; tạo ra N<sub>2</sub> hoặc N<sub>2</sub>O:
      <br>NH<sub>4</sub>NO<sub>2</sub> &rarr;(t&deg;) N<sub>2</sub> + 2H<sub>2</sub>O (Điều chế N<sub>2</sub> trong phòng thí nghiệm)
      <br>NH<sub>4</sub>NO<sub>3</sub> &rarr;(t&deg;) N<sub>2</sub>O + 2H<sub>2</sub>O (Nổ phân bón amonit)
    </div>
  </div>

  <!-- COMBO HỦY DIỆT BÀI 5 -->
  <div class="box box-combo">
    <div class="box-title">💥 COMBO HỦY DIỆT: PHƯƠNG PHÁP NHẬN BIẾT BẰNG DUNG DỊCH KIỀM (NaOH)</div>
    <p><strong>Dấu hiệu nhận biết:</strong> Đề bài cho các dung dịch muối mất nhãn như: NH<sub>4</sub>Cl, FeCl<sub>3</sub>, AlCl<sub>3</sub>, CuCl<sub>2</sub>, NaCl... chỉ dùng MỘT THUỐC THỬ DUY NHẤT.</p>
    <p><strong>ỐP NGAY THUỐC THỬ LÀ: DUNG DỊCH NaOH (ĐUN NÓNG NHẸ)</strong></p>
    <ul class="content-list">
      <li>Ống nào có <span class="hl-yellow">khí mùi khai bốc lên</span> (làm xanh quỳ tím ẩm) &rarr; Là muối <strong>NH<sub>4</sub><sup>+</sup></strong>.</li>
      <li>Ống nào có <span class="hl-red">kết tủa nâu đỏ</span> Fe(OH)<sub>3</sub> &rarr; Là muối <strong>Fe<sup>3+</sup></strong>.</li>
      <li>Ống nào có <span class="hl-blue">kết tủa xanh lam</span> Cu(OH)<sub>2</sub> &rarr; Là muối <strong>Cu<sup>2+</sup></strong>.</li>
      <li>Ống nào có <span class="hl-green">kết tủa trắng xanh hóa nâu ngoài không khí</span> &rarr; Là muối <strong>Fe<sup>2+</sup></strong>.</li>
      <li>Ống nào có <span class="hl-purple">kết tủa keo trắng, sau đó kết tủa tan dần</span> trong NaOH dư &rarr; Là muối <strong>Al<sup>3+</sup></strong>.</li>
      <li>Ống nào không có hiện tượng gì &rarr; Là muối kim loại kiềm như <strong>NaCl</strong>.</li>
    </ul>
  </div>

  <!-- SƠ ĐỒ TƯ DUY MINDMAP BÀI 5 -->
  <h3 class="sec-title">4. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Bài 5</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">AMMONIA & MUỐI AMMONIUM (BÀI 5)</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-blue-light);">1. TÍNH BASE CỦA NH3</h5>
        <ul>
          <li>Nhờ cặp electron tự do trên N</li>
          <li>Quỳ tím ẩm hóa xanh</li>
          <li>Tác dụng acid &rarr; Muối amoni</li>
          <li>Tạo kết tủa hydroxide không tan</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">2. TÍNH KHỬ CỦA NH3</h5>
        <ul>
          <li>N có số oxi hóa cực tiểu -3</li>
          <li>Cháy trong O2 &rarr; N2 + H2O</li>
          <li>Oxi hóa có xúc tác Pt &rarr; NO</li>
          <li>Khử CuO đen &rarr; Cu đỏ</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-green);">3. MUỐI AMMONIUM (NH4+)</h5>
        <ul>
          <li>100% tan & điện li mạnh</li>
          <li>Tác dụng kiềm &rarr; Khí NH3 khai</li>
          <li>Kém bền nhiệt (dễ nhiệt phân)</li>
          <li>NH4HCO3 làm bột nở bánh bao</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-purple);">4. ĐIỀU CHẾ & BẢO QUẢN</h5>
        <ul>
          <li>N2 + H2 ⇌ NH3 (Haber process)</li>
          <li>Không bón vôi chung với đạm amoni</li>
          <li>Làm khô NH3 bằng vôi sống CaO</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- THỰC CHIẾN STEP BY STEP BÀI 5 (2 BÀI MẪU) -->
  <h3 class="sec-title">5. Thực Chiến: 2 Bài Tập Mẫu Step-by-Step</h3>

  <!-- BÀI MẪU 1 -->
  <div class="step-solver">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 1: Nhận Biết Dung Dịch Mất Nhãn Bằng 1 Thuốc Thử</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Bằng phương pháp hóa học, hãy phân biệt 4 dung dịch mất nhãn chứa riêng biệt trong 4 lọ: NH<sub>4</sub>Cl, Na<sub>2</sub>SO<sub>4</sub>, (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>, NaCl. Chỉ được dùng DUY NHẤT một thuốc thử.</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi các ion cần nhận biết</strong>
          <p>&bull; Các cation: NH<sub>4</sub><sup>+</sup> (cho khí khai với OH<sup>&minus;</sup>), Na<sup>+</sup>.
          <br>&bull; Các anion: SO<sub>4</sub><sup>2&minus;</sup> (cho kết tủa trắng với Ba<sup>2+</sup>), Cl<sup>&minus;</sup>.
          <br>&bull; Tư duy: Cần một chất vừa có Ba<sup>2+</sup> vừa có OH<sup>&minus;</sup> &rarr; Chọn ngay <strong>dung dịch Ba(OH)<sub>2</sub></strong>!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Bảng tóm tắt hiện tượng</strong>
          <div class="tbl-wrap">
            <table>
              <thead><tr><th>Dung dịch</th><th>Hiện tượng khi nhỏ Ba(OH)<sub>2</sub> đun nóng</th></tr></thead>
              <tbody>
                <tr><td>NH<sub>4</sub>Cl</td><td>Chỉ có <strong>khí mùi khai</strong> bốc lên (NH<sub>3</sub>&uarr;)</td></tr>
                <tr><td>Na<sub>2</sub>SO<sub>4</sub></td><td>Chỉ có <strong>kết tủa trắng</strong> BaSO<sub>4</sub>&darr;</td></tr>
                <tr><td>(NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub></td><td><strong>Vừa có khí mùi khai</strong> bốc lên, <strong>vừa có kết tủa trắng</strong></td></tr>
                <tr><td>NaCl</td><td><strong>Không có hiện tượng gì</strong></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Viết các phương trình ion rút gọn</strong>
          <p>&bull; <code>NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup> &rarr; NH<sub>3</sub>&uarr; + H<sub>2</sub>O</code>
          <br>&bull; <code>Ba<sup>2+</sup> + SO<sub>4</sub><sup>2&minus;</sup> &rarr; BaSO<sub>4</sub>&darr;</code></p>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>THUỐC THỬ DUY NHẤT LÀ: Dung dịch Ba(OH)<sub>2</sub></strong>
        <p><em>Lời gia sư bình phẩm:</em> Thấy vi diệu chưa? 4 lọ cho 4 hiện tượng hoàn toàn khác nhau (chỉ khí, chỉ tủa, cả tủa lẫn khí, không hiện tượng). Đi thi gặp bài này thì 10 điểm trong lòng bàn tay!</p>
      </div>
    </div>
  </div>

  <!-- BÀI MẪU 2 -->
  <div class="step-solver" style="margin-top:16px;">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 2: Phản Ứng Khử Oxit Kim Loại Của Khí NH3</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Dẫn V lít khí NH<sub>3</sub> (đkc) đi qua ống sứ đựng 24 gam bột CuO nung nóng. Sau một thời gian, trong ống còn lại 19,2 gam chất rắn. Tính giá trị của V (giả sử chỉ xảy ra phản ứng khử CuO thành Cu).</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa "chất rắn giảm"</strong>
          <p>&bull; m<sub>chất rắn ban đầu (CuO)</sub> = 24 gam.
          <br>&bull; m<sub>chất rắn sau pư</sub> = 19,2 gam.
          <br>&bull; <span class="hl-red">BẢN CHẤT CẦN NHỚ:</span> Khối lượng chất rắn giảm đi chính là khối lượng của <strong>nguyên tử Oxygen [O]</strong> bị khí NH<sub>3</sub> cướp mất:
          <br>m<sub>giảm</sub> = m<sub>O</sub> = 24 &minus; 19,2 = <strong>4,8 gam</strong>!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tính số mol O bị cướp</strong>
          <p>&bull; n<sub>O bị cướp</sub> = 4,8 / 16 = <strong>0,3 mol</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tư duy chọn tỉ lệ phương trình</strong>
          <p>Phương trình: 2NH<sub>3</sub> + 3CuO &rarr; 3Cu + N<sub>2</sub> + 3H<sub>2</sub>O
          <br>Ta thấy: 2 mol NH<sub>3</sub> cướp được 3 mol nguyên tử O.
          <br>&rArr; <strong>n<sub>NH<sub>3</sub></sub> = (2/3) &times; n<sub>O</sub></strong> = (2/3) &times; 0,3 = <strong>0,2 mol</strong>.
          <br>&rArr; V<sub>NH<sub>3</sub> (đkc)</sub> = 0,2 &times; 24,79 = <strong>4,958 Lít</strong>.</p>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ CHÍNH XÁC: V = 4,958 Lít</strong>
        <p><em>Lời gia sư bình phẩm:</em> Đứa nào đi ngồi tính số mol CuO dư với Cu tạo thành rồi lập hệ phương trình thì đến tết mới xong! Dùng bảo toàn khối lượng nguyên tử O cướp mất chỉ mất đúng 2 dòng!</p>
      </div>
    </div>
  </div>

  <!-- BÀI KIỂM TRA 15 CÂU BÀI 5 -->
  <div class="quiz-section" id="b5-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">Bài Kiểm Tra Kiến Thức Bài 5: Ammonia & Muối Ammonium</div>
        <div class="quiz-sub">Gồm 8 câu trắc nghiệm + 4 câu đúng/sai + 3 câu tự luận</div>
      </div>
      <div class="quiz-score-badge" id="b5-score">Điểm: 0/15</div>
    </div>

    <!-- TRẮC NGHIỆM 1-8 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 1 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Dung dịch ammonia trong nước có môi trường gì và làm đổi màu quỳ tím như thế nào?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q1" value="A"> A. Môi trường base yếu, làm quỳ tím hóa xanh.</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="B"> B. Môi trường acid, làm quỳ tím hóa đỏ.</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="C"> C. Môi trường trung tính, không đổi màu quỳ tím.</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="D"> D. Môi trường base mạnh, làm quỳ tím mất màu.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH3 + H2O &hArr; NH4+ + OH- (base yếu, quỳ tím hóa xanh). Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 2 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hiện tượng "khói trắng" xuất hiện khi đưa hai đầu đũa thủy tinh nhúng vào hai dung dịch đặc nào lại gần nhau?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q2" value="A"> A. HNO<sub>3</sub> đặc và H<sub>2</sub>SO<sub>4</sub> đặc</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="B"> B. NaOH đặc và HCl đặc</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="C"> C. NH<sub>3</sub> đặc và HCl đặc</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="D"> D. NH<sub>3</sub> đặc và NaOH đặc</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH3(k) bay hơi gặp HCl(k) bay hơi tạo ra tinh thể muối NH4Cl(r) màu trắng lơ lửng như khói. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Tính chất hóa học nào sau đây là của ammonia (NH<sub>3</sub>)?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q3" value="A"> A. Tính acid mạnh và tính oxi hóa mạnh.</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="B"> B. Tính base yếu và tính khử mạnh.</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="C"> C. Chỉ có tính oxi hóa.</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="D"> D. Chỉ có tính khử, không có tính acid-base.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH3 có tính base yếu (do cặp e tự do nhận H+) và tính khử mạnh (do N có số oxi hóa cực tiểu -3). Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Để nhận biết ion ammonium (NH<sub>4</sub><sup>+</sup>) trong dung dịch, người ta dùng thuốc thử nào và có hiện tượng gì?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q4" value="A"> A. Dùng dung dịch HCl &rarr; có khí mùi hắc thoát ra.</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="B"> B. Dùng dung dịch BaCl<sub>2</sub> &rarr; có kết tủa trắng.</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="C"> C. Dùng AgNO<sub>3</sub> &rarr; có kết tủa vàng nhạt.</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="D"> D. Dùng dung dịch kiềm (NaOH/KOH), đun nóng &rarr; có khí mùi khai làm xanh quỳ tím ẩm.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH4+ + OH- &rarr; NH3&uarr; (mùi khai) + H2O. Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hợp chất nào sau đây được dùng làm bột nở trong quá trình làm bánh bao, bánh quy xốp?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q5" value="A"> A. NH<sub>4</sub>HCO<sub>3</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="B"> B. NH<sub>4</sub>NO<sub>3</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="C"> C. NH<sub>4</sub>Cl</label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="D"> D. (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub></label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH4HCO3 khi nung nóng bị phân hủy hoàn toàn thành các chất khí: NH3 + CO2 + H2O bay lên tạo các lỗ xốp làm nở bánh. Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Khi dẫn từ từ khí NH<sub>3</sub> đến dư vào dung dịch AlCl<sub>3</sub>, hiện tượng quan sát được là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q6" value="A"> A. Xuất hiện kết tủa keo trắng, sau đó kết tủa tan tạo dung dịch trong suốt.</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="B"> B. Có kết tủa màu nâu đỏ xuất hiện.</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="C"> C. Xuất hiện kết tủa keo trắng và kết tủa KHÔNG TAN khi NH<sub>3</sub> dư.</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="D"> D. Không có hiện tượng gì.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Al3+ + 3NH3 + 3H2O &rarr; Al(OH)3&darr; + 3NH4+. Vì NH3 là base yếu nên không hòa tan được Al(OH)3 kết tủa keo trắng. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Phản ứng đốt cháy NH<sub>3</sub> trong không khí có mặt xúc tác platin (Pt) ở 850&ndash;900&deg;C sinh ra sản phẩm chính chứa nitrogen là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q7" value="A"> A. N<sub>2</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="B"> B. NO</label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="C"> C. NO<sub>2</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="D"> D. N<sub>2</sub>O</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> 4NH3 + 5O2 &rarr;(Pt, 850&deg;C) 4NO + 6H2O. Nếu không có xúc tác Pt thì mới ra N2. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Dung dịch muối ammonium nào sau đây có phản ứng nhiệt phân tạo thành khí N<sub>2</sub>?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q8" value="A"> A. NH<sub>4</sub>Cl</label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="B"> B. NH<sub>4</sub>HCO<sub>3</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="C"> C. NH<sub>4</sub>NO<sub>3</sub></label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="D"> D. NH<sub>4</sub>NO<sub>2</sub></label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> NH4NO2 &rarr;(t&deg;) N2 + 2H2O (dùng điều chế N2 trong PTN). Chọn D.</div>
    </div>

    <!-- ĐÚNG SAI 9-12 -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 (Đúng / Sai)</div>
      <div class="quiz-q-text">Tất cả các muối chứa cation ammonium (NH<sub>4</sub><sup>+</sup>) đều tan tốt trong nước và là chất điện li mạnh.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> 100% muối ammonium đều tan và điện li hoàn toàn.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 (Đúng / Sai)</div>
      <div class="quiz-q-text">Dẫn khí NH<sub>3</sub> qua ống sứ đựng bột CuO màu đen nung nóng, thấy bột CuO chuyển sang màu xanh lam.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> NH3 khử CuO màu đen thành kim loại Cu có màu ĐỎ (chứ không phải màu xanh lam): 2NH3 + 3CuO &rarr; 3Cu + N2 + 3H2O.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 (Đúng / Sai)</div>
      <div class="quiz-q-text">Khí ammonia tan cực nhiều trong nước là nhờ tạo được liên kết hydrogen với phân tử nước.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> Liên kết hydrogen liên phân tử là nguyên nhân chính khiến 1 lít nước hòa tan được 700 lít NH3.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 (Đúng / Sai)</div>
      <div class="quiz-q-text">Người ta có thể làm khô khí NH<sub>3</sub> ẩm bằng cách dẫn nó qua bình đựng dung dịch H<sub>2</sub>SO<sub>4</sub> đặc.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI BÉT!</strong> NH3 là base sẽ phản ứng mãnh liệt với H2SO4 đặc tạo thành muối amoni sunfat, khí NH3 sẽ bị giữ lại hết trong bình! Muốn làm khô NH3 phải dùng chất hút ẩm có tính kiềm như vôi sống CaO.</div>
    </div>

    <!-- TỰ LUẬN 13-15 -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 13 (Tự luận thực tế)</div>
      <div class="quiz-q-text">Tại sao người nông dân tuyệt đối không được bón vôi sống (CaO) hoặc vôi tôi (Ca(OH)<sub>2</sub>) cùng lúc với phân đạm chứa gốc ammonium như đạm một lá (NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub> hoặc đạm hai lá NH<sub>4</sub>NO<sub>3</sub>?</div>
      <textarea placeholder="Giải thích phản ứng xảy ra làm mất đạm..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>1. Khi bón vôi vào đất ẩm, vôi sinh ra môi trường kiềm chứa nhiều ion OH<sup>&minus;</sup>: CaO + H<sub>2</sub>O &rarr; Ca<sup>2+</sup> + 2OH<sup>&minus;</sup>.
        <br>2. Phân đạm ammonium chứa ion NH<sub>4</sub><sup>+</sup> sẽ phản ứng ngay lập tức với OH<sup>&minus;</sup>:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup> &rarr; NH<sub>3</sub>&uarr; + H<sub>2</sub>O</code>
        <br>3. Khí ammonia (NH<sub>3</sub>) bay hơi mất vào không khí mang theo toàn bộ lượng nguyên tố nitrogen dinh dưỡng &rarr; <strong>Mất sạch tác dụng của phân đạm</strong>, gây lãng phí tiền bạc của người nông dân!
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 (Tự luận phân biệt chất)</div>
      <div class="quiz-q-text">Bằng phương pháp hóa học, hãy trình bày cách phân biệt 3 dung dịch muối mất nhãn sau chỉ bằng một thuốc thử duy nhất: NH<sub>4</sub>Cl, FeCl<sub>3</sub>, NaCl.</div>
      <textarea placeholder="Trình bày các bước nhận biết..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>&bull; Thuốc thử duy nhất: <strong>Dung dịch NaOH</strong>.
        <br>&bull; Cách tiến hành: Trích mẫu thử, nhỏ vài giọt NaOH vào từng mẫu và đun nóng nhẹ:
        <br>1. Mẫu thử xuất hiện khí mùi khai bốc lên làm xanh giấy quỳ ẩm &rarr; Là <strong>NH<sub>4</sub>Cl</strong>:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>NH<sub>4</sub>Cl + NaOH &rarr; NaCl + NH<sub>3</sub>&uarr; + H<sub>2</sub>O</code>
        <br>2. Mẫu thử xuất hiện kết tủa màu nâu đỏ &rarr; Là <strong>FeCl<sub>3</sub></strong>:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>FeCl<sub>3</sub> + 3NaOH &rarr; Fe(OH)<sub>3</sub>&darr;(nâu đỏ) + 3NaCl</code>
        <br>3. Mẫu thử không có bất kì hiện tượng gì &rarr; Là <strong>NaCl</strong>.
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 (Tự luận tính toán)</div>
      <div class="quiz-q-text">Cho 4,958 lít khí NH<sub>3</sub> (đkc) đi từ từ qua ống sứ đựng lượng dư bột CuO nung nóng đỏ. Sau khi phản ứng xảy ra hoàn toàn, chất rắn trong ống giảm m gam. Tính giá trị của m.</div>
      <textarea placeholder="Nháp bài toán bảo toàn khối lượng chất rắn..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>&bull; Số mol NH<sub>3</sub>: n<sub>NH<sub>3</sub></sub> = 4,958 / 24,79 = 0,2 mol.
        <br>&bull; Phương trình: 2NH<sub>3</sub> + 3CuO &rarr;(t&deg;) 3Cu + N<sub>2</sub>&uarr; + 3H<sub>2</sub>O
        <br>&bull; Bản chất: Khối lượng chất rắn giảm đi chính là khối lượng của <strong>nguyên tử Oxygen (O)</strong> bị tách khỏi CuO:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;m<sub>giảm</sub> = m<sub>O (trong CuO bị mất)</sub>
        <br>&bull; Theo phương trình: n<sub>O phản ứng</sub> = 1,5 &times; n<sub>NH<sub>3</sub></sub> = 1,5 &times; 0,2 = 0,3 mol.
        <br>&bull; Khối lượng chất rắn giảm: m = 0,3 &times; 16 = <strong>4,8 gam</strong>.
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b5')">📊 Nộp Bài & Chấm Điểm Bài 5</button>
  </div>
</section>
"""
