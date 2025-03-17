def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                line = line.strip()
                
                try: 
                    cat_id, name, age = line.split(",")
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка у рядку {line}")
                    
            return cats_info
        
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    
cats_info = get_cats_info("goit-pycore-hw-04/get_cats_info/cats_file.txt")
print(cats_info)
