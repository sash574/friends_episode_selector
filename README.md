# Friends Sitcom Episode Selector

This is a fun little project I implemented because I am a big fan of the Friends sitcom. Since the TV show is my all-time favorite comfort series, I wanted to implement a little episode selector to have some fun with choosing what episodes to watch.

![Image 1: GUI - Main Window](images/main_window.png)

Also, this was my first dive into GUI development (in general and with Tkinter), so I took it as a learning opportunity - but do not expect professional or perfect code here.

The data used is from Kaggle: https://www.kaggle.com/datasets/thebumpkin/ultimate-friends-tv-sitcom-dataset?resource=download

It contains information on the season, episode number (both seasonally and overall), the episodes title and description as well as the director, the writer, the air date and a link to the IMDb page with further information.

## Implementation

The repository contains a `requirements.txt` file that can be run to install all needed packages. Also, you need to ensure that Tkinter works on your machine (should be installed already with your Python version, otherwise: sudo apt install python3-tk (Linux Ubuntu)). 

Afterwards, the program works by simply running the main Python script `episode_selector.py`. This then opens a graphical user interface (= GUI) where one can randomly chose an episode to watch and play around with an image gallery.    
The program also contains an option to display the chosen episode and its details in a pop-up window instead of in the main window. You can find more information on this in the main code file.

![Image 2: GUI - Main Window After Selecting an Episode](images/main_window_after_buttonclick.png)

## To Dos

- [x] randomized episode selection
- [x] create GUI
- [x] pipe requirements.txt
- [x] season filter
- [ ] advanced filter options (i.e. based on contents of the description, specific directors etc.)