import random

#EXERCISE 1 

class Creature():
    
    def __init__(self,name,maxhp=10,hp_cap=10):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.Abilities={'Attack':1,'Defense':5,'Speed':5}

    def check_life(self):
        if self.maxhp <=0:
            self.maxhp=0
            print(self.name,'HP is: ', self.maxhp, self.name,' fainted.')
            return True
            
            
        else:
            print(self.name,'HP is: ',self.maxhp)
            return False



    def attack(self,target):
        print(self.name,'attacks',target.name)

        self.roll=random.randint(1, 20)
        self.attackplus=random.randint(1,4)
        if self.roll<(target.Abilities['Defense'])+(target.Abilities['Speed']):
            print('Attack not successful')

        else:
            print('Attack Succcessful')
            target.maxhp=(target.maxhp)-(self.Abilities['Attack']+self.attackplus)
            print('Attack did: ',self.Abilities['Attack']+self.attackplus,'damage to ',target.name)

    def turn(self,round_num,target):
        self.attack(target)
        if target.check_life==0:
            
            return True
        else:
            return False

# monster1=Creature('monster1',10)
# monster2=Creature('monster2',10)
# i=1
# while i<=20:    
#     print('##################### Round:',i,'########################\n')
        
#     print('monster1 attacks monster 2')
#     monster1.turn(i,monster2)
#     monster2.check_life()
#     if monster2.maxhp<=0:
#         print(monster2.name,'fainted.')
#         break
#     print()
    
        

#     print('monster 2 attacks monster 1')
#     monster2.turn(i,monster1)
#     monster1.check_life()
#     if monster1.maxhp<=0:
#         print(monster1.name,'fainted.')
#         break
#     print()
    
#     i+=1
# #END OF TASK 1

class Fighter(Creature):

    def __init__(self,name,Abilities,maxhp=50,hp_cap=50):
        self.name=name
        self.Abilities={'Attack':5,'Defense':10,'Speed':3}
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.shieldstatus=False
    
    def shield_up(self):
        if self.shieldstatus==False:
            print(self.name,' raises shield.')
            self.Abilities['Defense']+=5
            self.Abilities['Attack']-=5
            self.shieldstatus=True
        else:
            print('Shield already up!')

        

    def shield_down(self):
            
        if self.shieldstatus==True:
            print(self.name,' puts shield down.')
            self.Abilities['Defense']-=5
            self.Abilities['Attack']+=5
            self.shieldstatus=False

        
    
    
    def turn(self,round_num,target):
        if round_num%4==1:
            self.attack(target)
            self.shield_up()
            
            target.check_life()
            

        if round_num%4==2:
            self.attack(target)

            target.check_life()
           
        
        if round_num%4==3:
            self.attack(target)

            target.check_life()
           
        
        if round_num%4==0:
            self.shield_down()
            self.attack(target)

            target.check_life()
           


# #SCRIPT 2

# monster1=Creature('monster1')
# Fighter1=Fighter('Fighter1',{'Attack':5,'Defense':10,'Speed':3})
# i=1
# while i<=20:    
#     print('##################### Round:',i,'########################\n')
        
#     Fighter1.turn(i,monster1)
#     if monster1.maxhp<=0:
#         print(monster1.name,'fainted.')
#         print(Fighter1.name,'wins!')
#         break
#     print()
        

#     monster1.turn(i,Fighter1)
#     Fighter1.check_life()
#     if Fighter1.maxhp<=0:
#         print(monster1.name,'wins!')
#         break
#     print()
#     i+=1

# #END OF TASK 2

