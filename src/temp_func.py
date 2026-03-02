deg_str = chr(176)

def cel_to_fah(temp_c):
  temp_lst = temp_f.split(deg_str)
  f_val = float(temp_lst[0])
  cels  = f_val * 9/5 + 32 
  return f"{cels}{deg_str}F"

def fah_to_cel(temp_f):
  temp_lst = temp_f.split(deg_str)
  c_val = float(temp_lst[0])
  fahr  = c_val - 32 * 5/9
  return f"{fahr}{deg_str}C"

def temp_to_kel(temp):
    temp_lst = temp.split(deg_str)
    c_flag = temp_lst[1] == 'C'
    new_temp = (c_flag and float(temp_lst[0]) + 273.15) or (fah_to_cel(temp) + 273.15)
    return f"{new_temp} K"
