class Good:
    def __init__(self):
        pass

    def behaviour(self, habit, habit_choice, dist='All'):
        print "You are "+habit+" a good Human being, loves -- "+dist+" -- type of -- "+habit_choice+" --"
        
        
class VeryGood(Good):
    def behaviour (self, habit, dist='All'):
        #here, there is one less argument, habit_choice is missing
        Good.behaviour(self, 'Pet Lover', dist)
        
        
good = Good()
very_good = VeryGood()

good.behaviour('Pet Lover','Dogs')  

#Output : You are Pet Lover a good Human being, loves -- All -- type of -- Dogs --

very_good.behaviour('Pet Lover', 'Cats')
#Output : You are Pet Lover a good Human being, loves -- All -- type of -- Cats --

very_good.behaviour('Pet Lover')
#Output : You are Pet Lover a good Human being, loves -- All -- type of -- All --


#Observe here, very_good have two methods name behaviour() but when we pass less arguments 
# it passes the value of dist to the habit_choice parameter
        
