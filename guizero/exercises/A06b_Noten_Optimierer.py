# Function to update text widgets


from guizero import App, Slider, Text, TitleBox, Box, CheckBox, PushButton


def update_text1():
    text1.value = int(slider1.value) / 10
    calc_avg()


def update_text2():
    text2.value = int(slider2.value) / 10
    calc_avg()


def update_text3():
    text3.value = int(slider3.value) / 10
    calc_avg()


def update_text4():
    text4.value = int(slider4.value) / 10
    calc_avg()


def update_text5():
    text5.value = int(slider5.value) / 10
    calc_avg()


def calc_avg(manual=False):
    if manual or check_auto.value:
        avg = (int(slider1.value) * check1.value + int(slider2.value) * check2.value +
               int(slider3.value) * check3.value + int(slider4.value) * check4.value + int(slider5.value) * check5.value) / (check1.value + check2.value + check3.value + check4.value + check5.value)
        text_avg.value = f"{round(avg / 10, 2):.2f}"

# Methods to enable/disable sliders


def enable_slider1():
    enable_slider(slider1, check1.value)


def enable_slider2():
    enable_slider(slider2, check2.value)


def enable_slider3():
    enable_slider(slider3, check3.value)


def enable_slider4():
    enable_slider(slider4, check4.value)


def enable_slider5():
    enable_slider(slider5, check5.value)


def enable_slider(slider, check):
    if check:
        slider.enable()
    else:
        slider.disable()

    # If only one checkbox active, set this one to disable
    if check1.value + check2.value + check3.value + check4.value + check5.value == 1:
        if check1.value:
            check1.disable()
        elif check2.value:
            check2.disable()
        elif check3.value:
            check3.disable()
        elif check4.value:
            check4.disable()
        elif check5.value:
            check5.disable()
    else:
        check1.enable()
        check2.enable()
        check3.enable()
        check4.enable()
        check5.enable()

    calc_avg()


app = App(title="Noten-Optimierer", width=210, height=290, layout="grid")
sliderbox = TitleBox(app, text="Noten", grid=[0, 0, 2, 1],
                     width="fill", height="fill", layout="grid")

# Create 5 Labels for the sliders with Note 1, Note 2, etc.
text1 = Text(sliderbox, text="Note 1", grid=[0, 0])
text2 = Text(sliderbox, text="Note 2", grid=[1, 0])
text3 = Text(sliderbox, text="Note 3", grid=[2, 0])
text4 = Text(sliderbox, text="Note 4", grid=[3, 0])
text5 = Text(sliderbox, text="Note 5", grid=[4, 0])

# Create 5 sliders
limits = (10, 60)
slider1 = Slider(sliderbox, start=limits[1], end=limits[0], grid=[
                 0, 1], command=update_text1, horizontal=False)
slider2 = Slider(sliderbox, start=limits[1], end=limits[0], grid=[
                 1, 1], command=update_text2, horizontal=False)
slider3 = Slider(sliderbox, start=limits[1], end=limits[0], grid=[
                 2, 1], command=update_text3, horizontal=False)
slider4 = Slider(sliderbox, start=limits[1], end=limits[0], grid=[
                 3, 1], command=update_text4, horizontal=False)
slider5 = Slider(sliderbox, start=limits[1], end=limits[0], grid=[
                 4, 1], command=update_text5, horizontal=False)
slider1.value = 50
slider2.value = 50
slider3.value = 50
slider4.value = 50
slider5.value = 50


# Create 5 text widgets
text1 = Text(sliderbox, text="1", grid=[0, 2])
text2 = Text(sliderbox, text="1", grid=[1, 2])
text3 = Text(sliderbox, text="1", grid=[2, 2])
text4 = Text(sliderbox, text="1", grid=[3, 2])
text5 = Text(sliderbox, text="1", grid=[4, 2])

# Create a checkbox to enable/disable the sliders for each slider
check1 = CheckBox(sliderbox, text="", grid=[
                  0, 3], command=enable_slider1, enabled=False)
check2 = CheckBox(sliderbox, text="", grid=[1, 3], command=enable_slider2)
check3 = CheckBox(sliderbox, text="", grid=[2, 3], command=enable_slider3)
check4 = CheckBox(sliderbox, text="", grid=[3, 3], command=enable_slider4)
check5 = CheckBox(sliderbox, text="", grid=[4, 3], command=enable_slider5)

# Create a box for the average
avgbox = Box(app, grid=[0, 1], layout="grid")
lbl_avg = Text(avgbox, text="Notenschnitt: ", grid=[0, 2])
text_avg = Text(avgbox, text="...", grid=[1, 2])

# Add Checkbox to enable automatic calculation of average
check_auto = CheckBox(avgbox, text="Automatisch berechnen", grid=[0, 0, 2, 1])
check_auto.value = False
# Add button to calculate average
btn_avg = PushButton(avgbox, text="Berechnen", grid=[
                     0, 1, 2, 1], command=calc_avg, args=[True])


check1.value = True
check2.value = True
check3.value = True
check4.value = False
check5.value = False

enable_slider1()
enable_slider2()
enable_slider3()
enable_slider4()
enable_slider5()
calc_avg()

app.display()
