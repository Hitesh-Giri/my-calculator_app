import streamlit as st

# Configure page title and layout
st.set_page_config(page_title="Calculator", layout="centered")

# App header and short instruction
st.title("Simple Calculator")
st.write("Provide two numbers and choose an operation.")

# Create two columns for number inputs for nicer layout
col1, col2 = st.columns(2)
with col1:
    # First numeric input (float)
    a = st.number_input("First number", value=0.0, format="%.6f")
with col2:
    # Second numeric input (float)
    b = st.number_input("Second number", value=0.0, format="%.6f")

# Dropdown to select the arithmetic operation
op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"]) 

# Compute button triggers the calculation
if st.button("Compute"):
    try:
        # Perform the selected operation
        if op == "Add":
            res = a + b
        elif op == "Subtract":
            res = a - b
        elif op == "Multiply":
            res = a * b
        elif op == "Divide":
            # Guard against division by zero
            if b == 0:
                st.error("Division by zero is not allowed.")
                res = None
            else:
                res = a / b

        # Display result when calculation succeeded
        if res is not None:
            st.success(f"Result: {res}")
    except Exception as e:
        # Catch-all for any unexpected errors
        st.error(f"Error: {e}")

# Optional: allow user to type a small expression to evaluate
expr = st.text_input("Or enter an expression (e.g. 2+3*4)", key="expr")
if expr:
    if st.button("Evaluate expression"):
        try:
            # Very small safety check: only allow digits, operators and parentheses
            allowed = set("0123456789+-*/(). ")
            if set(expr) <= allowed:
                # Evaluate the expression and show the result
                res2 = eval(expr)
                st.success(f"Expression result: {res2}")
            else:
                # Inform user when expression has invalid characters
                st.error("Expression contains invalid characters.")
        except Exception as e:
            st.error(f"Could not evaluate expression: {e}")
