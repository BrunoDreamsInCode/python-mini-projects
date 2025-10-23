"""with open("my_text.txt") as file:
    content = file.read()
    print(content)"""


with open ("my_text.txt", mode="a") as file:
    file.write("\nCurrent last line over here!")

with open ("a_new_text_file_from_screch", mode="w") as new_file_txt_test:
    new_file_txt_test.write("Test new file being created")