class Archer(Creature):

    def __init__(self,name,Abilities,maxhp=30,hp_cap=30):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.Abilities={'Attack':7, 'Defense': 8, 'Speed': 8}
        self.statsmodified=False
    
    def sneak_attack(self,target):
        self.attackroll=0
        self.attackadder=random.randint(1, 8)
        print(self.name,'sneak attacks',target.name)

        self.roll1=random.randint(1, 20)
        self.roll2=random.randint(1, 20)
        
        if self.roll1>=self.roll2:
            self.attackroll==self.roll1
        else:
            self.attackroll==self.roll2

        if self.Abilities['Speed']>target.Abilities['Speed']:
            self.attackroll+=self.Abilities['Speed']-target.Abilities['Speed']
        
        if self.statsmodified==False:
            self.Abilities['Defense']-=3
            self.Abilities['Attack']+=3
            self.statsmodified=True
        
        else:
            self.Abilities['Defense']+=0
            self.Abilities['Attack']+=0

        
        if self.attackroll<(target.Abilities['Defense'])+(target.Abilities['Speed']):
            print('Attack not successful')

        else:
            print('Attack Succcessful')
            target.maxhp=(target.maxhp)-(self.Abilities['Attack']+self.attackadder)
            print('Attack did: ',self.Abilities['Attack']+self.attackadder,'damage to ',target.name)

    def attack(self,target):
        if self.statsmodified==True:
            self.statsmodified==False
            print(self.name, 'stats returned to normal.')
        self.Abilities['Attack']=7
        self.Abilities['Defense']=8
        self.Abilities['Speed']=8

        super().attack(target)

    def turn(self,round_num,target):
        if round_num%4==1:
            self.attack(target)
            
            if target.check_life()==0:
                return True
            else:
                return False

        if round_num%4==2:
            self.sneak_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
        
        if round_num%4==3:
            self.sneak_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
        
        if round_num%4==0:
            self.sneak_attack(target)
            
            if target.check_life()==0:
                return True
            else:
                return False
           

# fighter1=Fighter('fighter1')
# Colman=Archer('Colman')
# i=1
# while i<=20:    
#     print('##################### Round:',i,'########################\n')
        
#     Colman.turn(i,fighter1)
        

#     fighter1.turn(i,Colman)
#     i+=1
#END OF TASK 3

# Exercise 2 TASK 1

class Goblin(Creature):
    def __init__(self,name,Abilities,maxhp=15,hp_cap=15):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.Abilities={'Attack':4,'Defense':6,'Speed':6}


    def attack(self,target):
        super().attack(target)

    def check_life(self):
            super().check_life()

    def turn(self,round_num,target):
        super().turn(self,target)

class Orc(Creature):
    def __init__(self,name,Abilities,maxhp=50,hp_cap=50):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.Abilities={'Attack':10,'Defense':6,'Speed':2}

    def heavy_attack(self,target):
        self.modified=False

        if self.modified==False:
            print(self.name,'uses heavy attack on',target.name)

            self.Abilities['Attack']+=5
            self.Abilities['Defense']-=3
            super().attack(target)
        else:
            super().attack(target)
        
    def attack(self,target):
        self.Abilities['Attack']=10
        self.Abilities['Defense']=6
        self.Abilities['Speed']=2
        
        print(self.name,'attacks',target.name)

        self.roll=random.randint(1, 20)
        self.attackplus=random.randint(1,4)
        if self.roll<(target.Abilities['Defense'])+(target.Abilities['Speed']):
            print('Attack not successful')

        else:
            print('Attack Succcessful')
            target.maxhp=(target.maxhp)-(self.Abilities['Attack']+self.attackplus)
            print('Attack did: ',self.Abilities['Attack']+self.attackplus,'damage to ',target.name)

    def turn(self,round_num,target):
        if round_num%4==1:
            self.attack(target)
                
            if target.check_life()==0:
                return True
            else:
                return False

        if round_num%4==2:
            self.attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
            
        if round_num%4==3:
            self.attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
            
        if round_num%4==0:
            self.heavy_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False

# Scary_orc=Orc('Scary_Orc')
# Scary_goblin=Goblin('Scary_Goblin')
# i=1
# while i<=20:    
#     print('##################### Round:',i,'########################\n')
        
#     Scary_orc.turn(i,Scary_goblin)
#     print('\n')
    
#     Scary_goblin.turn(i,Scary_orc)
#     Scary_orc.check_life()
#     i+=1
#     print('\n')

#END OF TASK 1

