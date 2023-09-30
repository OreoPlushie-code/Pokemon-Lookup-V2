from tkinter import *
from tkinter import messagebox
from url_stems import *  
import webbrowser

pokemon_mode = True
item_Mode = False
ability_mode = False
move_mode = False

Dark_Mode_on = True



""" def test():
    f = open("save_info.txt", "w")
    f.writelines(["See you soon! \n", "Over and out."])
    f.close()

    with open("save_info.txt", "r")as file:
          print(file.readlines()[1]) """

#test()
def search():

    global pokemon_mode, item_Mode, ability_mode, move_mode, smogon_pokemon_url_stem, smogon_item_url_stem, smogon_moves_url_stem, smogon_abilities_url_stem

    smogon_mode = False
    search_query = main_entry_box.get().lower()

    if smogon_toggle_var.get() == 1:
          smogon_mode = True

          
    
    if " " in search_query:
            search_query = search_query.replace(" ","-")
    else: pass

    #--------------------------------------------------------------
 
    if pokemon_mode and smogon_mode:
            webbrowser.open(smogon_pokemon_url_stem + search_query)
            return 
        
    elif item_Mode:
            webbrowser.open(smogon_item_url_stem + search_query)
            return

    elif move_mode:
            webbrowser.open(smogon_moves_url_stem + search_query)
            return
    
    elif ability_mode:
            webbrowser.open(smogon_abilities_url_stem + search_query)
            return

    #------------------------------------------------------------------

    if pokemon_mode:
            webbrowser.open(pokemon_url_stem + search_query)
            return
        
    elif item_Mode:
            webbrowser.open(item_url_stem + search_query)
            return

    elif move_mode:
            webbrowser.open(move_url_stem + search_query)
            return
    
    elif ability_mode:
            webbrowser.open(abiltiy_url_stem + search_query)
            return

    main_entry_box.delete(0,END)

def change_mode():
    global pokemon_mode, item_Mode, ability_mode, move_mode 

    if pokemon_mode:
        pokemon_mode = False
        item_Mode = True
        mode_indicator_label.config(text="Item Mode")

    elif item_Mode:
        item_Mode = False
        ability_mode = True
        mode_indicator_label.config(text="Ability Mode")

    elif ability_mode:
        ability_mode = False
        move_mode = True
        mode_indicator_label.config(text="Move Mode")

    elif move_mode:
        pokemon_mode = True
        move_mode = False
        mode_indicator_label.config(text="Pokemon Mode")

def settings_menu():
     
     settings_menu_window = Toplevel()
     settings_menu_window.title("Settings")
     settings_menu_window.geometry("500x400")

     Title_Label = Label(settings_menu_window, text="Settings", font=("Gotham", 20,"bold"),fg="black")
     Toggle_Dark_Mode = Label(settings_menu_window, text="Toggle GUI Display Settings")
     Toggle_smogon_label = Label(settings_menu_window, text= "Use Smogon as default search")
     Dark_mode_button = Button(settings_menu_window, text="Toggle",command=toggle_dark_mode)
     smogon_toggle_checkbox = Checkbutton(settings_menu_window, var = smogon_toggle_var,command=smogon_toggle)


     Toggle_Dark_Mode.place(x=0,y=50)
     Toggle_smogon_label.place(x=0,y=100)
     Dark_mode_button.place(x=400,y=50)
     Title_Label.place(x = 200, y=0)
     smogon_toggle_checkbox.place(x=400, y=100)
     settings_menu_window.mainloop()
     
def toggle_dark_mode():
        global Dark_Mode_on
        if Dark_Mode_on:
            background.config(bg="#ffffff")
            title.config(bg="#ffffff", fg="#000000")
            mode_indicator_label.config(bg="#ffffff", fg="#000000")
            Dark_Mode_on = False
        else:
            background.config(bg="#000000")
            title.config(bg="#000000", fg="#ffffff")
            mode_indicator_label.config(bg="#000000", fg="#ffffff")
            Dark_Mode_on = True

def smogon_toggle():

    if smogon_toggle_var.get() == 1:
        messagebox.showinfo("Action Complete!", "Smogon is now your default search engine!")
    else: 
          messagebox.showinfo("Action Complete!", "Pokemon DB is now your default search engine!")

root = Tk();
root.title("Pokemon Searcher V2");
root.geometry("900x500");
icon = PhotoImage(file="pokeball icon.png")
root.iconphoto(True,icon)

smogon_toggle_var = IntVar()

background = Label(root, height=900, width=500,bg="#000000");
main_entry_box =  Entry(root, width=30, font=("Chiller", 30));
title = Label(root, text="Pokemon Lookup", font=("Chiller", 60),fg="#ffffff",bg="#000000");
search_button = Button(root, text="Search", font= ("Comic Sans MS", 20), command=search)
change_mode_button = Button(root, text="Change Mode", command=change_mode)
mode_indicator_label = Label(root, text= "Pokemon mode", font=("Gotham", 10),bg="#000000",fg="#ffffff")

main_entry_box.place(x = 150, y=300);
background.place(x=0, y=0);
title.place(x= 220, y=0);
search_button.place(x=370, y=400)
change_mode_button.place(x=500, y=420)
mode_indicator_label.place(x=170, y= 350)

menu_bar = Menu(root)
Options = Menu(menu_bar, tearoff=0)
Options.add_command(label= "Settings",command=settings_menu)
menu_bar.add_cascade(label="Options", menu=Options)
root.config(menu=menu_bar)
root.mainloop();