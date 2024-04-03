def truth_table(p, q):
    # Define all propositions and their negations
    props = {"p": p, "q": q, "~p": not p, "~q": not q}  # dictionary

    # Evaluate compound propositions using truth rules
    props["p ∨ q"] = props["p"] or props["q"]
    props["p ∧ q"] = props["p"] and props["q"]
    props["p → q"] = not props["p"] or props["q"]  # Implication rule
    props["p ↔ q"] = (props["p"] and props["q"]) or (not props["p"] and not props["q"])  # Bi-conditional rule

    # Created table header
    table = [[]]

    table.extend([[str(value) for value in props.values()]] for _ in range(1))
    # added the result in the table

    return table


# application
print("[  'p',    'q',    '~p',    '~q',   'p ∨ q', 'p ∧ q', 'p → q', 'p ↔ q']")
props_table = truth_table(True, True)
print(props_table[1])

props_table = truth_table(True, False)
print(props_table[1])

props_table = truth_table(False, True)
print(props_table[1])

props_table = truth_table(False, False)
print(props_table[1])
