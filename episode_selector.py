import pandas as pd
import random
import tkinter
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk

# open data
filepath = 'data/FriendsEpisodes.csv'
df = pd.read_csv(filepath)

##### main algorithms ######

def filter_button_click(event):

    '''
    Answers to a bind-function call for the Combobox.
    Gets filtered values, then filters global dataframe accordingly.
    Returns dataframe as "df" (same name as original dataframe) to then be used as the new global dataframe.
    '''

    global df

    # open data
    filepath = 'data/FriendsEpisodes.csv'
    df = pd.read_csv(filepath)

    # get selected filter option
    filtered_season = season_cb.get()

    # filter dataframe if needed
    if filtered_season != 'All':
        season_num = int(filtered_season)
        df = df[df['season'] == season_num]

    return df

def selector_button_click():

    '''
    Chooses a random episode number and then shows the details for the chosen episode as a label in the GUI. 
    Works for both the filtered and non-filtered dataframe.
    '''

    global df

    # randomly select episode number
    random_range_low = df['episode'].iloc[0]
    random_range_high = df['episode'].iloc[-1]
    random_episode_number = random.randrange(random_range_low, random_range_high + 1)

    ## find the episode in the DataFrame
    df_episode = df[df['episode'] == random_episode_number]

    ## check if the episode DataFrame is empty, otherwise print episode details
    if df_episode.empty:
        episode_details = f'\nEpisode number {random_episode_number} not found.'

    else:
        df_episode = df_episode.iloc[0]
        season = df_episode['season']
        number = df_episode['number']
        title = df_episode['title']
        director = df_episode['director']
        writer = df_episode['writer']
        air_date = df_episode['air_date']
        description = df_episode['description']
        link = df_episode['link']

        selection_header = f'Chosen Episode'

        chosen_episode = (
            f'Season: {season}\n'
            f'Episode: {number}'
        )

        episode_details = (
            f'Title: {title}\n'
            f'Description: {description}\n\n'
            f'Director: {director}\n'
            f'Writer: {writer}\n'
            f'Air Date: {air_date}'
        )

        more_information = f'More Information: {link}'

    selection_header_label.config(text=selection_header, font='TkDefaultFont 12 bold', bg="#9244B1", pady=5)
    chosen_episode_label.config(text=chosen_episode, bg="#9244B1", font='TkDefaultFont 11', pady=15)
    episode_label.config(text=episode_details, bg="#9244B1", font='TkDefaultFont 10')
    more_information_label.config(text=more_information, bg="#9244B1", font='TkDefaultFont 8 italic', pady=10)
    closing_label.config(text='Are you ready to enter the Friends-universe? Have fun!\nAnd if not: Just click the button again to select another episode or apply filters.', font='TkDefaultFont 10 bold', pady=10)

    return episode_details

def selector_button_click_popup():

    '''
    Chooses a random episode number and then shows the details for the chosen episode as a pop-up window in the GUI. 
    Works for both the filtered and non-filtered dataframe.
    '''

    global df

    # randomly select episode number; no filter
    random_range_low = df['episode'].iloc[0]
    random_range_high = df['episode'].iloc[-1]
    random_episode_number = random.randrange(random_range_low, random_range_high + 1)

    ## find the episode in the DataFrame
    df_episode = df[df['episode'] == random_episode_number]

    ## check if the episode DataFrame is empty, otherwise print episode details
    if df_episode.empty:
        episode_details = f'Episode number {random_episode_number} not found.'

    else:
        df_episode = df_episode.iloc[0]
        season = df_episode['season']
        number = df_episode['number']
        title = df_episode['title']
        director = df_episode['director']
        writer = df_episode['writer']
        air_date = df_episode['air_date']
        description = df_episode['description']
        link = df_episode['link']

        episode_details = (
            f'Chosen Episode\n\n'
            f'Season: {season}\n'
            f'Episode Number: {number}\n\n'
            f'Title: {title}\n'
            f'Director: {director}\n'
            f'Writer: {writer}\n'
            f'Air Date: {air_date}\n'
            f'Description: {description}\n'
        )

    tkinter.messagebox.showinfo('Chosen Episode Details',  episode_details, detail=f'More Information: {link}', icon='info')

    return episode_details


##### helper functions for design implementations #####

def show_image(img_no):

    '''
    Changes the image shown in the image gallery.
    Disables/Enables buttons below the gallery based on the image position.
    '''

    global current_img
    current_img = img_no
    image_label.config(image=list_images[img_no - 1], bg='#571770')

    # enable/disable buttons at the ends
    if img_no == 1:
        button_back.config(state='disabled')
    else:
        button_back.config(state='normal')

    if img_no == len(list_images):
        button_forward.config(state='disabled')
    else:
        button_forward.config(state='normal')

def forward():

    '''
    Draws on show_image function to skip to the next image in the image gallery.
    Disables/Enables buttons below the gallery based on the image position.
    '''

    show_image(current_img + 1)

def back():

    '''
    Draws on show_image function to skip to the previous image in the image gallery.
    Disables/Enables buttons below the gallery based on the image position.
    '''

    show_image(current_img - 1)


##### GUI development ######

