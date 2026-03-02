from temp_func import deg_str, print_steps, cel_to_fah, fah_to_cel, temp_to_kel
# DO NOT UPDATE CODE ABOVE THIS LINE

# - cel_to_fah
# TODO - (Input) Assign data for test cases - step 1
arg, exp, act = f"{0 }{deg_str}C", f"{32}{deg_str}F", cel_to_fah(arg)

# TODO - (Process) Introduce the assert statememts - step 3
assert act == exp, f"{print_steps(arg)} {act} != {exp} ? review temp_func.py"

# TODO - (Output) Print passing cases - step 4
opt = "cel_to_fah:\n\t"
opt += f"{arg}{deg_str}C is {exp}{deg_str}F"
print(opt)

# - fah_to_cel
# TODO - (Input) Assign data for test cases - step 1
# TODO - (Process) Introduce the assert statememts - step 3
# TODO - (Output) Print passing cases - step 4

# - temp_to_kel
# TODO - (Input) Assign data for test cases - step 1
# TODO - (Process) Introduce the assert statememts - step 3
# TODO - (Output) Print passing cases - step 4
