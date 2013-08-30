## before
class SpeedValidator(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validate(self):
        """if Speed upper 50, returns False"""
        result = self.a <= 50
        if not result:
            return False
        result = self.b <= 50
        if not result:
            return False
        return True

## after
class SpeedValidator2(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validate(self):
        result_a = self.a <= 50
        if not result_a:
            return False
        result_b = self.b <= 50
        if not result_b:
            return False
        return True


if __name__ == '__main__':
    b = SpeedValidator(10, 70)
    b2 = SpeedValidator2(10, 70)

    assert b.validate() == b2.validate()
