atn, eye = int(input()), int(input())
alien = {"TroyMartian": atn >= 3 and eye <= 4, "VladSaturnian": atn <= 6 and eye >= 2, "GraemeMercurian": atn <= 2 and eye <= 3}
print(*[name for name, condition in alien.items() if condition])