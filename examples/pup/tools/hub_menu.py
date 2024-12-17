from pybricks.tools import hub_menu

# Cet exemple suppose que vous avez trois autres programmes dans Pybricks Code,
# appelés "fly_mission", "drive_mission" et "zigzag". Cet exemple crée un
# menu qui vous permet de choisir lequel exécuter.

# Choisissez une lettre.
selected = hub_menu("F", "D", "Z")

# En fonction de la sélection, exécutez un programme.
if selected == "F":
    import fly_mission
elif selected == "D":
    import drive_mission
elif selected == "Z":
    import zigzag
