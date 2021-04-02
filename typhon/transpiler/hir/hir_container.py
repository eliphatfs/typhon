class HIR:
    def __init__(self):
        self.objects = []

    def ser_non_top(self, obj):
        if hasattr(obj, "OBJ_KID"):
            return id(obj)
        elif isinstance(obj, list):
            return [self.ser_non_top(ch) for ch in obj]
        elif isinstance(obj, (str, int, float, bool)):
            return obj
        elif obj is None:
            return 0
        elif hasattr(obj, "ser") and callable(obj.ser):
            return obj.ser()
        raise TypeError("Cannot serialize object", obj)

    def ser(self):
        ser = {}
        for obj in self.objects:
            if isinstance(obj, list):
                ser[id(obj)] = {
                    "OBJ_KID": obj.OBJ_KID,
                    "children": [self.ser_non_top(ch) for ch in obj]
                }
            else:
                ser[id(obj)] = {
                    k: self.ser_non_top(v) for k, v in obj.__dict__.items()
                }
                ser[id(obj)]["OBJ_KID"] = obj.OBJ_KID
        return ser
