from temp_func import cel_to_fah, fah_to_cel, temp_to_kel
# DO NOT UPDATE CODE ABOVE THIS LINE

deg_str = chr(176)
# - cel_to_fah
# TODO - (Input) Assign data for test cases
arg = f"{0}{ deg_str}C"
exp = f"{32}{deg_str}F"
act = cel_to_fah(arg)
assert act == exp, f"{act} is not {exp} ? review src/cel_to_fah"
# TODO - (Process) Introduce the assert statememts

# - fah_to_cel
# TODO - (Input) Assign data for test cases
# TODO - (Process) Introduce the assert statememts

# - temp_to_kel
# TODO - (Input) Assign data for test cases
# TODO - (Process) Introduce the assert statememts
