def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f'Помилка в рядку: {line.strip()}')
        if not salaries:
            return 0, 0 
        
        total_sum = sum(salaries)
        average_sum = total_sum / len(salaries)
        return total_sum, average_sum
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    
path = "goit-pycore-hw-04/total_salary/salaries.txt"
result = total_salary(path)
if result:
    total_sum, average_sum = result
    print(f"Загальна сума заробітної плати: {total_sum}, Середня заробітна плата: {average_sum}")