# -*- coding: utf-8 -*-

class GildedRose(object):

    # 2 new properties added min quality and max quality 
    def __init__(self, items):
        self.items = items
        self.min_quality = 0
        self.max_quality = 50

    # Update function for simple items     
    def regular_item_update(self, item):
        
        # Quality reduces by 1 before sell-in ends
        # Quality reduces by 2 after sell-in ends 
        if item.sell_in > 0:
            quality_adjustment = -1
        else:
            quality_adjustment = -2
        
        # Ensures that quality is not lower than 0
        item.quality = max((item.quality + quality_adjustment), self.min_quality)
        
        # Reduces sell-in by 1
        item.sell_in += -1

    # Update function for aged bries
    def aged_brie_update(self, item): 
        
        # Quality increases by 1 before sell-in ends
        # Quality increases by 2 after sell-in ends 
        if item.sell_in > 0:
            quality_adjustment = 1
        else:
            quality_adjustment = 2
        
        # Quality will never be higher than 50
        item.quality = min((item.quality + quality_adjustment), self.max_quality)
        
        # Reduces sell-in by 1
        item.sell_in += -1

    # Update function for sulfuras 
    def sulfuras_update(self, item):
        
        # Sell-in and quality remains the same all the time
        item.sell_in += 0
        item.quality += 0

    # Update function for backstage passes
    def backstage_passes_update(self, item):
        
        # Quality increases by 1 if sell-in more than 10
        if item.sell_in > 10:
            quality_adjustement = 1
            
            # Quality will never be higher than 50
            item.quality = min(item.quality + quality_adjustement , self.max_quality)
        
        # Quality increases by 2 if sell-in in between 10 and 5
        elif item.sell_in > 5:
            quality_adjustement = 2
            
            # Quality will never be higher than 50
            item.quality = min(item.quality + quality_adjustement , self.max_quality)
        
        # Quality increases by 3 if sell-in in between 5 and 0
        elif item.sell_in > 0:
            quality_adjustement = 3
            
            # Quality will never be higher than 50
            item.quality = min(item.quality + quality_adjustement , self.max_quality)
        else:
            item.quality = 0
        
        # Reduces sell-in by 1
        item.sell_in += -1

    # Update function for conjured
    def conjured_update(self, item):
        
        # Quality reduces by 2 before sell-in ends
        # Quality reduces by 4 after sell-in ends 
        if item.sell_in > 0:
            quality_adjustement = -2
        else:
            quality_adjustement = -4

        # Ensures that quality is not lower than 0
        item.quality = max((item.quality + quality_adjustement), self.min_quality)
        
        # Reduces sell-in by 1
        item.sell_in += -1    
    
    # Main function that calls other class "update quality" functions based on item name
    def update_quality(self):
        for item in self.items:
            if item.name == 'Aged Brie':
                self.aged_brie_update(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                self.backstage_passes_update(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                self.sulfuras_update(item)
            elif item.name == 'Conjured Mana Cake':
                self.conjured_update(item)
            else:
                self.regular_item_update(item)            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
