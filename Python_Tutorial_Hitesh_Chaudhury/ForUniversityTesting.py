# def truth_table(p, q):
#     """
#   This function generates a truth table for p, q, ~p, p ∨ q, p ∧ q, p → q, and p ↔ q.
#
#   Args:
#       p: The first proposition (boolean)
#       q: The second proposition (boolean)
#
#   Returns:
#       A list of lists representing the truth table.
#   """
#     # Define all propositions and their negations
#     props = {"p": p, "q": q, "~p": not p, "~q": not q}
#
#     # Evaluate compound propositions using truth rules
#     props["p ∨ q"] = props["p"] or props["q"]
#     props["p ∧ q"] = props["p"] and props["q"]
#     props["p → q"] = not props["p"] or props["q"]  # Implication rule
#     props["p ↔ q"] = (props["p"] and props["q"]) or (not props["p"] and not props["q"])  # Bi-conditional rule
#
#     # Create table header
#     table = [["p", "q", "~p", "p ∨ q", "p ∧ q", "p → q", "p ↔ q"]]
#
#     # Add each row with formatted values (all truth combinations)
#     table.extend([[str(value) for value in props.values()]] for _ in range(4))
#
#     return table
#
#
# # Example usage
# props_table = truth_table(True, False)
#
# # Print the truth table
# for row in props_table:
#     print(row)

def truth_table(p, q):
    """
    This function generates a truth table for p, q, ~p, ~q, p ∨ q, p ∧ q, p → q, and p ↔ q.

    Args:
        p: The first proposition (boolean)
        q: The second proposition (boolean)

    Returns:
        A list of lists representing the truth table.
    """
    # Define all propositions and their negations
    props = {"p": p, "q": q, "~p": not p, "~q": not q}

    # Evaluate compound propositions using truth rules
    props["p ∨ q"] = props["p"] or props["q"]
    props["p ∧ q"] = props["p"] and props["q"]
    props["p → q"] = not props["p"] or props["q"]  # Implication rule
    props["p ↔ q"] = (props["p"] and props["q"]) or (not props["p"] and not props["q"])  # Bi-conditional rule

    # Create table header
    table = [["p", "q", "~p", "~q", "p ∨ q", "p ∧ q", "p → q", "p ↔ q"]]

    # Generate all truth combinations
    all_truth_values = [(True, True), (True, False), (False, True), (False, False)]

    # Evaluate truth values for each combination and add to table
    for p_val, q_val in all_truth_values:
        props.update({"p": p_val, "q": q_val})  # Update propositions for each combination
        table.append([str(value) for value in props.values()])

    return table


# Print the truth table
# print("[  'p',    'q',    '~p',    '~q',   'p ∨ q', 'p ∧ q', 'p → q', 'p ↔ q']")
props_table = truth_table(True, True)
print(*props_table, sep='\n')  # Unpack and print all rows (including header)
