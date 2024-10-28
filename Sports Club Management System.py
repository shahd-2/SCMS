class Sportclub:
    def __init__(self , name , budget , founded_year ,location, number_of_medals , number_of_wins ,costume_color):
        self.name = name
        self.__budget = budget
        self.founded_year = founded_year
        self.location=location
        self.number_of_medals=number_of_medals
        self.number_of_wins= number_of_wins
        self.costume_color=costume_color
    def calculate_tax(self):
       return (0.2 * self.__budget)+(self.number_of_wins *0.1)+(self.number_of_medals * 0.1)

    def calculate_age(self , current_year):
        return current_year - self.founded_year
    def get_budget (self) :
        return self.__budget
    def set_budget (self , new_budget):
        self.__budget=new_budget
    def __gt__(self, other) :
        return self.number_of_medals > other.number_of_medals
    def __lt__(self, other):
        return self.number_of_medals < other.number_of_medals
    def __eq__(self, other):
        return self.number_of_medals == other.number_of_medals

class Player(Sportclub) :
    def __init__ (self, name , budget , founded_year , location , number_of_medals , number_of_wins ,costume_color, player_name, number, position, goals,
                  assists, matches, pnumber_of_medals ):
         Sportclub.__init__(self , name , budget , founded_year ,location , pnumber_of_medals , number_of_wins ,costume_color)
         self.player_name=player_name
         self.number=number
         self.position=position
         self.goals=goals
         self.assists=assists
         self.matches=matches
         self.pnumber_of_medals=pnumber_of_medals

    def calculate_performance (self):
        return  (self.goals * 0.7) + (self.assists * 0.15) +  (self.matches * 0.15)

class Coach(Sportclub) :
    def __init__(self, name, budget, founded_year,location, number_of_medals, number_of_wins , costume_color , coache_name , experience_level ,training_certificates, cnumber_of_medals):
        Sportclub.__init__(self, name, budget, founded_year,location, cnumber_of_medals, number_of_wins ,costume_color)
        self.coach_name=coache_name
        self.experience_level=experience_level
        self.training_certificates=training_certificates
        self.cnumber_of_medals=cnumber_of_medals
    def calculate_efficiency(self):
        return (self.experience_level * 0.5) + (self.training_certificates * 0.20) + (self.cnumber_of_medals * 0.30)
club1=Sportclub("Jordan",5000000 ,200 ,"عمان" ,100 ,200,
                'red /white')
club2=Sportclub("Qatar", 10 ,2000,'قطر',1,1 ,'dark red')

print(f"{club1.name} tax dues: {club1.calculate_tax()}")
print(f"{club2.name} tax dues: {club2.calculate_tax()}")

player1=Player("Jordan",5000000 ,200 ,"عمان" ,100 ,200,
                'red /white',"يزن نعيمات" , 9 ,"مهاجم " ,120 ,50,100
               ,35)
player2=Player("Qatar", 10 ,2000,'قطر',1,1 ,'dark red'
               ,"اكرم عفيف " , 11 ,    'مهاجم' ,3 ,0,1000,0)

print(f'{player1.player_name} performance score : {player1.calculate_performance()}')
print(f'{player2.player_name} performance score : {player2.calculate_performance()}')

coach1=Coach("Jordan",5000000 ,200 ,"عمان" ,100 ,200,
                'red /white' ,"جمال السلامي " ,15 ,48 ,17)
coach2=Coach("Qatar", 10 ,2000,'قطر',1,1 ,'dark red',
             "فليكس " ,2 ,5 ,3)

print(f'{coach1.coach_name} efficiency score : {coach1.calculate_efficiency()}')
print(f'{coach2.coach_name} efficiency score : {coach2.calculate_efficiency()}')