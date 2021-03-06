# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, roomTitle, enterText):
    self.roomTitle = roomTitle
    self.enterText = enterText
    self.items = {}
  def __repr__(self):
    return('Location: ' + self.roomTitle + '\n' + self.enterText + '\n')

  def nextRoom(self, direction):
    return getattr(self, direction)  
  
  def additem(self, item):
    self.items[item.name] = item
  
  def getItemsList(self):
    return [item for item in self.items]  
  
  def removeItem(self, itemName):
    del self.items[itemName]
    