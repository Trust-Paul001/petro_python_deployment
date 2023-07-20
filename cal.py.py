import streamlit as st

st.title("EDVANTAGE_LEARNING PROJECT CALCULATOR")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        st.error("Error: Cannot divide by zero")

def main():
  
    
    operation = st.selectbox(
        "Select operation:",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    if operation == "Addition":
        result = add(num1, num2)
        st.write("Result:", result)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
        st.write("Result:", result)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
        st.write("Result:", result)
    elif operation == "Division":
        result = divide(num1, num2)
        if result is not None:
            st.write("Result:", result)

if __name__ == "__main__":
    main()