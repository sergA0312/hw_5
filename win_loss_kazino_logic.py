import configparser

def determine_outcome(selected_slot, winning_slot):
    if selected_slot == winning_slot:
        return "win"
    else:
        return "loss"
