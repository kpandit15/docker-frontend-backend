import streamlit as st

def generate_table(number):
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(f"{number} x {i} = {result}")
    return table

def main():
    st.title("Multiplication Table Generator")
    
    # User input
    number = st.number_input("Enter a number: ", value=1, step=1)
    
    # Generate button
    if st.button("Generate Table"):
        # Generate and display table
        table = generate_table(number)
        
        # Display in a nice format
        st.subheader(f"Multiplication Table for {number}")
        for line in table:
            st.write(line)

if __name__ == "__main__":
    main()