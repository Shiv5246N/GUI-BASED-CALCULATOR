   if "asin" not in exp and "acos" in exp and "atan" in exp:
            exp = exp.replace("sin", "math.sin")
            exp = exp.replace("cos", "math.cos")
            exp = exp.replace("tan", "math.tan")
            exp = exp.replace("cot", "1/math.tan")
            ex