class OrcGeneral(Orc,Fighter):
    def __init__(self,name,Abilities,maxhp=100,hp_cap=100):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.shieldstatus=False
        self.Abilities={'Attack':10,'Defense':6,'Speed':2}

    def turn(self, round_num,target):
        if round_num%4==1:
            self.attack(target)
            self.shield_up()
            self.shieldstatus=True


                
            if target.check_life()==0:
                return True
            else:
                return False

        if round_num%4==2:
            self.attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
            
        if round_num%4==3:
            self.shield_down()
            self.shieldstatus=False

            self.attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
            
        if round_num%4==0:
            self.heavy_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False

class GoblinKing(Archer,Goblin):
    def __init__(self,name,Abilities,maxhp=50,hp_cap=50):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.statsmodified=False
        self.Abilities={'Attack':4,'Defense':6,'Speed':6}

    def turn(self,round_num,target):
        if round_num%4==1:
            self.attack(target)
            
            if target.check_life()==0:
                return True
            else:
                return False

        if round_num%4==2:
            self.sneak_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
        
        if round_num%4==3:
            self.sneak_attack(target)

            if target.check_life()==0:
                return True
            else:
                return False
        
        if round_num%4==0:
           self.sneak_attack(target)
        
        


# Scary_OrcGeneral=OrcGeneral('Scary_Orc_General')
# Scary_GoblinKing=GoblinKing('Scary_Goblin_King')
# i=1
# while i<=20:    
#     print('##################### Round:',i,'########################\n')
        
#     Scary_OrcGeneral.turn(i,Scary_GoblinKing)
#     print('\n')
    
#     Scary_GoblinKing.turn(i,Scary_OrcGeneral)
#     i+=1
#     print('\n')

#END OF TASK 1

#EXERCISE 3 TASK 1

