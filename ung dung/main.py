from guizero import App, Box, TextBox, Text, ListBox, PushButton, Combo, Slider, ButtonGroup, Drawing
import os
app = App(title="Nhà ráng tạo meme", width=700, height=500)

current_img_path = None

def load_img():
    img_file = []
    for f in os.listdir("images"):
        if f.endswith(('.png', '.jpg', '.jpeg')):
            img_file.append(f)
    return img_file

def show_img(slected_img):
    global current_img_path
    current_img_path = f"images/{slected_img}"

    drawing_img.image(0,0, current_img_path, width=200, height=200)

def update_meme():
    drawing_img.clear()

    drawing_img.text(
        0,0, text_box.value, color = color_combo.value, font=font_group.value
    )


main_box = Box(app, layout="grid", border=True)
khung_dieu_khien_1 = Box(main_box, align="top", width="fill", grid=[0, 0])
Text(khung_dieu_khien_1, text="ENTER TEXT:", align="left", width=15)
text_box = TextBox(khung_dieu_khien_1, align="left", width=30)

khung_dieu_khien_2 = Box(main_box, align="top", width="fill", grid=[0, 1])
Text(khung_dieu_khien_2, text="Select text color:", align="left", width=15)
color_combo = Combo(khung_dieu_khien_2, options = ["Green", "Blue", "Yellow", "Black"], align="left")

khung_dieu_khien_3 = Box(main_box, align="top", width="fill", grid=[0, 3])
Text(khung_dieu_khien_3, text="Select Font:", align="left", width=15)
font_group = ButtonGroup(khung_dieu_khien_3, options=["Arial", "Times New Roman"], selected="Arial", align="left", horizontal=False)

main_box_2 = Box(app, layout="grid")
khung_dieu_khien_5 = Box(main_box_2, align="top", width="fill", grid=[0, 4])
Text(khung_dieu_khien_5, text="Select meme sticker:", align="left", width=15)
combo = Combo(khung_dieu_khien_5, options = ["Car", "Square"], align="left")

khung_dieu_khien_6 = Box(main_box_2, align="top", width="fill", grid=[0, 5])
Text(khung_dieu_khien_6, text="X:", align="left", width=15)
slider = Slider(khung_dieu_khien_6, start=100, end=200, align="left")

khung_dieu_khien_7 = Box(main_box_2, align="top", width="fill", grid=[0, 6])
Text(khung_dieu_khien_7, text="Y:", align="left", width=15)
slider = Slider(khung_dieu_khien_7, start=100, end=200, align="left")

main_box_3 = Box(app, layout="grid")
add_button =PushButton(main_box_3, text="Add meme", grid=[0,0], command=update_meme)
add_button.bg ="white"
add_button.text_color = "black"

main_box_4 = Box(app, layout="grid")
img_listbox = ListBox(main_box_4, items=load_img(), scrollbar=False, grid=[0, 0], command=show_img)
img_listbox.bg = "white"
img_listbox.text_color = "black"

drawing_img = Drawing(main_box_4, width=200, height=200, grid=[1, 0])
drawing_img.bg = "white"

app.display()