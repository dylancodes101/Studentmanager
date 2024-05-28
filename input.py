class Input:

    def menu_config(self, headers, selected_attributes):
        while True:
            sel_input = input(
                "Enter the number of the attribute you want to display (use '!' to end): "
            )
            if "!" in sel_input:
                break
            try:
                sel_input = int(sel_input) - 1
                if 0 <= sel_input < len(headers):
                    selected_attributes.append(sel_input)
                else:
                    print("Invalid attribute number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def input_check(self, input_type, input_name):
        while True:
            try:
                input_name = input_type(input(f"Enter {input_name}: "))
                return input_name
            except ValueError:
                print(f"Invalid input. Please enter a {type}")

    def fake_students_amount(self):
        num = self.input_check(
            int, "the amount of fake students you want to generate")
        return num