def total_salary(path: str) -> list[str]:
    try:
        with open(path, encoding="utf-8") as file:
            total_sal = 0
            count = 0
            average_sal = 0
            for person in file:
                person = person.strip()
                if person:
                    try:
                        _, person_salary = person.split(",")
                        total_sal += float(person_salary)
                        count += 1
                    except ValueError:
                        print(f"Incorrect personal data: {person}")
            if count == 0:
                return (0, 0)
            else:
                average_sal = total_sal / count
                return (f"Загальна сума заробітної плати: {total_sal},\nСередня заробітна плата: {average_sal}")
    except FileNotFoundError:
        print(f"File {path} not found")
        return(0, 0)
    
result = total_salary("salary_file.txt")
print(result)



