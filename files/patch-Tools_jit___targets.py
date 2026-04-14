--- Tools/jit/_targets.py.orig	2026-04-14 17:00:00 UTC
+++ Tools/jit/_targets.py
@@ -54,7 +54,7 @@ class _Target(typing.Generic[_S, _R]):
     def _get_nop(self) -> bytes:
         if re.fullmatch(r"aarch64-.*", self.triple):
             nop = b"\x1f\x20\x03\xd5"
-        elif re.fullmatch(r"x86_64-.*|i686.*", self.triple):
+        elif re.fullmatch(r"x86_64-.*|i686.*|amd64.*", self.triple):
             nop = b"\x90"
         else:
             raise ValueError(f"NOP not defined for {self.triple}")
@@ -554,6 +554,14 @@ def get_target(host: str) -> _COFF | _ELF | _MachO:
         args = ["-fno-pic", "-mcmodel=medium", "-mlarge-data-threshold=0"]
         condition = "defined(__x86_64__) && defined(__linux__)"
         target = _ELF(host, condition, args=args)
+    elif re.fullmatch(r"amd64-.*-freebsd.*", host):
+        args = ["-fno-pic", "-mcmodel=medium", "-mlarge-data-threshold=0"]
+        condition = "defined(__x86_64__) && defined(__FreeBSD__)"
+        target = _ELF(host, condition, args=args)
+    elif re.fullmatch(r"aarch64-.*-freebsd.*", host):
+        args = ["-fpic","-mno-outline-atomics",]
+        condition = "defined(__aarch64__) && defined(__FreeBSD__)"
+        target = _ELF(host, condition, alignment=8, args=args)
     else:
         raise ValueError(host)
     return target
