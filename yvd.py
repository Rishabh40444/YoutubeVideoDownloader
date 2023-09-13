# LabelFrame is the combination of label and frame


from tkinter import *
from tkinter import filedialog # -> filedialog is used here to ask user where to download & store the video
from tkinter.ttk import *
from tkinter.messagebox import * # -> messagebox is used to display info,error messages or warnings 
from pytube import YouTube   # -> pytube is the module which helps in downloading Youtube video

class finalDownloader:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        self.root.title('YouTube Video Downloader')
        self.lb = LabelFrame(self.root, text='Choose Video', height=550, width=550)
        self.f = Frame(self.lb)
        self.f.pack(pady=10)
        Label(self.f, text='Enter URL', font=('arial',12)).grid(row=0, column=0, padx=5, pady=20)
        self.searchBar = Entry(self.f, width=45)
        self.searchBar.grid(row=0, column=1, padx=5, pady=20)
        Button(self.f, text='Search', command=self.stepTwo).grid(row=0, column=2, padx=5, pady=20)
        self.lb.pack(pady=20, padx=20, fill=BOTH)
        self.root.mainloop()

    def stepTwo(self):
        self.yt = YouTube(self.searchBar.get(), on_progress_callback=self.makeProgress)
        avail_res = self.get_resolutions()
        self.label = Label(self.lb, text=f"Title :- {self.yt.title}", font=('arial',20))
        self.label.pack(pady=10)
        self.f1 = Frame(self.lb)
        Label(self.f1, text='Select Resolution', font=('arial',12)).grid(row=0, column=0, padx=5, pady=20)
        self.selected_res = Combobox(self.f1, width=42, values=avail_res, state='readonly')
        self.selected_res.grid(row=0, column=1, padx=5, pady=20)
        Button(self.f1, text='Download', command=self.downloadVideo).grid(row=0, column=2, padx=5, pady=20)
        self.f1.pack(pady=10)

    def get_resolutions(self):
        # yt = YouTube(self.searchBar.get())
        all_res = ['144p','240p','360p','480p','720p','1080p','2160p']
        x = []
        for i in all_res:
            a = self.yt.streams.filter(res=i, type='video', progressive=True)
            print(a)
            if len(a)>0:
                x.append(i)
        return x

    def downloadVideo(self):
        location = filedialog.askdirectory()
        self.progressbar = Progressbar(self.lb, orient = HORIZONTAL,length = 300, mode = 'determinate')
        self.progressbar.pack(pady=20)
        # self.label1 = Label()
        self.selected_stream = self.yt.streams.filter(res=self.selected_res.get(), type='video', progressive=True).first()
        self.selected_stream.download(output_path=location)
        showinfo('','Video Downloaded Successfully')
        self.f1.destroy()
        self.label.destroy()
        self.searchBar.delete(0,END)
        self.progressbar.destroy()

    def makeProgress(self, chunk,file_handle, bytes_remaining):
        size = self.selected_stream.filesize

        progress = float(abs(bytes_remaining - size)/size) * float(100)
        print(progress)
        self.progressbar['value'] = int(progress)
        # self.label1.config(text=f'{progress}%')
        self.root.update_idletasks()


finalDownloader()
