class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if type(value) != int:
            self._make = value
        else:
            print('fuck off mate')

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def bhp(self):
        return self._bhp

    @bhp.setter
    def bhp(self, value):
        self._bhp = value

    @property
    def mph(self):
        return self._mph

    @mph.setter
    def mph(self, value):
        self._mph = value
