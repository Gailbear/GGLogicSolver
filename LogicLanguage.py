# Python Logic Language implementation

class Puzzle(object):
  def __init__(self):
    self.categories = []

  def alloy(self):
    # returns a string
    # optimization opportunity: more efficient string concatenation
    string = ""
    for category in self.categories:
      if category.ordered:
        string +="open util/ordering[" + category.name + "] as "+ category.name.lower() + "Ord\n"
    # create abstract signatures
    for index in range(len(self.categories)):
      before_names = [cat.name for cat in self.categories[:index]]
      after_names = [cat.name for cat in self.categories[index + 1:]]
      name = self.categories[index]
      # try for a single pass through the lists for optimization later
      string += "abstract sig " + name + " {\n"
      for aname in after_names:
        string += "\t" + name.lower() + "_" + aname.lower() + " : one " + aname + ",\n"
      string += "} {" 
      for bname in before_names:
        string += "\t this.~" + bname.lower() + "_" + name.lower() + "\n"
      if index != 0:
        firstname = self.categories[0].name
        string += "\tall x : " + firstname + " | x." + firstname.lower() + "_" + name.lower() + " = this"
        for aname in after_names:
          string += "and\n\t\tx." + firstname.lower() + "_" + aname.lower() + " = this.@" + name.lower() + "_" + aname.lower()
        string += "\n"
      string += "}\n\n"
      members = self.categores[index].members
      for member in members:
        string += "one sig " + member.name + " extends " + name + " {}\n"
      string += "\n"
      if self.categories[index].ordered:
        string += "fact {\n"
        ordname = name.lower() + "Ord"
        string += "\t" + ordname + "/first = " members[o].name + "\n"
        for m1, m2 in zip(members[:-1], members[1:]):
          string += "\t" + ordname + "/next[" + m1.name + "] = " + m2.name + "\n"
        string += "}\n\n"
      string += "\n"
    # create clues

class Category(object):
  def __init__(self, name = "Category", amount = 5, ordered = False):
    self.amount = amount
    self.ordered = ordered
    self.members = []
    self.name = name

class Member(object):
  def __init__(self, name = "Object"):
    self.name = name

class Relationship(object):
  def __init__(self, obj1 = None, obj2 = None):
   self.obj1 = obj1
   self.obj2 = obj2

class Is (Relationship):
  pass

class IsNot (Relationship):
  pass

class Before (Relationship):
  pass

class After (Relationship):
  pass

class ImmBefore (Relationship):
  pass

class ImmAfter (Relationship):
  pass
