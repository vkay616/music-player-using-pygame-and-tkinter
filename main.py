from tkinter import *
import pygame
from tkinter import filedialog
import tkinter.ttk as ttk

pygame.mixer.init()

class Music_System:
    
    def __init__(self, root):

        self.root = root
        self.root.title('Music Player')
        self.root.geometry('450x400')
        self.root.resizable(0, 0)

        self.checkpause = False

        # CREATING MENU
        self.main_menu = Menu(self.root)

        # ADD SONG MENU
        self.main_menu.add_command(label='Add', command=self.add_songs)

        # REMOVE SONG MENU
        self.main_menu.add_command(label='Remove', command=self.remove)

        # DELETE PLAYLIST MENU
        self.main_menu.add_command(label='Delete Playlist', command=self.delete_playlist)

        self.root.config(bg='#1a1a2e', menu=self.main_menu)
        self.root.iconbitmap("<FILE DIRECTORY FOR THE ICON>")

        # FRAME FOR SONG PLAYLIST
        self.playlist_frame = Frame(self.root, bg='#1a1a2e', borderwidth=0, highlightthickness=0)
        self.playlist_frame.place(x=0, y=70, width=450, height=330)
        
        # SCROLL BAR FOR PLAYLIST
        self.playlist_scroll = Scrollbar(self.playlist_frame, borderwidth=0, troughcolor='#ffffff')
        self.playlist_scroll.place(x=432, y=0, height=330)

        # SONG PLAYLIST
        self.songs_list = Listbox(self.root, bg='#1a1a2e', fg='#e94560', borderwidth=0, font=('helvetica', 11, 'bold'), highlightthickness=0, activestyle=NONE, selectbackground='#0f3460', selectforeground='#ffffff')
        self.songs_list.place(x=2, y=80, height=324, width=430)
        self.songs_list.config(yscrollcommand=self.playlist_scroll.set)
        self.playlist_scroll.config(command=self.songs_list.yview)

        # FRAME FOR CONTROLS
        self.controls_frame = Frame(self.root, borderwidth=0, bg='#1a1a2e')
        self.controls_frame.place(x=0, y=10, width=450, height=50)

        # CREATING BUTTONS
        self.back_btn = Button(self.controls_frame, image=backimg, width=60, borderwidth=0, bg='#1a1a2e', activebackground='#1a1a2e', command=self.back)
        self.next_btn = Button(self.controls_frame, image=nextimg, width=60, borderwidth=0, bg='#1a1a2e', activebackground='#1a1a2e', command=self.next)
        self.play_btn = Button(self.controls_frame, image=playimg, width=60, borderwidth=0, bg='#1a1a2e', activebackground='#1a1a2e', command=self.play)
        self.pause_btn = Button(self.controls_frame, image=pauseimg, width=60, borderwidth=0, bg='#1a1a2e', activebackground='#1a1a2e', command=lambda: self.pause(checkpause))
        self.stop_btn = Button(self.controls_frame, image=stopimg, width=60, borderwidth=0, bg='#1a1a2e', activebackground='#1a1a2e', command=self.stop)

        # PLACING BUTTONS
        self.back_btn.grid(row=0, column=0, padx=(26, 10), pady=5)
        self.next_btn.grid(row=0, column=1, padx=10, pady=5)
        self.play_btn.grid(row=0, column=2, padx=10, pady=5)
        self.pause_btn.grid(row=0, column=3, padx=10, pady=5)
        self.stop_btn.grid(row=0, column=4, padx=10, pady=5)

        # SEPARATOR
        self.separator2 = Frame(self.root, width=450, height=3, borderwidth=0, bg='#ffffff')
        self.separator2.place(x=0, y=70)


    # ADD SONG FUNCTION
    def add_songs(self):
        self.songs = filedialog.askopenfilenames(initialdir="<FILE DIRECTORY FOR THE MUSIC>", title='Choose a song', filetypes=(('mp3 Files', '*.mp3'), ))
        for song in self.songs:
            song = song.replace("<FILE DIRECTORY FOR THE MUSIC>", "")
            song = song.replace(".mp3", "")
            self.songs_list.insert(END, song) 

    # PLAY BUTTON FUNCTION
    def play(self):
        self.song = self.songs_list.get(ACTIVE)
        self.song = f'<FILE DIRECTORY FOR THE MUSIC>/{self.song}.mp3'
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
        
    # STOP BUTTON FUNCTION
    def stop(self):
        pygame.mixer.music.stop()
        self.songs_list.selection_clear(ACTIVE)

    # PAUSE BUTTON FUNCTION
    def pause(self, pause_counter):
        global checkpause
        checkpause = pause_counter
        if checkpause:
            pygame.mixer.music.unpause()
            checkpause = False
        else:
            pygame.mixer.music.pause()
            checkpause = True

    # NEXT BUTTON FUNCTION    
    def next(self):
        self.currentsong = self.songs_list.curselection()
        self.nextsong = self.currentsong[0] + 1
        self.song = self.songs_list.get(self.nextsong)
        self.song = f'<FILE DIRECTORY FOR THE MUSIC>/{self.song}.mp3'
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
        self.songs_list.selection_clear(0, END)
        self.songs_list.activate(self.nextsong)
        self.songs_list.selection_set(self.nextsong, last=None)

    # BACK BUTTON FUNCTION
    def back(self):
        self.currentsong = self.songs_list.curselection()
        self.prevsong = self.currentsong[0] - 1
        self.song = self.songs_list.get(self.prevsong)
        self.song = f'<FILE DIRECTORY FOR THE MUSIC>/{self.song}.mp3'
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(loops=0)
        self.songs_list.selection_clear(0, END)
        self.songs_list.activate(self.prevsong)
        self.songs_list.selection_set(self.prevsong, last=None)

    # REMOVE SONG FUNCTION
    def remove(self):
        self.songs_list.delete(ANCHOR)
        pygame.mixer.music.stop()

    # DELETE PLAYLIST FUNCTION
    def delete_playlist(self):
        self.songs_list.delete(0, END)
        pygame.mixer.music.stop()


root = Tk()

# IMAGES FOR BUTTONS
backimg = PhotoImage(file="<WORKING DIRECTORY>/images/back.png")
nextimg = PhotoImage(file="<WORKING DIRECTORY>/images/next.png")
playimg = PhotoImage(file="<WORKING DIRECTORY>/images/play.png")
pauseimg = PhotoImage(file="<WORKING DIRECTORY>/images/pause.png")
stopimg = PhotoImage(file="<WORKING DIRECTORY>/images/stop.png")

# COUNTER FOR CHECKING WHETHER THE SONG IS PAUSED OR NOT
global checkpause
checkpause = False

Music_System(root)

root.mainloop()