from emu.util import itoh, itob

class Core:
    ax = 0
    bx = 0
    cx = 0
    dx = 0
    si = 0
    di = 0
    sp = 0
    pc = 0
    #   ELG------------H
    # 0b0000000000000000
    flg = 0

    def __repr__(self):
        return f"<Core pc={self.pc}>"

    def dumps(self):
        return "\n".join([
            "Core Dump ---------------",
            f" AX:  {itoh(self.ax)}  pc: {itoh(self.pc)}",
            f" BX:  {itoh(self.bx)}  sp: {itoh(self.sp)}",
            f" CX:  {itoh(self.cx)}  si: {itoh(self.si)}",
            f" DX:  {itoh(self.dx)}  di: {itoh(self.di)}",
            f" FLG: {itob(self.flg)}"
        ])

