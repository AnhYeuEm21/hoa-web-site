# -*- coding: utf-8 -*-
"""
Module data_b6.py - NÂNG CẤP TOÀN DIỆN
- Bổ sung Sơ Đồ Tư Duy Mindmap Cho Bài 6
- Bổ sung 2 Bài Tập Thực Chiến Mẫu Chuẩn 3 Bước
- Đổi nút bấm: "🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!"
"""

B6_CONTENT = """
<!-- ========================================== -->
<!-- BÀI 6: HỢP CHẤT CỦA NITROGEN VỚI OXYGEN (SGK 38-41) -->
<!-- ========================================== -->
<section id="b6" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number">06</div>
    <div class="lesson-meta">
      <h2>Bài 6: Một Số Hợp Chất Của Nitrogen Với Oxygen & HNO<sub>3</sub></h2>
      <div class="lesson-sub">SGK Hóa học 11 – Kết Nối Tri Thức (Trang 38 đến trang 41)</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Mưa acid</span>
        <span class="lesson-tag">Hiện tượng phú dưỡng</span>
        <span class="lesson-tag">Tính oxi hóa cực mạnh của HNO3</span>
        <span class="lesson-tag">Thụ động hóa Fe, Al</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('sgk_b6_p38_39.png')">📖 Xem SGK Trang 38-39</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b6_p40_41.png')">📖 Xem SGK Trang 40-41</button>
  </div>

  <!-- PHẦN 1: CÁC OXIDE CỦA NITROGEN & HIỆN TƯỢNG MƯA ACID -->
  <h3 class="sec-title" id="b6-muaacid">1. Các Oxide NO<sub>x</sub> & Thảm Họa Mưa Acid</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch SGK Sang Tiếng Người: Mưa Acid Sinh Ra Như Thế Nào?</div>
    <p>Khí thải từ các nhà máy nhiệt điện than, luyện kim và ống xả xe máy, ô tô tống ra bầu khí quyển một lượng khổng lồ các khí oxide của nitrogen (viết gộp là <strong>NO<sub>x</sub></strong>, gồm NO, NO<sub>2</sub>) cùng với khí <strong>SO<sub>2</sub></strong>.</p>
    <p>Chuỗi phản ứng sinh ra axit trong các đám mây:</p>
    <div class="reaction-box">
      2NO + O<sub>2</sub> &rarr; 2NO<sub>2</sub>
      <br><strong>4NO<sub>2</sub> + O<sub>2</sub> + 2H<sub>2</sub>O &rarr; 4HNO<sub>3</sub></strong> (Nitric acid)
      <br><strong>2SO<sub>2</sub> + O<sub>2</sub> + 2H<sub>2</sub>O &rarr; 2H<sub>2</sub>SO<sub>4</sub></strong> (Sulfuric acid)
    </div>
    <p>Các giọt acid này hòa tan vào nước mưa, làm nước mưa có độ pH giảm mạnh xuống <strong>pH &lt; 5,6</strong> (mức bình thường của nước mưa là khoảng 5,6 do có CO<sub>2</sub> hòa tan). Nước mưa này được gọi là <strong>MƯA ACID</strong>.</p>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 HẬU QUẢ TÀN PHÁ CỦA MƯA ACID</div>
    <ul class="content-list">
      <li><strong>Ăn mòn tượng đài, công trình xây dựng:</strong> Các công trình bằng đá vôi hoặc kim loại bị phá hủy nghiêm trọng: <code>CaCO<sub>3</sub> + 2H<sup>+</sup> &rarr; Ca<sup>2+</sup> + CO<sub>2</sub>&uarr; + H<sub>2</sub>O</code>.</li>
      <li><strong>Tàn sát rừng cây:</strong> Mưa acid rửa trôi hết các khoáng chất dinh dưỡng trong đất và giải phóng các ion kim loại nặng độc hại (như Al<sup>3+</sup>) làm hỏng rễ cây, khiến cả cánh rừng bị khô héo và chết rụi.</li>
      <li><strong>Hủy diệt sinh thái ao hồ:</strong> Làm pH nước hồ hạ thấp đột ngột, làm chết các loài phiêu sinh thực vật, tôm, cua, cá không sống nổi.</li>
    </ul>
  </div>

  <!-- PHẦN 2: HIỆN TƯỢNG PHÚ DƯỠNG -->
  <h3 class="sec-title" id="b6-phuduong">2. Hiện Tượng Phú Dưỡng (Eutrophication)</h3>

  <div class="box box-story">
    <div class="box-title">🌊 "Bội Thực Dinh Dưỡng": Tại Sao Hồ Nước Bị Chết Ngạt?</div>
    <p>Mày đã bao giờ thấy một cái ao làng hay hồ nước trong thành phố bị một lớp váng xanh lè, đặc quánh như cháo bao phủ kín mặt nước, bốc mùi hôi thối nồng nặc và cá chết ngửa bụng hàng loạt chưa? Người ta gọi đó là <strong>HIỆN TƯỢNG PHÚ DƯỠNG</strong> (Phú = giàu có, Dưỡng = dinh dưỡng &rarr; Thừa mứa chất bổ quá hóa thảm họa!).</p>
  </div>

  <div class="box box-theory">
    <div class="box-title">📘 4 Giai Đoạn Của Hiện Tượng Phú Dưỡng (Chuẩn Đề Thi Hay Hỏi)</div>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Giai Đoạn</th>
            <th>Diễn Biến Cụ Thể</th>
            <th>Hậu Quả Hóa & Sinh Học</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Xả thải dư thừa</strong></td>
            <td>Nước thải sinh hoạt (chứa bột giặt phosphate), nước thải chăn nuôi và dư lượng phân bón hóa học (đạm nitrate NO<sub>3</sub><sup>&minus;</sup>, lân PO<sub>4</sub><sup>3&minus;</sup>) xả thẳng vào ao hồ.</td>
            <td>Nồng độ các nguyên tố <strong>N và P</strong> trong nước tăng vọt vượt ngưỡng cho phép.</td>
          </tr>
          <tr>
            <td><strong>2. Tảo nở hoa (Algal Bloom)</strong></td>
            <td>Được "bơm" thức ăn dồi dào, các loài tảo bèo, rong rêu sinh sôi nảy nở với tốc độ tên lửa, phủ kín toàn bộ mặt nước.</td>
            <td>Mặt hồ biến thành một thảm xanh dày đặc, chặn đứng ánh sáng mặt trời chiếu xuống tầng nước sâu.</td>
          </tr>
          <tr>
            <td><strong>3. Tảo chết hàng loạt</strong></td>
            <td>Sau khi ăn hết chất dinh dưỡng, lớp tảo khổng lồ bắt đầu chết đi và chìm xuống đáy hồ.</td>
            <td>Các vi khuẩn hiếu khí bắt đầu quá trình phân hủy xác tảo.</td>
          </tr>
          <tr>
            <td><strong>4. Thiếu hụt Oxy & Cá chết</strong></td>
            <td>Vi khuẩn hút cạn kiệt toàn bộ khí Oxy (O<sub>2</sub>) hòa tan trong nước để tiêu hủy xác tảo.</td>
            <td>Nước trở nên thiếu dưỡng khí trầm trọng, chuyển sang phân hủy kị khí sinh ra các khí độc mùi thối rữa (H<sub>2</sub>S, NH<sub>3</sub>, CH<sub>4</sub>). Cá tôm và toàn bộ hệ sinh thái thủy sinh bị <strong>chết ngạt hàng loạt</strong>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- PHẦN 3: NITRIC ACID (HNO3) - "ÔNG VUA OXI HÓA" -->
  <h3 class="sec-title" id="b6-hno3">3. Nitric Acid (HNO<sub>3</sub>) &ndash; "Sát Thủ Oxi Hóa" Của Hóa Học 11</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Cấu Tạo & Tính Chất Vật Lí</div>
    <p>HNO<sub>3</sub> tinh khiết là chất lỏng không màu, bốc khói mạnh trong không khí ẩm. Trong tự nhiên hoặc trong phòng thí nghiệm, dung dịch HNO<sub>3</sub> để lâu thường bị ngả sang <strong>MÀU VÀNG NÂU</strong> là do một phần acid bị phân hủy chậm dưới ánh sáng tạo ra khí NO<sub>2</sub> màu nâu đỏ tan ngược vào dung dịch:</p>
    <div class="reaction-box">
      4HNO<sub>3</sub> &rarr;(ánh sáng, t&deg;) 4NO<sub>2</sub>&uarr; (nâu đỏ) + O<sub>2</sub>&uarr; + 2H<sub>2</sub>O
    </div>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 2 TÍNH CHẤT HÓA HỌC SỐNG CÒN CỦA HNO3</div>
    <p><strong>1. Tính Acid Mạnh:</strong> Phân li hoàn toàn 100% trong nước ra H<sup>+</sup> và NO<sub>3</sub><sup>&minus;</sup>. Làm quỳ tím hóa đỏ, tác dụng basic oxide, base và muối của acid yếu hơn (như muối carbonate tạo bọt khí CO<sub>2</sub>).</p>

    <p style="margin-top:14px;"><strong>2. TÍNH OXI HÓA CỰC KỲ MẠNH (TRỌNG TÂM ĐỈNH CAO THI CỬ):</strong></p>
    <p>Trong HNO<sub>3</sub>, nguyên tử Nitrogen đạt mức oxi hóa cực đại là <strong>+5</strong>. Vì thế, HNO<sub>3</sub> có khả năng oxi hóa hầu hết các kim loại (trừ Vàng Au và Bạch kim Pt), nhiều phi kim và hợp chất.</p>
    
    <div class="box-warning" style="margin:10px 0;">
      <div class="box-title">🚨 NGUYÊN TẮC BẤT DI BẤT DỊCH KHI CHO KIM LOẠI + HNO3</div>
      <p><span class="hl-red">TUYỆT ĐỐI KHÔNG BAO GIỜ GIẢI PHÓNG KHÍ H<sub>2</sub>!</span></p>
      <p>Đứa nào viết kim loại + HNO<sub>3</sub> &rarr; muối + H<sub>2</sub> là giáo viên cho ăn điểm 0 tròn trĩnh ngay tại chỗ! H<sup>+</sup> không nhận e mà chính là thằng N<sup>+5</sup> nhận e để tạo ra các sản phẩm khử của Nitrogen!</p>
    </div>

    <p><strong>Bảng Sản Phẩm Khử Tùy Thuộc Nồng Độ Acid & Kim Loại:</strong></p>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Loại Dung Dịch HNO<sub>3</sub></th>
            <th>Sản Phẩm Khử Chủ Yếu</th>
            <th>Màu Sắc & Đặc Điểm Cần Nhớ</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>HNO<sub>3</sub> ĐẶC</strong></td>
            <td><strong>Khí NO<sub>2</sub></strong> (Nitrogen dioxide)</td>
            <td>Khí có <strong style="color:var(--accent-red);">màu nâu đỏ</strong>, mùi xốc, cực độc.</td>
          </tr>
          <tr>
            <td><strong>HNO<sub>3</sub> LOÃNG</strong></td>
            <td><strong>Khí NO</strong> (Nitrogen monoxide)</td>
            <td>Khí <strong>không màu, hóa nâu đỏ</strong> ngay ngoài không khí.</td>
          </tr>
          <tr>
            <td><strong>HNO<sub>3</sub> RẤT LOÃNG</strong><br><small>(khi tác dụng với kim loại mạnh: Mg, Al, Zn)</small></td>
            <td>
              &bull; <strong>N<sub>2</sub>O:</strong> Khí cười, không màu, ngọt.<br>
              &bull; <strong>N<sub>2</sub>:</strong> Khí không màu, không mùi.<br>
              &bull; <strong>NH<sub>4</sub>NO<sub>3</sub>:</strong> <span class="hl-red">DẠNG MUỐI TAN TRONG DUNG DỊCH, KHÔNG CÓ KHÍ THOÁT RA! (Bẫy chết người)</span>
            </td>
            <td>Đề bài bảo "cho Mg vào HNO<sub>3</sub> loãng thu được dung dịch X và <em>không có khí thoát ra</em>" &rarr; Biết ngay sản phẩm là muối <strong>NH<sub>4</sub>NO<sub>3</sub></strong>!</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p style="margin-top:10px;"><strong>Các Phương Trình Phải Khắc Sâu Vào Tủy Sống:</strong></p>
    <div class="reaction-box">
      &bull; Với Cu (đồng kim loại đỏ) + HNO<sub>3</sub> ĐẶC &rarr; dung dịch xanh lam + khí nâu đỏ:
      <br><strong>Cu + 4HNO<sub>3</sub>(đặc) &rarr; Cu(NO<sub>3</sub>)<sub>2</sub> + 2NO<sub>2</sub>&uarr; + 2H<sub>2</sub>O</strong>
      <br>&bull; Với Cu + HNO<sub>3</sub> LOÃNG &rarr; khí không màu hóa nâu:
      <br><strong>3Cu + 8HNO<sub>3</sub>(loãng) &rarr; 3Cu(NO<sub>3</sub>)<sub>2</sub> + 2NO&uarr; + 4H<sub>2</sub>O</strong>
      <br>&bull; Với Fe (luôn đẩy sắt lên hóa trị cao nhất là Fe<sup>3+</sup>!):
      <br><strong>Fe + 4HNO<sub>3</sub>(loãng) &rarr; Fe(NO<sub>3</sub>)<sub>3</sub> + NO&uarr; + 2H<sub>2</sub>O</strong> (Không bao giờ ra Fe<sup>2+</sup> nếu acid dư!)
    </div>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 BẪY THỤ ĐỘNG HÓA KIM LOẠI (CỰC HAY XUẤT HIỆN TRONG ĐỀ THI)</div>
    <p>Ba kim loại sau đây: <strong>Fe (Sắt), Al (Nhôm), Cr (Chromium)</strong>:</p>
    <p style="font-size:1.05rem;font-weight:700;color:var(--accent-red);text-align:center;margin:8px 0;">
      BỊ THỤ ĐỘNG HÓA TRONG DUNG DỊCH HNO<sub>3</sub> ĐẶC, NGUỘI!
    </p>
    <p><em>Hiện tượng:</em> Khi nhúng thanh sắt hoặc nhôm vào axit nitric đặc nguội, trên bề mặt kim loại lập tức hình thành một màng oxit cực kì mỏng, đặc khít và bền vững, ngăn không cho kim loại tiếp xúc tiếp với acid &rarr; Phản ứng lập tức dừng lại, kim loại không bị tan ra!</p>
    <p><em>Ứng dụng:</em> Người ta có thể dùng <strong>thùng bằng nhôm (Al) hoặc thép (Fe) để đựng và chuyên chở axit HNO<sub>3</sub> đặc nguội</strong> mà không sợ bị ăn mòn thủng bồn chứa!</p>
  </div>

  <!-- GÓC HỒI TƯỞNG LỚP 10 BÀI 6 -->
  <div class="accordion-item" style="margin:20px 0;">
    <button class="accordion-trigger" onclick="toggleAcc(this)">
      <span>🟣 <strong>KÝ ỨC ÙA VỀ (Cứu Nạn Lớp 10): Định Luật Bảo Toàn Electron Của Phản Ứng Oxi Hóa Khử</strong></span>
      <span class="acc-icon">▼</span>
    </button>
    <div class="accordion-content">
      <div class="accordion-inner">
        <div class="box box-recall">
          <div class="box-title">💡 Tuyệt Kĩ Giải Nhanh Bài Toán Kim Loại Tác Dụng HNO3</div>
          <p>Mày đéo cần cân bằng phương trình hóa học dài dằng dặc làm gì cho mệt óc. Chỉ cần nhớ định luật bảo toàn e của lớp 10:</p>
          <div class="formula-display" style="color:var(--accent-purple);">
            &sum; n<sub>e nhường</sub> = &sum; n<sub>e nhận</sub>
          </div>
          <ul class="content-list">
            <li>Kim loại nhường e: n<sub>e nhường</sub> = n<sub>KL</sub> &times; (hóa trị của kim loại: Na&times;1, Mg&times;2, Cu&times;2, Al&times;3, Fe&times;3...).</li>
            <li>Sản phẩm khử nhận e từ N<sup>+5</sup>:
              <br>&bull; N<sup>+5</sup> + 1e &rarr; N<sup>+4</sup> (NO<sub>2</sub>) &rArr; n<sub>e nhận</sub> = <strong>1 &times; n<sub>NO<sub>2</sub></sub></strong>
              <br>&bull; N<sup>+5</sup> + 3e &rarr; N<sup>+2</sup> (NO) &rArr; n<sub>e nhận</sub> = <strong>3 &times; n<sub>NO</sub></strong>
              <br>&bull; 2N<sup>+5</sup> + 8e &rarr; 2N<sup>+1</sup> (N<sub>2</sub>O) &rArr; n<sub>e nhận</sub> = <strong>8 &times; n<sub>N<sub>2</sub>O</sub></strong>
              <br>&bull; 2N<sup>+5</sup> + 10e &rarr; N<sub>2</sub><sup>0</sup> &rArr; n<sub>e nhận</sub> = <strong>10 &times; n<sub>N<sub>2</sub></sub></strong>
              <br>&bull; N<sup>+5</sup> + 8e &rarr; N<sup>-3</sup> (NH<sub>4</sub>NO<sub>3</sub>) &rArr; n<sub>e nhận</sub> = <strong>8 &times; n<sub>NH<sub>4</sub>NO<sub>3</sub></sub></strong>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- COMBO HỦY DIỆT BÀI 6 -->
  <div class="box box-combo">
    <div class="box-title">💥 2 CÔNG THỨC COMBO GIẢI SIÊU TỐC BÀI TOÁN HNO3 TRONG 15 GIÂY</div>
    <p><strong>Dấu hiệu nhận biết:</strong> Đề bài cho kim loại tác dụng HNO<sub>3</sub> sinh ra hỗn hợp khí (NO, NO<sub>2</sub>...), hỏi lượng axit HNO<sub>3</sub> đã phản ứng hoặc khối lượng muối nitrate thu được sau khi cô cạn dung dịch.</p>
    
    <div class="formula-display">
      n<sub>HNO<sub>3</sub> phản ứng</sub> = 2n<sub>NO<sub>2</sub></sub> + 4n<sub>NO</sub> + 10n<sub>N<sub>2</sub>O</sub> + 12n<sub>N<sub>2</sub></sub> + 10n<sub>NH<sub>4</sub>NO<sub>3</sub></sub> + 2n<sub>O (trong oxit nếu có)</sub>
    </div>
    <div class="formula-label">Hệ số thần thánh: NO2 đi với 2, NO đi với 4, N2O đi với 10, N2 đi với 12!</div>

    <div class="formula-display" style="margin-top:12px;">
      m<sub>muối nitrate</sub> = m<sub>kim loại</sub> + 62 &times; (&sum; n<sub>e trao đổi</sub>)
    </div>
    <div class="formula-label">Trong đó 62 là gốc NO3- (14 + 16&times;3 = 62); &sum; ne = n_NO2 + 3n_NO + 8n_N2O + 10n_N2</div>
  </div>

  <!-- SƠ ĐỒ TƯ DUY MINDMAP BÀI 6 -->
  <h3 class="sec-title">4. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Bài 6</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">HỢP CHẤT CỦA NITROGEN VỚI OXYGEN & HNO3 (BÀI 6)</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-red);">1. MƯA ACID</h5>
        <ul>
          <li>Nguyên nhân: Khí NOx và SO2</li>
          <li>Tạo HNO3 và H2SO4 trong mây</li>
          <li>pH &lt; 5,6 &rarr; Ăn mòn, tàn phá rừng</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-green);">2. PHÚ DƯỠNG</h5>
        <ul>
          <li>Dư thừa N (NO3-) và P (PO4 3-)</li>
          <li>Tảo nở hoa &rarr; Tảo chết</li>
          <li>Vi khuẩn hút cạn Oxy &rarr; Cá chết</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">3. HNO3 OXI HÓA MẠNH</h5>
        <ul>
          <li>N(+5) oxi hóa hầu hết kim loại</li>
          <li>Đặc &rarr; Khí NO2 (Nâu đỏ)</li>
          <li>Loãng &rarr; Khí NO (Không màu hóa nâu)</li>
          <li>TUYỆT ĐỐI không sinh ra H2!</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-purple);">4. THỤ ĐỘNG HÓA</h5>
        <ul>
          <li>Fe, Al, Cr bị thụ động</li>
          <li>Chỉ trong HNO3 ĐẶC NGUỘI</li>
          <li>Tạo màng oxit bảo vệ kim loại</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- THỰC CHIẾN STEP BY STEP BÀI 6 (2 BÀI MẪU) -->
  <h3 class="sec-title">5. Thực Chiến: 2 Bài Tập Mẫu Kim Loại + HNO3 Step-by-Step</h3>

  <!-- BÀI MẪU 1 -->
  <div class="step-solver">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 1: Cu Tác Dụng HNO3 Loãng (Tính Thể Tích Khí & Lượng Axit)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Cho 3,84 gam kim loại Cu tác dụng hoàn toàn với dung dịch HNO<sub>3</sub> loãng dư, thu được V lít khí NO (sản phẩm khử duy nhất ở đkc).
      <br>a) Tính thể tích khí NO thu được (V).
      <br>b) Tính số mol HNO<sub>3</sub> đã tham gia phản ứng.</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi dữ kiện & Đổi số mol</strong>
          <p>&bull; m<sub>Cu</sub> = 3,84 gam &rArr; n<sub>Cu</sub> = 3,84 / 64 = <strong>0,06 mol</strong>.
          <br>&bull; Cu tan trong HNO<sub>3</sub> nhường 2e: Cu &rarr; Cu<sup>2+</sup> + 2e.
          <br>&bull; Khí sinh ra là NO (N<sup>+5</sup> + 3e &rarr; N<sup>+2</sup>).</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Dùng bảo toàn electron tìm số mol NO</strong>
          <p>&bull; &sum; n<sub>e nhường</sub> = 2 &times; n<sub>Cu</sub> = 2 &times; 0,06 = 0,12 mol.
          <br>&bull; &sum; n<sub>e nhận</sub> = 3 &times; n<sub>NO</sub>
          <br>&bull; Theo ĐLBT electron: 3 &times; n<sub>NO</sub> = 0,12 &rArr; <strong>n<sub>NO</sub> = 0,12 / 3 = 0,04 mol</strong>.
          <br>&bull; Thể tích khí NO (đkc): V = 0,04 &times; 24,79 = <strong>0,9916 lít</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tại sao lôi công thức combo ra xài mà đéo ngồi cân bằng phương trình?</strong>
          <p>Vì cân bằng phương trình oxi hóa khử mất tới 1-2 phút bấm máy, trong khi công thức combo <strong>n<sub>HNO<sub>3</sub></sub> = 4 &times; n<sub>NO</sub></strong> giải quyết trong đúng 3 giây:</p>
          <div class="formula-display" style="font-size:0.95rem;">
            n<sub>HNO<sub>3</sub> phản ứng</sub> = 4 &times; 0,04 = 0,16 mol
          </div>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ: V<sub>NO</sub> = 0,9916 Lít &nbsp;|&nbsp; n<sub>HNO<sub>3</sub></sub> = 0,16 mol</strong>
        <p><em>Lời gia sư bình phẩm:</em> Thấy tốc độ của bảo toàn electron và công thức combo chưa? Đứa nào ngồi cân bằng 3Cu + 8HNO3 thì bạn bè đã làm xong sang câu khác rồi!</p>
      </div>
    </div>
  </div>

  <!-- BÀI MẪU 2 -->
  <div class="step-solver" style="margin-top:16px;">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 2: Hỗn Hợp Kim Loại Tác Dụng HNO3 &ndash; Tính Khối Lượng Muối Trong 15 Giây</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Hòa tan hoàn toàn 5,4 gam hỗn hợp gồm Mg và Al vào dung dịch HNO<sub>3</sub> loãng dư, thu được 4,958 lít khí NO (sản phẩm khử duy nhất ở đkc). Cô cạn cẩn thận dung dịch sau phản ứng thu được m gam muối khan. Hãy tính giá trị của m.</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bẫy thiếu dữ kiện</strong>
          <p>&bull; Đề bài cho 2 kim loại Mg và Al nhưng chỉ cho 1 con số khối lượng tổng (5,4g) và 1 lượng khí NO.
          <br>&bull; <span class="hl-red">BẪY TÂM LÝ:</span> Học sinh thường cố gắng đặt ẩn x, y lập hệ phương trình rồi hoảng loạn vì thiếu phương trình thứ 2!
          <br>&bull; Tư duy cao thủ: Đề hỏi khối lượng muối = m<sub>KL</sub> + m<sub>gốc NO<sub>3</sub><sup>&minus;</sup> trong muối</sub>. Mà số mol NO<sub>3</sub><sup>&minus;</sup> tạo muối chính bằng số mol electron trao đổi!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tính số mol electron trao đổi từ khí NO</strong>
          <p>&bull; n<sub>NO</sub> = 4,958 / 24,79 = <strong>0,2 mol</strong>.
          <br>&bull; N<sup>+5</sup> + 3e &rarr; NO &rArr; &sum; n<sub>e trao đổi</sub> = 3 &times; n<sub>NO</sub> = 3 &times; 0,2 = <strong>0,6 mol</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Ốp thẳng combo tính muối siêu tốc</strong>
          <p>Áp dụng công thức combo thần thánh: <strong>m<sub>muối</sub> = m<sub>KL</sub> + 62 &times; (&sum; n<sub>e</sub>)</strong>:</p>
          <div class="formula-display" style="font-size:0.95rem;">
            m<sub>muối</sub> = 5,4 + 62 &times; 0,6 = 5,4 + 37,2 = 42,6 gam
          </div>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ CHÍNH XÁC: m = 42,6 gam</strong>
        <p><em>Lời gia sư bình phẩm:</em> 15 giây bấm máy tính là xong một câu điểm 8+ trong đề thi THPT! Nhớ kĩ số 62 là khối lượng mol của gốc NO3- nhé!</p>
      </div>
    </div>
  </div>

  <!-- BÀI KIỂM TRA 15 CÂU BÀI 6 -->
  <div class="quiz-section" id="b6-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">Bài Kiểm Tra Kiến Thức Bài 6: Hợp Chất Oxygen Của N & HNO<sub>3</sub></div>
        <div class="quiz-sub">Gồm 8 câu trắc nghiệm + 4 câu đúng/sai + 3 câu tự luận</div>
      </div>
      <div class="quiz-score-badge" id="b6-score">Điểm: 0/15</div>
    </div>

    <!-- TRẮC NGHIỆM 1-8 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Mưa acid là hiện tượng nước mưa có giá trị pH bằng bao nhiêu?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q1" value="A"> A. pH &gt; 7</label>
        <label class="quiz-option"><input type="radio" name="b6_q1" value="B"> B. pH &lt; 5,6</label>
        <label class="quiz-option"><input type="radio" name="b6_q1" value="C"> C. pH = 7</label>
        <label class="quiz-option"><input type="radio" name="b6_q1" value="D"> D. pH từ 6,0 đến 7,0</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Nước mưa tự nhiên có pH &approx; 5,6 do hòa tan CO2. Khi bị nhiễm acid mạnh (HNO3, H2SO4) làm pH &lt; 5,6 thì gọi là mưa acid. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 2 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hiện tượng phú dưỡng (eutrophication) trong các thủy vực ao hồ chủ yếu do sự dư thừa của các nguyên tố dinh dưỡng nào?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q2" value="A"> A. Carbon (C) và Hydrogen (H)</label>
        <label class="quiz-option"><input type="radio" name="b6_q2" value="B"> B. Sắt (Fe) và Đồng (Cu)</label>
        <label class="quiz-option"><input type="radio" name="b6_q2" value="C"> C. Sodium (Na) và Chlorine (Cl)</label>
        <label class="quiz-option"><input type="radio" name="b6_q2" value="D"> D. Nitrogen (N) và Phosphorus (P)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Dư thừa ion nitrate (chứa N) và phosphate (chứa P) kích thích rong tảo bùng phát gây phú dưỡng. Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 3 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Kim loại nào sau đây bị THỤ ĐỘNG HÓA trong dung dịch HNO<sub>3</sub> đặc, nguội?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q3" value="A"> A. Fe (Sắt)</label>
        <label class="quiz-option"><input type="radio" name="b6_q3" value="B"> B. Cu (Đồng)</label>
        <label class="quiz-option"><input type="radio" name="b6_q3" value="C"> C. Mg (Magnesium)</label>
        <label class="quiz-option"><input type="radio" name="b6_q3" value="D"> D. Ag (Bạc)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Fe, Al, Cr bị thụ động hóa trong HNO3 đặc nguội (tạo màng oxit bảo vệ). Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 4 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Cho kim loại Cu tác dụng với dung dịch HNO<sub>3</sub> đặc, khí sinh ra có màu gì và là khí gì?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q4" value="A"> A. Khí H<sub>2</sub> không màu, cháy nổ.</label>
        <label class="quiz-option"><input type="radio" name="b6_q4" value="B"> B. Khí NO không màu, hóa nâu trong không khí.</label>
        <label class="quiz-option"><input type="radio" name="b6_q4" value="C"> C. Khí NO<sub>2</sub> màu nâu đỏ, mùi xốc độc hại.</label>
        <label class="quiz-option"><input type="radio" name="b6_q4" value="D"> D. Khí N<sub>2</sub> không màu, không mùi.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Cu + 4HNO3(đặc) &rarr; Cu(NO3)2 + 2NO2&uarr;(nâu đỏ) + 2H2O. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Dung dịch HNO<sub>3</sub> đặc để lâu ngày trong phòng thí nghiệm thường chuyển sang màu vàng là do:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q5" value="A"> A. Bị hấp thụ bụi bẩn từ môi trường.</label>
        <label class="quiz-option"><input type="radio" name="b6_q5" value="B"> B. Bị phân hủy chậm bởi ánh sáng tạo ra khí NO<sub>2</sub> màu nâu đỏ tan lại vào dung dịch.</label>
        <label class="quiz-option"><input type="radio" name="b6_q5" value="C"> C. Tác dụng với vỏ chai thủy tinh.</label>
        <label class="quiz-option"><input type="radio" name="b6_q5" value="D"> D. Bị bay hơi mất nước.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> 4HNO3 &rarr; 4NO2 + O2 + 2H2O. Khí NO2 sinh ra tan trong dung dịch làm acid chuyển màu vàng. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 6 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Kim loại nào sau đây KHÔNG tan được trong dung dịch HNO<sub>3</sub> (kể cả đặc nóng)?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q4" value="A"> A. Vàng (Au) và Bạch kim (Pt)</label>
        <label class="quiz-option"><input type="radio" name="b6_q6" value="B"> B. Bạc (Ag) và Đồng (Cu)</label>
        <label class="quiz-option"><input type="radio" name="b6_q6" value="C"> C. Sắt (Fe) và Kẽm (Zn)</label>
        <label class="quiz-option"><input type="radio" name="b6_q6" value="D"> D. Nhôm (Al) và Chì (Pb)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Au và Pt là kim loại quý trơ, không tác dụng với HNO3 (chỉ tan trong nước cường toan - hỗn hợp 3 HCl : 1 HNO3). Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 7 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Khi cho Fe tác dụng với dung dịch HNO<sub>3</sub> loãng dư, sản phẩm thu được chứa muối sắt mang số oxi hóa nào?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q7" value="A"> A. Fe<sup>0</sup></label>
        <label class="quiz-option"><input type="radio" name="b6_q7" value="B"> B. Fe<sup>+2</sup> (Fe(NO<sub>3</sub>)<sub>2</sub>)</label>
        <label class="quiz-option"><input type="radio" name="b6_q7" value="C"> C. Hỗn hợp Fe<sup>+2</sup> và Fe<sup>+3</sup></label>
        <label class="quiz-option"><input type="radio" name="b6_q7" value="D"> D. Fe<sup>+3</sup> (Fe(NO<sub>3</sub>)<sub>3</sub>)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> HNO3 có tính oxi hóa rất mạnh, nếu acid dư thì Fe luôn bị đẩy lên mức oxi hóa cao nhất là Fe(+3). Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 8 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hòa tan hoàn toàn 0,1 mol Fe vào dung dịch HNO<sub>3</sub> loãng dư, sản phẩm khử duy nhất là NO. Số mol khí NO thu được là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b6_q8" value="A"> A. 0,3 mol</label>
        <label class="quiz-option"><input type="radio" name="b6_q8" value="B"> B. 0,2 mol</label>
        <label class="quiz-option"><input type="radio" name="b6_q8" value="C"> C. 0,1 mol</label>
        <label class="quiz-option"><input type="radio" name="b6_q8" value="D"> D. 0,05 mol</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Fe &rarr; Fe3+ + 3e &rArr; ne nhường = 3 &times; 0,1 = 0,3 mol. N+5 + 3e &rarr; NO &rArr; n_NO = ne nhường / 3 = 0,3 / 3 = 0,1 mol. Chọn C.</div>
    </div>

    <!-- ĐÚNG SAI 9-12 -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 9 (Đúng / Sai)</div>
      <div class="quiz-q-text">Khi cho kim loại kẽm (Zn) tác dụng với dung dịch HNO<sub>3</sub> loãng, khí sinh ra là H<sub>2</sub>.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI BÉT!</strong> HNO3 là acid có tính oxi hóa mạnh, không bao giờ giải phóng H2 mà tạo ra các sản phẩm khử của N như NO, N2O, N2 hoặc NH4NO3.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 10 (Đúng / Sai)</div>
      <div class="quiz-q-text">Người ta có thể dùng các thùng bằng nhôm (Al) hoặc sắt (Fe) để chuyên chở dung dịch axit nitric (HNO<sub>3</sub>) đặc, nguội.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> Do hiện tượng thụ động hóa tạo màng oxit bảo vệ bề mặt Fe và Al, không phản ứng với HNO3 đặc nguội.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 (Đúng / Sai)</div>
      <div class="quiz-q-text">Tảo nở hoa trong hiện tượng phú dưỡng làm giảm nghiêm trọng lượng oxy hòa tan trong nước, dẫn đến việc cá tôm chết ngạt hàng loạt.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> Vi khuẩn tiêu thụ lượng lớn O2 để phân hủy xác tảo khiến nước cạn kiệt oxy.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 (Đúng / Sai)</div>
      <div class="quiz-q-text">Mưa acid chỉ làm hư hỏng tượng đá chứ không gây ảnh hưởng gì đến sinh trưởng của cây cối trong rừng.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Mưa acid làm chua đất, rửa trôi dinh dưỡng và hòa tan ion Al3+ độc hại làm cháy lá và chết rụi cả cánh rừng.</div>
    </div>

    <!-- TỰ LUẬN 13-15 -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 13 (Tự luận thực tế)</div>
      <div class="quiz-q-text">Hãy giải thích tại sao ở các vùng nông thôn hay đô thị, việc xả trực tiếp nước giặt quần áo (chứa chất tẩy rửa phosphate) và nước phân chuồng gia súc chưa qua xử lí xuống ao hồ lại là nguyên nhân chính gây ra thảm họa phú dưỡng? Đề xuất 2 biện pháp khắc phục.</div>
      <textarea placeholder="Trình bày nguyên nhân và giải pháp..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>1. <strong>Nguyên nhân:</strong> Bột giặt chứa hợp chất của phosphorus (ion PO<sub>4</sub><sup>3&minus;</sup>) và phân chuồng chứa nhiều hợp chất hữu cơ của nitrogen (ion NO<sub>3</sub><sup>&minus;</sup>, NH<sub>4</sub><sup>+</sup>). Khi xả thẳng xuống ao, hai nguyên tố này làm môi trường nước bị thừa dinh dưỡng trầm trọng, kích hoạt quá trình bùng nổ tảo lục và gây hiện tượng phú dưỡng.
        <br>2. <strong>Hai biện pháp khắc phục:</strong>
        <br>&bull; Xây dựng hệ thống xử lí nước thải sinh hoạt và bể biogas xử lí phân gia súc trước khi thải ra nguồn nước tự nhiên.
        <br>&bull; Sử dụng các loại bột giặt sinh học không chứa hợp chất photphat (phosphate-free detergent).
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 (Tự luận tính toán tổng hợp)</div>
      <div class="quiz-q-text">Hòa tan hoàn toàn 1,92 gam kim loại Cu vào một lượng vừa đủ dung dịch HNO<sub>3</sub> thu được V lít khí NO<sub>2</sub> (sản phẩm khử duy nhất ở đkc).
      <br>a) Tính thể tích khí NO<sub>2</sub> thu được ở đkc.
      <br>b) Tính khối lượng muối Cu(NO<sub>3</sub>)<sub>2</sub> thu được khi cô cạn dung dịch sau phản ứng.</div>
      <textarea placeholder="Nháp bài toán Cu + HNO3 đặc..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>&bull; Số mol Cu: n<sub>Cu</sub> = 1,92 / 64 = 0,03 mol.
        <br>&bull; Phương trình: Cu + 4HNO<sub>3</sub> &rarr; Cu(NO<sub>3</sub>)<sub>2</sub> + 2NO<sub>2</sub>&uarr; + 2H<sub>2</sub>O
        <br>&bull; a) Số mol NO<sub>2</sub>: n<sub>NO<sub>2</sub></sub> = 2 &times; n<sub>Cu</sub> = 2 &times; 0,03 = 0,06 mol.
        <br>&nbsp;&nbsp;&nbsp;&nbsp;Thể tích khí NO<sub>2</sub> (đkc): V = 0,06 &times; 24,79 = <strong>1,4874 lít</strong>.
        <br>&bull; b) Số mol muối Cu(NO<sub>3</sub>)<sub>2</sub> = n<sub>Cu</sub> = 0,03 mol.
        <br>&nbsp;&nbsp;&nbsp;&nbsp;Khối lượng muối: m = 0,03 &times; 188 = <strong>5,64 gam</strong>.
        <br><em>(Cách 2 dùng combo: m_muối = m_KL + 62 &times; n_e = 1,92 + 62 &times; 0,06 = 5,64 g).</em>
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 (Tự luận phân tích)</div>
      <div class="quiz-q-text">Cho ba mẫu kim loại riêng biệt: Fe, Cu, Ag vào ba ống nghiệm chứa dung dịch HNO<sub>3</sub> đặc, nguội. Hãy nêu hiện tượng xảy ra ở từng ống nghiệm và giải thích ngắn gọn.</div>
      <textarea placeholder="Nêu hiện tượng và viết phương trình nếu có..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>1. <strong>Ống nghiệm chứa Fe:</strong> Không có hiện tượng gì xảy ra, Fe không bị tan do Fe bị <em>thụ động hóa</em> trong HNO<sub>3</sub> đặc nguội.
        <br>2. <strong>Ống nghiệm chứa Cu:</strong> Kim loại Cu tan dần, dung dịch từ không màu chuyển sang màu xanh lam của Cu(NO<sub>3</sub>)<sub>2</sub>, có bọt khí màu nâu đỏ (NO<sub>2</sub>) mùi xốc sủi lên:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>Cu + 4HNO<sub>3</sub>(đặc) &rarr; Cu(NO<sub>3</sub>)<sub>2</sub> + 2NO<sub>2</sub>&uarr; + 2H<sub>2</sub>O</code>
        <br>3. <strong>Ống nghiệm chứa Ag:</strong> Kim loại Ag tan dần, tạo dung dịch không màu AgNO<sub>3</sub> và sủi bọt khí màu nâu đỏ (NO<sub>2</sub>):
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>Ag + 2HNO<sub>3</sub>(đặc) &rarr; AgNO<sub>3</sub> + NO<sub>2</sub>&uarr; + H<sub>2</sub>O</code>
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b6')">📊 Nộp Bài & Chấm Điểm Bài 6</button>
  </div>
</section>
"""
