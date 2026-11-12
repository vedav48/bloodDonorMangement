import streamlit as st
from donorView import BloodDonorManager
donor_instance = BloodDonorManager()
tab1, tab2,tab3 = st.tabs(["ADD Donor", "View Donors","Update Donor"])
with tab1:
    st.header("Add New Donor....!")
    name = st.text_input("Enter Donor Name")
phone = st.text_input("Enter Donor Phone Number")
blood_group = st.selectbox("Select Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
city = st.text_input("Enter Donor City")
last_donation = st.date_input("Enter Last Donation Date")
if st.button("Submit"):
    result = donor_instance.post(name=name,blood_group=blood_group,phone=phone,  city=city, last_donation=last_donation )
    st.success("Donor added successfully...")
with tab2:
    st.header("View Blood Donor Details....!")
    record=donor_instance.get()
    if record:
        st.table([
            {
                "ID": r[0],
                "Name": r[1],
                "Blood Group": r[2],
                "Phone": r[3],
                "City": r[4],
                "Last Donation": r[5]
            }
            for r in record
        ])
    else:
        st.warning("No donor records found!")
with tab3:
    st.title("Update Donor Details")
    records= donor_instance.get()
    if records:
        donor_ids = [r[0] for r in records]
        id = st.selectbox("Select donor id",donor_ids,key="update_id")
        record = donor_instance.get_object(id=id)
        # record = 1, Anu, 0+, 9876543234, Kochi, 2026-11-11
        name = st.text_input("Enter your name :", value=record[1])
        phone = st.text_input("Enter Donor Phone Number", value=record[3])
# blood_group = st.selectbox("Select Your Blood Group",
#                            blood_group,
#                            index=blood_group,
#                            index(record[2]),
#                            keys="update_group"
#                            )
city = st.text_input("Enter your city", value=record[4])
last_donation = st.date_input("Last donation date :", value=record[5])