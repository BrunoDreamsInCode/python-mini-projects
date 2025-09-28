alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


selection_type_resolution = str(input("Type 'encode' to encrypt and 'decode' to decrypt: ")).lower()
resolution = []


if selection_type_resolution == 'encode':
    print("DEBUG You selected a >ENCODE< mode")
    code = str(input("Type your message: "))
    shift_number = int(input("Type the shift number: "))

    for i in range(len(code)):
        for index, letter in enumerate(alphabet):
            if code[i].lower() == letter:
                resolution.append(alphabet[(index + shift_number) % len(alphabet)])

elif selection_type_resolution == 'decode':
    code = str(input("Type your message"))
    shift_number = int(input("Type the shift number: "))

    for i in range(len(code)):
        for index, letter in enumerate(alphabet):
            if code[i].lower() == letter:
                resolution.append(alphabet[(index - shift_number) % len(alphabet)])
else:
    print("Select a valid option")


print(f"Results: {''.join(resolution)}")
