import os


def generate_files(template_path, output_directory, num_files):
    # Lecture du contenu de la template
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    # Création des fichiers basés sur la template
    for i in range(4, num_files + 1):
        filename = f"page_{i}.py"
        filepath = os.path.join(output_directory, filename)
        with open(filepath, 'w') as output_file:
            output_file.write(template_content.format(file_number=i))


if __name__ == "__main__":
    template_path = "template.py"  # Chemin vers le fichier template
    output_directory = "tomes/tome1"    # Répertoire où les fichiers seront générés
    num_files = 350                 # Nombre de fichiers à générer

    generate_files(template_path, output_directory, num_files)
