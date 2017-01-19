class Car(object):


    def def words(words):
  a = words.split()
  split_words = []
  for word in a:
    try:
      x = int(word)
      split_words.append(x)
    except:
      split_words.append(word)

  words_dict = {word: split_words.count(word) for word in split_words}

  return words_dict
a=words("hey there people of earth a we have or rather we are people from planet earth b")
print(words(a))__init__(self, name='General', model='GM' ,car_type='honda' ):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man

    def drive(self, spd):
        if self.car_type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self

    def wheels(self, num_of_wheels):
        return num_of_wheels


    def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
