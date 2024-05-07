import customtkinter as ctk
from random import randint
import plotly.express as px


def validate_input(P):
    """Validates the input.

    Args:
        P (int): the value the text would have after the change.

    Returns:
        bool: True if the input is digit-only or empty, and False otherwise.
    """

    return P.isdigit() or P == ""

def select_on_focus(event):
    event.widget.select_range(0, ctk.END)

class Die():
    def __init__(self, size) -> None:
        self.size = size
        self.app_label = None
        self.app_inputbox = None

dice = {
    'd2': Die(2),
    'd4': Die(4),
    'd6': Die(6),
    'd8': Die(8),
    'd10': Die(10),
    'd12': Die(12),
    'd20': Die(20),
    'd100': Die(100)
}

def simulate_rolls(dice_components, repeats):
    if repeats == "":
        repeats = 1
    else:
        repeats = int(repeats)

    plot_title = f'Dice roll results ({repeats} repeats)<br><sup>dice list: '
    max_dice_size = 0  # for the plots
    all_rolls_aggregated = []
    for _ in range(repeats):
        for die_name, die in dice_components.items():
            # Make the amount of specific die rolled an integer
            if die.app_inputbox.get() == "":
                n_die = 0
            else:
                n_die = int(die.app_inputbox.get())

            if n_die > 0:
                plot_title += f'{n_die}{die_name} + '
                max_dice_size = max(max_dice_size, die.size)

            # Roll the die
            for i in range(n_die):
                x = randint(1, die.size)
                all_rolls_aggregated.append(x)

    plot_title = plot_title[:-3]  # just remove the last ' + '
    plot_title += '</sup>'  # close the html tag opened

    plot_stats_all_rolls(all_rolls_aggregated, max_dice_size, plot_title)

def plot_stats_all_rolls(rolls, max_dice_size, plot_title):
    data = {'dice_range': list(range(1, max_dice_size + 1)), '# rolled': [0]*max_dice_size}
    for roll in rolls:
        data['# rolled'][roll - 1] += 1
    


    fig = px.bar(data, x='dice_range', y='# rolled', title=plot_title)
    fig.show()
    



ctk.set_appearance_mode("System")
ctk.set_appearance_mode("blue")

app = ctk.CTk()
app.title("Sushis's stupid dice roll simulator - Legrosours edition")
app.grid_columnconfigure(0, weight=1)


# Make labels and user input fields
row_pos = 0
for die in dice:
    label = ctk.CTkLabel(app, text=die)
    label.grid(row=row_pos, column=0, padx=20, pady=20)
    
    entry = ctk.CTkEntry(app, placeholder_text="0", validate="key", validatecommand=(app.register(validate_input), "%P"))  # make it so only integers are allowed
    entry.grid(row=row_pos, column=1, padx=20, pady=20)
    entry.bind(sequence='<FocusIn>', command=select_on_focus)

    dice[die].app_label = label
    dice[die].app_inputbox = entry
    
    row_pos += 1

repeats_label = ctk.CTkLabel(app, text="Repeats")
repeats_label.grid(row=row_pos)
repeats_entry = ctk.CTkEntry(app, placeholder_text="1", validate="key", validatecommand=(app.register(validate_input), "%P"))  # make it so only integers are allowed
repeats_entry.grid(row=row_pos, column=1, padx=20, pady=20)
repeats_entry.bind(sequence='<FocusIn>', command=select_on_focus)
row_pos += 1

simulate_button = ctk.CTkButton(app, text="Simulate", command=lambda: simulate_rolls(dice, repeats_entry.get()))
# app.grid_rowconfigure(row_pos, weight=1)
simulate_button.grid(row=row_pos, column=1, padx=20, pady=20, sticky="nsew")



app.mainloop()



