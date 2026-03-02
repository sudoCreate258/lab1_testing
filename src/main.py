from temp_func import cel_to_fah, fah_to_cel, temp_to_kel
# DO NOT UPDATE CODE ABOVE THIS LINE

deg_str = chr(176)
# - cel_to_fah
# TODO - (Input) Assign data for test cases
arg = f"{0 }{deg_str}C"
exp = f"{32}{deg_str}F"
act = cel_to_fah(arg)

# TODO - (Process) Introduce the assert statememts
assert act == exp, f"{act} is not {exp} ? review cel_to_fah"

# TODO - (Output) Print passing cases
opt = "cel_to_fah:\n\t"
opt += f"{arg}{deg_str}C is {exp}{deg_str}F"
print(opt)

assert False, 'test'
# - fah_to_cel
# TODO - (Input) Assign data for test cases
# TODO - (Process) Introduce the assert statememts
# TODO - (Output) Print passing cases

# - temp_to_kel
# TODO - (Input) Assign data for test cases
# TODO - (Process) Introduce the assert statememts
# TODO - (Output) Print passing cases
