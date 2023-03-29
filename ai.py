import tkinter as tk
import openai


openai.api_key = "openai dan olgan api ni shu yerga qoyasiz"


model_engine = "text-davinci-002"
max_tokens = 100


def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens
    )
    message = completions.choices[0].text
    return message


def send_message(event=None):
    user_input = user_input_field.get()
    user_input_field.delete(0, tk.END)
    chat_history.insert(tk.END, f"Siz : {user_input}")
    prompt = "\n".join(chat_history.get("1.0", tk.END).split("\n")[-5:])
    message = generate_text(prompt)
    chat_history.insert(tk.END, f"\n\nAI : {message}", "bot")
    chat_history.see(tk.END)


def clear_chat_history():
    chat_history.delete("1.0", tk.END)

root = tk.Tk()
root.title("ChatGPT")

chat_history = tk.Text(root, height=20, width=50, wrap=tk.WORD, font=("Helvetica", 12))
chat_history.tag_config("bot", foreground="blue")
chat_history.pack(side=tk.TOP, padx=10, pady=10)


user_input_field = tk.Entry(root, width=50, font=("Helvetica", 12))
user_input_field.bind("<Return>", send_message)
user_input_field.pack(side=tk.BOTTOM, padx=10, pady=10)


send_button = tk.Button(root, text="Send", font=("Helvetica", 12), bg="light green", fg="black", command=send_message)
send_button.pack(side=tk.LEFT, padx=20, pady=10)


clear_button = tk.Button(root, text="Clear", font=("Helvetica", 12), bg="red", fg="white", command=clear_chat_history)
clear_button.pack(side=tk.LEFT, padx=20, pady=10)

root.mainloop()
