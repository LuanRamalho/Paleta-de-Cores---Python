import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from colorsys import rgb_to_hsv, hsv_to_rgb

# Função para gerar a paleta harmoniosa
def generate_harmonious_palette(base_color):
    number_of_colors = 5
    base_hue = extract_hue(base_color)
    color_palette = []
    for i in range(number_of_colors):
        hue = (base_hue + (360 / number_of_colors) * i) % 360
        color = hsv_to_rgb(hue / 360, 0.7, 0.5)  # 70% de saturação e 50% de brilho
        color_hex = f'#{int(color[0] * 255):02x}{int(color[1] * 255):02x}{int(color[2] * 255):02x}'
        color_palette.append(color_hex)
    return color_palette

# Função para extrair o valor do matiz (hue) da cor base
def extract_hue(color):
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
    hue, _, _ = rgb_to_hsv(r / 255, g / 255, b / 255)
    return hue * 360

# Função para copiar o código hexadecimal da cor
def copy_code(color_hex):
    root.clipboard_clear()
    root.clipboard_append(color_hex)
    messagebox.showinfo("Copiado!", f"Cor Copiada: {color_hex}")

# Função principal de geração de paleta
def generate_palette():
    base_color = colorchooser.askcolor(title="Selecione a Cor Base")[1]
    if base_color:
        root.configure(bg=base_color)
        for widget in color_palette_container.winfo_children():
            widget.destroy()
        
        palette = generate_harmonious_palette(base_color)
        for color in palette:
            color_box = tk.Label(color_palette_container, bg=color, width=8, height=4, relief="solid")
            color_box.bind("<Button-1>", lambda e, c=color: copy_code(c))
            color_box.pack(side=tk.LEFT, padx=5, pady=5)

# Interface Tkinter
root = tk.Tk()
root.title("Gerador de Paleta de Cores")
root.geometry("400x200")
root.configure(bg="#ffffff")

# Elementos da interface
label = tk.Label(root, text="Selecione a Cor Base:", font=("Poppins", 12), bg="#ffffff")
label.pack(pady=10)

button = tk.Button(root, text="Gerar Paleta", font=("Poppins", 10), command=generate_palette)
button.pack(pady=5)

color_palette_container = tk.Frame(root, bg="#ffffff")
color_palette_container.pack(pady=10)

root.mainloop()
