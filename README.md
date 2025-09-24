<div align="center">

# 🦺 NHẬN DIỆN THIẾT BỊ BẢO HỘ LAO ĐỘNG (PPE) TẠI CÔNG TRƯỜNG  

<img src="thicong.jpg" alt="Logo" width="1000"/>

---

### 🔬 Ứng dụng trí tuệ nhân tạo trong giám sát an toàn lao động thông qua nhận diện PPE  

**Hệ thống phát hiện thiết bị bảo hộ cá nhân bắt buộc bằng YOLOv8 và Streamlit**  

</div>

---

## 🔎 Giới thiệu  

Trong các công trường xây dựng, việc tuân thủ **quy định về sử dụng thiết bị bảo hộ cá nhân (PPE)** là bắt buộc nhằm đảm bảo an toàn cho người lao động. Tuy nhiên, trên thực tế vẫn còn tình trạng công nhân **không mang hoặc mang thiếu PPE**, gây nguy cơ tai nạn.  

Hệ thống **PPE Detection System** được xây dựng nhằm **tự động nhận diện và cảnh báo vi phạm PPE trong thời gian thực**, từ đó hỗ trợ công tác quản lý, giám sát và nâng cao ý thức tuân thủ quy định an toàn lao động.  

---

## 🏗️ Kiến trúc hệ thống  

Quy trình hoạt động của hệ thống được triển khai qua các bước:  

1. **Tải dữ liệu đầu vào**: Người dùng cung cấp video, hình ảnh hoặc camera trực tiếp từ công trường.  
2. **Xử lý khung hình**: Các frame được trích xuất và đưa vào mô hình YOLO.  
3. **Nhận diện đối tượng**: YOLOv8 phát hiện người và thiết bị PPE (mũ, áo, găng tay, kính, giày).  
4. **Xác định vi phạm**: So sánh với danh sách PPE bắt buộc để xác định trường hợp vi phạm.  
5. **Hiển thị kết quả**:  
   - Vẽ bounding box trực tiếp trên video/hình ảnh.  
   - Lưu ảnh vi phạm kèm timestamp vào thư mục `violations/`.  
6. **Thống kê báo cáo**: Xuất dashboard với số vi phạm theo ngày/tháng và phân loại theo loại PPE bị thiếu.  

---

## ✨ Tính năng chính  

- 🎥 **Nhận diện vi phạm PPE thời gian thực** trên video hoặc camera.  
- 🧑‍🤝‍🧑 **Theo dõi công nhân** và phát hiện thiếu PPE (mũ, áo, găng tay, kính, giày).  
- 🖼️ **Lưu bằng chứng vi phạm** (ảnh + thời gian).  
- 📊 **Dashboard thống kê** số lượng vi phạm theo thời gian và theo loại PPE.  
- 🌐 **Giao diện web trực quan** được xây dựng bằng Streamlit.  

---

## 🔧 Công nghệ sử dụng  

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)  
- [![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=ai&logoColor=black)](https://github.com/ultralytics/ultralytics)  
- [![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)  
- [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)  
- Pandas, Matplotlib  

---

## 📊 Kết quả thử nghiệm  

<img src="violations/22.jpg" alt="Kết quả vi phạm" width="800"/>  

- Hệ thống đã phát hiện công nhân **thiếu PPE bắt buộc** (ví dụ: không đội mũ, không đeo găng tay).  
- Mỗi trường hợp vi phạm được **lưu kèm ảnh minh họa và thời gian phát hiện** trong thư mục `violations/`.  
- **Dashboard thống kê** cho phép người quản lý dễ dàng theo dõi tình trạng tuân thủ PPE theo ca, ngày, hoặc tháng.  
- Kết quả cho thấy hệ thống có khả năng hoạt động ổn định trong môi trường công trường thực tế.  

---

## 📂 Cấu trúc thư mục  

