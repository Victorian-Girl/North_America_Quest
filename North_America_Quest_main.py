import random
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from random import randint


root = Tk()
root.title("Geography Quest/Quete de Géographie!")
root.geometry("400x200")

# define image
bg = PhotoImage(file="north america picture/northern america3.png")

# create a canvas
my_canvas = Canvas(root, width=400, height=200)
my_canvas.pack(fill="both", expand=True)

# set image in canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")

# add a label
my_canvas.create_text(200, 25, text="Chose a language / Choisisser une langue", font=("Helvetica", 15))


def english():
    global english
    root_e = tkinter.Toplevel()
    root_e.title("Geography Quest!")
    root_e.geometry("950x950")

    # define image
    bg1 = PhotoImage(file="north america picture/northern america3.png")

    # create a canvas
    my_canvas1 = Canvas(root_e, width=950, height=950)
    my_canvas1.pack(fill="both", expand=True)

    # set image in canvas
    my_canvas1.create_image(0, 0, image=bg1, anchor="nw")

    # add a label
    my_canvas1.create_text(500, 100, text="Welcome!", font=("Helvetica", 50), fill="black")
    my_canvas1.create_text(500, 700, text="to North America", font=("Helvetica", 50), fill="black")

    # create randomizing state function
    def random_state():
        # create a list of state names
        global our_states
        our_states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
                      "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky",
                      "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "missouri", "montana",
                      "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina",
                      "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina",
                      "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington",
                      "west-virginia", "wisconsin", "wyoming"]

        # generate a random number
        global rando
        rando = randint(0, len(our_states)-1)
        state = "states images/" + our_states[rando] + ".jpg"

        # create our state images
        global state_image
        state_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=state_image, bg="white")

    # create answer function
    def state_answer():
        answer = answer_input.get()
        answer = answer.replace(" ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_states[rando]:
            response = "Correct! " + our_states[rando].title()

        else:
            response = "Incorrect! " + our_states[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_state()

    # create state quest function
    def states():
        # hide previous frames
        hide_all_frames()
        state_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(state_frame)
        show_state.pack(pady=15)
        random_state()

        # create answer box
        global answer_input
        answer_input = Entry(state_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize state images
        rando_button = Button(state_frame, text="Pass", command=states)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(state_frame, text="Answer", command=state_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(state_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create state capital answers
    def state_capital_answer():
        if capital_radio.get() == our_state_capitals[answer]:
            response = "Correct! " + our_state_capitals[answer].title() + " is the capital of " + answer.title()
        else:
            response = "Incorrect! " + our_state_capitals[answer].title() + " is the capital of " + answer.title()
 
        answer_label_capitals.config(text=response)

    # create states capitals quest function
    def state_capitals():
        # hide previous frames
        hide_all_frames()
        state_capitals_frame.pack(fill="both", expand=1)


        global show_state
        show_state = Label(state_capitals_frame)
        show_state.pack(pady=15)

    # create states capitals quest function
    def state_capitals2():
        # hide previous frames
        hide_all_frames()
        state_capitals_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(state_capitals_frame)
        show_state.pack(pady=15)

        global our_states
        our_states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware",
                      "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky",
                      "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "missouri", "montana",
                      "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina",
                      "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina",
                      "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington",
                      "west-virginia", "wisconsin", "wyoming"]

        global our_state_capitals
        our_state_capitals = {
            'alabama': 'Montgomery',
            'alaska': 'Juneau',
            'arizona': 'Phoenix',
            'arkansas': 'Little Rock',
            'california': 'Sacramento',
            'colorado': 'Denver',
            'connecticut': 'Hartford',
            'delaware': 'Dover',
            'florida': 'Tallahassee',
            'georgia': 'Atlanta',
            'hawaii': 'Honolulu',
            'idaho': 'Boise',
            'illinois': 'Springfield',
            'indiana': 'Indianapolis',
            'iowa': 'Des Monies',
            'kansas': 'Topeka',
            'kentucky': 'Frankfort',
            'louisiana': 'Baton Rouge',
            'maine': 'Augusta',
            'maryland': 'Annapolis',
            'massachusetts': 'Boston',
            'michigan': 'Lansing',
            'minnesota': 'St. Paul',
            'mississippi': 'Jackson',
            'missouri': 'Jefferson City',
            'montana': 'Helena',
            'nebraska': 'Lincoln',
            'nevada': 'Carson City',
            'new-hampshire': 'Concord',
            'new-jersey': 'Trenton',
            'new-mexico': 'Santa Fe',
            'new-york': 'Albany',
            'north-carolina': 'Raleigh',
            'north-dakota': 'Bismarck',
            'ohio': 'Columbus',
            'oklahoma': 'Oklahoma City',
            'oregon': 'Salem',
            'pennsylvania': 'Harrisburg',
            'rhode-island': 'Providence',
            'south-carolina': 'Columbia',
            'south-dakota': 'Pierre',
            'tennessee': 'Nashville',
            'texas': 'Austin',
            'utah': 'Salt Lake City',
            'vermont': 'Montpelier',
            'virginia': 'Richmond',
            'washington': 'Olympia',
            'west-virginia': 'Charleston',
            'wisconsin': 'Madison',
            'wyoming': 'Cheyenne'
        }

        # create an empty answer list and counter
        answer_list = []
        count = 1
        global answer

        # ggnerate our tree random capitals
        while count < 4:
            rando = randint(0, len(our_states) - 1)
            # if first selection, make it our answer
            if count == 1:
                answer = our_states[rando]
                global state_image
                state = "states images/" + our_states[rando] + ".jpg"
                state_image = ImageTk.PhotoImage(Image.open(state))
                show_state.config(image=state_image)

            # add our first selection to a new list
            answer_list.append(our_states[rando])

            # remove from the old list
            our_states.remove(our_states[rando])

            # shuffle our original list
            random.shuffle(our_states)
            count += 1

        random.shuffle(answer_list)

        global capital_radio
        capital_radio = StringVar()
        capital_radio.set(our_state_capitals[answer_list[0]])

        capital_radio_butto1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[0]])
        capital_radio_butto2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[1]])
        capital_radio_butto3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[2]])

        capital_radio_butto1.pack()
        capital_radio_butto2.pack()
        capital_radio_butto3.pack()

        # create a button to answer
        capital_answer_button = Button(state_capitals_frame, text="Answer", command=state_capital_answer)
        capital_answer_button.pack(pady=15)

        # create an answer label
        global answer_label_capitals
        answer_label_capitals = Label(state_capitals_frame, text="", bg="white", font=("Helvetica", 18))
        answer_label_capitals.pack(pady=15)

        # add a nextbutton
        pass_button = Button(state_capitals_frame, text="Next", command=state_capitals2)
        pass_button.pack(pady=15)

    # create randomizing state flag function
    def random_states_flag():
        # create a list of state names
        global our_states_flag
        our_states_flag = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
                           "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas",
                           "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota",
                           "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico",
                           "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania",
                           "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont",
                           "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]

        # generate a random number
        global rando
        rando = randint(0, len(our_states_flag) - 1)
        state = "states capitals flag/" + our_states_flag[rando] + ".png"

        # create our state flag images
        global flag_image
        flag_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=flag_image, bg="white")

    # create answer function
    def states_cap_flag_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_states_flag[rando]:
            response = "Correct! " + our_states_flag[rando].title()

        else:
            response = "Incorrect! " + our_states_flag[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_states_flag()

    # create state flag flashcard function
    def states_cap_flag():
        # hide previous frames
        hide_all_frames()
        states_flag_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(states_flag_frame)
        show_state.pack(pady=15)
        random_states_flag()

        # create answer box
        global answer_input
        answer_input = Entry(states_flag_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize state images
        rando_button = Button(states_flag_frame, text="Pass", command=states_cap_flag)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(states_flag_frame, text="Answer", command=states_cap_flag_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(states_flag_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create randomizing provinces function
    def random_provinces():
        # create a list of province names
        global our_provinces
        our_provinces = ["alberta", "british-columbia", "manitoba", "new foundland and labrador", "new-brunswick",
                         "northwest-territories", "nova scotia", "nunavut", "ontario", "prince edward island",
                         "quebec", "saskatchewan", "yukon"]

        # generate a random number
        global rando
        rando = randint(0, len(our_provinces) - 1)
        provinces = "provinces picture/" + our_provinces[rando] + ".png"

        # create our provinces images
        global provinces_image
        provinces_image = ImageTk.PhotoImage(Image.open(provinces))
        show_provinces.config(image=provinces_image, bg="white")

    # create answer function
    def provinces_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_provinces[rando]:
            response = "Correct! " + our_provinces[rando].title()

        else:
            response = "Incorrect! " + our_provinces[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_provinces()

    # create provinces quest function
    def can_provinces():
        # hide previous frames
        hide_all_frames()
        provinces_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_frame)
        show_provinces.pack(pady=15)
        random_provinces()

        # create answer box
        global answer_input
        answer_input = Entry(provinces_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize provinces images
        rando_button = Button(provinces_frame, text="Pass", command=can_provinces)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(provinces_frame, text="Answer", command=provinces_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(provinces_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create provinces capitals quest function
    def can_capitals():
        # hide previous frames
        hide_all_frames()
        provinces_capitals_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_capitals_frame)
        show_provinces.pack(pady=15)

    # create province capital answers
    def provinces_capital_answer():
        if capital_radio.get() == our_provinces_capitals[answer]:
            response = "Correct! " + our_provinces_capitals[answer].title() + " is the capital of " + answer.title()
        else:
            response = "Incorrect! " + our_provinces_capitals[answer].title() + " is the capital of " + answer.title()

        answer_label_capitals.config(text=response)

    # create provinces capitals quest function
    def can_capitals2():
        # hide previous frames
        hide_all_frames()
        provinces_capitals_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_capitals_frame)
        show_provinces.pack(pady=15)

        global our_provinces
        our_provinces = ["alberta", "british-columbia", "manitoba", "new foundland and labrador", "new-brunswick",
                         "northwest-territories", "nova scotia", "nunavut", "ontario", "prince edward island",
                         "quebec", "saskatchewan", "yukon"]

        global our_provinces_capitals
        our_provinces_capitals = {
            "alberta": "Edmonton",
            "british-columbia": "victoria",
            "manitoba": "Winnipeg",
            "new foundland and labrador": "St. John's",
            "new-brunswick": "Fredericton",
            "northwest-territories": "Yellowknife",
            "nova scotia": "Halifax",
            "nunavut": "Iqaluit",
            "ontario": "Toronto",
            "prince edward island": "Charlottetown",
            "quebec": "Quebec",
            "saskatchewan": "Regina",
            "yukon": "whitehorse"
        }

        # create an empty answer list and counter
        answer_list = []
        count = 1
        global answer

        # generate our tree random capitals
        while count < 4:
            rando = randint(0, len(our_provinces) - 1)
            # if first selection, make it our answer
            if count == 1:
                answer = our_provinces[rando]
                global provinces_image
                provinces = "provinces picture/" + our_provinces[rando] + ".png"
                provinces_image = ImageTk.PhotoImage(Image.open(provinces))
                show_provinces.config(image=provinces_image)

            # add our first selection to a new list
            answer_list.append(our_provinces[rando])

            # remove from the old list
            our_provinces.remove(our_provinces[rando])

            # shuffle our original list
            random.shuffle(our_provinces)
            count += 1

        random.shuffle(answer_list)

        global capital_radio
        capital_radio = StringVar()
        capital_radio.set(our_provinces_capitals[answer_list[0]])

        capital_radio_butto1 = Radiobutton(provinces_capitals_frame, text=our_provinces_capitals[answer_list[0]].title()
                                           , bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[0]])
        capital_radio_butto2 = Radiobutton(provinces_capitals_frame, text=our_provinces_capitals[answer_list[1]].title()
                                           , bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[1]])
        capital_radio_butto3 = Radiobutton(provinces_capitals_frame, text=our_provinces_capitals[answer_list[2]].title()
                                           , bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[2]])

        capital_radio_butto1.pack()
        capital_radio_butto2.pack()
        capital_radio_butto3.pack()

        # create a button to answer
        capital_answer_button = Button(provinces_capitals_frame, text="Answer", command=provinces_capital_answer)
        capital_answer_button.pack(pady=15)

        # create an answer label
        global answer_label_capitals
        answer_label_capitals = Label(provinces_capitals_frame, text="", bg="white", font=("Helvetica", 18))
        answer_label_capitals.pack(pady=15)

        # add a nextbutton
        pass_button = Button(provinces_capitals_frame, text="Next", command=can_capitals2)
        pass_button.pack(pady=15)

    # create randomizing can_prov_flag function
    def random_prov_flag():
        # create a list of state names
        global our_provinces_flag
        our_provinces_flag = ["alberta", "british-columbia", "labrador", "manitoba",  "new-brunswick",
                              "northwest-territories", "nova scotia", "nunavut", "ontario", "prince edward island",
                              "quebec", "saskatchewan", "yukon"]

        # generate a random number
        global rando
        rando = randint(0, len(our_provinces_flag) - 1)
        state = "canadian provinces flag/" + our_provinces_flag[rando] + ".png"

        # create our sprovinces flag images
        global flag_image
        flag_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=flag_image, bg="white")

    # create answer function
    def can_prov_flag_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_provinces_flag[rando]:
            response = "Correct! " + our_provinces_flag[rando].title()

        else:
            response = "Incorrect! " + our_provinces_flag[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_prov_flag()

    # create can_prov_flag quest function
    def can_prov_flag():
        # hide previous frames
        hide_all_frames()
        provinces_flag_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(provinces_flag_frame)
        show_state.pack(pady=15)
        random_prov_flag()

        # create answer box
        global answer_input
        answer_input = Entry(provinces_flag_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize can_prov_flag images
        rando_button = Button(provinces_flag_frame, text="Pass", command=can_prov_flag)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(provinces_flag_frame, text="Answer", command=can_prov_flag_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(provinces_flag_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # hide all previous frames
    def hide_all_frames():
        # loop through and destroy all children in previous frames
        for widget in state_frame.winfo_children():
            widget.destroy()

        for widget in state_capitals_frame.winfo_children():
            widget.destroy()

        for widget in states_flag_frame.winfo_children():
            widget.destroy()

        for widget in provinces_frame.winfo_children():
            widget.destroy()

        for widget in provinces_capitals_frame.winfo_children():
            widget.destroy()

        for widget in provinces_flag_frame.winfo_children():
            widget.destroy()

        state_frame.pack_forget()
        state_capitals_frame.pack_forget()
        states_flag_frame.pack_forget()
        provinces_frame.pack_forget()
        provinces_capitals_frame.pack_forget()
        provinces_flag_frame.pack_forget()

    # create our menu
    my_menu = Menu(root_e)
    root_e .config(menu=my_menu)

    # create geography menu items
    states_menu = Menu(my_menu)
    my_menu.add_cascade(label="Geography", menu=states_menu)
    states_menu.add_command(label="States", command=states)
    states_menu.add_command(label="States Capitals", command=state_capitals2)
    states_menu.add_command(label="States Flag", command=states_cap_flag)
    states_menu.add_separator()
    states_menu.add_command(label="Canada Provinces", command=can_provinces)
    states_menu.add_command(label="Canada Capitals", command=can_capitals2)
    states_menu.add_command(label="Provinces Flag", command=can_prov_flag)
    states_menu.add_separator()
    states_menu.add_command(label="Exit", command=root_e.destroy)

    # create our frames
    state_frame = Frame(my_canvas1, width=500, height=500, bg="white")
    state_capitals_frame = Frame(my_canvas1, width=500, height=500, bg="white")
    states_flag_frame = Frame(my_canvas1, width=500, height=500, bg="white")

    provinces_frame = Frame(my_canvas1, width=500, height=500, bg="white")
    provinces_capitals_frame = Frame(my_canvas1, width=500, height=500, bg="white")
    provinces_flag_frame = Frame(my_canvas1, width=500, height=500, bg="white")

    root_e.mainloop()


def french():
    global french
    root_f = tkinter.Toplevel()
    root_f.title("Questionnaire Géographique!")
    root_f.geometry("950x950")

    # define image
    bg2 = PhotoImage(file="north america picture/northern america3.png")

    # create a canvas
    my_canvas2 = Canvas(root_f, width=950, height=950)
    my_canvas2.pack(fill="both", expand=True)

    # set image in canvas
    my_canvas2.create_image(0, 0, image=bg2, anchor="nw")

    # add a label
    my_canvas2.create_text(500, 100, text="Bienvenue!", font=("Helvetica", 50), fill="black")
    my_canvas2.create_text(500, 700, text="En Amérique du Nord", font=("Helvetica", 50), fill="black")

    # create randomizing state function
    def random_state():
        # create a list of state names
        global our_states
        our_states = ["alabama", "alaska", "arizona", "arkansas", "californie", "caroline du nord", "carolione du sud",
                      "colorado", "connecticut", "dakota du nord", "dakota du sud", "delaware", "floride", "georgie",
                      "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiane", "maine",
                      "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana",
                      "nebraska", "nevada", "new-hampshire", "new-jersey", "new-york", "nouveau-mexique", "ohio",
                      "oklahoma", "oregon", "pennsylvanie", "rhode-island", "tennessee", "texas", "utah", "vermont",
                      "virginie-occidentale", "virginie", "washington", "wisconsin", "wyoming"]

        # generate a random number
        global rando
        rando = randint(0, len(our_states) - 1)
        state = "etat us/" + our_states[rando] + ".jpg"

        # create our state images
        global state_image
        state_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=state_image, bg="white")

    # create answer function
    def state_answer():
        answer = answer_input.get()
        answer = answer.replace(" ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_states[rando]:
            response = "Correct! " + our_states[rando].title()

        else:
            response = "Incorrect! " + our_states[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_state()

    # create states quest function
    def states():
        # hide previous frames
        hide_all_frames()
        state_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(state_frame)
        show_state.pack(pady=15)
        random_state()

        # create answer box
        global answer_input
        answer_input = Entry(state_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize state images
        rando_button = Button(state_frame, text="Suivante", command=states)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(state_frame, text="Réponse", command=state_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(state_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create state capital answers
    def state_capital_answer():
        if capital_radio.get() == our_state_capitals[answer]:
            response = "Correct! " + our_state_capitals[answer].title() + " est la capitale du " + answer.title()
        else:
            response = "Incorrect! " + our_state_capitals[answer].title() + " est la capitale du " + answer.title()

        answer_label_capitals.config(text=response)

    # create states capitals quest function
    def state_capitals():
        # hide previous frames
        hide_all_frames()
        state_capitals_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(state_capitals_frame)
        show_state.pack(pady=15)

    # create states capitals quest function
    def state_capitals2():
        # hide previous frames
        hide_all_frames()
        state_capitals_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(state_capitals_frame)
        show_state.pack(pady=15)

        global our_states
        our_states = ["alabama", "alaska", "arizona", "arkansas", "californie", "caroline du nord", "caroline du sud",
                      "colorado", "connecticut", "dakota du nord", "dakota du sud", "delaware", "floride", "georgie",
                      "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiane", "maine",
                      "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana",
                      "nebraska", "nevada", "new-hampshire", "new-jersey", "new-york", "nouveau-mexique", "ohio",
                      "oklahoma", "oregon", "pennsylvanie", "rhode-island", "tennessee", "texas", "utah", "vermont",
                      "virginie-occidentale", "virginie", "washington", "wisconsin", "wyoming"]

        global our_state_capitals
        our_state_capitals = {
            'alabama': 'Montgomery',
            'alaska': 'Juneau',
            'arizona': 'Phoenix',
            'arkansas': 'Little Rock',
            'californie': 'Sacramento',
            'caroline du nord': 'Raleigh',
            'caroline du sud': 'Columbia',
            'colorado': 'Denver',
            'connecticut': 'Hartford',
            'dakota du nord': 'Bismarck',
            'dakota du sud': 'Pierre',
            'delaware': 'Dover',
            'floride': 'Tallahassee',
            'georgie': 'Atlanta',
            'hawaii': 'Honolulu',
            'idaho': 'Boise',
            'illinois': 'Springfield',
            'indiana': 'Indianapolis',
            'iowa': 'Des Monies',
            'kansas': 'Topeka',
            'kentucky': 'Frankfort',
            'louisiane': 'Baton Rouge',
            'maine': 'Augusta',
            'maryland': 'Annapolis',
            'massachusetts': 'Boston',
            'michigan': 'Lansing',
            'minnesota': 'St. Paul',
            'mississippi': 'Jackson',
            'missouri': 'Jefferson City',
            'montana': 'Helena',
            'nebraska': 'Lincoln',
            'nevada': 'Carson City',
            'new-hampshire': 'Concord',
            'new-jersey': 'Trenton',
            'new-york': 'Albany',
            'nouveau-mexique': 'Santa Fe',
            'ohio': 'Columbus',
            'oklahoma': 'Oklahoma City',
            'oregon': 'Salem',
            'pennsylvanie': 'Harrisburg',
            'rhode-island': 'Providence',
            'tennessee': 'Nashville',
            'texas': 'Austin',
            'utah': 'Salt Lake City',
            'vermont': 'Montpelier',
            'virginie-occidentale': 'Charleston',
            'virginie': 'Richmond',
            'washington': 'Olympia',
            'wisconsin': 'Madison',
            'wyoming': 'Cheyenne'
        }

        # create an empty answer list and counter
        answer_list = []
        count = 1
        global answer

        # ggnerate our tree random capitals
        while count < 4:
            rando = randint(0, len(our_states) - 1)
            # if first selection, make it our answer
            if count == 1:
                answer = our_states[rando]
                global state_image
                state = "etat us/" + our_states[rando] + ".jpg"
                state_image = ImageTk.PhotoImage(Image.open(state))
                show_state.config(image=state_image)

            # add our first selection to a new list
            answer_list.append(our_states[rando])

            # remove from the old list
            our_states.remove(our_states[rando])

            # shuffle our original list
            random.shuffle(our_states)
            count += 1

        random.shuffle(answer_list)

        global capital_radio
        capital_radio = StringVar()
        capital_radio.set(our_state_capitals[answer_list[0]])

        capital_radio_butto1 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[0]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[0]])
        capital_radio_butto2 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[1]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[1]])
        capital_radio_butto3 = Radiobutton(state_capitals_frame, text=our_state_capitals[answer_list[2]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_state_capitals[answer_list[2]])

        capital_radio_butto1.pack()
        capital_radio_butto2.pack()
        capital_radio_butto3.pack()

        # create a button to answer
        capital_answer_button = Button(state_capitals_frame, text="Réponse", command=state_capital_answer)
        capital_answer_button.pack(pady=15)

        # create an answer label
        global answer_label_capitals
        answer_label_capitals = Label(state_capitals_frame, text="", bg="white", font=("Helvetica", 18))
        answer_label_capitals.pack(pady=15)

        # add a nextbutton
        pass_button = Button(state_capitals_frame, text="Suivante", command=state_capitals2)
        pass_button.pack(pady=15)

    # create randomizing state flag function
    def random_states_flag():
        # create a list of state names
        global our_states_flag
        our_states_flag = ["alabama", "alaska", "arizona", "arkansas", "californie", "caroline du nord",
                           "carolione du sud", "colorado", "connecticut", "dakota du nord", "dakota du sud",
                           "delaware", "floride", "georgie", "hawaii", "idaho", "illinois", "indiana", "iowa",
                           "kansas", "kentucky", "louisiane", "maine", "maryland", "massachusetts", "michigan",
                           "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire",
                           "new-jersey", "new-york", "nouveau-mexique", "ohio", "oklahoma", "oregon", "pennsylvanie",
                           "rhode-island", "tennessee", "texas", "utah", "vermont", "virginie-occidentale",
                           "virginie", "washington", "wisconsin", "wyoming"]

        # generate a random number
        global rando
        rando = randint(0, len(our_states_flag) - 1)
        state = "drapeau etats us/" + our_states_flag[rando] + ".png"

        # create our state flag images
        global flag_image
        flag_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=flag_image, bg="white")

    # create answer function
    def states_cap_flag_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_states_flag[rando]:
            response = "Correct! " + our_states_flag[rando].title()

        else:
            response = "Incorrect! " + our_states_flag[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_states_flag()

    # create states flag quest  function
    def states_cap_flag():
        # hide previous frames
        hide_all_frames()
        states_flag_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(states_flag_frame)
        show_state.pack(pady=15)
        random_states_flag()

        # create answer box
        global answer_input
        answer_input = Entry(states_flag_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize state images
        rando_button = Button(states_flag_frame, text="Suivante", command=states_cap_flag)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(states_flag_frame, text="Réponse", command=states_cap_flag_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(states_flag_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create randomizing provinces function
    def random_provinces():
        # create a list of province names
        global our_provinces
        our_provinces = ["alberta", "columbie britannique", "île du prince-édouard", "manitoba", "nouveau-brunswick",
                         "nouvelle-écosse", "nunavut", "ontario", "québec", "saskatchewan", "terre-neuve et labrador",
                         "territoires du nord-ouest", "yukon"]

        # generate a random number
        global rando
        rando = randint(0, len(our_provinces) - 1)
        provinces = "province canadienne/" + our_provinces[rando] + ".png"

        # create our provinces images
        global provinces_image
        provinces_image = ImageTk.PhotoImage(Image.open(provinces))
        show_provinces.config(image=provinces_image, bg="white")

    # create answer function
    def provinces_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_provinces[rando]:
            response = "Correct! " + our_provinces[rando].title()

        else:
            response = "Incorrect! " + our_provinces[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_provinces()

    # create provinces quest  function
    def can_provinces():
        # hide previous frames
        hide_all_frames()
        provinces_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_frame)
        show_provinces.pack(pady=15)
        random_provinces()

        # create answer box
        global answer_input
        answer_input = Entry(provinces_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize provinces images
        rando_button = Button(provinces_frame, text="Suivante", command=can_provinces)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(provinces_frame, text="Réponse", command=provinces_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(provinces_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # create provinces capitals quest  function
    def can_capitals():
        # hide previous frames
        hide_all_frames()
        provinces_capitals_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_capitals_frame)
        show_provinces.pack(pady=15)

    # create province capital answers
    def provinces_capital_answer():
        if capital_radio.get() == our_provinces_capitals[answer]:
            response = "Correct! " + our_provinces_capitals[answer].title() + " est la capitale du " + answer.title()
        else:
            response = "Incorrect! " + our_provinces_capitals[answer].title() + " est la capitale du " + answer.title()

        answer_label_capitals.config(text=response)

    # create provinces capitals quest  function
    def can_capitals2():
        # hide previous frames
        hide_all_frames()
        provinces_capitals_frame.pack(fill="both", expand=1)

        global show_provinces
        show_provinces = Label(provinces_capitals_frame)
        show_provinces.pack(pady=15)

        global our_provinces
        our_provinces = ["alberta", "columbie britannique", "île du prince-édouard", "manitoba", "nouveau-brunswick",
                         "nouvelle-écosse", "nunavut", "ontario", "québec", "saskatchewan", "terre-neuve et labrador",
                         "territoires du nord-ouest", "yukon"]

        global our_provinces_capitals
        our_provinces_capitals = {
            "alberta": "Edmonton",
            "columbie britannique": "victoria",
            "île du prince-édouard": "Charlottetown",
            "manitoba": "Winnipeg",
            "nouveau-brunswick": "Fredericton",
            "nouvelle-écosse": "Halifax",
            "nunavut": "Iqaluit",
            "ontario": "Toronto",
            "québec": "Québec",
            "saskatchewan": "Regina",
            "terre-neuve et labrador": "St. John's",
            "territoires du nord-ouest": "Yellowknife",
            "yukon": "whitehorse"
        }

        # create an empty answer list and counter
        answer_list = []
        count = 1
        global answer

        # generate our tree random capitals
        while count < 4:
            rando = randint(0, len(our_provinces) - 1)
            # if first selection, make it our answer
            if count == 1:
                answer = our_provinces[rando]
                global provinces_image
                provinces = "province canadienne/" + our_provinces[rando] + ".png"
                provinces_image = ImageTk.PhotoImage(Image.open(provinces))
                show_provinces.config(image=provinces_image)

            # add our first selection to a new list
            answer_list.append(our_provinces[rando])

            # remove from the old list
            our_provinces.remove(our_provinces[rando])

            # shuffle our original list
            random.shuffle(our_provinces)
            count += 1

        random.shuffle(answer_list)

        global capital_radio
        capital_radio = StringVar()
        capital_radio.set(our_provinces_capitals[answer_list[0]])

        capital_radio_butto1 = Radiobutton(provinces_capitals_frame,
                                           text=our_provinces_capitals[answer_list[0]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[0]])
        capital_radio_butto2 = Radiobutton(provinces_capitals_frame,
                                           text=our_provinces_capitals[answer_list[1]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[1]])
        capital_radio_butto3 = Radiobutton(provinces_capitals_frame,
                                           text=our_provinces_capitals[answer_list[2]].title(),
                                           bg="white", variable=capital_radio,
                                           value=our_provinces_capitals[answer_list[2]])

        capital_radio_butto1.pack()
        capital_radio_butto2.pack()
        capital_radio_butto3.pack()

        # create a button to answer
        capital_answer_button = Button(provinces_capitals_frame, text="Réponse", command=provinces_capital_answer)
        capital_answer_button.pack(pady=15)

        # create an answer label
        global answer_label_capitals
        answer_label_capitals = Label(provinces_capitals_frame, text="", bg="white", font=("Helvetica", 18))
        answer_label_capitals.pack(pady=15)

        # add a nextbutton
        pass_button = Button(provinces_capitals_frame, text="Suivante", command=can_capitals2)
        pass_button.pack(pady=15)

    # create randomizing can_prov_flag function
    def random_prov_flag():
        # create a list of state names
        global our_provinces_flag
        our_provinces_flag = ["alberta", "columbie britannique", "île du prince-édouard", "labrador", "manitoba",
                              "nouveau-brunswick", "nouvelle-écosse", "nunavut", "ontario", "québec", "saskatchewan",
                              "territoires du nord-ouest", "yukon"]

        # generate a random number
        global rando
        rando = randint(0, len(our_provinces_flag) - 1)
        state = "drapeau prov can/" + our_provinces_flag[rando] + ".png"

        # create our sprovinces flag images
        global flag_image
        flag_image = ImageTk.PhotoImage(Image.open(state))
        show_state.config(image=flag_image, bg="white")

    # create answer function
    def can_prov_flag_answer():
        answer = answer_input.get()
        answer = answer.replace("   ", "")

        # determine if our answer is right or wrong
        if answer.lower() == our_provinces_flag[rando]:
            response = "Correct! " + our_provinces_flag[rando].title()

        else:
            response = "Incorrect! " + our_provinces_flag[rando].title()

        answer_label.config(text=response)

        # clear entry box
        answer_input.delete(0, "end")

        random_prov_flag()

    # create can_prov_flag flashcard function
    def can_prov_flag():
        # hide previous frames
        hide_all_frames()
        provinces_flag_frame.pack(fill="both", expand=1)

        global show_state
        show_state = Label(provinces_flag_frame)
        show_state.pack(pady=15)
        random_prov_flag()

        # create answer box
        global answer_input
        answer_input = Entry(provinces_flag_frame, font=("Helvetica", 18), bd=2)
        answer_input.pack(pady=15)

        # create button to randomize can_prov_flag images
        rando_button = Button(provinces_flag_frame, text="Suivante", command=can_prov_flag)
        rando_button.pack(pady=10)

        # create a button to answer the question
        answer_button = Button(provinces_flag_frame, text="Réponse", command=can_prov_flag_answer)
        answer_button.pack(pady=5)

        # create a label to tell us if we got the answer right or not
        global answer_label
        answer_label = Label(provinces_flag_frame, text="", font=("Helvetica", 18), bg="white")
        answer_label.pack(pady=15)

    # hide all previous frames
    def hide_all_frames():
        # loop through and destroy all children in previous frames
        for widget in state_frame.winfo_children():
            widget.destroy()

        for widget in state_capitals_frame.winfo_children():
            widget.destroy()

        for widget in states_flag_frame.winfo_children():
            widget.destroy()

        for widget in provinces_frame.winfo_children():
            widget.destroy()

        for widget in provinces_capitals_frame.winfo_children():
            widget.destroy()

        for widget in provinces_flag_frame.winfo_children():
            widget.destroy()

        state_frame.pack_forget()
        state_capitals_frame.pack_forget()
        states_flag_frame.pack_forget()
        provinces_frame.pack_forget()
        provinces_capitals_frame.pack_forget()
        provinces_flag_frame.pack_forget()

    # create our menu
    my_menu = Menu(root_f)
    root_f.config(menu=my_menu)

    # create geography menu items
    states_menu = Menu(my_menu)
    my_menu.add_cascade(label="Géographie", menu=states_menu)
    states_menu.add_command(label="États Américain", command=states)
    states_menu.add_command(label="Capitales des États Américaine", command=state_capitals2)
    states_menu.add_command(label="Drapeau des États Américaine", command=states_cap_flag)
    states_menu.add_separator()
    states_menu.add_command(label="Provinces du Canada", command=can_provinces)
    states_menu.add_command(label="Capitales des Provinces Canadienne", command=can_capitals2)
    states_menu.add_command(label="Drapeau des Capitales Canadienne", command=can_prov_flag)
    states_menu.add_separator()
    states_menu.add_command(label="Quitter", command=root_f.destroy)

    # create our frames
    state_frame = Frame(my_canvas2, width=500, height=500, bg="white")
    state_capitals_frame = Frame(my_canvas2, width=500, height=500, bg="white")
    states_flag_frame = Frame(my_canvas2, width=500, height=500, bg="white")

    provinces_frame = Frame(my_canvas2, width=500, height=500, bg="white")
    provinces_capitals_frame = Frame(my_canvas2, width=500, height=500, bg="white")
    provinces_flag_frame = Frame(my_canvas2, width=500, height=500, bg="white")

    root_f.mainloop()


french_boutton = Button(my_canvas, text="French/Français", font=("Helvetica", 10, "bold"), bg="deep sky blue",
                        command=french)
french_boutton.pack(pady=15, padx=45, side="left")

english_button = Button(my_canvas, text="English/Anglais", font=("Helvetica", 10, "bold"), bg="deep sky blue",
                        command=english)
english_button.pack(pady=15, padx=45, side="right")

main_menu = Menu(root)
root.config(menu=main_menu)

main = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File / Fichier", menu=main)
main.add_command(label="Exit / Quitter", command=quit)

root.mainloop()
