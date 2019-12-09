# Conditionals
MSK_CONDITIONS_ENABLED      = 0b11000000
MSK_CONDITIONS_VALUE        = 0b00110000
MSK_CONDITIONS_EQ_VALUE     = 0b00100000
MSK_CONDITIONS_LG_VALUE     = 0b00010000
FLG_CONDITIONS_EQ_ENABLED   = 0b10000000
FLG_CONDITIONS_LG_ENABLED   = 0b01000000

# Access Selectors
FLG_BYREF  = 0b1000
MSK_PARAM  = 0b0111
AX_SEL     = 0b0000
BX_SEL     = 0b0001
CX_SEL     = 0b0010
DX_SEL     = 0b0011
SP_SEL     = 0b0100
PC_SEL     = 0b0110
ROM_SEL    = 0b0111

# OPCODES
MSK_OPCODE = 0b1111
OPCODE_NOP = 0b0000  # (0x00) No operation
OPCODE_MOV = 0b0001  # (0x01) Move data from SRC to DST
OPCODE_CMP = 0b0010  # (0x02) Compare SRCA and SRCB and set the core.flags
OPCODE_JMP = 0b0011  # (0x03) Move the value into PC - Dont increment PC
OPCODE_OUT = 0b0100  # (0x04) Send data SRC out port PORT
OPCODE_IN  = 0b0101  # (0x05) Read from port PORT and store in DST
OPCODE_HLT = 0b0110  # (0x06) Halt the CPU
OPCODE_BRK = 0b0111  # (0x07) Debug Break
OPCODE_ADD = 0b1000  # (0x08) Add SRCA and SRCB and store result in DST
OPCODE_SUB = 0b1001  # (0x09) Sub SRCB from SRCA and store result in DST
OPCODE_MUL = 0b1010  # (0x0A) Mul SRCA and SRCB and store result in DST
OPCODE_DIV = 0b1011  # (0x0B) Div SRCB by SRCA and store result in DST
OPCODE_NOT = 0b1100  # (0x0C) Bitwise NOT on SRC and store in DST
OPCODE_AND = 0b1101  # (0x0D) Bitwise AND between SRCA and SRCB and store result in DST
OPCODE_OR  = 0b1110  # (0x0E) Bitwise OR between SRCA and SRCB and store result in DST
OPCODE_XOR = 0b1111  # (0x0F) Bitwise XOR between SRCA and SRCB and store result in DST

# CORE FLAGS
FLG_CORE_EQ  = 0b1000000000000000
FLG_CORE_LT  = 0b0100000000000000
FLG_CORE_GT  = 0b0010000000000000
FLG_CORE_HLT = 0b0000000000000001
