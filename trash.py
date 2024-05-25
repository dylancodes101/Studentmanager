def generate_student_table(students):
  headers = set()
  for student in students:
      headers.update(student.get_attributes().keys())
  headers = sorted(headers)

  input_handler = Input()
  selected_attributes = []
  input_handler.menu_config(headers, selected_attributes)

  headers_new = [headers[i] for i in selected_attributes]

  def display_table(start_index):
      table = []
      end_index = start_index + 10
      for i, student in enumerate(students[start_index:end_index], start=start_index):
          row = [getattr(student, header, None) for header in headers_new]
          table.append(row)
      print(tabulate(table, headers=headers_new))

  current_index = 0
  while True:
      display_table(current_index)

      user_input = input("Enter 'n' for next 10, 'p' for previous 10, or 'q' to quit: ").strip().lower()
      if user_input == 'n':
          if current_index + 10 < len(students):
              current_index += 10
          else:
              print("No more students to display.")
      elif user_input == 'p':
          if current_index - 10 >= 0:
              current_index -= 10
          else:
              print("You are at the beginning of the list.")
      elif user_input == 'q':
          break
      else:
          print("Invalid input. Please enter 'n', 'p', or 'q'.")
