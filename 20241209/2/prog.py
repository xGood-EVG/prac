import math
import sys


prog = []
vrs = {}
labels = {}

ops =  {'add', 'sub', 'mul', 'div'}
comps = {'ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle'}

pos = 0
for s in sys.stdin.readlines():
    s = s.strip().split()

    if len(s) == 0:
        continue

    if s[0][-1] == ':':
        labels[s[0][:-1]] = pos
        s.pop(0)

        if len(s) == 0:
            continue

    match s:
        case ['stop']:
            prog.append(['stop', ])
        case ['store', num, var]:
            prog.append(['store', num, var])
        case [op, r1, r2, r3] if op in ops:
            prog.append([op, r1, r2, r3])
        case [comp, r1, r2, lab] if comp in comps:
            prog.append([comp, r1, r2, lab])
        case ['out', var]:
            prog.append(['out', var])
        case _:
            continue

    pos += 1

prog.append(['stop'])

for line in prog:
    if line[0] in comps and line[3] not in labels:
    	exit(0)

i = 0
while True:
	s = prog[i]

	match s:
		case ['stop']:
			break
		case ['store', num, var]:
			try:
				vrs[var] = float(num)
			except Exception:
				pass

			i += 1
		case [op, r1, r2, r3] if op in ops:
			r1 = vrs.setdefault(r1, 0)
			r2 = vrs.setdefault(r2, 0)

			match op:
				case 'add':
					vrs[r3] = r1 + r2
				case 'sub':
					vrs[r3] = r1 - r2
				case 'mul':
					vrs[r3] = r1 * r2
				case 'div':
					try:
						vrs[r3] = r1 / r2
					except Exception:
						vrs[r3] = math.inf

			i += 1
		case [comp, r1, r2, lab] if comp in comps:
			r1 = vrs.setdefault(r1, 0)
			r2 = vrs.setdefault(r2, 0)
			match comp:
				case 'ifeq':
					if r1 == r2:
						i = labels[lab]
					else:
						i += 1
				case 'ifne':
					if r1 != r2:
						i = labels[lab]
					else:
						i += 1
				case 'ifgt':
					if r1 > r2:
						i = labels[lab]
					else:
						i += 1
				case 'ifge':
					if r1 >= r2:
						i = labels[lab]
					else:
						i += 1
				case 'iflt':
					if r1 < r2:
						i = labels[lab]
					else:
						i += 1
				case 'ifle':
					if r1 <= r2:
						i = labels[lab]
					else:
						i += 1
		case ['out', var]:
			print(vrs.setdefault(var, 0))
			i += 1
		case _:
			i += 1
			continue