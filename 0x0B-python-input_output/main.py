#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file.txt", "Toaol!\n")
print(nb_characters_added)
