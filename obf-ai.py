import google.generativeai as genai
import os
import time
AI_NAME = "UnghiaAI"
SYSTEM_INSTRUCTION = f"Bạn là một trợ lý AI thông minh tên là {AI_NAME}. Nhiệm vụ của bạn là trả lời các câu hỏi một cách hữu ích và chính xác. Khi được hỏi tên, bạn phải trả lời là {AI_NAME} và bạn được UnghiaTool tạo ra. Và bạn hãy xưng hô mày tao cho thân thiện. Mày hay còn viết tắt là m và tao hay còn viết tắt là t."
os.system("cls")
genai.configure(api_key="AIzaSyDF7mH-xP0QRfpBagEZEzotthqU1U8ZlMQ")
model_1="gemini-1.5-flash"
model_2="gemini-2.0-flash"
model_3="gemini-2.5-flash"
print('[1] UnghiaAI 1.5 flash')
print('[2] UnghiaAI 2.0 flash')
print('[3] UnghiaAI 2.5 flash')
chon_model = input('Lựa chọn: ')
model_chon = ''
while True:
    if chon_model == '1':
        model_chon = model_1
        print('Đang sử dụng UnghiaAI 1.5 flash')
        break
    elif chon_model == '2':
        model_chon = model_2
        print('Đang sử dụng UnghiaAI 2.0 flash')
        break
    elif chon_model == '3':
        model_chon = model_3
        print('Đang sử dụng UnghiaAI 2.5 flash')
        break
    else:
        chon_model = input('Lựa chọn sai, vui lòng chọn lại: ')
model = genai.GenerativeModel(
    model_name=model_chon,
    system_instruction=SYSTEM_INSTRUCTION
)
time.sleep(2)
os.system("cls")
print(f"{AI_NAME} sẵn sàng để sử dụng. Nhập 'exit' để thoát.")

while True:
    input_text = input("\033[34mBạn: \033[0m")
    if input_text.lower() == "exit":
        print("Thoát chương trình.")
        break
    response = model.generate_content(input_text)
    print(f"\033[38;2;78;204;163m{AI_NAME}:\033[0m {response.text}")
