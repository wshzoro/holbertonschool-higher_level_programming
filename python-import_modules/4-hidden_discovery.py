import hidden_4

if __name__ == "__main__":
    print("Module hidden_4 importé avec succès !")
    
    # Parcourir toutes les variables définies dans hidden_4
    for name in dir(hidden_4):
        if not name.startswith("__"):
            print(name)
