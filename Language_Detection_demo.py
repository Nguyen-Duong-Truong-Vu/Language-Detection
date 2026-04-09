import joblib
import re

# Hàm clean text (phải giống lúc train)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[!@#$(),\n"%^*?\:\;~\[\]0-9]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Load mô hình
model = joblib.load('language_detector.pkl')

print("=== HỆ THỐNG NHẬN DIỆN NGÔN NGỮ ===")
while True:
    input_text = input("\nNhập câu (hoặc 'q' để thoát): ")
    if input_text.lower() == 'q':
        break
    
    clean_input = clean_text(input_text)
    prediction = model.predict([clean_input])
    print(f"🌍 Dự đoán: {prediction[0]}")
