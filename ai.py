import tkinter as tk
import openai

# Api
openai.api_key = "openai dan olgan api ni shu yerga qoyasiz"

# ChatGPT model parametrlari
model_engine = "text-babbage-001"
max_tokens = 100

# Chatgpt modeli yordamida matnni yaratish funksiyasi
def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens
    )
    message = completions.choices[0].text
    return message

# chatgpt dan javob olish
def send_message(event=None):
    user_input = user_input_field.get()
    user_input_field.delete(0, tk.END)
    chat_history.insert(tk.END, f"Siz: {user_input}")
    prompt = "\n".join(chat_history.get("1.0", tk.END).split("\n")[-5:])
    message = generate_text(prompt)
    chat_history.insert(tk.END, f"ChatGPT: {message}")
    chat_history.see(tk.END)

# tarixni tozalash funksiyasi
def clear_chat_history():
    chat_history.delete("1.0", tk.END)

# Oyna yaratish
root = tk.Tk()
root.title("ChatGPT")

# chat tarixi
chat_history = tk.Text(root, height=20, width=50, wrap=tk.WORD, font=("Helvetica", 12))
chat_history.pack(side=tk.TOP, padx=10, pady=10)

# Foydalanuvchi kiritish maydoni
user_input_field = tk.Entry(root, width=50, font=("Helvetica", 12))
user_input_field.bind("<Return>", send_message)
user_input_field.pack(side=tk.BOTTOM, padx=10, pady=10)

# Yuborish
send_button = tk.Button(root, text="Yuborish", font=("Helvetica", 12), bg="green", fg="black", command=send_message)
send_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Tozalash
clear_button = tk.Button(root, text="Tozalash", font=("Helvetica", 12), bg="red", fg="white", command=clear_chat_history)
clear_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Dasturni ishga tushirish
root.mainloop()


# telegram : @khasanov_shohjahon