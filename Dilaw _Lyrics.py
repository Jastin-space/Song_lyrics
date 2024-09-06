import time
import sys

# Define the title of the song
title = "Dilaw by Maki"

# Define the lyrics of the song and their respective delays in seconds
lyrics_with_delays = [
    ("Mukhang delikado na naman ako", 1),
    ("O bakit ba kinikilig na naman ako?", 0.1),
    ("Pero ngayon ay parang kakaiba", 0.2),
    ("'Pag nakatingin sa'yong mata, ang mundo ay kalmahan", 0.1),  
    ("", 0.01),
    ("Ngayong nand'yan ka na, 'di magmamadali, ikaw lang ang katabi", 0.07), 
    ("Hanggang sa ang buhok ay pumuti", 1),
    ("'Di na maghahanap ng kung anong sagot sa mga tanong", 0.1),
    ("Dahil ikaw ang katiyakan ko", 0.1),
    ("Hinding-hindi na ako bibitaw,", 1),
    ("ngayong ikaw na ang kasayaw", 2), 
    ("Kung meron mang kulay ang aking nagsisilbing tanglaw", 2),
    ("Ikaw, ikaw ay DILAW", 0.1)
]

# Custom letter delays for specific lines
custom_letter_delays = {
    "'Pag nakatingin sa'yong mata, ang mundo ay kalmahan": 0.08,
    "Ngayong nand'yan ka na, 'di magmamadali, ikaw lang ang katabi": 0.06,
    "'Di na maghahanap ng kung anong sagot sa mga tanong": 0.07,
    "Hinding-hindi na ako bibitaw,": 0.09,
    "ngayong ikaw na ang kasayaw": 0.1,
    "Kung meron mang kulay ang aking nagsisilbing tanglaw": 0.1,
    "Ikaw, ikaw ay DILAW": 0.1
}

# Function to display the song title and lyrics letter by letter
def display_karaoke(title, lyrics_with_delays, default_letter_delay=0.1):
    print(f"Title: {title}\n")
    print("Lyrics:\n")
    
    for line, line_delay in lyrics_with_delays:
        custom_letter_delay = custom_letter_delays.get(line, default_letter_delay)
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(custom_letter_delay)
        print()  # Print newline after each line is completed
        time.sleep(line_delay)

# Call the function to display the song title and lyrics letter by letter
display_karaoke(title, lyrics_with_delays)
