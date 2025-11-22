import streamlit as st
st.title('The Smart Grocer Calculator')
st.subheader('A grocery store sells three items:')
st.write('Enter your price and kg')
Rice_price = st.number_input('Price of rice per kg:',step=1)
Rice_qty = st.number_input('enter qty of rice:',step=1)
Sugar_price = st.number_input('Price of sugar per kg:',step=1)
Sugar_qty = st.number_input('enter qty of sugar :',step=1)
Oil_price = st.number_input('Price of oil per kg',step=1)
Oil_qty = st.number_input('enter qty of oil:',step=1)


total = (Rice_price*Rice_qty)+(Sugar_price*Sugar_qty)+(Oil_price*Oil_qty)
st.write(f"Total_cost:{total}")

if st.button("Calculate"):
    if total>=500:
        discount = 10
        final_price = total-(total*(discount/100))
        st.success(f"final amount is: {final_price}")

        st.info(f"Before Discount Amount: {total}")
        st.info(f"Discount Applied: {discount}")
        st.success(f"Final Amount After Discount: {final_price}")
    else:
        st.success("No discount")






