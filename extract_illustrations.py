"""
Extrait les illustrations du PDF d'un tome vers static/illustrations/<tome>/.

    python extract_illustrations.py tome1.pdf static/illustrations/tome1

- Vignettes : images placées dans le texte, juste après le paragraphe qu'elles illustrent.
  Elles sont rattachées au paragraphe en cours à l'endroit de l'image -> p{N}_vignette.{ext}
- Planches : pages pleine image sans texte. Leur légende (avec le numéro du paragraphe) fait partie
  de l'image scannée, elles sont donc nommées d'après la page du PDF -> planche_pdf{page}.{ext}
  et à renommer une fois la légende lue.
- Couverture, pages de garde et petits ornements sont ignorés.

Un index illustrations.json décrit chaque fichier extrait.
"""
import json
import os
import re
import sys

import fitz

DEFAULT_OUTPUT_DIR = os.path.join("static", "illustrations", "tome1")
FIRST_STORY_PAGE = 7  # avant : couverture et pages de garde
MIN_VIGNETTE_SIZE = (100, 40)  # en dessous : ornement décoratif
CHAPTER_MARKER = re.compile(r"^\s*(\d{1,3})\s*$")


def save_image(doc, xref: int, name: str, output_dir: str) -> str:
    """Enregistre l'image `xref` sous output_dir/name.<ext> et renvoie le nom du fichier."""
    image = doc.extract_image(xref)
    file_name = f"{name}.{image['ext']}"
    with open(os.path.join(output_dir, file_name), "wb") as output:
        output.write(image["image"])
    return file_name


def extract(pdf_path: str, output_dir: str = DEFAULT_OUTPUT_DIR, max_chapters: int = 350) -> list:
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    index = []
    current_chapter = 0
    previous_line = ""
    vignettes_per_chapter = {}

    for page_number in range(doc.page_count):
        page = doc.load_page(page_number)
        images = page.get_images(full=True)
        has_text = bool(page.get_text().strip())

        # Éléments de la page dans l'ordre de lecture : lignes de texte et images, triées par hauteur
        items = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                text = "".join(span["text"] for span in line["spans"]).strip()
                if text:
                    items.append((line["bbox"][1], "text", text))
        for image in images:
            for rect in page.get_image_rects(image[0]):
                items.append((rect.y0, "image", image))
        items.sort(key=lambda item: item[0])

        for _, kind, value in items:
            if kind == "text":
                # même règle que utils.extract_chapters_from_pdf : seul le numéro suivant
                # ouvre un paragraphe, et jamais juste après « rendez-vous au »
                match = CHAPTER_MARKER.match(value)
                if (
                    match
                    and int(match.group(1)) == current_chapter + 1
                    and int(match.group(1)) <= max_chapters
                    and not re.search(r"\bau$", previous_line)
                ):
                    current_chapter = int(match.group(1))
                previous_line = value
                continue

            xref, width, height = value[0], value[2], value[3]
            if page_number < FIRST_STORY_PAGE:
                continue  # couverture et pages de garde
            elif not has_text:
                kind, chapter, name = "planche", None, f"planche_pdf{page_number}"
            elif width < MIN_VIGNETTE_SIZE[0] or height < MIN_VIGNETTE_SIZE[1] or current_chapter == 0:
                continue  # ornement, ou illustration des règles avant le paragraphe 1
            else:
                count = vignettes_per_chapter.get(current_chapter, 0) + 1
                vignettes_per_chapter[current_chapter] = count
                suffix = "" if count == 1 else f"_{count}"
                kind, chapter, name = "vignette", current_chapter, f"p{current_chapter}_vignette{suffix}"

            file_name = save_image(doc, xref, name, output_dir)
            index.append(
                {
                    "file": file_name,
                    "type": kind,
                    "paragraph": chapter,
                    "pdf_page": page_number,
                    "size": [width, height],
                }
            )

    with open(os.path.join(output_dir, "illustrations.json"), "w", encoding="utf-8") as output:
        json.dump(index, output, ensure_ascii=False, indent=1)
    return index


if __name__ == "__main__":
    result = extract(
        sys.argv[1] if len(sys.argv) > 1 else "tome1.pdf",
        sys.argv[2] if len(sys.argv) > 2 else DEFAULT_OUTPUT_DIR,
    )
    for kind in ("vignette", "planche"):
        print(f"{kind}s : {sum(1 for item in result if item['type'] == kind)}")
