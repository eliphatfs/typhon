using System;
using System.Diagnostics;
using System.Text.Json;
using System.IO;
using TyphonHIRBackend;

class Program
{
    static Stopwatch _init = Stopwatch.StartNew();
    static void ReportElapsed(string operation)
    {
        Console.WriteLine($"{operation} finished. Elapsed: {_init.Elapsed.TotalMilliseconds:0.000} ms.");
        _init = Stopwatch.StartNew();
    }
    static void Main(string[] args)
    {
        ReportElapsed("Initialization");
        var hirDoc = JsonDocument.Parse(File.ReadAllText(args[0]));
        ReportElapsed("Parsing");
        var hirCompiler = new HIRCompiler(hirDoc.RootElement);
        var compiledModule = hirCompiler.Compile();
        ReportElapsed("Compile");
        var mainKlass = compiledModule.GetType("__global__");
        var entry = mainKlass.GetMethod("__main__");
        Console.WriteLine(
            "__main__ returns `{0}`.",
            entry.Invoke(Activator.CreateInstance(mainKlass), new object[0])
        );
        ReportElapsed("Run");
    }
}