# initialize and customize root window
root = tkinter.Tk()
root.title('Friends Episode Selector')
root.geometry('1000x1050')
# root.resizable(False, False)
root.config(bg="#571770")                   # old color: # old colors: lightpurple (#bfa0e2, #e0cff3)

photo = tkinter.PhotoImage(file='images/2066887.png')
root.iconphoto(False, photo)

# add images as gallery
image_no_1 = ImageTk.PhotoImage(Image.open('images/2066889.jpg').resize((500, 350)))
image_no_2 = ImageTk.PhotoImage(Image.open('images/1898573.jpg').resize((500, 350)))
image_no_3 = ImageTk.PhotoImage(Image.open('images/1810196.jpg').resize((500, 350)))
image_no_4 = ImageTk.PhotoImage(Image.open('images/1810247.jpg').resize((500, 350)))

list_images = [image_no_1, image_no_2, image_no_3, image_no_4]
current_img = 1

    # create a frame for the image gallery
gallery_frame = tkinter.Frame(root, bg='#571770')
gallery_frame.pack(anchor='center', pady=12)

    # image label inside the frame
image_label = tkinter.Label(gallery_frame, image=image_no_1, bg='#571770')
image_label.pack()

    # source label inside the frame
source_label = tkinter.Label(gallery_frame, text='Source: https://wallpaperaccess.com/friends-series', anchor='center', fg='lightgrey', bg='#571770')
source_label.pack()

    # buttons frame inside the frame
button_frame = tkinter.Frame(gallery_frame, bg='#571770')
button_frame.pack()

button_back = tkinter.Button(button_frame, text='←', command=back, state='disabled', bg="#d6b8e2", highlightbackground='#370a49')
button_forward = tkinter.Button(button_frame, text='→', command=forward, bg="#d6b8e2", highlightbackground='#370a49')
button_back.pack(side='left', padx=10)
button_forward.pack(side='left', padx=10)

# introductory text
label_text1 = 'Welcome to the episode selector for the popular sitcom Friends.'
introduction_text = tkinter.Label(root, text=label_text1, anchor='center', font='TkDefaultFont 12 bold', fg="#8beef1", wraplength=600, bg='#571770')
introduction_text.pack(pady=10)

label_text2 = 'Have you ever sat before your laptop and not been able to choose an episode? That is now over, thanks to this program. Simply click on the button and have the perfect episode chosen for you!\nAnd if you want some more control, you can even apply filters.'
introduction_text = tkinter.Label(root, text=label_text2, anchor='center', fg="#8beef1", wraplength=600, bg='#571770')
introduction_text.pack()

label_text3 = 'Have fun!'
introduction_text = tkinter.Label(root, text=label_text3, anchor='center', fg="#8beef1", font='TkDefaultFont 10 italic bold', bg='#571770')
introduction_text.pack(pady=10)

# filter buttons + save button

    # create a frame for the filter options
filter_frame = tkinter.Frame(root, bg='#571770')
filter_frame.pack(anchor='center', pady=5) 

    # label for combobox
tkinter.Label(filter_frame, text = 'Select a season:', font=('TkDefaultFont', 10), bg='#571770', fg='white').pack(side='left')

    # combobox
season_options = list(range(1,11))
season_options.insert(0, 'All')
season_cb = ttk.Combobox(filter_frame, state='normal', values=season_options, width=10, font='TkDefaultFont 10', background='#571770')
season_cb.current(0)
# season_cb.set('Select a season')
season_cb.pack(side='left')

season_cb.bind('<<ComboboxSelected>>', filter_button_click)

'''    # button to display selection  
filter_button = tkinter.Button(filter_frame, text='Apply filters', command=filter_button_click)
filter_button.pack(side='left')'''

# button for episode selection 
    ## change to command=button_click_popup for popup instead of label text display of the episode details
selector_button = tkinter.Button(root, text='Click to select an episode!', font='TkDefaultFont 10', highlightbackground='#370a49', bg='orange', fg='white', activebackground='yellow', width=50, command=selector_button_click)
selector_button.pack()

    # display episode information and details (filled after button click)
results_frame = tkinter.Frame(root, bg="#9244B1", relief='sunken', highlightbackground='purple')
results_frame.pack(anchor='center', pady=10)

selection_header = ''
chosen_episode = ''
episode_details = ''
more_information = ''

selection_header_label = tkinter.Label(results_frame, text=selection_header, anchor='center', fg='white', bg='#571770', wraplength=600)
selection_header_label.pack()

chosen_episode_label = tkinter.Label(results_frame, text=chosen_episode, anchor='center', fg='white', bg='#571770', wraplength=600)
chosen_episode_label.pack()

episode_label = tkinter.Label(results_frame, text=episode_details, anchor='center', fg='white', bg='#571770', wraplength=600)
episode_label.pack()

more_information_label = tkinter.Label(results_frame, text=more_information, anchor='center', fg='white', bg='#571770', wraplength=600)
more_information_label.pack()

    # closing statement (filled after button click)
closing_statement = ''

closing_label = tkinter.Label(root, text=closing_statement, anchor='center', fg="#f7b7b5", bg='#571770', wraplength=600)
closing_label.pack()

# start the main event loop
root.mainloop()
