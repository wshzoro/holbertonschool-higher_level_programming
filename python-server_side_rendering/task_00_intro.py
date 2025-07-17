import os

def generate_invitations(template, attendees):
    # Vérification du type des entrées
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérification si le template est vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Vérification si la liste d'invités est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Liste des clés attendues
    keys = ["name", "event_title", "event_date", "event_location"]

    # Traitement de chaque invité
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in keys:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        # Nom du fichier de sortie
        filename = f"output_{i}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
