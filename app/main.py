import joblib

# Load model đã train
model = joblib.load("models/spam_model.pkl")

print("===================================")
print("   NAIVE BAYES - SPAM CLASSIFIER")
print("===================================")

while True:

    message = input("\nNhập nội dung tin nhắn: ")

    # Thoát chương trình
    if message.lower() == "exit":
        print("Đã thoát chương trình.")
        break

    # Dự đoán
    prediction = model.predict([message])[0]

    # Xác suất dự đoán
    probability = model.predict_proba([message]).max()

    print("\n===== KẾT QUẢ =====")

    if prediction == "spam":
        print("⚠️ KẾT QUẢ: SPAM")
    else:
        print("✅ KẾT QUẢ: HAM")

    print(f"Độ tin cậy: {probability:.2%}")