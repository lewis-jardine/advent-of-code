from ctypes import c_uint16 as uint16

with open("input.txt", "r") as f:
    lines = f.readlines()
    # Strip and split into list of strings
    # lines = ["123 -> x\n",
    #     "456 -> y\n",
    #     "x AND y -> d\n",
    #     "x OR y -> e\n",
    #     "x LSHIFT 2 -> f\n",
    #     "y RSHIFT 2 -> g\n",
    #     "NOT x -> h\n",
    #     "NOT y -> i\n"
    # ]
    lines = [line.strip().split() for line in lines]

# Circuit stored in dict with key wire name, val wire signal in 16 bit int
circuit = {}

"""
Need to run through steps twice:
Once to construct circuit, second to provide signals
Store circuit in dict with key wire name, val dict with signal, input gate
circuit = {
    x: {
        signal: 123
    },
    y: {
        signal: 456
    },
    d: {
        input: {
            gate: AND,
            src: [x, y]
        }
        signal: 0
    },
    e: {
        input: {
            gate: OR,
            src: [x, y]
        },
        signal: 0
    },
    f: {
        input: {
            gate: LSHIFT,
            src: x,
            val: 2
        },
        signal: 0
    },
    g: {
        input: {
            gate: RSHIFT,
            src: y,
            val: 2
        },
        signal: 0
    },
    h: {
        input: {
            gate: NOT,
            src: x,
        },
        signal: 0
    }
    i: {
        input: {
            gate: NOT,
            src: y,
        },
        signal: 0
    }
}
"""
# Create circuit on first loop
for line in lines:

    # Possibilites are NOT, OR, AND, RSHIFT, LSHIFT, no gate connection
    if line[0] == 'NOT':
        circuit[line[3]] = {
            "input": {
                "gate": "NOT",
                "src": line[1]
            },
            "signal": 0
        }

    elif line[1] == 'OR' or line[1] == 'AND':
        circuit[line[4]] = {
            "input": {
                "gate": line[1],
                "src": [line[0], line[2]],
            },
            "signal": 0
        }
    
    elif line[1] == 'RSHIFT' or line[1] == 'LSHIFT':
        circuit[line[4]] = {
            "input": {
                "gate": line[1],
                "src": line[0],
                "val": int(line[2])
            },
            "signal": 0
        }

    # Only line which starts with digit
    elif line[0][0].isdigit():
        circuit[line[2]] = {
            "signal": int(line[0]),
            "EOC": True
        }

    # Must be no gate connector
    else: 
        circuit[line[2]] = {
            "input": {
                "gate": False,
                "src": line[0]
            },
            "signal": 0
        }

# Overide wire B with part1 wire A answer (3176)
circuit["b"]["signal"] = 3176

# Circuit built, now work backwards from desired wire to get its signal
def get_signal(src_wire):
    src_wire = circuit[src_wire]
    
    # End of chain (EOC) if it doesnt have an input, or input has already been calcd
    if "EOC" in src_wire:
        return src_wire["signal"]
    
    # Go through each gate type, get input signal then return bitwise operation
    match src_wire["input"]["gate"]:
        case False:
            return get_signal(src_wire["input"]["src"])
    
        case "NOT":
            signal = get_signal(src_wire["input"]["src"])
            src_wire["EOC"] = True
            src_wire["signal"] = uint16(~signal).value
            return src_wire["signal"]

        case "AND":
            # Possibility of signal src being digit, check for each signal
            src_1, src_2 = src_wire["input"]["src"]
            if src_1.isdigit():
                signal_1 = int(src_1)
            else:
                signal_1 = get_signal(src_1)
            if src_2.isdigit():
                signal_2 = int(src_2)
            else:
                signal_2 = get_signal(src_2)
            src_wire["EOC"] = True
            src_wire["signal"] = uint16(signal_1 & signal_2).value
            return src_wire["signal"]
        
        case "OR":
            signal_1 = get_signal(src_wire["input"]["src"][0])
            signal_2 = get_signal(src_wire["input"]["src"][1])
            src_wire["EOC"] = True
            src_wire["signal"] = uint16(signal_1 | signal_2).value
            return src_wire["signal"]
        
        case "LSHIFT":
            signal = get_signal(src_wire["input"]["src"])
            src_wire["EOC"] = True
            src_wire["signal"] = uint16(signal << src_wire["input"]["val"]).value
            return src_wire["signal"]
        
        case "RSHIFT":
            signal = get_signal(src_wire["input"]["src"])
            src_wire["EOC"] = True
            src_wire["signal"] = uint16(signal >> src_wire["input"]["val"]).value
            return src_wire["signal"]


# start_wire = input("Select wire signal to be calculated: ")
start_wire = 'a'
signal = get_signal(start_wire)
print(signal)
