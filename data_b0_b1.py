# -*- coding: utf-8 -*-
"""
Module data_b0_b1.py - NÂNG CẤP TOÀN DIỆN
- Bổ sung Thẻ Lật Flashcard Tương Tác
- Bổ sung Sơ Đồ Tư Duy Mindmap Trực Quan Cho Bài 1
- Bổ sung Bài Tập Thực Chiến Mẫu Số 2 (Dự đoán Le Chatelier) Chuẩn 3 Bước
- Đổi nút bấm: "🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!"
"""

B0_CONTENT = """
<!-- ========================================== -->
<!-- TẦNG 0: NỀN TẢNG MẤT GỐC - HỒI SINH HÓA 10 -->
<!-- ========================================== -->
<section id="b0" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number" style="background: linear-gradient(135deg, #7c4dff, #b388ff);">00</div>
    <div class="lesson-meta">
      <h2>Tầng 0: Cấp Cứu Mất Gốc – Hồi Sinh Trước Khi Học Lớp 11</h2>
      <div class="lesson-sub">Những thứ bắt buộc phải nhớ từ Hóa 10, không nhớ thì học lớp 11 như vịt nghe sấm!</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Số mol</span>
        <span class="lesson-tag">Nồng độ CM</span>
        <span class="lesson-tag">ĐKC 24.79</span>
        <span class="lesson-tag">Số oxi hóa</span>
        <span class="lesson-tag">Khử cho - O nhận</span>
      </div>
    </div>
  </div>

  <div class="box box-story">
    <div class="box-title">💬 Lời Tâm Sự Của Gia Sư Dành Cho Dân Mất Gốc</div>
    <p>Chào người anh em! Tao biết mày đang hoang mang tột độ khi mở sách Hóa 11 ra: toàn cái mẹ gì mà <span class="tooltip" data-tip="Hằng số cân bằng hóa học, chỉ tính nồng độ chất khí và chất tan trong dung dịch">Kc</span>, <span class="tooltip" data-tip="Độ chua/kiềm của dung dịch, tính bằng trừ logarit của nồng độ ion H+">pH</span>, <span class="tooltip" data-tip="Phản ứng chạy cả 2 chiều thuận và nghịch cùng lúc">thuận nghịch</span>, <span class="tooltip" data-tip="Quá trình chất tan rã thành các hạt ion mang điện tích trong nước">sự điện li</span>, <span class="tooltip" data-tip="Tập hợp các chất gồm N2O, NO, NO2, N2O4... tạo ra mưa acid">NOx</span>... Đừng có sợ! Bản chất môn Hóa cấp 3 nó giống như xây nhà: mày chưa có móng lớp 10 thì xây tầng 11 kiểu gì chả sập.</p>
    <p>Ở Tầng 0 này, tao sẽ nhét lại vào đầu mày 4 món "vũ khí tối thượng" của lớp 10 bằng thứ tiếng người bình dân nhất. Mày chỉ cần đọc hết 10 phút là tự tin bước vào bài 1 ngang cơ với lũ bạn!</p>
  </div>

  <h3 class="sec-title">1. Số Mol (n) – "Đơn Vị Đếm" Của Thế Giới Hóa Học</h3>
  <div class="box box-theory">
    <div class="box-title">📘 Dịch Sang Tiếng Người</div>
    <p>Nguyên tử nó nhỏ li ti như hạt cát giữa sa mạc, mắt thường đéo bao giờ nhìn thấy được. Chẳng lẽ đi cân 1 nguyên tử Fe? Không ai làm thế cả!</p>
    <p>Người ta gom <strong>6,022 &times; 10<sup>23</sup></strong> hạt lại thành 1 bó, đặt tên cái bó đó là <strong>1 MOL</strong> (giống như ở ngoài chợ mày mua 1 chục trứng = 10 quả, 1 tá bút chì = 12 cây vậy). Cứ nhớ: <strong>1 mol = 1 bó siêu to khổng lồ</strong>.</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 Bộ 3 Công Thức Tính Mol Sống Còn</div>
    <div class="formula-display">
      n = m / M  (mol)
    </div>
    <div class="formula-label">Áp dụng khi đề bài cho khối lượng (gam)</div>
    <ul class="content-list">
      <li><strong>m:</strong> Khối lượng chất tan (đơn vị: <strong>gam</strong> - nếu đề cho kg thì nhân 1000).</li>
      <li><strong>M:</strong> Khối lượng mol (Phân tử khối, tra bảng tuần hoàn: H=1, C=12, N=14, O=16, Na=23, S=32, Cl=35.5, Fe=56, Cu=64...).</li>
    </ul>

    <div class="formula-display" style="margin-top:16px;">
      n = C<sub>M</sub> &times; V  (mol)
    </div>
    <div class="formula-label">Áp dụng khi đề bài cho Dung dịch lỏng</div>
    <ul class="content-list">
      <li><strong>C<sub>M</sub> (hay ghi tắt là M):</strong> Nồng độ mol (mol/L) - biểu thị 1 lít dung dịch có bao nhiêu mol chất tan.</li>
      <li><strong>V:</strong> Thể tích dung dịch - <span class="hl-red">BẮT BUỘC PHẢI ĐỔI RA LÍT (L)</span>. Đề cho mL mà không chia cho 1000 là ăn đòn!</li>
    </ul>

    <div class="formula-display" style="margin-top:16px;">
      V<sub>khí (đkc)</sub> = n &times; 24,79  (Lít)  &rArr;  n = V / 24,79
    </div>
    <div class="formula-label">Áp dụng cho chất KHÍ ở Điều kiện chuẩn (25°C, 1 bar - SGK MỚI)</div>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 BẪY TỬ THẦN TỪ LỚP 10 MỚI (CỰC KỲ QUAN TRỌNG)</div>
    <p>Sách giáo khoa cũ ngày xưa dạy: V = n &times; 22,4 (ở 0°C, 1 atm). <strong>BỎ NGAY VÀ LUÔN!</strong></p>
    <p>Chương trình mới (GDPT 2018) dùng <strong>Điều kiện chuẩn (đkc) là 25°C và 1 bar</strong>, con số thần thánh bây giờ là <span class="hl-yellow"><strong>24,79</strong></span>. Đi thi đứa nào bấm 22,4 là ra đáp án bẫy trắc nghiệm của giám khảo và nhận điểm 0 ngay lập tức!</p>
  </div>

  <h3 class="sec-title">2. Số Oxi Hóa & Câu Thần Chú "Khử Cho – O Nhận"</h3>
  <div class="box box-theory">
    <div class="box-title">📘 Dịch Nghĩa Bản Chất</div>
    <p>Số oxi hóa là điện tích giả định của nguyên tử khi ta coi mọi liên kết đều là liên kết ion (thằng nào hút electron mạnh hơn thì giật lấy dấu âm, thằng bị cướp mang dấu dương).</p>
    <p>Quy tắc bất di bất dịch:</p>
    <ul class="content-list">
      <li>Đơn chất đứng 1 mình (như N<sub>2</sub>, O<sub>2</sub>, Cu, Fe, H<sub>2</sub>) &rarr; Số oxh luôn luôn bằng <strong>0</strong>.</li>
      <li>Trong hợp chất: Thằng <strong>H</strong> hầu như luôn là <strong>+1</strong>, thằng <strong>O</strong> hầu như luôn là <strong>-2</strong> (trừ một vài thằng dị hợm như H<sub>2</sub>O<sub>2</sub> thì O là -1).</li>
      <li>Kim loại kiềm (nhóm IA: Na, K, Li) luôn là <strong>+1</strong>; kiềm thổ (nhóm IIA: Mg, Ca, Ba) luôn là <strong>+2</strong>; Nhôm Al luôn là <strong>+3</strong>.</li>
      <li><strong>Tổng số oxi hóa trong 1 phân tử trung hòa điện BẮT BUỘC BẰNG 0.</strong></li>
      <li><strong>Tổng số oxi hóa trong 1 ion đa nguyên tử BẰNG ĐÚNG ĐIỆN TÍCH CỦA ION ĐÓ.</strong></li>
    </ul>
  </div>

  <div class="box box-story">
    <div class="box-title">💡 Mẹo Nhớ Bựa: Câu Thần Chú Bất Hủ Của Dân Chuyên Hóa</div>
    <div style="font-size:1.2rem;font-weight:800;color:var(--accent-yellow);text-align:center;margin:12px 0;">
      "KHỬ CHO – O NHẬN" &nbsp;|&nbsp; "TĂNG KHỬ – GIẢM O"
    </div>
    <ul class="content-list">
      <li><strong>Chất khử:</strong> Là thằng <em>CHO</em> electron &rarr; Mất âm thì nó <em>TĂNG</em> số oxi hóa lên (Quá trình này gọi là <em>sự oxi hóa</em> hay <em>quá trình oxi hóa</em>).</li>
      <li><strong>Chất oxi hóa:</strong> Là thằng <em>NHẬN</em> electron &rarr; Hút thêm âm thì nó <em>GIẢM</em> số oxi hóa xuống (Quá trình này gọi là <em>sự khử</em> hay <em>quá trình khử</em>).</li>
    </ul>
    <p style="margin-top:8px;"><em>Ví dụ bựa:</em> Mày cho đi tiền (cho e) &rarr; mày là người hào phóng (Chất khử), đẳng cấp uy tín của mày tăng lên (số oxh tăng). Thằng ăn cắp nhận tiền (nhận e) &rarr; nó là kẻ xấu (Chất oxi hóa), nhân phẩm nó giảm xuống (số oxh giảm)!</p>
  </div>

  <h3 class="sec-title">3. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Tầng 0</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">BẢO BỐI LỚP 10 DÙNG CHO LỚP 11</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-blue-light);">1. TÍNH SỐ MOL</h5>
        <ul>
          <li>Khối lượng: n = m / M</li>
          <li>Dung dịch: n = CM &times; V (L)</li>
          <li>Khí ĐKC: n = V / 24,79</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">2. NỒNG ĐỘ DUNG DỊCH</h5>
        <ul>
          <li>CM = n / V (mol/L)</li>
          <li>C% = (mct / mdd) &times; 100%</li>
          <li>Pha loãng: C1&times;V1 = C2&times;V2</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-green);">3. OXI HÓA - KHỬ</h5>
        <ul>
          <li>Khử cho (e) &rarr; Tăng số oxh</li>
          <li>O nhận (e) &rarr; Giảm số oxh</li>
          <li>Bảo toàn e: &sum; e nhường = &sum; e nhận</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-purple);">4. ĐIỆN TÍCH ION</h5>
        <ul>
          <li>Cation (+) mất e</li>
          <li>Anion (-) nhận e</li>
          <li>Dung dịch: &sum; điện tích + = &sum; điện tích -</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

B1_CONTENT = """
<!-- ========================================== -->
<!-- BÀI 1: KHÁI NIỆM VỀ CÂN BẰNG HÓA HỌC (SGK 6-15) -->
<!-- ========================================== -->
<section id="b1" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number">01</div>
    <div class="lesson-meta">
      <h2>Bài 1: Khái Niệm Về Cân Bằng Hóa Học</h2>
      <div class="lesson-sub">SGK Hóa học 11 – Kết Nối Tri Thức (Trang 6 đến trang 15)</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Phản ứng thuận nghịch</span>
        <span class="lesson-tag">Cân bằng động</span>
        <span class="lesson-tag">Hằng số Kc</span>
        <span class="lesson-tag">Nguyên lí Le Chatelier</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('sgk_b1_p06_07.png')">📖 Xem SGK Trang 6-7</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b1_p08_09.png')">📖 Xem SGK Trang 8-9</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b1_p10_11.png')">📖 Xem SGK Trang 10-11</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b1_p12_13.png')">📖 Xem SGK Trang 12-13</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b1_p14_15.png')">📖 Xem SGK Trang 14-15</button>
  </div>

  <!-- PHẦN 1: PHẢN ỨNG MỘT CHIỀU VÀ PHẢN ỨNG THUẬN NGHỊCH -->
  <h3 class="sec-title" id="b1-kn">1. Phản Ứng Một Chiều & Phản Ứng Thuận Nghịch</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch SGK Sang Tiếng Người (Băm Nát Định Nghĩa)</div>
    <p><strong>1. Phản ứng một chiều (&rarr;):</strong> Hiểu đơn giản là chiếc xe đứt phanh lao thẳng xuống vực thẳm. Nó chỉ chạy từ trái sang phải, các chất tham gia biến thành sản phẩm đến khi cạn kiệt thì dừng lại. Sản phẩm sinh ra <em>KHÔNG BAO GIỜ</em> thèm kết hợp lại với nhau để quay trở lại chất ban đầu trong cùng điều kiện.</p>
    <p><em>Kí hiệu:</em> Mũi tên đơn 1 chiều &rarr;</p>
    <div class="reaction-box">
      <span class="reactant">CH<sub>4</sub>(g) + 2O<sub>2</sub>(g)</span> <span class="arrow">&rarr;</span> <span class="product">CO<sub>2</sub>(g) + 2H<sub>2</sub>O(g)</span>
      <div style="font-size:0.8rem;color:var(--text-muted);">(Khí gas bật lửa đốt xong thành khói và hơi nước, đố mày gom khói lại bắt nó biến ngược thành gas được!)</div>
    </div>

    <p style="margin-top:14px;"><strong>2. Phản ứng thuận nghịch (&hArr;):</strong> Là mối quan hệ "yêu lại người yêu cũ". Trong cùng điều kiện, chất tham gia phản ứng với nhau tạo ra sản phẩm (gọi là <em>chiều thuận</em>), đồng thời các chất sản phẩm cũng phản ứng lại với nhau để tái sinh ra chất ban đầu (gọi là <em>chiều nghịch</em>).</p>
    <p><em>Kí hiệu:</em> Mũi tên 2 chiều &hArr; (gồm 2 nửa mũi tên ngược chiều nhau).</p>
    <div class="reaction-box">
      <span class="reactant">H<sub>2</sub>(g) + I<sub>2</sub>(g)</span> <span class="arrow">&hArr;</span> <span class="product">2HI(g)</span>
    </div>
  </div>

  <div class="box box-story">
    <div class="box-title">💡 Ví Dụ Bựa Để Não Mày Khắc Cốt Ghi Tâm</div>
    <p>Tưởng tượng mày đang cầm 1 cái xô múc nước đổ vào bể, nhưng đáy bể lại có một cái van rò rỉ đang xả nước ra ngoài. Mày đổ nước vào là <em>chiều thuận</em>, nước rò ra là <em>chiều nghịch</em>. Cả hai việc diễn ra cùng lúc song song. Mày không bao giờ làm cho cái xô cạn sạch được vì nước rò ra lại gom lại được một phần.</p>
    <p>Bởi vậy: <strong>Trong phản ứng thuận nghịch, hiệu suất ĐÉO BAO GIỜ ĐẠT ĐƯỢC 100%!</strong> Lúc nào trong bình cũng chứa cả chất ban đầu lẫn chất sản phẩm, không có thằng nào bị tiêu biến hoàn toàn.</p>
  </div>

  <div class="compare-grid">
    <div class="compare-card left">
      <h5>⚡ PHẢN ỨNG MỘT CHIỀU (&rarr;)</h5>
      <ul>
        <li>Chỉ xảy ra theo 1 chiều duy nhất từ trái sang phải.</li>
        <li>Chất tham gia hết sạch (nếu vừa đủ tỉ lệ).</li>
        <li>Hiệu suất có thể đạt tới 100%.</li>
        <li>Kí hiệu: Mũi tên một chiều &rarr;.</li>
      </ul>
    </div>
    <div class="compare-card right">
      <h5>🔄 PHẢN ỨNG THUẬN NGHỊCH (&hArr;)</h5>
      <ul>
        <li>Xảy ra đồng thời theo 2 chiều ngược nhau.</li>
        <li>Các chất tham gia KHÔNG BAO GIỜ hết sạch.</li>
        <li>Hiệu suất luôn luôn &lt; 100%.</li>
        <li>Kí hiệu: Hai nửa mũi tên ngược chiều &hArr;.</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN 2: TRẠNG THÁI CÂN BẰNG HÓA HỌC -->
  <h3 class="sec-title" id="b1-cb">2. Trạng Thái Cân Bằng Hóa Học – "Cân Bằng Động"</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch Định Nghĩa SGK (Trang 7)</div>
    <p>Lúc mới trộn các chất vào bình:</p>
    <ul class="content-list">
      <li>Ban đầu: Nồng độ chất phản ứng lớn nhất &rarr; Tốc độ phản ứng thuận (<strong>v<sub>t</sub></strong>) cực đại. Lúc này sản phẩm chưa có nên tốc độ nghịch (<strong>v<sub>n</sub></strong>) = 0.</li>
      <li>Theo thời gian: Chất phản ứng giảm dần &rarr; <strong>v<sub>t</sub> giảm dần</strong>. Sản phẩm sinh ra ngày càng nhiều &rarr; <strong>v<sub>n</sub> tăng dần</strong>.</li>
      <li>Đến một thời điểm định mệnh: Tốc độ thuận bằng đúng tốc độ nghịch!</li>
    </ul>
    <div class="formula-display" style="color:var(--accent-green);border-color:var(--accent-green);">
      v<sub>thuận</sub> = v<sub>nghịch</sub>
    </div>
    <p>Thời điểm này gọi là <strong>TRẠNG THÁI CÂN BẰNG HÓA HỌC</strong>.</p>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 BẪY THI TRẮC NGHIỆM: ĐỪNG NGHĨ LÀ NÓ ĐỨNG YÊN!</div>
    <p>Người ta gọi cân bằng hóa học là <strong>CÂN BẰNG ĐỘNG</strong> (Dynamic Equilibrium), nghĩa là tại trạng thái cân bằng:</p>
    <ul class="content-list">
      <li><span class="hl-red">Phản ứng KHÔNG HỀ DỪNG LẠI!</span> Phản ứng thuận và nghịch vẫn diễn ra liên tục với tốc độ vũ bão như nhau. Trong 1 giây có bao nhiêu phân tử sản phẩm sinh ra thì cũng có bấy nhiêu phân tử sản phẩm bị phá vỡ để trở lại chất ban đầu.</li>
      <li>Do tốc độ sinh ra = tốc độ mất đi, nên <strong>NỒNG ĐỘ CỦA TẤT CẢ CÁC CHẤT ĐƯỢC GIỮ NGUYÊN KHÔNG ĐỔI</strong>.</li>
      <li><strong>Bẫy đề thi:</strong> Nếu đề thi hỏi "Ở trạng thái cân bằng, nồng độ các chất phản ứng bằng nồng độ các chất sản phẩm" &rarr; <span class="hl-red">SAI BÉT!</span> Nồng độ các chất chỉ KHÔNG ĐỔI theo thời gian, chứ KHÔNG NHẤT THIẾT PHẢI BẰNG NHAU!</li>
    </ul>
  </div>

  <div class="box box-story">
    <div class="box-title">🏃 Ví Dụ Đời Thường: Thang Cuốn Ngược Chiều</div>
    <p>Mày chạy bộ lên trên một chiếc thang cuốn đang chạy trôi xuống dưới. Nếu tốc độ chân mày chạy lên bằng đúng tốc độ thang trôi xuống (v<sub>lên</sub> = v<sub>xuống</sub>), thì nhìn từ xa, người ta thấy mày đứng im tại một vị trí trong không gian. Nhưng thực tế mày có đứng im không? Đéo hề! Chân mày vẫn cắm đầu chạy thục mạng và thang cuốn vẫn trôi ầm ầm. Đó chính là bản chất của <strong>CÂN BẰNG ĐỘNG</strong>!</p>
  </div>

  <!-- PHẦN 3: HẰNG SỐ CÂN BẰNG Kc -->
  <h3 class="sec-title" id="b1-kc">3. Mổ Xẻ Tận Gốc Hằng Số Cân Bằng (K<sub>c</sub>)</h3>

  <div class="box box-formula">
    <div class="box-title">📐 Công Thức Tính Hằng Số Cân Bằng Kc (SGK Trang 8)</div>
    <p>Xét phản ứng thuận nghịch tổng quát ở thể khí hoặc dung dịch:</p>
    <div style="text-align:center;font-size:1.1rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">
      aA + bB &hArr; cC + dD
    </div>
    <div class="formula-display">
      K<sub>c</sub> = <span class="fraction"><span class="num">[C]<sup>c</sup> &times; [D]<sup>d</sup></span><span class="den">[A]<sup>a</sup> &times; [B]<sup>b</sup></span></span>
    </div>
    <div class="formula-label">Quy tắc vàng: TỬ SỐ LÀ SẢN PHẨM &ndash; MẪU SỐ LÀ CHẤT THAM GIA &ndash; HỆ SỐ LÀM SỐ MŨ</div>
    <ul class="content-list">
      <li><strong>[A], [B], [C], [D]:</strong> Nồng độ mol (mol/L) của các chất <em>TẠI THỜI ĐIỂM CÂN BẰNG</em> (không phải nồng độ ban đầu!).</li>
      <li><strong>a, b, c, d:</strong> Hệ số tỉ lượng trong phương trình hóa học đã được cân bằng chính xác.</li>
      <li><strong>Ý nghĩa của K<sub>c</sub>:</strong>
        <br>&bull; Nếu <strong>K<sub>c</sub> rất lớn (&gt;&gt; 1):</strong> Phản ứng thuận chiếm ưu thế áp đảo, nồng độ sản phẩm cực nhiều.
        <br>&bull; Nếu <strong>K<sub>c</sub> rất nhỏ (&lt;&lt; 1):</strong> Phản ứng nghịch chiếm ưu thế, phản ứng thuận hầu như không xảy ra được mấy.
      </li>
    </ul>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 2 BẪY TỬ THẦN KHI ỐP CÔNG THỨC Kc (HỌC SINH 90% DÍNH ĐÒN)</div>
    <p><strong>BẪY 1: CHẤT RẮN (SOLID) KHÔNG ĐƯỢC PHÉP XUẤT HIỆN TRONG BIỂU THỨC K<sub>c</sub>!</strong></p>
    <p>Nồng độ của chất rắn tinh khiết được coi là hằng số và được gộp thẳng vào hằng số K<sub>c</sub>. Đứa nào viết chất rắn vào là giáo viên gạch bài không thương tiếc!</p>
    <div class="reaction-box">
      Ví dụ: C(s) + CO<sub>2</sub>(g) &hArr; 2CO(g)
      <br><span style="color:var(--accent-green);">ĐÚNG:</span> <strong>K<sub>c</sub> = [CO]<sup>2</sup> / [CO<sub>2</sub>]</strong> (Bỏ qua C rắn hoàn toàn!)
      <br><span style="color:var(--accent-red);">SAI NGU:</span> K<sub>c</sub> = [CO]<sup>2</sup> / ([C] &times; [CO<sub>2</sub>]) &larr; VỨT ĐI!
    </div>
    <p style="margin-top:10px;"><strong>BẪY 2: K<sub>c</sub> CHỈ PHỤ THUỘC VÀO BẢN CHẤT PHẢN ỨNG VÀ NHIỆT ĐỘ (T)!</strong></p>
    <p>Dù mày có tăng áp suất, nhét thêm nồng độ, hay đổ cả tấn chất xúc tác vào thì giá trị số của <strong>K<sub>c</sub> VẪN GIỮ NGUYÊN KHÔNG ĐỔI</strong>, miễn là nhiệt độ không đổi! Chỉ khi nào MÀY THAY ĐỔI NHIỆT ĐỘ thì K<sub>c</sub> mới biến động.</p>
  </div>

  <!-- GÓC HỒI TƯỞNG LỚP 10 BÀI 1 -->
  <div class="accordion-item" style="margin:20px 0;">
    <button class="accordion-trigger" onclick="toggleAcc(this)">
      <span>🟣 <strong>KÝ ỨC ÙA VỀ (Cứu Nạn Lớp 10): Enthalpy Biến Thiên &Delta;<sub>r</sub>H&deg;<sub>298</sub> Là Cái Gì?</strong></span>
      <span class="acc-icon">▼</span>
    </button>
    <div class="accordion-content">
      <div class="accordion-inner">
        <div class="box box-recall">
          <div class="box-title">💡 Triệu Hồi Kiến Thức Bài 13 Lớp 10 Để Phục Vụ Le Chatelier</div>
          <p>Mượn tạm từ bài Năng lượng hóa học lớp 10 nhé, để tí nữa giải quyết vụ tăng giảm nhiệt độ ở Bài 1 này:</p>
          <ul class="content-list">
            <li><strong>&Delta;<sub>r</sub>H&deg;<sub>298</sub> &lt; 0 (Âm): PHẢN ỨNG TỎA NHIỆT.</strong> Phản ứng giải phóng năng lượng làm môi trường xung quanh nóng lên. <em>(Mẹo nhớ: Âm là nhả nhiệt ra).</em></li>
            <li><strong>&Delta;<sub>r</sub>H&deg;<sub>298</sub> &gt; 0 (Dương): PHẢN ỨNG THU NHIỆT.</strong> Phản ứng hút nhiệt làm môi trường xung quanh lạnh đi hoặc phải cấp nhiệt nó mới chịu chạy. <em>(Mẹo nhớ: Dương là húp nhiệt vào).</em></li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 4: NGUYÊN LÍ CHUYỂN DỊCH CÂN BẰNG LE CHATELIER -->
  <h3 class="sec-title" id="b1-lechatelier">4. Nguyên Lí Chuyển Dịch Cân Bằng Le Chatelier – "Hội Chứng Chống Đối"</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch Nguyên Lí Sang Tiếng Người (Bản Chất 100%)</div>
    <p>Nhà hóa học người Pháp Le Chatelier phát biểu một chân lí nghe rất hàn lâm, nhưng tao dịch sang tiếng chợ búa cho mày dễ hiểu:</p>
    <div style="font-size:1.1rem;font-weight:700;color:var(--accent-yellow);background:var(--bg-card);padding:14px;border-radius:var(--radius-sm);border:1px dashed var(--accent-yellow);text-align:center;margin:12px 0;">
      "MÀY CÀNG ÉP NÓ LÀM GÌ &ndash; NÓ CÀNG LÀM NGƯỢC LẠI ĐỂ CHỐNG LẠI MÀY!"
    </div>
    <p>Một hệ đang cân bằng yên ổn, mày tác động từ bên ngoài vào (thay đổi nồng độ, nhiệt độ, áp suất) thì cân bằng sẽ tự động <strong>dịch chuyển theo chiều LÀM GIẢM tác động đó</strong>.</p>
  </div>

  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Yếu Tố Tác Động</th>
          <th>Hành Động Của Mày</th>
          <th>Phản Ứng Của Hệ (Chống Lại Mày)</th>
          <th>Chiều Dịch Chuyển</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="2"><strong>1. Nồng Độ</strong></td>
          <td><span class="hl-blue">Thêm chất A vào</span> (làm nồng độ A tăng)</td>
          <td>Hệ tìm cách <em>tiêu thụ bớt A</em> đi</td>
          <td>Dịch sang phía <strong>ngược lại</strong> (tiêu thụ A)</td>
        </tr>
        <tr>
          <td><span class="hl-red">Rút bớt chất B ra</span> (làm nồng độ B giảm)</td>
          <td>Hệ tìm cách <em>tạo thêm B</em> để bù lại</td>
          <td>Dịch sang phía <strong>chứa B</strong></td>
        </tr>
        <tr>
          <td rowspan="2"><strong>2. Áp Suất (P)</strong><br><small style="color:var(--text-muted);">(Chỉ tác dụng với hệ có chất KHÍ)</small></td>
          <td><span class="hl-blue">Tăng áp suất (nén bình lại)</span></td>
          <td>Hệ tìm cách <em>giảm áp suất</em> xuống</td>
          <td>Dịch về chiều có <strong>ÍT SỐ MOL KHÍ HƠN</strong></td>
        </tr>
        <tr>
          <td><span class="hl-red">Giảm áp suất (nới rộng bình)</span></td>
          <td>Hệ tìm cách <em>tăng áp suất</em> lên</td>
          <td>Dịch về chiều có <strong>NHIỀU SỐ MOL KHÍ HƠN</strong></td>
        </tr>
        <tr>
          <td rowspan="2"><strong>3. Nhiệt Độ (T)</strong><br><small style="color:var(--text-muted);">(Mẹo: Tăng Thu - Giảm Tỏa)</small></td>
          <td><span class="hl-blue">Tăng nhiệt độ (nung nóng)</span></td>
          <td>Hệ tìm cách <em>hút bớt nhiệt</em> cho mát lại</td>
          <td>Dịch về chiều <strong>THU NHIỆT (&Delta;H &gt; 0)</strong></td>
        </tr>
        <tr>
          <td><span class="hl-red">Hạ nhiệt độ (làm lạnh)</span></td>
          <td>Hệ tìm cách <em>tỏa thêm nhiệt</em> cho ấm lên</td>
          <td>Dịch về chiều <strong>TỎA NHIỆT (&Delta;H &lt; 0)</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 2 NGOẠI LỆ ĐẶC BIỆT CỰC HAY BỊ LỪA TRONG ĐỀ THI!</div>
    <p><strong>NGOẠI LỆ 1: CHẤT XÚC TÁC (Catalyst)</strong></p>
    <p><span class="hl-red">Chất xúc tác KHÔNG LÀM CHUYỂN DỊCH CÂN BẰNG!</span></p>
    <p>Tại sao? Vì chất xúc tác làm tăng tốc độ phản ứng thuận bao nhiêu lần thì nó cũng làm tăng tốc độ phản ứng nghịch bấy nhiêu lần. Cả hai thằng cùng tăng như nhau thì tỉ số vẫn giữ nguyên. Tác dụng duy nhất của xúc tác là <strong>giúp hệ NHANH ĐẠT ĐẾN TRẠNG THÁI CÂN BẰNG HƠN</strong>, tiết kiệm thời gian chứ không làm tăng thêm 1 gam sản phẩm nào cả!</p>
    <p style="margin-top:10px;"><strong>NGOẠI LỆ 2: ÁP SUẤT KHI HAI VẾ CÙNG SỐ MOL KHÍ</strong></p>
    <p>Xét phản ứng: H<sub>2</sub>(g) + I<sub>2</sub>(g) &hArr; 2HI(g)</p>
    <p>Bên trái có 1 + 1 = 2 mol khí. Bên phải có 2 mol khí. Số mol khí 2 vế BẰNG NHAU (2 = 2). Khi mày tăng hay giảm áp suất, hệ đéo biết chạy đường nào vì bên nào cũng chật chội như nhau &rarr; <strong>ÁP SUẤT KHÔNG LÀM CHUYỂN DỊCH CÂN BẰNG NÀY!</strong></p>
  </div>

  <!-- COMBO HỦY DIỆT BÀI 1 -->
  <div class="box box-combo">
    <div class="box-title">💥 COMBO HỦY DIỆT: BẢNG "3 DÒNG THẦN THÁNH" GIẢI MỌI BÀI TẬP Kc</div>
    <p><strong>Dấu hiệu nhận biết:</strong> Đề bài cho nồng độ ban đầu của các chất, hoặc cho Kc bắt tìm nồng độ cân bằng / hiệu suất phản ứng. Cứ thấy đề có chữ "ban đầu", "phản ứng", "cân bằng" là ốp ngay bảng 3 dòng:</p>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Giai Đoạn</th>
            <th>N<sub>2</sub>(g)</th>
            <th>+ 3H<sub>2</sub>(g)</th>
            <th>&hArr; 2NH<sub>3</sub>(g)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>1. Ban đầu (B)</strong></td><td>C<sub>1</sub></td><td>C<sub>2</sub></td><td>0</td></tr>
          <tr><td><strong>2. Phản ứng (P)</strong></td><td>x</td><td>3x</td><td>2x (tính theo hệ số phương trình)</td></tr>
          <tr><td><strong>3. Cân bằng (C)</strong></td><td>C<sub>1</sub> &ndash; x</td><td>C<sub>2</sub> &ndash; 3x</td><td>2x (Lấy Ban đầu TRỪ Phản ứng)</td></tr>
        </tbody>
      </table>
    </div>
    <p>Sau đó ốp thẳng các giá trị dòng 3 (C) vào biểu thức K<sub>c</sub>: <strong>K<sub>c</sub> = [NH<sub>3</sub>]<sup>2</sup> / ([N<sub>2</sub>] &times; [H<sub>2</sub>]<sup>3</sup>)</strong> để giải phương trình tìm x!</p>
  </div>

  <!-- SƠ ĐỒ TƯ DUY MINDMAP BÀI 1 -->
  <h3 class="sec-title">5. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Bài 1</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">CÂN BẰNG HÓA HỌC (BÀI 1)</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-blue-light);">1. BẢN CHẤT CÂN BẰNG</h5>
        <ul>
          <li>Cân bằng động: vt = vn > 0</li>
          <li>Nồng độ không đổi theo thời gian</li>
          <li>Phản ứng thuận nghịch: H &lt; 100%</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">2. HẰNG SỐ CÂN BẰNG Kc</h5>
        <ul>
          <li>Kc = [SP] / [TG] với số mũ tỉ lượng</li>
          <li>Chất rắn (s) TUYỆT ĐỐI không ghi</li>
          <li>Chỉ phụ thuộc bản chất & nhiệt độ T</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-red);">3. LE CHATELIER</h5>
        <ul>
          <li>Tăng chất A &rarr; dịch chiều giảm A</li>
          <li>Tăng P &rarr; dịch chiều ít mol khí</li>
          <li>Tăng T &rarr; dịch chiều Thu (&Delta;H &gt; 0)</li>
          <li>Hạ T &rarr; dịch chiều Tỏa (&Delta;H &lt; 0)</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-purple);">4. HAI NGOẠI LỆ</h5>
        <ul>
          <li>Xúc tác: Không làm chuyển dịch cân bằng</li>
          <li>Số mol khí 2 vế bằng nhau: P vô tác dụng</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- THỰC CHIẾN STEP BY STEP (2 BÀI MẪU) -->
  <h3 class="sec-title">6. Thực Chiến: 2 Bài Tập Mẫu Step-by-Step</h3>
  
  <!-- BÀI MẪU 1 -->
  <div class="step-solver">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 1: Tính Hằng Số Cân Bằng Kc (Dạng Tính Toán)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Cho phản ứng: N<sub>2</sub>O<sub>4</sub>(g) &hArr; 2NO<sub>2</sub>(g). Ở nhiệt độ t&deg;C, nạp 0,5 mol N<sub>2</sub>O<sub>4</sub> vào bình kín dung tích 2 lít. Khi phản ứng đạt trạng thái cân bằng, đo được nồng độ NO<sub>2</sub> trong bình là 0,2 M. Hãy tính giá trị hằng số cân bằng K<sub>c</sub> của phản ứng ở nhiệt độ này.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bẫy đề thi</strong>
          <p>&bull; Từ khóa: Bình kín V = 2 lít; lượng ban đầu = 0,5 mol N<sub>2</sub>O<sub>4</sub>.
          <br>&bull; <span class="hl-red">BẪY NGU NGƯỜI:</span> Đề cho 0,5 MOL chứ không phải nồng độ M! Bình 2 lít thì nồng độ ban đầu phải là [N<sub>2</sub>O<sub>4</sub>]<sub>ban đầu</sub> = 0,5 / 2 = 0,25 M. Đứa nào lấy luôn số 0,5 ốp vào là toang!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Lập bảng 3 dòng (B &ndash; P &ndash; C)</strong>
          <div class="tbl-wrap">
            <table>
              <thead><tr><th>Dòng (M)</th><th>N<sub>2</sub>O<sub>4</sub>(g)</th><th>&hArr; 2NO<sub>2</sub>(g)</th></tr></thead>
              <tbody>
                <tr><td>Ban đầu</td><td>0,25</td><td>0</td></tr>
                <tr><td>Phản ứng</td><td>0,1 &larr; (vì tạo ra 0,2 NO<sub>2</sub> thì cần 0,2/2 = 0,1 N<sub>2</sub>O<sub>4</sub>)</td><td>0,2</td></tr>
                <tr><td>Cân bằng</td><td>0,25 &ndash; 0,1 = <strong>0,15 M</strong></td><td><strong>0,2 M</strong></td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tại sao dùng công thức này mà không dùng công thức khác?</strong>
          <p>Vì đề bài yêu cầu tìm K<sub>c</sub> ở trạng thái cân bằng của phản ứng đồng thể khí, ta ốp thẳng biểu thức định nghĩa: <strong>K<sub>c</sub> = [NO<sub>2</sub>]<sup>2</sup> / [N<sub>2</sub>O<sub>4</sub>]</strong> (nhớ số 2 của NO<sub>2</sub> biến thành bình phương [NO<sub>2</sub>]<sup>2</sup>!).</p>
          <div class="formula-display" style="font-size:0.95rem;">
            K<sub>c</sub> = (0,2)<sup>2</sup> / 0,15 = 0,04 / 0,15 &approx; 0,267
          </div>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ CHÍNH XÁC: K<sub>c</sub> &approx; 0,267</strong>
        <p style="margin-top:6px;"><em>Lời gia sư bình phẩm:</em> Nếu mày làm đúng 0,267 thì chúc mừng, mày tỉnh đòn hơn 80% học sinh đi thi! Còn đứa nào bấm ra 0,08 hoặc 0,16 là ăn chửi ngay vì quên chia thể tích 2 lít hoặc quên số mũ 2 của NO2 nhé!</p>
      </div>
    </div>
  </div>

  <!-- BÀI MẪU 2 -->
  <div class="step-solver" style="margin-top:16px;">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 2: Dự Đoán Chuyển Dịch Le Chatelier (Dạng Lý Thuyết Vận Dụng)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Cho cân bằng hóa học trong bình kín: CO(g) + H<sub>2</sub>O(g) &hArr; CO<sub>2</sub>(g) + H<sub>2</sub>(g) có &Delta;<sub>r</sub>H&deg;<sub>298</sub> = -41,2 kJ. Cân bằng sẽ chuyển dịch theo chiều nào (thuận, nghịch hay không đổi) khi:
      <br>a) Tăng nhiệt độ của bình phản ứng?
      <br>b) Tăng áp suất chung của hệ bằng cách nén piston?
      <br>c) Bơm thêm khí CO vào bình?</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bẫy đề bài</strong>
          <p>&bull; &Delta;H = -41,2 kJ &lt; 0 &rarr; Chiều thuận là chiều <strong>TỎA NHIỆT</strong>, chiều nghịch là chiều <strong>THU NHIỆT</strong>.
          <br>&bull; Đếm số mol khí hai vế: Vế trái có 1 mol CO + 1 mol H<sub>2</sub>O = <strong>2 mol khí</strong>. Vế phải có 1 mol CO<sub>2</sub> + 1 mol H<sub>2</sub> = <strong>2 mol khí</strong>. Số mol khí hai vế BẰNG NHAU (2 = 2)!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tóm tắt tác động</strong>
          <p>&bull; Tác động a: Tăng nhiệt độ T.
          <br>&bull; Tác động b: Tăng áp suất P.
          <br>&bull; Tác động c: Tăng nồng độ chất phản ứng [CO].</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tư duy nguyên lý Le Chatelier để phán đoán</strong>
          <p>&bull; Câu a: Tăng T &rarr; Hệ chống lại bằng cách chuyển dịch theo chiều thu nhiệt &rarr; Dịch theo <strong>CHIỀU NGHỊCH</strong>.
          <br>&bull; Câu b: Hai vế đều có 2 mol khí (2 = 2), không bên nào chật hơn bên nào &rarr; <strong>ÁP SUẤT KHÔNG LÀM CHUYỂN DỊCH CÂN BẰNG</strong>! (Bẫy kinh điển).
          <br>&bull; Câu c: Thêm CO &rarr; Hệ tìm cách tiêu thụ bớt CO &rarr; Dịch theo <strong>CHIỀU THUẬN</strong>.</p>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>KẾT QUẢ: a) Chiều nghịch &nbsp;|&nbsp; b) KHÔNG CHUYỂN DỊCH &nbsp;|&nbsp; c) Chiều thuận</strong>
        <p style="margin-top:6px;"><em>Lời gia sư bình phẩm:</em> Đứa nào ở câu b ghi "dịch theo chiều nghịch" thì úp mặt vào tường tự kiểm điểm đi! Đã dặn số mol khí 2 vế bằng nhau (2 = 2) thì nén hay giãn bình nó vẫn trơ ra như gỗ đá!</p>
      </div>
    </div>
  </div>

  <!-- BÀI KIỂM TRA 15 CÂU BÀI 1 -->
  <div class="quiz-section" id="b1-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">Bài Kiểm Tra Kiến Thức Bài 1 (Chuẩn Độ Khó Thi Giữa Kì)</div>
        <div class="quiz-sub">Gồm 8 câu trắc nghiệm + 4 câu đúng/sai + 3 câu tự luận mổ xẻ</div>
      </div>
      <div class="quiz-score-badge" id="b1-score">Điểm: 0/15</div>
    </div>

    <!-- TRẮC NGHIỆM 1-8 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Đặc điểm nào sau đây là ĐÚNG khi một phản ứng thuận nghịch đạt trạng thái cân bằng?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q1" value="A"> A. Phản ứng thuận và nghịch đều dừng lại hoàn toàn.</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="B"> B. Tốc độ phản ứng thuận bằng tốc độ phản ứng nghịch (vt = vn).</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="C"> C. Nồng độ của chất tham gia bằng nồng độ của chất sản phẩm.</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="D"> D. Khối lượng chất tham gia bằng khối lượng chất sản phẩm.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Cân bằng hóa học là cân bằng ĐỘNG, phản ứng không dừng lại mà vt = vn, nồng độ các chất không đổi chứ không bắt buộc bằng nhau. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 2 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Cho cân bằng: CaCO<sub>3</sub>(s) &hArr; CaO(s) + CO<sub>2</sub>(g). Biểu thức hằng số cân bằng Kc của phản ứng là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q2" value="A"> A. Kc = ([CaO] &times; [CO<sub>2</sub>]) / [CaCO<sub>3</sub>]</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="B"> B. Kc = [CaO] &times; [CO<sub>2</sub>]</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="C"> C. Kc = [CO<sub>2</sub>]</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="D"> D. Kc = 1 / [CO<sub>2</sub>]</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> BẪY CHẤT RẮN! CaCO3 và CaO đều là chất rắn (s) nên KHÔNG được viết vào biểu thức Kc. Do đó Kc = [CO2]. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 3 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hằng số cân bằng Kc của một phản ứng thuận nghịch phụ thuộc vào yếu tố nào sau đây?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q3" value="A"> A. Bản chất phản ứng và nhiệt độ.</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="B"> B. Nồng độ các chất ban đầu.</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="C"> C. Áp suất chung của hệ.</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="D"> D. Chất xúc tác.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Kc CHỈ phụ thuộc vào bản chất phản ứng và nhiệt độ. Nồng độ, áp suất, xúc tác đều không làm thay đổi giá trị Kc. Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Cho cân bằng: N<sub>2</sub>(g) + 3H<sub>2</sub>(g) &hArr; 2NH<sub>3</sub>(g) (&Delta;rH&deg; = -91,8 kJ). Để hiệu suất tổng hợp NH<sub>3</sub> tăng lên, ta cần:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q4" value="A"> A. Tăng nhiệt độ và giảm áp suất.</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="B"> B. Tăng nhiệt độ và tăng áp suất.</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="C"> C. Giảm nhiệt độ và giảm áp suất.</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="D"> D. Giảm nhiệt độ và tăng áp suất.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Phản ứng thuận tỏa nhiệt (&Delta;H &lt; 0) &rarr; Muốn cân bằng dịch theo chiều thuận (tăng NH3) phải GIẢM NHIỆT ĐỘ (giảm tỏa). Chiều thuận có 4 mol khí &rarr; 2 mol khí (giảm số mol khí) &rarr; Muốn dịch thuận phải TĂNG ÁP SUẤT. Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Chất xúc tác có tác dụng gì đối với một phản ứng thuận nghịch đang ở trạng thái cân bằng?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q5" value="A"> A. Làm cân bằng chuyển dịch theo chiều thuận.</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="B"> B. Làm tăng tốc độ đạt tới trạng thái cân bằng mà không làm dịch chuyển cân bằng.</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="C"> C. Làm tăng giá trị hằng số cân bằng Kc.</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="D"> D. Làm chuyển dịch cân bằng theo chiều phản ứng thu nhiệt.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Chất xúc tác làm tăng tốc độ phản ứng thuận và nghịch bằng nhau nên KHÔNG làm chuyển dịch cân bằng và KHÔNG làm đổi Kc. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Cân bằng hóa học nào sau đây KHÔNG bị chuyển dịch khi thay đổi áp suất của hệ?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q6" value="A"> A. 2SO<sub>2</sub>(g) + O<sub>2</sub>(g) &hArr; 2SO<sub>3</sub>(g)</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="B"> B. N<sub>2</sub>O<sub>4</sub>(g) &hArr; 2NO<sub>2</sub>(g)</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="C"> C. H<sub>2</sub>(g) + I<sub>2</sub>(g) &hArr; 2HI(g)</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="D"> D. C(s) + H<sub>2</sub>O(g) &hArr; CO(g) + H<sub>2</sub>(g)</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Ở câu C: 1 mol H2(g) + 1 mol I2(g) &hArr; 2 mol HI(g). Số mol khí hai vế bằng nhau (2 = 2) nên áp suất không ảnh hưởng. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Cho cân bằng: 2NO<sub>2</sub>(g, màu nâu đỏ) &hArr; N<sub>2</sub>O<sub>4</sub>(g, không màu) có &Delta;rH&deg; &lt; 0. Khi ngâm bình phản ứng vào cốc nước đá lạnh, màu nâu đỏ của bình sẽ:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q7" value="A"> A. Đậm dần lên.</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="B"> B. Nhạt dần đi.</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="C"> C. Giữ nguyên không đổi.</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="D"> D. Chuyển sang màu xanh lá cây.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Ngâm vào nước đá = hạ nhiệt độ &rarr; cân bằng dịch theo chiều tỏa nhiệt (&Delta;H &lt; 0) tức là chiều thuận &rarr; tạo nhiều N2O4 không màu hơn &rarr; màu nâu đỏ nhạt dần đi. Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Hệ số nhiệt độ của hằng số cân bằng: Biết phản ứng thuận là THU NHIỆT (&Delta;rH&deg; &gt; 0). Khi tăng nhiệt độ, giá trị hằng số cân bằng Kc sẽ:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q8" value="A"> A. Tăng lên.</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="B"> B. Giảm xuống.</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="C"> C. Không thay đổi.</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="D"> D. Có thể tăng hoặc giảm tùy nồng độ.</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Phản ứng thu nhiệt (&Delta;H &gt; 0), khi tăng T cân bằng dịch theo chiều thuận &rarr; nồng độ sản phẩm tăng, chất phản ứng giảm &rarr; Kc = [sản phẩm]/[chất phản ứng] sẽ TĂNG LÊN. Chọn A.</div>
    </div>

    <!-- ĐÚNG SAI 9-12 -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 (Đúng / Sai)</div>
      <div class="quiz-q-text">Ở trạng thái cân bằng hóa học, nồng độ của các chất tham gia và sản phẩm không đổi theo thời gian nhưng phản ứng vẫn tiếp tục diễn ra.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> Đây là định nghĩa chuẩn của cân bằng động.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 (Đúng / Sai)</div>
      <div class="quiz-q-text">Thêm chất xúc tác vào hệ phản ứng thuận nghịch làm tăng hiệu suất tạo thành sản phẩm.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Chất xúc tác chỉ làm tăng tốc độ đạt tới cân bằng chứ KHÔNG làm chuyển dịch cân bằng và KHÔNG làm tăng hiệu suất.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 (Đúng / Sai)</div>
      <div class="quiz-q-text">Khi tăng nồng độ một chất trong hệ cân bằng, cân bằng sẽ chuyển dịch theo chiều làm giảm nồng độ chất đó.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> Chuẩn theo nguyên lí Le Chatelier (chống lại sự thay đổi).</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 (Đúng / Sai)</div>
      <div class="quiz-q-text">Trong biểu thức tính hằng số cân bằng Kc của phản ứng C(s) + H2O(g) &hArr; CO(g) + H2(g), ta có mẫu số là [C] &times; [H2O].</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Carbon C ở thể rắn (s) nên KHÔNG được viết vào biểu thức Kc. Mẫu số chỉ có [H2O] mà thôi!</div>
    </div>

    <!-- TỰ LUẬN 13-15 -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 13 (Tự luận vận dụng)</div>
      <div class="quiz-q-text">Người ta sản xuất vôi sống theo phản ứng: CaCO<sub>3</sub>(s) &hArr; CaO(s) + CO<sub>2</sub>(g) (&Delta;rH&deg; = +178 kJ). Em hãy giải thích tại sao trong thực tế các lò nung vôi thủ công người ta phải nung ở nhiệt độ cao (khoảng 900 - 1000&deg;C) và phải liên tục mở cửa lò hút khí CO<sub>2</sub> ra ngoài?</div>
      <textarea placeholder="Nhập câu trả lời của bạn vào đây để tự kiểm tra kiến thức..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>HƯỚNG DẪN CHẤM ĐIỂM CHI TIẾT:</strong>
        <br>1. Phản ứng nung vôi có &Delta;H = +178 kJ &gt; 0 là <em>phản ứng thu nhiệt</em>. Do đó cần duy trì nhiệt độ cao (900-1000&deg;C) để cân bằng chuyển dịch theo chiều thuận (chiều thu nhiệt tạo ra CaO).
        <br>2. Hút liên tục khí CO<sub>2</sub> ra ngoài làm nồng độ [CO<sub>2</sub>] trong lò luôn giảm. Theo nguyên lí Le Chatelier, cân bằng sẽ liên tục dịch chuyển theo chiều thuận để bù lại lượng CO<sub>2</sub> bị lấy đi, từ đó nung được vôi hoàn toàn với hiệu suất cao nhất.
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 (Tự luận tính toán)</div>
      <div class="quiz-q-text">Một bình kín dung tích 10 lít chứa 0,5 mol H<sub>2</sub> và 0,5 mol I<sub>2</sub> ở 448&deg;C. Khi phản ứng H<sub>2</sub>(g) + I<sub>2</sub>(g) &hArr; 2HI(g) đạt cân bằng, hằng số Kc = 50. Hãy tính nồng độ của HI ở trạng thái cân bằng.</div>
      <textarea placeholder="Nháp các bước giải tại đây..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>&bull; Nồng độ ban đầu: [H<sub>2</sub>] = [I<sub>2</sub>] = 0,5 / 10 = 0,05 M.
        <br>&bull; Gọi x là nồng độ H<sub>2</sub> phản ứng (M) &rarr; I<sub>2</sub> phản ứng là x M, tạo ra HI là 2x M.
        <br>&bull; Nồng độ ở trạng thái cân bằng: [H<sub>2</sub>] = 0,05 - x; [I<sub>2</sub>] = 0,05 - x; [HI] = 2x.
        <br>&bull; Biểu thức Kc = [HI]<sup>2</sup> / ([H<sub>2</sub>][I<sub>2</sub>]) = (2x)<sup>2</sup> / (0,05 - x)<sup>2</sup> = 50.
        <br>&bull; Lấy căn bậc hai hai vế: 2x / (0,05 - x) = &radic;50 &approx; 7,071.
        <br>&bull; Giải ra: 2x = 0,3535 - 7,071x &rArr; 9,071x = 0,3535 &rArr; x &approx; 0,039 M.
        <br>&bull; Nồng độ cân bằng của HI = 2x = <strong>0,078 M</strong>.
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 (Tự luận thực tế)</div>
      <div class="quiz-q-text">Tại sao khi mở nắp lon nước ngọt có ga (chứa cân bằng: CO<sub>2</sub>(aq) &hArr; CO<sub>2</sub>(g)), ta lại thấy bọt khí sủi ùng ục trào lên và sau một lúc để ngoài không khí thì nước ngọt bị nhạt (mất hết ga)?</div>
      <textarea placeholder="Giải thích dựa trên nguyên lí Le Chatelier..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>1. Trong lon nước ngọt kín, khí CO<sub>2</sub> được nén ở áp suất cao để hòa tan vào nước: CO<sub>2</sub>(aq) &hArr; CO<sub>2</sub>(g).
        <br>2. Khi bật nắp lon, áp suất trong lon đột ngột giảm xuống bằng áp suất khí quyển. Theo nguyên lí Le Chatelier, cân bằng lập tức chuyển dịch theo chiều làm tăng áp suất, tức là chiều giải phóng khí CO<sub>2</sub>(g) &rarr; bọt khí sủi ùng ục trào ra ngoài.
        <br>3. Khí CO<sub>2</sub> bay mất dần vào không khí làm nồng độ CO<sub>2</sub> hòa tan trong nước giảm về gần bằng 0, khiến nước ngọt bị mất hết vị tê the (mất ga).
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b1')">📊 Nộp Bài & Chấm Điểm Bài 1</button>
  </div>
</section>
"""
