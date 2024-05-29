# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_regular(self):
        items = [
            Item("foo", 2, 2), # Testing regular behaviour
            Item("bro", 0, 3), # Testing when sell_in 0, quality should reduce by 2
            Item("old", 0, 1)  # Testing when quality should never be lower than 0
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual("foo", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

        self.assertEqual("bro", items[1].name)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(1, items[1].quality)

        self.assertEqual("old", items[2].name)
        self.assertEqual(-1, items[2].sell_in)
        self.assertEqual(0, items[2].quality)

    def test_aged_brie(self):
        items = [
            Item("Aged Brie", 2, 2), # Testing regular behaviour
            Item("Aged Brie", 0, 3), # Testing when sell_in 0, quality should be increased by 2
            Item("Aged Brie", 0, 49) # Testing when quality should never be higher than 50
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(5, items[1].quality)

        self.assertEqual("Aged Brie", items[2].name)
        self.assertEqual(-1, items[2].sell_in)
        self.assertEqual(50, items[2].quality)


    def test_sulfuras(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 2, 2) # Testing regular behaviour, nothing should change for Sulfuras            
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_passes(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 14, 5), # Testing when sell_in > 10
            Item("Backstage passes to a TAFKAL80ETC concert", 7, 5), # Testing when sell_in > 5 < 10
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 5), # Testing when sell_in > 0 < 5
            Item("Backstage passes to a TAFKAL80ETC concert", 1, 49) # Testing when quality should never be higher than 50
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(13, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[1].name)
        self.assertEqual(6, items[1].sell_in)
        self.assertEqual(7, items[1].quality)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[2].name)
        self.assertEqual(0, items[2].sell_in)
        self.assertEqual(8, items[2].quality)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[3].name)
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(50, items[3].quality)

    def test_conjured(self):
        items = [
            Item("Conjured Mana Cake", 2, 3), # Testing regular behaviour
            Item("Conjured Mana Cake", 0, 5), # Testing when sell_in 0, quality should be reduced by 4
            Item("Conjured Mana Cake", 0, 2) # Testing when quality should never be lower than 0
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual("Conjured Mana Cake", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

        self.assertEqual("Conjured Mana Cake", items[1].name)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(1, items[1].quality)

        self.assertEqual("Conjured Mana Cake", items[2].name)
        self.assertEqual(-1, items[2].sell_in)
        self.assertEqual(0, items[2].quality)    

        
if __name__ == '__main__':
    unittest.main()
