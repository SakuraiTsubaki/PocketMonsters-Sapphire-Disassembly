# Japanese Thumb entry reachable disassembly

Starting at the proven Thumb transition target `0x0800024c`, conservative control-flow traversal records 107 reachable halfwords, 18 direct CFG edges, and 21 BL call sites. BL targets are recorded without following callees, and unreachable gaps are represented by explicit `.org` directives in the source.

The source halfwords in ascending address order have canonical SHA-256 `684e093b6efc32ff1dcc8b87b45b6aa4f14047472f3d1086a0dc877f4f66b4aa`. No return is reachable in this graph, so this is documented as a non-returning bootstrap path rather than a complete function boundary. Every emitted `.hword` is checked against its original little-endian ROM bytes.

