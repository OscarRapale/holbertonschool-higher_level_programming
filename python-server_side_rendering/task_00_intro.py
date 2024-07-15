import os

def generate_invitations(template, attendees):
    """
    Generate invitations from a template and a list of attendees.

    Parameters:
    template (str): The invitation template with placeholders.
    attendees (list): A list of dictionaries, each representing an attendee.

    Returns:
    None
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be in a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        attendee = attendee.copy()
        if 'event_date' not in attendee:
            print("Warning: Replacing missing data 'event_date' with 'N/A'.")
            attendee['event_date'] = "N/A"
        try:
            invitation = template.format(**attendee)
        except KeyError as e:
            print(f"Warning: Replacing missing data {e} with 'N/A'.")
            attendee[str(e)] = "N/A"
            invitation = template.format(**attendee)
        with open(f"output_{index}.txt", "w") as file:
            file.write(invitation)
