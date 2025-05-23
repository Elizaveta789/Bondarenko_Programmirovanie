import re

with open("writer.txt", encoding="utf-8") as file:
    text = file.read()


lines = list(filter(None, text.split('\n')))


writer_p = re.compile(r'(?P<name>[А-ЯЁ][а-яё\-\s]+\s[А-ЯЁ]\.[А-ЯЁ]\.?)\((?P<birth>\d{4})[-–](?P<death>\d{4})\)')
works_p = re.compile(r'[«"](.*?)[»"]')


def every_line(line):
    writers = writer_p.search(line)
    if not writers:
        return None

    name = writers.group('name')
    birth = writers.group('birth')
    death = writers.group('death')


    works = works_p.findall(line)

    return {
        'name': name,
        'birth': birth,
        'death': death,
        'works': works
    }

all_works = works_p.findall(text)

all_inf = list(filter(None, map(every_line, lines)))


for writer in all_inf:
    works_str = ', '.join(writer['works']) if writer['works'] else 'произведения не указаны'
    print(f"{writer['name']} ({writer['birth']}-{writer['death']}): {works_str}")


print(f"\nОбщее количество произведений: {len(all_works)}")