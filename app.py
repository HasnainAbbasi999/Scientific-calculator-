import streamlit as st
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return math.pow(x, y)

def sqrt(x):
    return math.sqrt(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def logarithm(x):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive values."
    else:
        return math.log10(x)

# Streamlit UI for Scientific Calculator
st.title("Scientific Calculator")

operation = st.selectbox("Select Operation", 
                         ["Add", "Subtract", "Multiply", "Divide", "Power", 
                          "Square Root", "Sine", "Cosine", "Tangent", "Logarithm"])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    
    if operation == "Add":
        st.write(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "Divide":
        st.write(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    elif operation == "Power":
        st.write(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

elif operation == "Square Root":
    num = st.number_input("Enter number:", value=0.0)
    st.write(f"Square Root of {num} = {sqrt(num)}")

elif operation in ["Sine", "Cosine", "Tangent"]:
    angle = st.number_input("Enter angle in degrees:", value=0.0)
    
    if operation == "Sine":
        st.write(f"Sine({angle}) = {sine(angle)}")
    elif operation == "Cosine":
        st.write(f"Cosine({angle}) = {cosine(angle)}")
    elif operation == "Tangent":
        st.write(f"Tangent({angle}) = {tangent(angle)}")

elif operation == "Logarithm":
    num = st.number_input("Enter number:", value=1.0)
    st.write(f"Logarithm({num}) = {logarithm(num)}")
