# dict
# set

# x = {"apple", "banana"}
# y = {"granade", "apple"}

# z = x.union(y)
# z = x.difference(y)
# x.difference_update(y)
# z = x.intersection(y)
# x.intersection_update(y)
# z = x.symmetric_difference(y)
# x.symmetric_difference_update(y)
# print(x)


# words = {}
#
#
# def count_words(word):
#     word = word.lower()
#     if word in words.keys():
#         words[word] += 1
#     else:
#         words[word] = 1
#
#
# text = "Hello world. Word hello is my favourite word"
# words_list = text.split()  # ["Hello", "world.", "Word", ...]
#
# for word in words_list:
#     word = word.replace(".", "").replace(",", "")
#     count_words(word=word)
#
# print(words)
from colorama import Fore, init

init(autoreset=True)

cart = []
print(Fore.BLUE + "add      => Savatchaga qo'shish\n"
                  "del      => Savatchadan o'chirish\n"
                  "show     => Savatchani ko'rsatish\n"
                  "search   => Savatchadan qidirish\n"
                  "exit     => Dasturni tugatish")

while True:
    command = input("\nBuyriq kiriting (add, del, show, search, exit): ")

    if command == "add":
        product = input(Fore.LIGHTMAGENTA_EX + "Maxsulot nomini kiriting: ")

        if product in cart:
            confirmation = input(
                Fore.GREEN + f"{product.capitalize()} maxsuloti savatchangizda allaqahon mavjud, yana qo'shishni istaysizmi (ha, yoq): ")

            if confirmation == "ha":
                cart.append(product)
                print(Fore.GREEN + f"{product.capitalize()} maxsuloti savatchaga muvaffaqiyatli qo'shildi")
            else:
                print(Fore.LIGHTRED_EX + "Bekor qilindi")

        else:
            cart.append(product)
            print(Fore.GREEN + f"{product.capitalize()} maxsuloti savatchaga muvaffaqiyatli qo'shildi")

    elif command == "del":
        # Maxsulot nomi so'ralishi kerak
        # Agar qabul qilingan maxsulot savatchada bor bo'lsa, unda:
        #   1. Maxsulot savatchada 1 marta uchrayotgan bo'lsa, unda o'chirib yuborilishi kerak
        #   2. (Ixtiyoriy). Maxsulot savatchada 2 yoki undan ko'p marta uchrasa, unda toki tugamagunicha so'rash kerak: "Olma maxsulot 2 marta uchramoqda, 1 tasini o'chirmoqchimisi (ha, yoq):"
        # Agar qabul qilingan maxsulot savatchada yo'q bo'lsa, unda
        #   unda bu haqida xabar berilishi kerak
        ...

    elif command == "show":
        print(Fore.CYAN + "Sizning savatchangizdagi maxsulotlar: " + ", ".join(cart))