namespace TyphonHIRBackend.Intrinsics
{
    public class BuiltinsInt
    {
        private long _x;
        public BuiltinsInt __init__(long x)
        {
            _x = x;
            return this;
        }

        public bool __le__(BuiltinsInt o)
        {
            return _x <= o._x;
        }

        public BuiltinsInt __add__(BuiltinsInt o) => new BuiltinsInt().__init__(_x + o._x);
        public BuiltinsInt __sub__(BuiltinsInt o) => new BuiltinsInt().__init__(_x - o._x);
        public override string ToString()
        {
            return _x.ToString();
        }
    }
}
