a = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
#a = a.lower
match a:
	case "сорок два" | "42":
		print("Да")
	case _:
		print("Нет")
