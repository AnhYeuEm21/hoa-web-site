# -*- coding: utf-8 -*-
"""
Module data_b2.py - NÂNG CẤP TOÀN DIỆN
- Bổ sung Sơ Đồ Tư Duy Mindmap Cho Bài 2
- Bổ sung Bài Tập Thực Chiến Mẫu Số 2 (Pha loãng & Chuẩn độ) Chuẩn 3 Bước
- Đổi nút bấm: "🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!"
"""

B2_CONTENT = """
<!-- ========================================== -->
<!-- BÀI 2: CÂN BẰNG TRONG DUNG DỊCH NƯỚC (SGK 16-26) -->
<!-- ========================================== -->
<section id="b2" class="lesson-section">
  <div class="lesson-header">
    <div class="lesson-number">02</div>
    <div class="lesson-meta">
      <h2>Bài 2: Cân Bằng Trong Dung Dịch Nước</h2>
      <div class="lesson-sub">SGK Hóa học 11 – Kết Nối Tri Thức (Trang 16 đến trang 26)</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Sự điện li</span>
        <span class="lesson-tag">Thuyết Brønsted-Lowry</span>
        <span class="lesson-tag">Tích số ion Kw</span>
        <span class="lesson-tag">Thang đo pH</span>
        <span class="lesson-tag">Chuẩn độ acid-base</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p16_17.png')">📖 Xem SGK Trang 16-17</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p18_19.png')">📖 Xem SGK Trang 18-19</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p20_21.png')">📖 Xem SGK Trang 20-21</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p22_23.png')">📖 Xem SGK Trang 22-23</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p24_25.png')">📖 Xem SGK Trang 24-25</button>
    <button class="sgk-btn" onclick="openSgkModal('sgk_b2_p26.png')">📖 Xem SGK Trang 26</button>
  </div>

  <!-- PHẦN 1: SỰ ĐIỆN LI & CHẤT ĐIỆN LI -->
  <h3 class="sec-title" id="b2-dieli">1. Sự Điện Li & Phân Loại Chất Điện Li</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch SGK Sang Tiếng Người (Bản Chất Sự Dẫn Điện)</div>
    <p>Hồi nhỏ chắc mày từng thắc mắc: <em>Tại sao bị ướt tay cắm ổ điện thì bị giật tung người, nhưng nước cất tinh khiết thì đéo dẫn điện?</em></p>
    <p>Bản chất dòng điện là <strong>dòng chuyển dời có hướng của các hạt mang điện</strong>. Trong kim loại là electron, còn trong dung dịch lỏng là các <span class="tooltip" data-tip="Hạt nguyên tử hoặc nhóm nguyên tử mang điện tích dương (+) hoặc âm (-)">ION</span>!</p>
    <p><strong>Sự điện li:</strong> Là quá trình các chất khi tan vào nước bị các phân tử nước kéo dãn và bẻ gãy liên kết, rã ra thành các ion dương (cation) và ion âm (anion).</p>
  </div>

  <div class="box box-story">
    <div class="box-title">💡 Câu Chuyện "Quẩy Bar": Phân Biệt Chất Điện Li Cực Dễ</div>
    <p>Tưởng tượng 1 quán Bar tên là "Dung Dịch Nước":</p>
    <ul class="content-list">
      <li><strong>Chất điện li MẠNH:</strong> Giống như một đám thanh niên bốc lửa 100 đứa kéo vào bar. Vừa mở nhạc lên là 100/100 đứa bung lụa nhảy nhót tách rời nhau ra hết (phân li 100% ra ion). Mũi tên viết 1 chiều &rarr;.</li>
      <li><strong>Chất điện li YẾU:</strong> Giống như 100 ông bà già vào bar. Nhạc đập đùng đùng mà chỉ có 1-2 người chịu đứng dậy lắc lư (phân li thành ion), còn 98-99 người vẫn ngồi dính chặt lấy nhau thành phân tử. Mũi tên viết thuận nghịch &hArr;.</li>
      <li><strong>Chất KHÔNG điện li:</strong> Giống như khúc gỗ quăng vào bar. Tan trong nước nhưng giữ nguyên 100% dạng phân tử trung hòa, không sinh ra 1 hạt ion nào &rarr; bóng đèn tịt ngòi không sáng.</li>
    </ul>
  </div>

  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Loại Chất</th>
          <th>Đặc Điểm Phân Li</th>
          <th>Phương Trình Ví Dụ</th>
          <th>Gồm Những Thằng Nào Cần Nhớ?</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:var(--accent-blue-light);">Điện li MẠNH (&rarr;)</strong></td>
          <td>Tan bao nhiêu phân li hết 100% thành ion.</td>
          <td>
            NaCl &rarr; Na<sup>+</sup> + Cl<sup>&minus;</sup><br>
            HCl &rarr; H<sup>+</sup> + Cl<sup>&minus;</sup><br>
            Ba(OH)<sub>2</sub> &rarr; Ba<sup>2+</sup> + 2OH<sup>&minus;</sup>
          </td>
          <td>
            &bull; <strong>Acid mạnh:</strong> HCl, HNO<sub>3</sub>, H<sub>2</sub>SO<sub>4</sub>, HBr, HI, HClO<sub>4</sub>.<br>
            &bull; <strong>Base mạnh:</strong> LiOH, NaOH, KOH, Ca(OH)<sub>2</sub>, Ba(OH)<sub>2</sub>.<br>
            &bull; <strong>Hầu hết các muối tan:</strong> NaCl, KNO<sub>3</sub>, Na<sub>2</sub>SO<sub>4</sub>, CuCl<sub>2</sub>...
          </td>
        </tr>
        <tr>
          <td><strong style="color:var(--accent-yellow);">Điện li YẾU (&hArr;)</strong></td>
          <td>Chỉ có một phần nhỏ phân li ra ion, đa số vẫn ở dạng phân tử.</td>
          <td>
            CH<sub>3</sub>COOH &hArr; CH<sub>3</sub>COO<sup>&minus;</sup> + H<sup>+</sup><br>
            HF &hArr; H<sup>+</sup> + F<sup>&minus;</sup><br>
            NH<sub>3</sub> + H<sub>2</sub>O &hArr; NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup>
          </td>
          <td>
            &bull; <strong>Acid yếu:</strong> CH<sub>3</sub>COOH (giấm ăn), HF, H<sub>2</sub>S, H<sub>2</sub>CO<sub>3</sub>, HNO<sub>2</sub>, H<sub>2</sub>SO<sub>3</sub>.<br>
            &bull; <strong>Base yếu:</strong> NH<sub>3</sub>, các hydroxide kết tủa như Cu(OH)<sub>2</sub>, Fe(OH)<sub>3</sub>, Al(OH)<sub>3</sub>.<br>
            &bull; Nước nguyên chất (H<sub>2</sub>O).
          </td>
        </tr>
        <tr>
          <td><strong style="color:var(--accent-red);">Không điện li</strong></td>
          <td>Tan nhưng không tạo ion, không dẫn điện.</td>
          <td>C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(s) &rarr; C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>(aq)</td>
          <td>Đường saccarozơ, glucozơ, rượu ethanol (C<sub>2</sub>H<sub>5</sub>OH), glixerol, nước cất...</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PHẦN 2: THUYẾT BRONSTED - LOWRY -->
  <h3 class="sec-title" id="b2-bronsted">2. Thuyết Brønsted &ndash; Lowry Về Acid &ndash; Base</h3>

  <div class="box box-theory">
    <div class="box-title">📘 Dịch Định Nghĩa Sang Tiếng Người (Bỏ Định Nghĩa Cũ Của Lớp 9 Đi!)</div>
    <p>Lớp 9 mày học: Acid là chất có H, Base là chất có nhóm OH. Lên lớp 11, định nghĩa đó quá chật hẹp (khí NH<sub>3</sub> đéo có nhóm OH nào nhưng vẫn làm quỳ tím hóa xanh!).</p>
    <p>Năm 1923, hai ông Brønsted và Lowry đưa ra định nghĩa chuẩn quốc tế dựa trên hạt proton H<sup>+</sup>:</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0;">
      <div style="background:rgba(92,111,255,0.1);padding:14px;border-radius:var(--radius-sm);border:1px solid var(--accent-blue);">
        <strong style="color:var(--accent-blue-light);font-size:1.1rem;">ACID</strong>
        <p style="margin-top:6px;font-weight:600;">Là chất có khả năng <span class="hl-blue">CHO PROTON (H<sup>+</sup>)</span></p>
        <small style="color:var(--text-muted);">(Cho đi H<sup>+</sup> để thành bazơ liên hợp)</small>
      </div>
      <div style="background:rgba(255,171,64,0.1);padding:14px;border-radius:var(--radius-sm);border:1px solid var(--accent-orange);">
        <strong style="color:var(--accent-orange);font-size:1.1rem;">BASE</strong>
        <p style="margin-top:6px;font-weight:600;">Là chất có khả năng <span class="hl-orange">NHẬN PROTON (H<sup>+</sup>)</span></p>
        <small style="color:var(--text-muted);">(Hút H<sup>+</sup> về mình để thành acid liên hợp)</small>
      </div>
    </div>
    <p><strong>Chất LƯỠNG TÍNH:</strong> Là chất "hai mang", gặp thằng mạnh hơn cho H<sup>+</sup> thì nó nhận (đóng vai Base), gặp thằng thèm H<sup>+</sup> thì nó nhường (đóng vai Acid). Điển hình: <strong>H<sub>2</sub>O, ion HCO<sub>3</sub><sup>&minus;</sup>, HSO<sub>3</sub><sup>&minus;</sup>, Al(OH)<sub>3</sub>, Zn(OH)<sub>2</sub></strong>.</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 Minh Họa Phản Ứng Cho &ndash; Nhận Proton H+</div>
    <div class="reaction-box">
      <strong>Ví dụ 1:</strong> CH<sub>3</sub>COOH + H<sub>2</sub>O &hArr; CH<sub>3</sub>COO<sup>&minus;</sup> + H<sub>3</sub>O<sup>+</sup>
      <br>&bull; CH<sub>3</sub>COOH ném H<sup>+</sup> cho nước &rarr; <strong>CH<sub>3</sub>COOH là ACID</strong>.
      <br>&bull; H<sub>2</sub>O bắt lấy H<sup>+</sup> &rarr; <strong>H<sub>2</sub>O là BASE</strong>.
    </div>
    <div class="reaction-box" style="margin-top:8px;">
      <strong>Ví dụ 2:</strong> NH<sub>3</sub> + H<sub>2</sub>O &hArr; NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup>
      <br>&bull; H<sub>2</sub>O ném H<sup>+</sup> cho NH<sub>3</sub> &rarr; <strong>H<sub>2</sub>O là ACID</strong>.
      <br>&bull; NH<sub>3</sub> tóm lấy H<sup>+</sup> &rarr; <strong>NH<sub>3</sub> là BASE</strong>.
    </div>
    <p style="font-size:0.85rem;color:var(--accent-yellow);">Thấy chưa? Ở ví dụ 1 nước đóng vai Base, sang ví dụ 2 nước lại đóng vai Acid &rarr; Nước là chất <strong>LƯỠNG TÍNH</strong>!</p>
  </div>

  <!-- PHẦN 3: TÍCH SỐ ION CỦA NƯỚC & THANG pH -->
  <h3 class="sec-title" id="b2-ph">3. Tích Số Ion Của Nước & Mổ Xẻ Thang pH</h3>

  <div class="box box-formula">
    <div class="box-title">📐 Tích Số Ion Của Nước Kw (Bảo Bối Tính Toán)</div>
    <p>Ngay cả nước cất siêu tinh khiết cũng tự phân li một lượng vô cùng nhỏ:</p>
    <div style="text-align:center;font-size:1rem;color:var(--accent-blue-light);margin:6px 0;">H<sub>2</sub>O &hArr; H<sup>+</sup> + OH<sup>&minus;</sup></div>
    <p>Ở nhiệt độ phòng (25&deg;C), tích nồng độ của 2 ion này luôn luôn là một hằng số bất di bất dịch:</p>
    <div class="formula-display">
      K<sub>w</sub> = [H<sup>+</sup>] &times; [OH<sup>&minus;</sup>] = 1,0 &times; 10<sup>&minus;14</sup>
    </div>
    <div class="formula-label">Áp dụng cho MỌI DUNG DỊCH NƯỚC ở 25°C!</div>
    <p style="margin-top:8px;">Ý nghĩa: Trong bất kì dung dịch nước nào, biết [H<sup>+</sup>] là mày suy ra ngay [OH<sup>&minus;</sup>] bằng cách lấy <strong>10<sup>&minus;14</sup> / [H<sup>+</sup>]</strong> và ngược lại!</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 Bộ Công Thức Tính pH "Bách Phát Bách Trúng"</div>
    <div class="formula-display">
      pH = &minus;log[H<sup>+</sup>]  &hArr;  [H<sup>+</sup>] = 10<sup>&minus;pH</sup>
    </div>
    <div class="formula-display" style="margin-top:8px;">
      pOH = &minus;log[OH<sup>&minus;</sup>]  &hArr;  [OH<sup>&minus;</sup>] = 10<sup>&minus;pOH</sup>
    </div>
    <div class="formula-display" style="margin-top:8px;color:var(--accent-green);border-color:var(--accent-green);">
      pH + pOH = 14  (ở 25&deg;C)
    </div>
  </div>

  <div class="box box-theory">
    <div class="box-title">📘 Bảng Phân Cấp Môi Trường Theo pH (25&deg;C)</div>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Môi Trường</th>
            <th>Nồng Độ [H<sup>+</sup>]</th>
            <th>Giá Trị pH</th>
            <th>Hiện Tượng Quỳ Tím</th>
            <th>Hiện Tượng Phenolphthalein</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong style="color:var(--accent-red);">ACID (Chua)</strong></td>
            <td>[H<sup>+</sup>] &gt; 10<sup>&minus;7</sup> M</td>
            <td><strong>pH &lt; 7</strong> (càng nhỏ càng chua)</td>
            <td>Hóa <strong style="color:var(--accent-red);">ĐỎ</strong></td>
            <td>Không đổi màu (không màu)</td>
          </tr>
          <tr>
            <td><strong style="color:var(--accent-green);">TRUNG TÍNH</strong></td>
            <td>[H<sup>+</sup>] = 10<sup>&minus;7</sup> M</td>
            <td><strong>pH = 7</strong> (nước tinh khiết)</td>
            <td>Giữ nguyên màu tím</td>
            <td>Không đổi màu (không màu)</td>
          </tr>
          <tr>
            <td><strong style="color:var(--accent-blue-light);">BASE (Kiềm)</strong></td>
            <td>[H<sup>+</sup>] &lt; 10<sup>&minus;7</sup> M</td>
            <td><strong>pH &gt; 7</strong> (càng lớn càng nồng)</td>
            <td>Hóa <strong style="color:var(--accent-blue-light);">XANH</strong></td>
            <td>Hóa <strong style="color:var(--accent-purple);">HỒNG TÍM</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="box box-warning">
    <div class="box-title">🚨 BẪY LỪA PHỔ BIẾN NHẤT ĐỜI HỌC SINH KHI TÍNH pH</div>
    <p><strong>CẢNH BÁO 1: Bẫy dung dịch Base (NaOH, Ba(OH)<sub>2</sub>)</strong></p>
    <p>Đề bài cho dung dịch NaOH 0,01 M. Học sinh tính ra [OH<sup>&minus;</sup>] = 0,01 = 10<sup>&minus;2</sup> M. Xong ngứa tay lấy luôn <code>&minus;log(0,01) = 2</code> rồi phán bừa: "pH = 2" &rarr; <span class="hl-red">ĂN 0 ĐIỂM NGAY LẬP TỨC!</span></p>
    <p>Dung dịch kiềm sao mà pH = 2 (môi trường acid) được? Con số 2 đó là <strong>pOH</strong>! Muốn ra pH mày phải lấy <strong>14 &minus; 2 = 12</strong> mới chính xác!</p>
    <p style="margin-top:10px;"><strong>CẢNH BÁO 2: Pha loãng Acid không bao giờ vượt quá 7!</strong></p>
    <p>Có 1 cốc HCl pH = 5. Mày đổ 1 bể bơi nước vào pha loãng, pH nó tăng dần lên nhưng <strong>ĐÉO BAO GIỜ VƯỢT QUÁ 7 ĐƯỢC</strong>! Vì mày có đổ bao nhiêu nước thì cốc nước vẫn là acid, không bao giờ nước lã biến acid thành nước kiềm được!</p>
  </div>

  <!-- PHẦN 4: CHUẨN ĐỘ ACID - BASE -->
  <h3 class="sec-title" id="b2-chd">4. Chuẩn Độ Acid &ndash; Base</h3>
  <div class="box box-theory">
    <div class="box-title">📘 Nguyên Tắc Chuẩn Độ Bằng Buret</div>
    <p>Chuẩn độ là phương pháp xác định nồng độ của một dung dịch acid hoặc base chưa biết bằng một dung dịch khác đã biết chính xác nồng độ (gọi là dung dịch chuẩn).</p>
    <ul class="content-list">
      <li>Dụng cụ: <strong>Buret</strong> (ống thủy tinh có khóa và vạch chia thể tích chính xác để nhỏ từng giọt), <strong>Bình tam giác</strong> (Erlenmeyer chứa dung dịch cần chuẩn độ).</li>
      <li>Chất chỉ thị: Thường dùng <strong>phenolphthalein</strong>. Khi nhỏ kiềm vào acid có phenolphthalein, đến khi dung dịch từ không màu chuyển sang màu <span class="hl-purple">hồng nhạt bền vững trong 30 giây</span> (gọi là <em>điểm tương đương</em>) thì khóa buret lại và đọc thể tích đã dùng.</li>
    </ul>
  </div>

  <!-- GÓC HỒI TƯỞNG LỚP 10 BÀI 2 -->
  <div class="accordion-item" style="margin:20px 0;">
    <button class="accordion-trigger" onclick="toggleAcc(this)">
      <span>🟣 <strong>KÝ ỨC ÙA VỀ (Cứu Nạn Lớp 10): Định Luật Pha Loãng Dung Dịch</strong></span>
      <span class="acc-icon">▼</span>
    </button>
    <div class="accordion-content">
      <div class="accordion-inner">
        <div class="box box-recall">
          <div class="box-title">💡 Công Thức Pha Loãng Không Làm Đổi Số Mol Chất Tan</div>
          <p>Khi mày thêm nước vào dung dịch, thể tích tăng lên làm nồng độ loãng đi, nhưng <strong>số mol chất tan n không hề thay đổi</strong>:</p>
          <div class="formula-display">
            C<sub>1</sub> &times; V<sub>1</sub> = C<sub>2</sub> &times; V<sub>2</sub>
          </div>
          <p>Nhớ: V<sub>2</sub> là thể tích dung dịch SAU KHI PHA (V<sub>2</sub> = V<sub>1</sub> + V<sub>nước thêm vào</sub>).</p>
        </div>
      </div>
    </div>
  </div>

  <!-- COMBO HỦY DIỆT BÀI 2 -->
  <div class="box box-combo">
    <div class="box-title">💥 COMBO HỦY DIỆT: TRỘN ACID VỚI BASE &ndash; TÌM pH DUNG DỊCH SAU TRỘN</div>
    <p><strong>Dấu hiệu nhận biết:</strong> Đề bài cho trộn V<sub>1</sub> lít dung dịch acid (HCl, H<sub>2</sub>SO<sub>4</sub>) với V<sub>2</sub> lít dung dịch base (NaOH, Ba(OH)<sub>2</sub>). Bắt tìm pH của dung dịch thu được.</p>
    <p><strong>3 Bước làm chuẩn chỉ như một cái máy:</strong></p>
    <ul class="content-ol">
      <li><strong>Bước 1:</strong> Tính tổng số mol H<sup>+</sup>: n<sub>H<sup>+</sup></sub> = C<sub>M</sub> &times; V &times; (số H trong acid). Tính tổng mol OH<sup>&minus;</sup>: n<sub>OH<sup>&minus;</sup></sub> = C<sub>M</sub> &times; V &times; (số OH trong base).</li>
      <li><strong>Bước 2:</strong> Bản chất phản ứng trung hòa: <code>H<sup>+</sup> + OH<sup>&minus;</sup> &rarr; H<sub>2</sub>O</code>. So sánh xem thằng nào DƯ:
        <br>&bull; Nếu <strong>H<sup>+</sup> dư:</strong> n<sub>H<sup>+</sup> dư</sub> = n<sub>H<sup>+</sup></sub> &minus; n<sub>OH<sup>&minus;</sup></sub> &rarr; [H<sup>+</sup>]<sub>dư</sub> = n<sub>H<sup>+</sup> dư</sub> / (V<sub>1</sub> + V<sub>2</sub>) &rarr; <strong>pH = &minus;log[H<sup>+</sup>]<sub>dư</sub></strong>.
        <br>&bull; Nếu <strong>OH<sup>&minus;</sup> dư:</strong> n<sub>OH<sup>&minus;</sup> dư</sub> = n<sub>OH<sup>&minus;</sup></sub> &minus; n<sub>H<sup>+</sup></sub> &rarr; [OH<sup>&minus;</sup>]<sub>dư</sub> = n<sub>OH<sup>&minus;</sup> dư</sub> / (V<sub>1</sub> + V<sub>2</sub>) &rarr; pOH = &minus;log[OH<sup>&minus;</sup>]<sub>dư</sub> &rarr; <strong>pH = 14 &minus; pOH</strong>.
        <br>&bull; Nếu <strong>vừa đủ:</strong> pH = 7.
      </li>
    </ul>
  </div>

  <!-- SƠ ĐỒ TƯ DUY MINDMAP BÀI 2 -->
  <h3 class="sec-title">5. Sơ Đồ Tư Duy (Mindmap) Chốt Hạ Bài 2</h3>
  <div class="mindmap">
    <div style="text-align:center;"><span class="mindmap-center">CÂN BẰNG TRONG DUNG DỊCH NƯỚC (BÀI 2)</span></div>
    <div class="mindmap-branches">
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-blue-light);">1. SỰ ĐIỆN LI</h5>
        <ul>
          <li>Mạnh: Acid mạnh, Base kiềm, Muối tan (&rarr;)</li>
          <li>Yếu: Acid yếu, Base yếu, Nước (&hArr;)</li>
          <li>Không điện li: Đường, rượu, nước cất</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-yellow);">2. THUYẾT BRØNSTED</h5>
        <ul>
          <li>Acid: Cho H+ (proton donor)</li>
          <li>Base: Nhận H+ (proton acceptor)</li>
          <li>Lưỡng tính: Vừa cho vừa nhận (H2O, HCO3-)</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-green);">3. THANG ĐO pH</h5>
        <ul>
          <li>Kw = [H+][OH-] = 10^-14 (25&deg;C)</li>
          <li>pH = -log[H+]; pOH = -log[OH-]</li>
          <li>pH + pOH = 14</li>
          <li>Acid: pH &lt; 7 | Base: pH &gt; 7</li>
        </ul>
      </div>
      <div class="mindmap-branch">
        <h5 style="color:var(--accent-purple);">4. CHUẨN ĐỘ ACID-BASE</h5>
        <ul>
          <li>Dụng cụ: Buret + Bình tam giác</li>
          <li>Chỉ thị: Phenolphthalein (hồng trong kiềm)</li>
          <li>Công thức: n_H+ = n_OH- tại điểm tương đương</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- THỰC CHIẾN STEP BY STEP (2 BÀI MẪU) -->
  <h3 class="sec-title">6. Thực Chiến: 2 Bài Tập Mẫu Chuẩn Độ & Tính pH Step-by-Step</h3>

  <!-- BÀI MẪU 1 -->
  <div class="step-solver">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 1: Trộn Dung Dịch Acid & Base (Dạng Tính pH Sau Trộn)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Trộn 100 mL dung dịch H<sub>2</sub>SO<sub>4</sub> 0,05 M với 100 mL dung dịch NaOH 0,12 M. Tính giá trị pH của dung dịch thu được sau khi trộn (coi thể tích dung dịch không đổi khi trộn).</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bẫy bị gài</strong>
          <p>&bull; V<sub>1</sub> = 100 mL = 0,1 L; V<sub>2</sub> = 100 mL = 0,1 L &rarr; Thể tích sau trộn V<sub>dd</sub> = 0,1 + 0,1 = 0,2 L.
          <br>&bull; <span class="hl-red">BẪY CHẾT NGƯỜI:</span> Axit là H<sub>2</sub>SO<sub>4</sub> có tới <strong>2 nguyên tử H</strong>! Số mol H<sup>+</sup> phải nhân đôi!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tóm tắt sạch dữ kiện & Tính mol từng ion</strong>
          <p>&bull; n<sub>H<sup>+</sup></sub> = 2 &times; n<sub>H<sub>2</sub>SO<sub>4</sub></sub> = 2 &times; (0,1 &times; 0,05) = <strong>0,01 mol</strong>.
          <br>&bull; n<sub>OH<sup>&minus;</sup></sub> = n<sub>NaOH</sub> = 0,1 &times; 0,12 = <strong>0,012 mol</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tại sao lôi công thức pOH ra xài mà đéo xài luôn pH = -log[H+]?</strong>
          <p>Vì 0,012 mol OH<sup>&minus;</sup> &gt; 0,01 mol H<sup>+</sup> &rArr; <strong>OH<sup>&minus;</sup> BỊ DƯ!</strong> Dung dịch sau phản ứng có môi trường kiềm, bắt buộc phải tính nồng độ [OH<sup>&minus;</sup>]<sub>dư</sub> trước, suy ra pOH, rồi mới lấy 14 trừ đi pOH để ra pH!</p>
          <div class="formula-display" style="font-size:0.95rem;">
            [OH<sup>&minus;</sup>]<sub>dư</sub> = (0,012 &minus; 0,01) / 0,2 = 0,01 M = 10<sup>&minus;2</sup> M
            <br>pOH = &minus;log(10<sup>&minus;2</sup>) = 2  &rArr;  pH = 14 &minus; 2 = 12
          </div>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ CHÍNH XÁC: pH = 12</strong>
        <p><em>Lời gia sư bình phẩm:</em> Đứa nào tính ra pH = 2 thì nhận ngay 1 gậy vào đầu nhé! Dung dịch dư bazơ kiềm sờ trơn tay mà bảo pH = 2 (chua như chanh) à?</p>
      </div>
    </div>
  </div>

  <!-- BÀI MẪU 2 -->
  <div class="step-solver" style="margin-top:16px;">
    <div class="step-solver-header">🎯 Bài Tập Mẫu 2: Pha Loãng Dung Dịch Acid (Dạng Tránh Bẫy Vượt Quá 7)</div>
    <div class="step-solver-body">
      <p><strong>ĐỀ BÀI:</strong> Có 10 mL dung dịch HCl có pH = 2. Cần thêm bao nhiêu mL nước cất vào để thu được dung dịch có pH = 4?</p>

      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi từ khóa & Bản chất logarit của thang pH</strong>
          <p>&bull; pH = 2 &rarr; [H<sup>+</sup>]<sub>1</sub> = 10<sup>&minus;2</sup> M = 0,01 M.
          <br>&bull; pH = 4 &rarr; [H<sup>+</sup>]<sub>2</sub> = 10<sup>&minus;4</sup> M = 0,0001 M.
          <br>&bull; Thang pH là thang đo logarit cơ số 10: pH tăng 1 đơn vị thì nồng độ H<sup>+</sup> giảm 10 lần. Ở đây pH tăng từ 2 lên 4 (tăng 2 đơn vị) &rarr; nồng độ giảm 10<sup>2</sup> = 100 lần!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tóm tắt số mol</strong>
          <p>&bull; Thể tích ban đầu: V<sub>1</sub> = 10 mL = 0,01 L.
          <br>&bull; Số mol H<sup>+</sup> ban đầu: n<sub>H<sup>+</sup></sub> = [H<sup>+</sup>]<sub>1</sub> &times; V<sub>1</sub> = 0,01 &times; 0,01 = 10<sup>&minus;4</sup> mol.
          <br>&bull; Thêm nước cất thì số mol H<sup>+</sup> KHÔNG ĐỔI: n<sub>H<sup>+</sup> sau</sub> = 10<sup>&minus;4</sup> mol.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tư duy chọn công thức thể tích</strong>
          <p>Ta áp dụng công thức: <strong>V<sub>2</sub> = n<sub>H<sup>+</sup></sub> / [H<sup>+</sup>]<sub>2</sub></strong> = 10<sup>&minus;4</sup> / 10<sup>&minus;4</sup> = 1 Lít = 1000 mL.
          <br>&bull; Lượng nước cất cần thêm vào: <strong>V<sub>nước</sub> = V<sub>2</sub> &minus; V<sub>1</sub></strong> = 1000 &minus; 10 = 990 mL.</p>
        </div>
      </div>

      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="answer-content">
        🎉 <strong>ĐÁP SỐ: V<sub>nước thêm vào</sub> = 990 mL</strong>
        <p><em>Lời gia sư bình phẩm:</em> Nhớ kĩ: V2 là thể tích tổng cả cốc sau khi pha, đề bài hỏi lượng nước <em>thêm vào</em> thì phải lấy V2 trừ đi V1 ban đầu. Đứa nào kết luận 1000 mL là bị trừ nửa số điểm oan uổng!</p>
      </div>
    </div>
  </div>

  <!-- BÀI KIỂM TRA 15 CÂU BÀI 2 -->
  <div class="quiz-section" id="b2-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">Bài Kiểm Tra Kiến Thức Bài 2 (Chuẩn Độ Khó Giữa Kì)</div>
        <div class="quiz-sub">Gồm 8 câu trắc nghiệm + 4 câu đúng/sai + 3 câu tự luận</div>
      </div>
      <div class="quiz-score-badge" id="b2-score">Điểm: 0/15</div>
    </div>

    <!-- TRẮC NGHIỆM 1-8 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 1 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Dung dịch chất nào sau đây KHÔNG dẫn được điện?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q1" value="A"> A. Dung dịch NaCl</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="B"> B. Dung dịch HCl</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="C"> C. Dung dịch đường saccarozơ (C<sub>12</sub>H<sub>22</sub>O<sub>11</sub>)</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="D"> D. Dung dịch NaOH</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Đường saccarozơ là chất không điện li, tan trong nước ở dạng phân tử trung hòa, không tạo ion nên không dẫn điện. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 2 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Chất nào sau đây là chất điện li YẾU?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q2" value="A"> A. HNO<sub>3</sub></label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="B"> B. CH<sub>3</sub>COOH</label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="C"> C. KOH</label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="D"> D. BaCl<sub>2</sub></label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> CH3COOH (axit axetic) là axit hữu cơ yếu, trong dung dịch chỉ phân li một phần. Các chất còn lại là axit mạnh, bazơ mạnh và muối tan (điện li mạnh). Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 3 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Theo thuyết Brønsted &ndash; Lowry, ion nào sau đây là chất LƯỠNG TÍNH?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q3" value="A"> A. SO<sub>4</sub><sup>2&minus;</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="B"> B. Cl<sup>&minus;</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="C"> C. NH<sub>4</sub><sup>+</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="D"> D. HCO<sub>3</sub><sup>&minus;</sup></label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> HCO3- vừa có thể nhường H+ tạo CO3(2-) (tính acid), vừa có thể nhận H+ tạo H2CO3 (tính base) &rarr; lưỡng tính. Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 4 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Một dung dịch có [H<sup>+</sup>] = 1,0 &times; 10<sup>&minus;3</sup> M. Giá trị pH của dung dịch này là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q4" value="A"> A. 3</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="B"> B. 11</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="C"> C. &minus;3</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="D"> D. 7</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> pH = -log[H+] = -log(10^-3) = 3. Chọn A.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 5 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Dung dịch Ba(OH)<sub>2</sub> 0,005 M có giá trị pH bằng bao nhiêu ở 25&deg;C?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q5" value="A"> A. 2</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="B"> B. 11,7</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="C"> C. 12</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="D"> D. 2,3</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Ba(OH)2 &rarr; Ba2+ + 2OH-. Nồng độ [OH-] = 2 &times; 0,005 = 0,01 M = 10^-2 M &rarr; pOH = 2 &rarr; pH = 14 - 2 = 12. Chọn C.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 6 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Khi nhỏ vài giọt dung dịch phenolphthalein vào dung dịch NaOH, dung dịch sẽ chuyển sang màu:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q6" value="A"> A. Đỏ</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="B"> B. Hồng tím</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="C"> C. Xanh</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="D"> D. Vàng</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Phenolphthalein không màu trong môi trường acid và trung tính, chuyển sang màu hồng tím trong môi trường kiềm (pH &gt; 8,3). Chọn B.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 7 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Chuẩn độ 20 mL dung dịch HCl chưa biết nồng độ cần dùng vừa đủ 15 mL dung dịch NaOH 0,1 M (chỉ thị phenolphthalein). Nồng độ mol của dung dịch HCl là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q7" value="A"> A. 0,100 M</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="B"> B. 0,133 M</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="C"> C. 0,050 M</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="D"> D. 0,075 M</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Phản ứng: HCl + NaOH &rarr; NaCl + H2O (tỉ lệ 1:1). Ta có: C_HCl &times; V_HCl = C_NaOH &times; V_NaOH &rArr; C_HCl &times; 20 = 0,1 &times; 15 &rArr; C_HCl = 1,5 / 20 = 0,075 M. Chọn D.</div>
    </div>

    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 (Trắc nghiệm)</div>
      <div class="quiz-q-text">Ở 25&deg;C, tích số ion của nước Kw bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q8" value="A"> A. 1,0 &times; 10<sup>&minus;14</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="B"> B. 1,0 &times; 10<sup>&minus;7</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="C"> C. 1,0 &times; 10<sup>14</sup></label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="D"> D. 7,0</label>
      </div>
      <div class="quiz-explain"><strong>Giải thích:</strong> Kw = [H+][OH-] = 1,0 &times; 10^-14 ở 25&deg;C. Chọn A.</div>
    </div>

    <!-- ĐÚNG SAI 9-12 -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 9 (Đúng / Sai)</div>
      <div class="quiz-q-text">Dung dịch nước cất tinh khiết dẫn điện tốt do có nhiều ion tự do.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Nước cất tinh khiết điện li cực kì yếu (chỉ 10^-7 mol/L), hầu như không dẫn điện.</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 10 (Đúng / Sai)</div>
      <div class="quiz-q-text">Theo thuyết Brønsted &ndash; Lowry, ion NH<sub>4</sub><sup>+</sup> đóng vai trò là một acid vì có khả năng nhường H<sup>+</sup>.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> NH4+ + H2O &hArr; NH3 + H3O+ (cho H+ nên là acid).</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 11 (Đúng / Sai)</div>
      <div class="quiz-q-text">Khi pha loãng một dung dịch HCl có pH = 3 bằng cách thêm nhiều nước cất, giá trị pH có thể tăng lên đến 8.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: SAI.</strong> Pha loãng dung dịch acid thì pH tăng dần nhưng TIỆM CẬN 7 chứ KHÔNG BAO GIỜ VƯỢT QUÁ 7 (không thể biến acid thành base).</div>
    </div>

    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 12 (Đúng / Sai)</div>
      <div class="quiz-q-text">Dung dịch có pH = 4 có nồng độ ion H<sup>+</sup> gấp 10 lần dung dịch có pH = 5.</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain"><strong>Đáp án: ĐÚNG.</strong> pH = 4 &rarr; [H+] = 10^-4 M; pH = 5 &rarr; [H+] = 10^-5 M. 10^-4 / 10^-5 = 10 lần (thang logarit).</div>
    </div>

    <!-- TỰ LUẬN 13-15 -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 13 (Tự luận thực tế)</div>
      <div class="quiz-q-text">Người nông dân thường bón vôi sống (CaO) hoặc vôi tôi (Ca(OH)<sub>2</sub>) vào các chân ruộng bị chua hoặc ao nuôi tôm cá có độ pH thấp. Em hãy giải thích cơ chế hóa học của biện pháp này?</div>
      <textarea placeholder="Giải thích cơ chế trung hòa độ pH..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>1. Ruộng bị "chua" tức là đất/nước có tính acid cao, nồng độ ion H<sup>+</sup> dư thừa nhiều khiến pH &lt; 7 làm cây trồng và thủy sản chậm lớn hoặc chết.
        <br>2. Khi bón vôi CaO hoặc Ca(OH)<sub>2</sub> vào nước, vôi tan tạo ra ion OH<sup>&minus;</sup>: CaO + H<sub>2</sub>O &rarr; Ca<sup>2+</sup> + 2OH<sup>&minus;</sup>.
        <br>3. Ion OH<sup>&minus;</sup> sẽ lập tức phản ứng trung hòa với ion H<sup>+</sup> gây chua: <code>H<sup>+</sup> + OH<sup>&minus;</sup> &rarr; H<sub>2</sub>O</code>, làm giảm [H<sup>+</sup>], qua đó nâng độ pH của đất và nước ao lên mức an toàn (pH từ 7,0 đến 8,0).
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 (Tự luận tính toán)</div>
      <div class="quiz-q-text">Cần thêm bao nhiêu mL nước cất vào 100 mL dung dịch HCl có pH = 2 để thu được dung dịch mới có pH = 3?</div>
      <textarea placeholder="Nháp các bước tính toán..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI CHI TIẾT:</strong>
        <br>&bull; Dung dịch ban đầu: pH<sub>1</sub> = 2 &rArr; [H<sup>+</sup>]<sub>1</sub> = 10<sup>&minus;2</sup> M = 0,01 M; Thể tích V<sub>1</sub> = 100 mL = 0,1 L.
        <br>&bull; Số mol H<sup>+</sup>: n<sub>H<sup>+</sup></sub> = 0,01 &times; 0,1 = 0,001 mol.
        <br>&bull; Dung dịch sau pha loãng: pH<sub>2</sub> = 3 &rArr; [H<sup>+</sup>]<sub>2</sub> = 10<sup>&minus;3</sup> M = 0,001 M.
        <br>&bull; Thể tích dung dịch sau pha loãng: V<sub>2</sub> = n<sub>H<sup>+</sup></sub> / [H<sup>+</sup>]<sub>2</sub> = 0,001 / 0,001 = 1 L = 1000 mL.
        <br>&bull; Lượng nước cất cần thêm vào: V<sub>nước</sub> = V<sub>2</sub> &minus; V<sub>1</sub> = 1000 &minus; 100 = <strong>900 mL</strong>.
        <br><em>(Mẹo trắc nghiệm: pH tăng 1 đơn vị thì thể tích dung dịch phải tăng 10 lần &rarr; 100 mL tăng thành 1000 mL &rarr; thêm 900 mL nước).</em>
      </div>
    </div>

    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 (Tự luận lý thuyết)</div>
      <div class="quiz-q-text">Dựa vào thuyết Brønsted &ndash; Lowry, hãy viết phương trình hóa học chứng minh các chất sau có tính base trong nước: NH<sub>3</sub> và ion CH<sub>3</sub>COO<sup>&minus;</sup>.</div>
      <textarea placeholder="Viết các phản ứng nhận proton H+..."></textarea>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu nghĩ sai!</button>
      <div class="sample-answer">
        <strong>LỜI GIẢI:</strong>
        <br>Theo thuyết Brønsted &ndash; Lowry, chất có tính base là chất có khả năng NHẬN proton (H<sup>+</sup>):
        <br>1. Phân tử NH<sub>3</sub> nhận H<sup>+</sup> từ phân tử nước:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>NH<sub>3</sub> + H<sub>2</sub>O &hArr; NH<sub>4</sub><sup>+</sup> + OH<sup>&minus;</sup></code> (tạo ion OH<sup>&minus;</sup> làm môi trường có tính base).
        <br>2. Ion CH<sub>3</sub>COO<sup>&minus;</sup> nhận H<sup>+</sup> từ phân tử nước:
        <br>&nbsp;&nbsp;&nbsp;&nbsp;<code>CH<sub>3</sub>COO<sup>&minus;</sup> + H<sub>2</sub>O &hArr; CH<sub>3</sub>COOH + OH<sup>&minus;</sup></code> (sinh ra OH<sup>&minus;</sup> khiến dung dịch muối CH<sub>3</sub>COONa có môi trường kiềm yếu, pH &gt; 7).
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b2')">📊 Nộp Bài & Chấm Điểm Bài 2</button>
  </div>
</section>
"""
