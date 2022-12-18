class Amina:
    def __init__(self, age):
        self.age = age

class Sabina:
    def __init__(self, name):
        self.name = name

class Kaliya:
    def kali_method(self):
        print('привет')


class Kanikey:
    def kani_method(self):
        print('я инопланетянин')


class Sophia(Amina, Sabina, Kaliya, Kanikey):
    def __init__(self, name, age):
        Amina.__init__(self, name)
        Sabina.__init__(self, age)


sop = Sophia('Lana', 20)
sop.kali_method()
sop.kani_method()

lol = open('file.txt', 'w', encoding='UTF-8')
lol.write(' git init\n git add .\n git commit -m "..."\n git push origin master\n git branch\n git checkout -b ... \n '
          'git remote remove origin\n git merge ...\n git checkout master\n git remote add origin\n git branch -d ...\n ')
lol.close()











