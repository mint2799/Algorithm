s = input()
mapping = {
    "fdsajkl;": "in-out", "jkl;fdsa": "in-out",
    "asdf;lkj": "out-in", ";lkjasdf": "out-in",
    "asdfjkl;": "stairs",
    ";lkjfdsa": "reverse"
}
print(mapping.get(s, "molu"))