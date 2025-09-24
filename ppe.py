import streamlit as st
from ultralytics import YOLO
import cv2
import os
from datetime import datetime
import tempfile


model = YOLO("best.pt")  # Load model PPE
save_dir = "violations"
os.makedirs(save_dir, exist_ok=True)
required_ppe = {"hardhat", "safety vest", "mask"}


st.set_page_config(page_title="PPE Detection", page_icon="🦺", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<p class="big-title">🦺 PPE Detection System</p>', unsafe_allow_html=True)
st.markdown('<p class="big-subtitle">Hệ thống nhận diện thiết bị bảo hộ của công nhân tại công trường </p>', unsafe_allow_html=True)
st.write("---")

# Sidebar
st.sidebar.header("⚙️ Cài đặt hệ thống")
uploaded_file = st.sidebar.file_uploader("📂 Tải video công trường", type=["mp4", "avi", "mov"])
save_interval = st.sidebar.slider("⏱️ Thời gian lưu ảnh vi phạm (giây)", 3, 15, 5)
conf_threshold = st.sidebar.slider("🎯 Ngưỡng tin cậy", 0.3, 0.9, 0.5)

# Main layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 Thông tin")
    st.info(
        f"""
        **PPE bắt buộc**:
        - 🪖 Mũ bảo hộ  
        - 👕 Áo phản quang  
        - 😷 Khẩu trang  
        """
    )
  

with col2:
    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(uploaded_file.read())
        video_path = tfile.name

        # Hiển thị video gốc
        st.video(video_path)

        if st.button("▶️ Bắt đầu nhận diện", type="primary"):
            cap = cv2.VideoCapture(video_path)

            last_save_time = None
            stframe = st.empty()
            saved_images = []  # danh sách ảnh vi phạm đã lưu

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = model(frame)
                violation_found = False
                person_ppe = {}
                person_boxes = {}

                for result in results:
                    boxes = result.boxes
                    names = model.names

                    for box in boxes:
                        cls_id = int(box.cls[0])
                        label = names[cls_id].lower()
                        conf = float(box.conf[0])
                        if conf < conf_threshold:
                            continue
                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        color = (0, 255, 0)
                        if "no" in label:
                            color = (0, 0, 255)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                        cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

                        if "person" in label:
                            pid = len(person_ppe) + 1
                            person_ppe[pid] = set()
                            person_boxes[pid] = (x1, y1, x2, y2)
                        elif any(ppe in label for ppe in required_ppe):
                            if len(person_ppe) > 0:
                                person_ppe[list(person_ppe.keys())[-1]].add(label)

                for pid, ppe_set in person_ppe.items():
                    missing = required_ppe - ppe_set
                    if missing:
                        violation_found = True
                        x1, y1, x2, y2 = person_boxes[pid]
                        cv2.putText(frame, f"Thiếu: {', '.join(missing)}", (x1, y2 + 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                if violation_found:
                    now = datetime.now()
                    if last_save_time is None or (now - last_save_time).total_seconds() >= save_interval:
                        timestamp = now.strftime("%Y%m%d_%H%M%S")
                        save_path = os.path.join(save_dir, f"phathienvipham_{timestamp}.jpg")
                        cv2.imwrite(save_path, frame)
                        saved_images.append(save_path)
                        st.sidebar.error(f"🚨 Ảnh vi phạm đã lưu: {save_path}")
                        last_save_time = now

                frame_resized = cv2.resize(frame, (720, 400))
                stframe.image(frame_resized, channels="BGR")

            cap.release()
            st.success("✅ Nhận diện hoàn tất!")

            # Hiển thị ảnh vi phạm trong web
            if saved_images:
                st.subheader("📸 Ảnh vi phạm đã phát hiện")
                cols = st.columns(3)
                for i, img_path in enumerate(saved_images):
                    cols[i % 3].image(img_path, use_container_width=True)

# Footer
st.markdown('<p class="footer">© 2025 PPE Detection System - Demo</p>', unsafe_allow_html=True)
