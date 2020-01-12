def main():
  file = open("day-1-input.txt", "r")
  file_input = file.readlines()
  mass = sum([int(line) // 3 - 2 for line in file_input])
  print(mass)
  mass = 0
  for line in file_input:
    module_mass = int(line) // 3 - 2
    while module_mass > 0:
        mass += module_mass
        module_mass = module_mass // 3 - 2
  print(mass)

