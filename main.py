import colorama

print("=== COLORAMA ===")


print(f"Тип {type(colorama)}")
print(f"Версія  {colorama.__version__}")
print(f"Де вона встановлена: {colorama.__file__}\n")


важливі_атрибути = ['Fore', 'Back', 'Style', 'init', 'deinit']

print("=== Головні компоненти ===")
for name in важливі_атрибути:
    компонент = getattr(colorama, name)

    print(f"Назва: {name} | {type(компонент)}")
