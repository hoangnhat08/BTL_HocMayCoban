# BTL Học Máy Cơ Bản

Dự án bài tập lớn môn **Học máy cơ bản**, tập trung nghiên cứu và xây dựng mô hình **Naive Bayes** cho bài toán phân loại dữ liệu.

##  Giới thiệu

**Naive Bayes** là một thuật toán học máy thuộc nhóm **Supervised Learning**, được xây dựng dựa trên định lý Bayes và giả định rằng các đặc trưng đầu vào độc lập có điều kiện với nhau.

Trong dự án này, nhóm thực hiện các bước cơ bản của một quy trình Machine Learning:

* Thu thập và chuẩn bị dữ liệu
* Tiền xử lý dữ liệu
* Phân tích dữ liệu
* Xây dựng mô hình Naive Bayes
* Huấn luyện mô hình
* Dự đoán dữ liệu
* Đánh giá hiệu năng mô hình
* Kiểm thử API

##  Mục tiêu

Dự án nhằm giúp sinh viên:

* Hiểu được khái niệm Machine Learning.
* Hiểu quy trình xây dựng một mô hình học máy.
* Hiểu nguyên lý hoạt động của thuật toán Naive Bayes.
* Biết cách huấn luyện và sử dụng mô hình Machine Learning bằng Python.
* Biết cách xây dựng API để phục vụ mô hình.
* Biết cách kiểm thử API và mô hình.

##  Thuật toán Naive Bayes

Naive Bayes là thuật toán phân loại dựa trên **định lý Bayes**:

```text
P(A|B) = P(B|A)P(A) / P(B)
```

Trong Machine Learning, mô hình sử dụng xác suất của các đặc trưng để dự đoán lớp của một mẫu dữ liệu mới.

Tên "Naive" xuất phát từ giả định đơn giản rằng các đặc trưng đầu vào độc lập với nhau khi đã biết lớp.

### Một số ưu điểm

* Đơn giản và dễ triển khai.
* Tốc độ huấn luyện nhanh.
* Hoạt động tốt với nhiều bài toán phân loại.
* Phù hợp với dữ liệu có số lượng đặc trưng lớn.

### Một số hạn chế

* Giả định các đặc trưng độc lập có thể không đúng trong thực tế.
* Hiệu quả có thể giảm khi các đặc trưng có mối quan hệ phụ thuộc mạnh.

##  Cấu trúc dự án

```text
BTL_HocMayCoban/
│
├── app/
│   └── main.py
│
├── backend/
│   └── server.py
│
├── tests/
│   └── test_api.py
│
├── train/
│   └── train_model.py
│
├── .gitignore
│
└── README.md
```

### Mô tả các thư mục

| Thư mục/File           | Chức năng                          |
| ---------------------- | ---------------------------------- |
| `app/`                 | Chứa mã nguồn ứng dụng chính       |
| `app/main.py`          | File chính của ứng dụng            |
| `backend/`             | Chứa phần xử lý backend/API        |
| `backend/server.py`    | Khởi tạo và xử lý server           |
| `train/`               | Chứa mã nguồn huấn luyện mô hình   |
| `train/train_model.py` | Thực hiện quá trình train model    |
| `tests/`               | Chứa các file kiểm thử             |
| `tests/test_model.py`    | Kiểm thử API                       |
| `.gitignore`           | Các file/thư mục không đưa lên Git |
| `README.md`            | Tài liệu mô tả dự án               |

## ⚙ Yêu cầu môi trường

Dự án được phát triển bằng **Python**.

Khuyến nghị sử dụng:

```text
Python 3.x
PyCharm
Git
```

##  Cài đặt

Clone project từ GitHub:

```bash
git clone https://github.com/hoangnhat08/BTL_HocMayCoban.git
```

Di chuyển vào thư mục project:

```bash
cd BTL_HocMayCoban
```

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell báo lỗi do Execution Policy, có thể sử dụng:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Sau đó kích hoạt lại:

```powershell
.\.venv\Scripts\Activate.ps1
```

##  Cài đặt thư viện

Nếu project có file `requirements.txt`, cài đặt bằng:

```bash
pip install -r requirements.txt
```

Hoặc cài đặt các thư viện cần thiết tùy theo quá trình phát triển project.

##  Huấn luyện mô hình

File huấn luyện mô hình:

```text
train/train_model.py
```

Chạy:

```bash
python train/train_model.py
```

Quá trình huấn luyện bao gồm các bước cơ bản:

```text
Dataset
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Naive Bayes
   ↓
Training
   ↓
Prediction
   ↓
Evaluation
```

##  Kiểm thử

Các file kiểm thử được đặt trong:

```text
tests/
```

File kiểm thử API:

```text
tests/test_api.py
```

Nếu sử dụng `pytest`, chạy:

```bash
pytest
```

##  Backend / API

Backend được triển khai trong:

```text
backend/server.py
```

API có nhiệm vụ tiếp nhận dữ liệu từ phía client và xử lý các yêu cầu liên quan đến mô hình Machine Learning.

Có thể chạy backend tùy theo cấu hình của project.

##  Đánh giá mô hình

Sau khi huấn luyện, mô hình có thể được đánh giá bằng các chỉ số phổ biến trong bài toán phân loại:

### Accuracy

```text
Accuracy = Số dự đoán đúng / Tổng số mẫu
```

Accuracy cho biết tỷ lệ dự đoán chính xác của mô hình.

### Precision

Đánh giá mức độ chính xác của các mẫu được mô hình dự đoán thuộc một lớp.

### Recall

Đánh giá khả năng mô hình tìm ra các mẫu thực sự thuộc một lớp.

### F1-Score

Là trung bình điều hòa của Precision và Recall:

```text
F1 = 2 × Precision × Recall / (Precision + Recall)
```

##  Quy trình Machine Learning

Quy trình của dự án:

```text
Xác định bài toán
       ↓
Thu thập dữ liệu
       ↓
Khám phá dữ liệu (EDA)
       ↓
Tiền xử lý dữ liệu
       ↓
Chia tập Train/Test
       ↓
Huấn luyện Naive Bayes
       ↓
Dự đoán
       ↓
Đánh giá mô hình
       ↓
Triển khai API
       ↓
Kiểm thử
```

##  Git và GitHub

Source code của dự án được quản lý bằng **Git** và lưu trữ trên GitHub.

Repository:

**BTL_HocMayCoban**

https://github.com/hoangnhat08/BTL_HocMayCoban

Các thay đổi được cập nhật bằng:

```bash
git add .
git commit -m "Update project"
git push
```

##  Tác giả

**Nguyễn Hoàng Nhất**

Sinh viên ngành Công nghệ thông tin
Trường Đại học Sư phạm Kỹ thuật Hưng Yên

---



Dự án được thực hiện trong khuôn khổ môn học:

**Học máy cơ bản**

---

> **Note:** README sẽ được cập nhật thêm khi dự án phát triển và bổ sung các chức năng, mô hình, kết quả thực nghiệm và hình ảnh minh họa.
