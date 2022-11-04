from faker import Faker

fake = Faker()
fake.random


class Org:

    def __init__(self, generator: Faker):
        self.generator = generator
        self.render = {
            'number': self._getNumber(),
            'name': self._getName(),
            'desc': self._getDesc(),
            'channel': self._getChannel(),
            'status': self._getStatus(),
            'orgType': self._getOrgType(),
            'parentNumber': self._getParentNumber(),
            'sqft': self._getSqFt(),
            'address': self._getAddress(),
            'phone': self._getPhone(),
            'latlon': self._getLatLong(),
            'datecreated': self._getDateCreated(),
            'datemodified': self._getDateModified(),
            'deleteflag': self._getDeleteFlag()
        }

    def _getNumber(self):
        return self.generator.license_plate().split('-')[0].split(' ')[0]

    def _getName(self):
        return self.generator.company()

    def _getDesc(self):
        return self.generator.sentence()

    def _getChannel(self):
        return self.generator.random.choice(['physical store', 'warehouse', 'online'])

    def _getStatus(self):
        return self.generator.random.choice(['active', 'closed', None])

    def _getOrgType(self):
        return self.generator.random.choice(['Brick & Mortar', 'Fulfillment Center', 'eBay', 'Amazon', None])

    def _getParentNumber(self):
        return self.generator.random.choice([None, self._getNumber()])

    def _getSqFt(self):
        return self.generator.random.randint(50, 9999)

    def _getRegion(self):
        pass

    def _getBusinessUnit(self):
        pass

    def _getImageUrl(self):
        pass

    def _getURL(self):
        pass

    def _getAddress(self):
        addr = {
            'address1': self.generator.street_address(),
            'address2': self.generator.random.choices([self.generator.secondary_address(), None], weights=(1,9))[0],
            'city': self.generator.city(),
            'state': self.generator.state_abbr(),
            'zip': self.generator.postcode(),
            'country': self.generator.country_code(),
        }
        return addr

    def _getPhone(self):
        return self.generator.phone_number()

    def _getDateCreated(self):
        return self.generator.date()

    def _getDateModified(self):
        return self.generator.date()

    def _getDeleteFlag(self):
        return self.generator.boolean(chance_of_getting_true = .01)

    def _getLatLong(self):
        return self.generator.latlng()
