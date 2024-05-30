from tabulate import tabulate


#students:the class of students
#data the actuall dict storing the info
#gets the attribute for the class and updates the set
# a set() (basically an easy dict)https://chatgpt.com/share/7ea61115-a859-4486-a0cb-923cb8c363f4
def generate_sel_output(students, data):
    headers = set()

    for student in students:
        headers.update(student.get_attributes().keys())
    headers = sorted(headers)

    header_table = [(i + 1, header) for i, header in enumerate(headers)]
    print(tabulate(header_table, headers=["#", "Attribute"]))












    """#sel = int(
        #input("Sort by which attribute (enter corresponding number): ")) - 1
    #sort_attribute = header_table[sel][1]

    sorted_data = sorted(data,
                         key=lambda x: int(x[sort_attribute])
                         if x[sort_attribute].isdigit() else x[sort_attribute],
                         reverse=True)
    #print(tabulate(sorted_data, headers='keys', tablefmt='grid'))"""
