heading_valid = list(range(1, 7))

def heading_generator(h_string,h_size,p_list):
    heading_code = f"<h{h_size}>{h_string}</h{h_size}>"
    for p_text in p_list:
        heading_code += f"\n<p>{p_text}</p>"
    return heading_code

print(heading_valid)
heading_type = int(input("Please select a number from 1 to 6 for your heading type, then press enter: ").strip())
while heading_type not in heading_valid:
    heading_type = int(input("Invalid. Please type a number 1 through 6, then press enter: ").strip())

title = input("Please type out the text for your heading and press enter: ").strip()

paragraph_list = []
p_num = 0
while True:
    paragraph = input(f"Add paragraph #{p_num + 1}? Type one out and press enter. Submit a blank answer when finished:  ").strip()
    if (paragraph == ""):
        break
    else:
        p_num += 1
        paragraph_list.append(paragraph)

print(heading_generator(title,heading_type,paragraph_list))
