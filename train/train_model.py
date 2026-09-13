import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# 1. Đọc dataset
data = pd.read_csv("data/spam.csv")

print("===== DATASET =====")
print(data.head())

print("\nSố lượng dữ liệu:", len(data))

print("\nPhân bố dữ liệu:")
print(data["label"].value_counts())


# 2. Lấy dữ liệu đầu vào và nhãn
X = data["message"]
y = data["label"]


# 3. Chia dữ liệu train và test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 4. Tạo mô hình Naive Bayes
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("naive_bayes", MultinomialNB())
])


# 5. Huấn luyện mô hình
print("\n===== TRAINING =====")

model.fit(X_train, y_train)

print("Đã huấn luyện xong!")


# 6. Dự đoán dữ liệu test
y_pred = model.predict(X_test)


# 7. Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)

print("\n===== KẾT QUẢ =====")

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 8. Lưu mô hình
joblib.dump(model, "models/spam_model.pkl")

print("\nĐã lưu mô hình tại:")
print("models/spam_model.pkl")