class Wizard(Creature):
    def __init__(self,name,Abilities,maxhp=20,hp_cap=20,mana=100):
        self.name=name
        self.maxhp=maxhp
        self.hp_cap=hp_cap
        self.Abilities={'Attack':3,'Defense':5,'Speed':5,'Arcana':10}
        self.mana=mana #range(0,100)

    def attack(self,target):
        self.mana+=20
        if self.mana>=100:
            self.mana=100
            print('Mana is full.')
        print(self.name,'attacks',target.name)

        self.roll=random.randint(1, 20)
        self.attackplus=random.randint(1,4)
        if self.roll<(target.Abilities['Defense'])+(target.Abilities['Speed']):
            print('Attack not successful')

        else:
            print('Attack Succcessful')
            target.maxhp=(target.maxhp)-(self.Abilities['Attack']+self.attackplus)
            print('Attack did: ',self.Abilities['Attack']+self.attackplus,'damage to ',target.name)
            if target.maxhp<=0:
                        print(target.name, 'fainted.')
    
    def recharge(self):
        self.mana+=30

        if self.mana>=100:
            self.mana=100
            print('Mana is full.')
        else:
            print('Mana is recharged to',self.mana)

    def fire_bolt(self,target):
        
        self.roll=random.randint(1, 20)+((self.Abilities['Arcana']*0.5)//1)
        x=random.randint(1,self.Abilities['Arcana'])

        self.attackplus=random.randint(1,4)
        if self.roll<(target.Abilities['Defense'])+(target.Abilities['Speed']):
            print('Attack not successful')

        else:
            print('Attack Succcessful')
            self.mana+=10
            if self.mana>=100:
                self.mana=100
                print('Mana is full.')
            else:
                print('Mana is recharged to',self.mana)
            target.maxhp=(target.maxhp)-x
            print('Attack did: ',x,'damage to ',target.name,'HP: ', target.maxhp)
            if target.maxhp<=0:
                        print(target.name, 'fainted.')
    
    def heal(self,target):
        if self.mana<20:
            
            print('Mana is too low to heal.')
        else:
            self.mana-=20
            z=(random.randint(0,8))+((self.Abilities['Arcana']*0.5)//1)
            target.maxhp+=z
            if target.maxhp>=target.hp_cap:
                target.maxhp=target.hp_cap
            print(self.name, 'healed ', target.name,' by ', z,' HP.')
            print(target.name,' HP is ',target.maxhp,'.')
            
    
    def mass_heal(self,target):

        if self.mana<30:
            
            print('Mana is too low to heal.')
        else:
            self.mana-=30
            y=(random.randint(0,10))+((self.Abilities['Arcana']))
            for i in target:
                i.maxhp+=y
                if i.maxhp>=i.hp_cap:
                    i.maxhp=i.hp_cap
                print(self.name, 'healed',i.name,' by ', y,' HP.')
                print(i.name, 'HP is ', i.maxhp)


    def fire_storm(self,target):
        if self.mana<50:
            print('Mana too low to cast firestorm')
        
        else:
            self.mana-=50
            x=(random.randint(1,20))+(self.Abilities['Speed'])

            fulldamage=(random.randint(5,20))+(self.Abilities['Arcana'])
            if x>=self.Abilities['Arcana']:
                fulldamage=(fulldamage)//2
                for i in target:
                    i.maxhp-=fulldamage
                    print(self.name,'did ',fulldamage,'damage to ',i.name, 'HP: ',i.maxhp)
                    if i.maxhp<=0:
                        print(i.name, 'fainted.')

            else:
                for i in target:
                    i.maxhp-=(random.randint(5,20))+(self.Abilities['Arcana'])

                    print(self.name,'did ',((fulldamage*0.5)//1),'damage to ',i.name, 'HP: ', i.maxhp)
                    if i.maxhp<=0:
                        print(i.name, 'fainted.')


# allieslist=[]
# enemieslist=[]


# Gandalf=Wizard('Gandalf',{'Attack':3,'Defense':5,'Speed':5,'Arcana':10})
# Gandalf.fire_bolt
# Gandalf.fire_storm(enemieslist)
# Gandalf.mass_heal(allieslist)
# Gandalf.heal(buddy1)
# Gandalf.heal(buddy2)

# END OF TASK 2

#EXERCISE 4 TASK 1

class Battle:

    def __init__(self):
        
        self.enemies = [GoblinKing('GoblinKing',{'Attack':7,'Defense':8,'Speed':8},50), OrcGeneral('OrcGeneral',{'Attack':10,'Defense':6,'Speed':2},100), Goblin('Goblin',{'Attack':4,'Defense':6,'Speed':6},15), Orc('Orc',{'Attack':10,'Defense':6,'Speed':2,},50)]

        self.allies = [Fighter('Fighter', {'Attack':5,'Defense':10,'Speed':3},50), Archer('Archer',{'Attack':7,'Defense':8,'Speed':8},30)]

        self.player = Wizard('Gandalf', {'Attack':3,'Defense':5,'Speed':5,'Arcana':10},20)

        self.friendly_list=self.allies + [self.player]

        self.round = 1


    
        

#TASK 2

    def auto_select(self,target_list):
        chosen_target = random.choice(target_list)
        return chosen_target
        
            
        
       

    def select_target(self,target_list):
        for i in target_list:
            if i.maxhp<=0:
                self.target_list.remove(i)
        
        for i in target_list:
            print(target_list.index(i),': ',i.name,' HP: ',i.maxhp,'/',i.hp_cap)
        
        
        while True:
            
            selection=int(input('Select a target from the list: '))
            

            if selection in range(len(target_list)):   
                print('You have selected ',target_list[selection].name)
                return target_list[selection]
            
            else:
                print('Please select a valid target.')
                continue

            



#TASK 3

    def start(self):
        
        game_over=False

        combined_list=[self.player,]
        
        for i in self.enemies:
            combined_list.append(i)
        for i in self.allies:
            combined_list.append(i)

        round_num=1
        # Sorting the list of creatures by speed
        combined_list.sort(key=lambda x:x.Abilities['Speed'], reverse=True)
        
        j=1
        print('The Battle Begins.')

        while j > 0:
            
            if game_over==False:
           
                print('####################################')
                print('ROUND NUMBER: ',round_num)
                print('####################################')
                print('\n')
                
                

                for i in combined_list:   
                    if i.maxhp<=0: 
                        combined_list.remove(i) 

                    for q in self.enemies:
                        if q.maxhp<=0:
                            self.enemies.remove(q)  


                    for w in self.friendly_list:
                        if w.maxhp<=0:
                            self.friendly_list.remove(w)
                        
                    
                    if i in self.friendly_list:
                        x=self.auto_select(self.enemies)
                        
                        if i!=self.player:
                            if self.player.maxhp<=0:
                                print(self.player.name,' fainted, Game Over.')
                                game_over=True
                                break
                                
                            
                                    

                            i.turn(round_num,x)
                            print('')
                            for i in combined_list:   
                                if i.maxhp<=0: 
                                    combined_list.remove(i) 

                                for q in self.enemies:
                                    if q.maxhp<=0:
                                        self.enemies.remove(q)  


                                for w in self.friendly_list:
                                    if w.maxhp<=0:
                                        self.friendly_list.remove(w)



                        else:
                            battle1.player_turn()

                            for i in combined_list:   
                                        if i.maxhp<=0: 
                                            combined_list.remove(i) 

                                        for q in self.enemies:
                                            if q.maxhp<=0:
                                                self.enemies.remove(q)  


                                        for w in self.friendly_list:
                                            if w.maxhp<=0:
                                                self.friendly_list.remove(w)
                    
                    elif i in self.enemies:   
                        x=self.auto_select(self.friendly_list)
                        i.turn(round_num,x)
                        for i in combined_list:   
                                        if i.maxhp<=0: 
                                            combined_list.remove(i) 

                                        for q in self.enemies:
                                            if q.maxhp<=0:
                                                self.enemies.remove(q)  


                                        for w in self.friendly_list:
                                            if w.maxhp<=0:
                                                self.friendly_list.remove(w)
                
                    if len(self.enemies)==0:
                        print('All enemies defeated.')
                        print('Game Over')
                        game_over=True
                        break

                        
            
                    if len(self.friendly_list)==0:
                        print('All allies defeated.')
                        print('Game Over')
                        game_over=True
                        break

                        

                    if self.player.maxhp==0:
                        print('Player killed, Game over.')
                        game_over=True
                        break          
                    
                    

                round_num+=1
                print('\n')
            
            else:
                break
        
            
        

    def player_turn(self):

        print('')
        print('Player: ', self.player.name, 'HP:', self.player.maxhp, '/',self.player.hp_cap,'Mana:', self.player.mana,'/100')
        print('')
        print('Allies:')
        for i in self.allies:
            print(i.name, 'HP: ',i.maxhp,'/',i.hp_cap)
        print('=================================')
        
        print('Actions ', 'A: Attack','R: Recharge Mana')
        print('Spells ', '1: Heal ', '2: Firebolt ', '3: Mass Heal', '4: Firestorm' )
        print('To quit game type : QUIT')
        

        while True:
            
                
                choice= str(input('Enter action: ')).upper()

                
                
                if choice=='QUIT':
                    print('Quitting Game.')
                    quit()
                
                elif choice == 'A':
                    print('')
                    self.player.attack(self.select_target(self.enemies))
                    break
                
                
                elif choice == 'R':
                    print('')
                    if self.player.mana==100:
                        print('Mana full!')
                    self.player.recharge()
                    break
                
                elif choice == '1':
                    print('')
                    if self.player.mana <20:
                        print('Mana too low to use heal.')
                        continue
                    else:
                        self.player.heal(self.select_target(self.friendly_list))
                    break
                
                
                elif choice == '2':
                    print('')
                    self.player.fire_bolt(self.select_target(self.enemies))
                    break

                elif choice == '3':
                    print('')
                    if self.player.mana < 30:
                        print('Mana too low to use mass heal.')
                        continue
                    else:    
                        self.player.mass_heal(self.friendly_list)
                    break

                elif choice == '4':
                    print('')
                    if self.player.mana < 50:
                        print('Mana too low to use fire storm.')
                        continue
                    else:
                        self.player.fire_storm(self.enemies)
                    break
                
                else:
                    print('Please enter valid choice.')

                    continue
            
     


battle1 = Battle()

battle1.start()



    












        

            


