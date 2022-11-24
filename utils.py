EPS = 1e-6

def latex_format(s):
    return s.strip().replace("*","").replace("exp(","e^{").replace(")","}")

def python_format(s):
    return s.strip().replace("e^{","exp(").replace("}",")")

# python_format("""
# -e^{t_s-t_f} - t_fe^{t_s-t_f} + t_se^{t_s-t_f} + e^{-t_f} + t_fe^{-t_f}
# """)