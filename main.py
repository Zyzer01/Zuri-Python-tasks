class Student: 
    #[assignment] Skeleton class. Add your code here
def __init__(self, name, age, tracks, score):
    self.name = name
    self.age = age
    self.tracks = tracks
    self.score = score
 

    def change_name (self, name):
    self.name = name
    return self.name
 
    def change_age (self, age):
    self.age = age
    return self.age
 

    def add_track(self, track):
    self.tracks.append(track)
    return self.tracks
 
    def get_ score(self):
    return self.score
 

Bob = Student (name="Bob", age=26, tracks=["FE", "BE"],score=20.90)


print("Initially...")
print (Bob.name)
print (Bob.age)
print (Bob.tracks[0])
print (Bob.score)

# Expected methods
Bob.change _name ("Peter")
Bob.change_age (34)
Bob.add_track("Product Designer")
Bob.get_score()

print ("After changing name, age, tracks and score..")
print (Bob.name)
print (Bob.age)
print (Bob.tracks[0])
print (Bob.score)