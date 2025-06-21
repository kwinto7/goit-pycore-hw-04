def get_cats_info(path: str) -> list[object]:
    cats = []
    try:
        with open(path, encoding="utf-8") as file:
            
            for cat in file:
                cat = cat.strip()
                if cat:
                   try:
                        cat_id, cat_name, cat_age = cat.split(",")
                        cats.append({
                            "id": cat_id,
                            "name": cat_name,
                            "age": cat_age
                        })
                   except ValueError:
                       print(f"incorrect data: {cat}")
    except FileNotFoundError:
        print(f"File {path} not found")
    return cats

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

