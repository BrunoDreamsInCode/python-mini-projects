def calculate_love_score(name_man, name_girl):
    true_amount = 0
    love_amount = 0
    check_true = "true"
    check_love = "love"
    both_names = (name_man + name_girl).lower()

#true count
    for letter in both_names:
        if letter in check_true:
            true_amount += 1

#love count
    for letter in both_names:
        if letter in check_love:
            love_amount += 1

    print(f"{true_amount}{love_amount}")

#output
calculate_love_score(name_man='Kanye West', name_girl='Kim Kardashian')