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
    temp_lst = (len(temp.split()) == 1 and temp.split(deg_str)) or (temp.split())
    c_flag = temp_lst[1] == 'C'
    f_flag = temp_lst[1] == 'F'
  
    new_temp = c_flag and (float(temp_lst[0]) + 273.15)
    new_temp = new_temp or (f_flag and ((float(temp_lst[0]) + 459.67) * 5/9))
    return f"{new_temp:.2f} K"

def print_steps(temp):
    temp_lst = (len(temp.split()) == 1 and temp.split(deg_str)) or (temp.split())
    val = float(temp_lst[0])
    c_flag = temp_lst[1] == 'C'
    f_flag = temp_lst[1] == 'F'
    k_flag = temp_lst[1] == 'K'

    str_cels =  f"C{deg_str} = ({deg_str}F - 32) / (9/5)\n"
    str_cels += f"C{deg_str} = ({val} - 32) / (9/5)\n"
    str_cels += f"C{deg_str} = {val - 32} / {9/5}\n"
    str_cels += f"C{deg_str} = {(val - 32) / (9/5):.3f}\n"
    
    f_flag and print(str_cels)
    
    #TODO create string for fahr - step 2
    str_fahr = "" 
    c_flag and print(str_fahr)
    
    
    str_kelv =  f"C{deg_str} = K - 273.15\n"           #print C from K
    str_kelv += f"C{deg_str} = {val} - 273.15\n"  
    str_kelv += f"C{deg_str} = {val - 273.15:.3f}\n\n"
    
    str_kelv += f"F{deg_str} = (K * (9/5)) - 459.67\n" #print F from K
    str_kelv += f"F{deg_str} = ({val} * (9/5)) - 459.67\n"
    str_kelv += f"F{deg_str} = ({val} * ({9/5})) - 459.67\n"
    str_kelv += f"F{deg_str} = ({val  * (9/5)} - 459.67\n"
    str_kelv += f"F{deg_str} = {val  * (9/5) - 459.67:.3f}\n"
    
    k_flag and print(str_kelv)
    
    return ""
