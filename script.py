#Art Marketplace Project
#Completed as part of Codecademy - Class Inheritance Review Project
#Meant to demonstrate an art market place that can buy and sell pieces of art.
#By: E.Cope
#Date: Jan. 2020


class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    string = self.artist + ". \"" + self.title + "\". " + str(self.year) + ", " + self.medium + ". " + self.owner.name + ", " + self.owner.location + "."
    return string
  
#5
#girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Madonlin (Fanny Tellier)", "oil on canvas", 1910)

#6
#print(girl_with_mandolin)

#7
class Marketplace:
  
  #8
  def __init__(self):
    self.listings = []
  
  #9
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  #10
  def remove_listing(self, listing):
    self.listings.remove(listing)
  
  #11
  def show_listings(self):
    for listing in self.listings:
      print(listing)

#12/13
veneer = Marketplace()
veneer.show_listings()

#14
class Client:
  #15
  def __init__(self, name, location, museum):
    self.name = name
    self.location = location
    self.is_museum = museum
    
  #26
  def sell_artwork(self, artwork, price):
    if (self == artwork.owner):
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
  
#16/17/18
edytta = Client("Edytta Halpirt", "Private Collector", False)
moma = Client("THE MOMA", "New York", True)
#21
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Madonlin (Fanny Tellier)", "oil on canvas", 1910, edytta)
#22
#print(girl_with_mandolin)

#23
class Listing:
  def __init__(self, art, price, client):
    self.art = art
    self.price = price
    self.seller = client
    
  def __repr__(self):
    string = "%s, %s." %(self.art.title, self.price)
    return string
  
#27/28
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)   
print(girl_with_mandolin)

veneer.show_listings() #nothing prints bc there are no listings left

#skipped part 35 -- Extension
