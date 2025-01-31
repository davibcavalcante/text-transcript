import os
import tkinter as tk
from tkinter import filedialog, messagebox
from api.transcript import get_transcription

def reset_labels():
  file_path.set('Selecione o arquivo a ser transcrito')
  folder_path.set('Selecione a pasta para salvar a transcrição')
  file_name.set('')

def select_file():
  file = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4;*.mp3")])
  if file:
    file_path.set(file)

def select_folder():
  folder = filedialog.askdirectory()
  if folder:
    folder_path.set(folder)

def execute_action():
  file = file_path.get()
  if file:
    loading_screen = create_loading_screen()
    root.after(100, start_transcription, file, loading_screen)
  else:
    messagebox.showwarning("Aviso", "Por favor, selecione um arquivo para ser transcrito")

def start_transcription(file, loading_screen):
  transcript = get_transcription(file)
  loading_screen.destroy()

  if transcript.status == 'error':
    messagebox.showinfo("Falha", "A transcrição falhou, tente novamente um arquivo diferente.")
    print("A transcrição falhou, tente novamente um arquivo diferente.")
    reset_labels()

  elif transcript.status == 'completed':
    messagebox.showinfo("Sucesso", f"Transcrição concluída com sucesso!\nO arquivo foi salvo em: {folder_path.get()}")
    output_file = os.path.join(folder_path.get(), f"{file_name.get()}.txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
      f.write(transcript.text)

    print("Transcrição concluída com sucesso!\nO arquivo foi salvo em:", folder_path.get())
    reset_labels()

def create_loading_screen():
  loading_screen = tk.Toplevel(root)
  loading_screen.title("Carregando...")
  loading_screen.geometry("300x100")
  label = tk.Label(loading_screen, text="Transcrição em andamento, por favor aguarde...")
  label.pack(expand=True)
  return loading_screen

def setup_ui():
  global file_path, folder_path, file_name

  file_path = tk.StringVar()
  folder_path = tk.StringVar()
  file_name = tk.StringVar()

  reset_labels()

  btn_select_file = tk.Button(root, text="Selecionar Arquivo", command=select_file, width=20)
  btn_select_file.grid(row=0, column=0, padx=10, pady=10, sticky="w")

  label_file = tk.Label(root, textvariable=file_path, wraplength=350, fg="blue")
  label_file.grid(row=0, column=1, padx=10, pady=10, sticky="w")

  btn_select_folder = tk.Button(root, text="Selecionar Pasta", command=select_folder, width=20)
  btn_select_folder.grid(row=1, column=0, padx=10, pady=10, sticky="w")

  label_folder = tk.Label(root, textvariable=folder_path, wraplength=350, fg="blue")
  label_folder.grid(row=1, column=1, padx=10, pady=10, sticky="w")

  label_file_name = tk.Label(root, text="Nome do arquivo", width=20)
  label_file_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")

  entry_file_name = tk.Entry(root, textvariable=file_name, width=30)
  entry_file_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

  btn_confirm = tk.Button(root, text="Confirmar", command=execute_action, width=20)
  btn_confirm.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='w')

def get_root():
  window = tk.Tk()
  window.title("MP4/MP3 Uploader")
  window.geometry("415x180")
  return window

def load_screen():
  global root
  root = get_root()
  setup_ui()
  root.mainloop()