deg_str = chr(176)

def cel_to_fah(temp_c):
  temp_lst = temp_c.split(deg_str)
  c_val = float(temp_lst[0])
  fah  = c_val * 9/5 + 32 
  return f"{fah:.1f}{deg_str}F"

def fah_to_cel(temp_f):
  temp_lst = temp_f.split(deg_str)
  f_val = float(temp_lst[0])
  cels  = f_val - 32 * 5/9
  return f"{cels:.1f}{deg_str}C"

def temp_to_kel(temp):
    temp_lst = temp.split(deg_str)
    c_flag = temp_lst[1] == 'C'
    f_flag = temp_lst[1] == 'F'
  
    new_temp = c_flag and (float(temp_lst[0]) + 273.15)
    new_temp = new_temp or (f_flag and ((float(temp_lst[0]) + 459.67) * 5/9))
    return f"{new_temp:.1f} K"

def print_steps(temp):
    temp_lst = temp.split(deg_str)
    val = float(temp_lst[0])
    c_flag = temp_lst[1] == 'C'
    f_flag = temp_lst[1] == 'F'

    str_cels =  f"C{deg_str} = ({deg_str}F - 32) / (9/5)\n"
    str_cels += f"C{deg_str} = ({val} - 32) / (9/5)\n"
    str_cels += f"C{deg_str} = {val - 32} / {9/5}\n"
    str_cels += f"C{deg_str} = {(val - 32) / (9/5)}\n"
    f_flag and print(str_cels)
    
    #TODO create string for fahr - step 2
    str_fahr = "" 
    c_flag and print(str_fahr)
    
    return ""
