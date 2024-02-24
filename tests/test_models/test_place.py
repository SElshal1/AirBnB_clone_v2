test_place.py
#!/usr/bin/python3
""" """
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.city_id), str)

    def test_user_id(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.user_id), str)

    def test_name(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.name), str)

    def test_description(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.description), str)

    def test_number_rooms(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.max_guest), int)

    def test_price_by_night(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.price_by_night), int)

    def test_latitude(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.latitude), float)

    def test_longitude(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.latitude), float)

    def test_amenity_ids(self):
        """ """
        nw = self.value()
        self.assertEqual(type(nw.amenity_ids), list)
