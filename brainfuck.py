import re, sys

def execute(commands):
    cells = [0] * 1024
    cellptr = 0
    codeptr = 0
    
    # scan to match [ and ]
    loops = []
    opens = {}
    closes = {}
    while codeptr < len(commands):
        if commands[codeptr] == '[':
            loops.append(codeptr)
        elif commands[codeptr] == ']':
            start = loops.pop()
            opens[start] = codeptr
            closes[codeptr] = start
        codeptr += 1
    
    assert len(loops) == 0, 'opening and closing brackets don\'t match'

    # reset code pointer and actually run program
    codeptr = 0    
    while codeptr < len(commands):
        if commands[codeptr] == '+':
            cells[cellptr] += 1
        elif commands[codeptr] == '-':
            cells[cellptr] -= 1
        elif commands[codeptr] == '<':
            cellptr -= 1
        elif commands[codeptr] == '>':
            cellptr += 1
        elif commands[codeptr] == ',':
            cells[cellptr] = raw_input()
        elif commands[codeptr] == '.':
            print chr(cells[cellptr])
        elif commands[codeptr] == '[':
            if cells[cellptr] == 0:
                codeptr = opens[codeptr]
        elif commands[codeptr] == ']':
            if cells[cellptr] != 0:
                codeptr = closes[codeptr]
        codeptr += 1



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: python brainfuck.py <input.b>'
        sys.exit(1)
    with open(sys.argv[1]) as f:
        program = f.read()
        filtered = re.sub('[^+-[],.<>]', '', program)
        commands = list(filtered)
        execute(commands)


