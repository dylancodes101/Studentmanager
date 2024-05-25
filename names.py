import random

class Names:
    def generate_name_first(self):
        first_names = ["Aaron", "Bethany", "Carter", "Dana", "Ethan", "Fiona", "Gavin", "Hannah", "Ian", "Jenna",
                       "Kyle", "Liam", "Mia", "Noah", "Olivia", "Parker", "Quinn", "Riley", "Sophia", "Tyler",
                       "Uma", "Victor", "Willow", "Xander", "Yara", "Zane", "Alice", "Benjamin", "Chloe", "David",
                       "Ella", "Felix", "Grace", "Henry", "Isla", "Jack", "Kaitlyn", "Lucas", "Madeline", "Nathan",
                       "Olivia", "Patrick", "Quincy", "Rebecca", "Samuel", "Tara", "Ulysses", "Victoria", "Wyatt",
                       "Xena", "Yusuf", "Zoey", "Aiden", "Brianna", "Caleb", "Daisy", "Elijah", "Faith", "Gabriel",
                       "Hailey", "Isaac", "Jade", "Kevin", "Lillian", "Mason", "Natalie", "Owen", "Paisley", "Quinn",
                       "Ryan", "Savannah", "Thomas", "Ursula", "Vincent", "Wendy", "Xavier", "Yvonne", "Zachary",
                       "Abigail", "Blake", "Connor", "Delilah", "Evan", "Freya", "George", "Hazel", "Ivan", "Jasmine",
                       "Kai", "Leah", "Michael", "Nina", "Oscar", "Penelope", "Quentin", "Ruby", "Sebastian", "Tessa",
                       "Umar", "Vivian"]
        return random.choice(first_names)

    def generate_name_middle(self):
        middle_names = ["Ann", "Brian", "Christine", "David", "Elizabeth", "Francis", "Grace", "Henry", "Isabel",
                        "James", "Katherine", "Lloyd", "Marie", "Nicholas", "Olivia", "Patrick", "Quincy", "Rose",
                        "Stephen", "Tara", "Ulysses", "Victoria", "William", "Xavier", "Yvonne", "Zachary"]
        return random.choice(middle_names)

    def generate_name_last(self):
        last_names = ["Adams", "Bennett", "Coleman", "Diaz", "Edwards", "Foster", "Garcia", "Hall", "Irwin", "Johnson",
                      "Kelly", "Lopez", "Mitchell", "Nelson", "Owens", "Perez", "Quinn", "Rivera", "Sanders", "Taylor",
                      "Underwood", "Valdez", "Ward", "Xu", "Young", "Zimmerman"]
        return random.choice(last_names)
