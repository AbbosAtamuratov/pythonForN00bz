import module
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    module.init(value_a, value_b)
    result = module.do_it()
    view.view_data(result)