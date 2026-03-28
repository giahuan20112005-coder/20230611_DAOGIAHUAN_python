import gradio as gr
from google import genai

# 1. Cấu hình SDK MỚI của Google
API_KEY = "AIzaSyAUvjzLNCLW5t8GyybqKRMPNch3Gg39vSA"
client = genai.Client(api_key=API_KEY)

# 2. Hàm xử lý chat (Tương thích với mọi bản Gradio)
def chat_with_gemini(message, history):
    try:
        # Chuyển đổi lịch sử chat sang định dạng của SDK mới
        history_contents = []
        for step in history:
            # Gradio mặc định lưu history dạng list gồm 2 phần tử [user_text, bot_text]
            if isinstance(step, (list, tuple)) and len(step) == 2:
                history_contents.append({"role": "user", "parts": [{"text": step[0]}]})
                history_contents.append({"role": "model", "parts": [{"text": step[1]}]})
        
        # Bắt đầu phiên chat với model mới nhất
        chat = client.chats.create(
            model="gemini-2.5-flash",
            history=history_contents
        )
        
        # Gửi tin nhắn mới và lấy phản hồi
        response = chat.send_message(message)
        return response.text
        
    except Exception as e:
        return f"Lỗi kết nối: {e}"

# 3. CSS Tối giản
css = """
h1 {
    text-align: center; color: #2c3e50; font-family: Arial, sans-serif; margin-top: 10px;
}
"""

# 4. Giao diện (Lược bỏ mọi tham số thừa để tránh lỗi TypeError)
with gr.Blocks() as ung_dung:
    gr.HTML("<h1>🤖 GIAO TIẾP & LẬP TRÌNH CÙNG AI</h1>")
    
    # Chỉ gọi hàm fn cơ bản nhất, Gradio sẽ tự động dựng UI chuẩn
    gr.ChatInterface(fn=chat_with_gemini)
    
    gr.HTML("""
    <div style="text-align: center; margin-top: 20px; font-size: 0.9em; color: #666;">
      Powered by Google GenAI SDK & Gemini 2.5 Flash
    </div>
    """)

# 5. Chạy ứng dụng
if __name__ == "__main__":
    # Đẩy css vào hàm launch theo đúng cảnh báo của Gradio
    ung_dung.launch(inline=False, share=False, css=css)