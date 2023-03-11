import newton
import hermit
import input_output
import general_func
import root_system

OK = 1
NO = 0

def polinom_method_ex(data, n, x):
    newton_method = OK
    hermit_method = OK

    border_one, border_two = general_func.create_border(data, n, x)

    newton_data = []
    if (newton_method):
        newton_data = newton.newton_method_ex(data, border_one, border_two, n, x)
    
    if (hermit_method):
        hermit.hermit_method_ex(data, border_one, border_two, n, x, newton_data)


    
def menu():
    polinom_method = OK
    root = OK

    name_file = "../data/data.txt"

    data = input_output.read_file(name_file)

    if (len(data)):
        general_func.sort_table(data) 
        input_output.create_table(data)

        n, x = input_output.read_element()

        if (polinom_method):
            polinom_method_ex(data, n, x)

        if (root):
            root_system.root_system_ex(n)

if __name__ == "__main__":
    menu()
