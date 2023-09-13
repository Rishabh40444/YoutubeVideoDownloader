from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from pytube import YouTube
from tkinter import filedialog
import time


class downloader:
    def __init__(self):
        self.root = Tk()
        self.root.title('Youtube Video Downloader')
        self.root.geometry('600x600')
        self.lb = Frame(self.root)
        self.lb.pack(fill=BOTH,padx=20, pady=20)

        Label(self.lb, text='Search Youtube Video', font=('arial',20, 'bold')).pack(pady=20)
        self.f1 = Frame(self.lb)
        Label(self.f1, text='Search', font=('arial',12)).grid(row=0, column=0, padx=5, pady=10)
        self.searchBar = Entry(self.f1, width=50)
        self.searchBar.grid(row=0, column=1, padx=5)
        Button(self.f1, text='Search', command=self.step2).grid(row=0, column=2, padx=5)


        self.f1.pack()


        self.root.mainloop()
#----------------------------------------------------------------------------------------

    # Select Resolution and Download Video
    def step2(self):
        self.yt = YouTube(self.searchBar.get())
        self.label = Label(self.lb, text=f'Title :- {self.yt.title}', font=('arial', 18))
        self.label.pack(pady=25)
        self.f2 = Frame(self.lb)
        self.f2.pack()
        Label(self.f2, text='Select Resolution', font=('arial', 18)).grid(row=0, column=0, padx=5, pady=15)
        # allres = self.get_resolutions()
        self.available_resolutions = Combobox(self.f2, values=self.get_resolutions(), state='readonly')
        self.available_resolutions.grid(row=0, column=1, padx=5)
        Button(self.f2, text='Download', command=self.downloadVideo).grid(row=0,column=2, padx=5)
#-----------------------------------------------------------------------------------------
    # Fetch all the available resolutions of the Video
    def get_resolutions(self):
        user_res = ['144p','240p', '360p', '480p', '720p', '1080p','2160p']
        x = []
        for i in user_res:
            a = self.yt.streams.filter(res=i, type='video')
            # print(i,'-----',a)
            if len(a) > 0:
                x.append(i)
        # Returning all available resolutions
        return x
#----------------------------------------------------------------------------------------
    def downloadVideo(self):
        location = filedialog.askdirectory()
        # self.progress = Progressbar(self.lb, orient = HORIZONTAL,length = 300, mode = 'indeterminate')
        # self.progress.pack()
        # self.bar()
        # time.sleep(secs=1)
        selected_resolution = self.available_resolutions.get()
        self.yt.streams.filter(res=selected_resolution, type='video').first().download(output_path=location)
        # self.progress.destroy()
        print(self.yt.streams.filter)
        print('Done')
        showinfo('', 'Video Downloaded Successfully')
        self.f2.destroy()
        self.label.destroy()
        self.searchBar.delete(0, END)

#----------------------------------------------------------------------------------------
    # def resetWindow(self):



    # def bar(self):
    #     print('Progressbar')
    #     while True:
    #         self.progress['value'] = 0
    #         self.f2.update_idletasks()
    #         self.lb.update_idletasks()
    #         self.root.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 25
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 50
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 75
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 100
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 75
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 50
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 25
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         self.progress['value'] = 0
    #         self.f2.update_idletasks()
    #         time.sleep(0.2)
    #
    #         # self.progress['value'] = 40
    #         # self.root.update_idletasks()
    #         # time.sleep(0.2)
    #         #
    #         # self.progress['value'] = 20
    #         # self.root.update_idletasks()
    #         # time.sleep(0.2)
    #         # self.progress['value'] = 0


downloader()