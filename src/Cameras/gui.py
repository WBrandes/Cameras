from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk


class App:

    def __init__(self, parent):

        self.master = Tk()

        self.master.overrideredirect(True)
        self.master.overrideredirect(False)
        self.master.attributes("-fullscreen", True)

        self.parent = parent

        self.current_screen = 0

        relief_pattern = SUNKEN
        border_width = 10

        self.loading_bar_width = int(self.master.winfo_screenwidth() * 0.33)

        #Main Screen
        self.main_screen = Frame(self.master, borderwidth=border_width, relief=relief_pattern)
        # self.main_screen.place(relwidth=1.0, relheight=1.0)

        self.width = self.main_screen.winfo_screenwidth()
        self.height = self.main_screen.winfo_screenheight()

        self.image_holder = Frame(self.main_screen, pady=50)
        self.image_holder.pack()

        self.slide_one = Frame(self.image_holder)
        self.slide_one.grid(row=0, column=0)
        self.slide_two = Frame(self.image_holder)
        self.slide_two.grid(row=0, column=1)
        self.slide_three = Frame(self.image_holder)
        self.slide_three.grid(row=0, column=2)

        self.img_size = int(0.25 * self.width)

        self.img_camera = PIL.Image.open("media/CameraGraphic.png").resize((self.img_size, self.img_size), PIL.Image.ANTIALIAS)
        self.camera_graphic = PIL.ImageTk.PhotoImage(self.img_camera)

        self.img_recording = PIL.Image.open("media/RecordingGraphic.png").resize((self.img_size, self.img_size), PIL.Image.ANTIALIAS)
        self.recording_graphic = PIL.ImageTk.PhotoImage(self.img_recording)

        self.img_processing = PIL.Image.open("media/ProcessingGraphic.png").resize((self.img_size, self.img_size), PIL.Image.ANTIALIAS)
        self.processing_graphic = PIL.ImageTk.PhotoImage(self.img_processing)

        self.image_title_one = Label(self.slide_one, text="Step 1 \n Stand in camera's view",
                                     font=("Times New Roman", 30))
        self.image_title_one.pack()
        self.image_one = Label(self.slide_one, image=self.camera_graphic)
        self.image_one.pack()

        self.image_title_two = Label(self.slide_two, text="Step 2 \n Wait for recording",
                                     font=("Times New Roman", 30))
        self.image_title_two.pack()
        self.image_two = Label(self.slide_two, image=self.recording_graphic)
        self.image_two.pack()

        self.image_title_three = Label(self.slide_three, text="Step 3 \n Processing of video",
                                     font=("Times New Roman", 30))
        self.image_title_three.pack()
        self.image_three = Label(self.slide_three, image=self.processing_graphic)
        self.image_three.pack()

        # self.length_title = Label(self.main_screen, text="Length of Test (seconds)", font=("Times New Roman", 24), wraplength=self.width - 200.0, justify=CENTER)
        # self.length_title.pack()
        #
        # self.length_container = Frame(self.main_screen, pady=20)
        # self.length_container.pack()
        #
        # self.length_setting = StringVar()
        # self.length_setting.set("5")
        # self.length_box = Entry(self.length_container, textvariable=self.length_setting, font=("Times New Roman", 24), justify=CENTER)
        # self.length_box.pack()

        self.start_button = Button(self.main_screen, text="Start", font=("Times New Roman", 24), width=15, pady=10, command=self.start_button)
        self.start_button.pack()



        #Countdown Screen
        self.countdown_screen = Frame(self.master, borderwidth=border_width, relief=relief_pattern)

        self.camera_image = Label(self.countdown_screen)
        self.camera_image.pack()

        Label(self.countdown_screen, text="Countdown", font=("Times New Roman", 48), justify=CENTER).pack()

        self.countdown_timer = Label(self.countdown_screen, text="15", font=("Times New Roman", 48), justify=CENTER)
        self.countdown_timer.pack()

        Label(self.countdown_screen, text="seconds until start", font=("Times New Roman", 48), justify=CENTER).pack()



        #Running Screen
        self.running_screen = Frame(self.master, borderwidth=border_width, relief=relief_pattern)
        # self.running_screen = Button(self.running_screen, text="Continue", font=("Times New Roman", 24), width=15, pady=10, command=self.advance_screen)
        # self.running_screen.pack()
        # self.running_screen.place(relwidth=1.0, relheight=1.0)

        self.running_label = Label(self.running_screen, text="Recording...", font=("Times New Roman", 48), pady=100, justify=CENTER)
        self.running_label.pack()

        self.running_timer = Label(self.running_screen, text="5", font=("Times New Roman", 48), pady=10, justify=CENTER)
        self.running_timer.pack()

        self.quit_button = Button(self.running_screen, text="Back", font=("Times New Roman", 24), pady=10, command=self.parent.return_to_start)
        self.quit_button.pack()



        #Processing Screen
        self.processing_screen = Frame(self.master, borderwidth=border_width, relief=relief_pattern)
        self.processing_screen.place(relwidth=1.0, relheight=1.0)

        self.processing_label = Label(self.processing_screen, text="Processing...", font=("Times New Roman", 48), pady=100,
                                   justify=CENTER)
        self.processing_label.pack()

        self.processing_percentage = Label(self.processing_screen, text="5", font=("Times New Roman", 48), pady=10, justify=CENTER)
        self.processing_percentage.pack()

        self.loading_bar_placeholder = Frame(self.processing_screen)
        self.loading_bar_placeholder.pack()
        self.loading_bar = Frame(self.loading_bar_placeholder, height=40, width=550)
        self.loading_bar.pack()

        self.loading_empty = Frame(self.loading_bar, bg="#E3E3E3", height=40, width=self.loading_bar_width)
        self.loading_empty.grid(row=0, column=0, sticky=W)

        self.loading_full = Frame(self.loading_bar, bg="green", height=40, width=0)
        self.loading_full.grid(column=0, row=0, sticky=W)

        # Spacing, cuz the dang pady on the button just makes it bigger... I guess I could set the size of the button to something exact but meh
        Frame(self.processing_screen, height=25).pack()

        self.quit_button = Button(self.processing_screen, text="Back", font=("Times New Roman", 24), pady=10, command=self.parent.return_to_start)
        self.quit_button.pack()



        #Results Screen
        self.results_screen = Frame(self.master, borderwidth=border_width, relief=relief_pattern)

        Label(self.results_screen, text="Results", font=("Times New Roman", 64), justify=CENTER, pady=50.0).pack()

        self.result_image_frame = Frame(self.results_screen)
        self.result_image1 = Label(self.result_image_frame)
        self.result_image2 = Label(self.result_image_frame)

        self.result_image1.grid(row = 0, column = 0)
        self.result_image2.grid(row = 0, column = 1)
        self.result_image_frame.pack()

        results = "Sway averaged 0.2 m/s/s across the test."
        self.end_results = Label(self.results_screen, text=results, font=("Times New Roman", 36), pady=50, wraplength=self.width - 200.0, justify=CENTER)
        self.end_results.pack()

        self.back_button = Button(self.results_screen, text="Back", font=("Times New Roman", 24), width=15, pady=10, command=self.parent.return_to_start)
        self.back_button.pack()

        self.screens = [self.main_screen, self.countdown_screen, self.running_screen, self.processing_screen, self.results_screen]

    def start_gui(self):
        self.master.mainloop()

    def start_button(self):

        run_time = 0.1

        # try:
        #     run_time = float(self.length_setting.get())
        # except:
        #     pass

        self.parent.start(15.0, run_time)

    def set_screen(self, new_screen):
        self.screens[self.current_screen].place_forget()
        self.screens[new_screen].place(relwidth=1.0, relheight=1.0)
        self.current_screen = new_screen

    def __del__(self):
        self.master.destroy()
